#!/usr/bin/bash

BACKUPDIR=/backup/home/jacquem

# ssh
cp -r $BACKUPDIR/.ssh ~

# evolution emails
cp -r $BACKUPDIR/.local/share/evolution ~/.local/share/
cp -r $BACKUPDIR/.config/evolution ~/.config/
