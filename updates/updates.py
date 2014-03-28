from helga.plugins import command, match, random_ack
from helga.db import db
from helga import log
from datetime import datetime
import smokesignal

logger = log.getLogger(__name__)

def clearAll():
    logger.info('Clearing all standup updates.')
    db.standup.drop()

# I doubt this will work, so I need some help on what to do
@smokesignal.on('signon')
def init_standup():
    # Clear all updates every midnight.
    if datetime.now().hour == 0:
        clearAll()

@command(
    'updates',
    aliases = ['standup'],
    help = 'List updates from today. Usage: (!|helga) '
        '(updates|standup) [all|<nick>]. '
        '[all] will list all updates from everyone in all channels.'
        '[<nick>] will list updates from a single person in the current channel.'
        'Ex) !updates sduncan'
)
def updates(client, channel, nick, message, cmd, args):
    def report(updates):
        client.me(channel, 'whispers to ' + nick)
        for update in updates:
            client.msg(nick, '(%s) %s' % (
                update['who'],
                update['what']
            ))
    try:
        if args[0] is 'clear':
            # Clear all updates - drops the entire collection.
            # Note this is unlisted in the help description - use wisely.
            clearAll()
            client.msg(channel, random_ack())
        elif args[0] is 'all':
            # List all updates from everyone in all channels.
            report(db.standup.find())
        else:
            # List updates from a single person in the current channel.
            report(db.standup.find({
                'who': args[0],
                'where': channel
            ))
    except IndexError:
        # List all updates in the current channel.
        report(db.standup.find({
            'where': channel
        ))
    return None

@match(r'^(?i)update:')
def update(client, channel, nick, message, matches):
    logger.info('Adding a new standup update for %s.' % nick)
    db.standup.insert({
        'who': nick,
        'what': message,
        'when': datetime.now().strftime('%H:%M'),
        'where': channel
    })
    return None
