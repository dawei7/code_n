#!/usr/bin/env bash
tr -s '[:space:]' '\n' < words.txt \
  | grep -v '^$' \
  | sort \
  | uniq -c \
  | sort -k1,1nr -k2,2r \
  | awk '{print $2 " " $1}'
