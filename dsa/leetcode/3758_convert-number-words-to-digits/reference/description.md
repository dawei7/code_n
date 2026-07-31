## Description

You are given a string `s` containing only lowercase English letters. Within it, complete English number words for the digits `0` through `9` may appear concatenated without spaces.

Extract valid number words in their left-to-right order and replace each extracted word with its corresponding digit. Parse from the current position according to these rules:

- When a complete number word begins there, append its digit and move forward by the entire word length.
- When no number word begins there, skip exactly one character and resume from the next position.

Return the digits as a string. If the scan never encounters a complete number word, return the empty string `""`.
