from datetime import datetime

from helga import log
from helga.db import db
from helga.plugins import command, match


logger = log.getLogger(__name__)


def _updates_command(client, channel, nick, message, cmd, args):
    try:
        who = args[0]
    except IndexError:
        who = None

    # MongoDB can't handle date types, only datetime
    today = datetime.utcnow().date()

    search = {
        'where': channel,
        'when': {
            '$gte': datetime(today.year, today.month, today.day, 0, 0, 0),
            '$lte': datetime(today.year, today.month, today.day, 23, 59, 59),
        }
    }

    if who:
        search['who'] = who

    updates = db.updates.find(search)

    client.me(channel, 'whispers to {0}'.format(nick))
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


@match(r'^(?i)update')
@command('updates', help='List updates from today. Usage: helga updates [<nick>]')
def updates(client, channel, nick, message, *args):
    if len(args) == 1:
        return _updates_match(client, channel, nick, message, args[0])
    else:
        return _updates_command(client, channel, nick, message, args[0], args[1])
