helga-contrib-updates
=====================

A helga plugin to list IRC channel updates.

    helga updates [<nick>|<channel>] [YYYY-MM-DD]


## Creating a new update

New updates are created by adding ```Update:``` to the beginning of a message.
```Update:``` is case-insensitive.

    Update: This is important information.


## Listing past updates

The plugin will send you a private message with the list of updates for today.
Optionally, you can ask for a specific date (see above) using a format YYYY-MM-DD.
All update timestamps are stored in UTC.

#### !updates
Lists updates from everyone in the current channel.

#### !updates <channel>
Lists updates from everyone in a specific channel.

#### !updates <nick>
Lists updates from a single person in the current channel.

#### !updates YYYY-MM-DD
Lists updates from specific date of the current channel.
