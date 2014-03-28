helga-contrib-updates
=====================

A helga plugin to list IRC channel updates.

    (!|helga) (updates|standup) [all|clear|<nick>]

## Creating a new update
New updates are created by adding ```Update:``` to the beginning of a message. ```Update:``` is case-insensitive and the colon is required.

    Update: This is important information.

## Listing past updates
The plugin will send you a private message with the list of updates for today. This list of updates is cleared at midnight daily.

#### !updates
Lists all updates from the current channel.

#### !updates all
Lists all updates from everyone in all channels.

#### !updates &lt;nick&gt;
Lists updates from a single person in the current channel.

## Utility

#### !updates clear
Clears all updates from all channels.
