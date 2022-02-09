#!/usr/bin/env bash
brightness=$(light)
brightness=${brightness%.*}

if [[ $brightness -gt 50 ]]; then
	echo "%{F-}󰛨 %{F-}$brightness%"
else
	echo "%{F-}󰛩 %{F-}$brightness%"
fi
