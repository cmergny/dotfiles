#!/usr/bin/env bash

# Terminate any currently running instances
pkill -9 polybar -e

# Pause while killall completes
while pgrep -u $UID -x polybar > /dev/null; do sleep 1; done

# Look a the monitor conenct and launch a bar for each of them
if type "xrandr" > /dev/null; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
	echo $m
    MONITOR=$m polybar --reload example -c ~/.config/polybar/config &
  done
else
  polybar --reload example -c ~/.config/polybar/config &
fi

# polybar --reload example -c ~/.config/polybar/config &
# Launch bar(s)
# polybar dummy -q &
# polybar top -q &
# polybar bottom -q  &

echo "polybars launched..."
