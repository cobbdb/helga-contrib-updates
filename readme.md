# helga-contrib-updates [![PyPI version](https://badge.fury.io/py/helga-contrib-updates.svg)](http://badge.fury.io/py/helga-contrib-updates)

A helga plugin to list and record IRC channel updates.

    $ pip install helga-contrib-updates

Syntax:

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

#### !updates &lt;channel&gt;
Lists updates from everyone in a specific channel.

#### !updates &lt;nick&gt;
Lists updates from a single person in the current channel.

#### !updates YYYY-MM-DD
Lists updates from specific date of the current channel.

#### !updates (&lt;nick&gt;|&lt;channel&gt;) YYYY-MM-DD
Search for updates from a specific date for a single person or channel.
