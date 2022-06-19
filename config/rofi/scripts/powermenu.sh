#!/bin/bash

MESSAGE="What do you want to do Cyril ?"
POWER="襤"
RESTART="勒"
LOGOUT=""
LOCK=""
RES=`echo "$POWER|$RESTART|$LOGOUT|$LOCK" | rofi -dmenu -p "$MESSAGE" -sep "|" -theme powermenu -monitor -1`
[ "$RES" = "$POWER" ] && systemctl poweroff
[ "$RES" = "$RESTART" ] && systemctl reboot
[ "$RES" = "$LOGOUT" ] && i3 exit
[ "$RES" = "$LOCK" ] && sleep .1 && i3lock-fancy-multimonitor
