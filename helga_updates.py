import re

from datetime import datetime

from helga import log
from helga.db import db
from helga.plugins import command, match


logger = log.getLogger(__name__)


def _updates_command(client, channel, nick, message, cmd, args):
    who = None
    when = datetime.utcnow().date()

    # We can search by date
    if len(args) == 2:
        who = args[0]
        when = datetime.strptime(args[1], '%Y-%m-%d').date()
    else:
        try:
            who = args[0]
        except IndexError:
            pass
        else:
            if re.match(r'[\d]{4}-[\d]{2}-[\d]{2}', who):
                when, who = who, None
                when = datetime.strptime(when, '%Y-%m-%d').date()

    # Handle if the 'who' is actually a channel
    if who and who.startswith('#'):
        who, where = None, who
    else:
        where = channel

    search = {
        'where': where,
        'when': {
            '$gte': datetime(when.year, when.month, when.day, 0, 0, 0),
            '$lte': datetime(when.year, when.month, when.day, 23, 59, 59),
        }
    }

    client.me(channel, 'whispers to {0}'.format(nick))

    if who:
        client.msg(nick, 'Updates by {who} for {when}'.format(who=who, when=when))
        search['who'] = who
    else:
        client.msg(nick, 'Updates for {when}'.format(when=when))

    updates = db.updates.find(search)

    for update in updates:
        client.msg(nick, '({who}) {what}'.format(who=update['who'],
                                                 what=update['what']))


def _updates_match(client, channel, nick, message, matches):
    logger.info('Adding a new standup update for {0}.'.format(nick))

    db.updates.insert({
        'who': nick,
        'what': message,
        'when': datetime.utcnow(),
        'where': channel,
    })


@match(r'^(?i)update[^\w]')
@command('updates', help=('List standup updates. Usage: helga updates '
                          '[<nick>|<channel>] [YYYY-MM-DD]'))
def updates(client, channel, nick, message, *args):
    if len(args) == 1:
        return _updates_match(client, channel, nick, message, args[0])
    else:
        return _updates_command(client, channel, nick, message, args[0], args[1])
