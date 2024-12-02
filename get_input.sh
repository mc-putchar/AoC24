#!/usr/bin/bash
set -a
source .env
set +a

DAY="$1"
URL="https://adventofcode.com/2024/day/${DAY##0}/input"
curl -o "$DAY/input" --cookie "$COOKIE" "$URL"
