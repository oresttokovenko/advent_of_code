#!/bin/zsh

function download_aoc_input() {
  local year_num=$1
  local day_num=$2

  echo "Year: $year_num, Day: $day_num"

  curl "https://adventofcode.com/${year_num}/day/${day_num}/input" \
    -H "cookie: session=$AOC_SESSION" \
    --compressed >> input.txt
}

download_aoc_input $1 $2
