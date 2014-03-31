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

    search = {'where': channel}
    if who:
        search['who'] = who

    updates = db.updates.find(search)

    client.me(channel, 'whispers to {0}'.format(nick))
    for update in updates:
        client.msg(nick, '({who}) {what}'.format(**update))


def _updates_match(client, channel, nick, message, matches):
    logger.info('Adding a new standup update for {0}.'.format(nick))
    db.standup.insert({
        'who': nick,
        'what': message,
        'when': datetime.now().strftime('%H:%M'),
        'where': channel
    })


@match(r'^(?i)update')
@command('updates', help='List updates from today. Usage: helga updates [<nick>]')
def updates(client, channel, nick, message, *args):
    if len(args) == 1:
        return _updates_match(client, channel, nick, message, args[0])
    else:
        return _updates_command(client, channel, nick, message, args[0], args[1])
