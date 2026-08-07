## General
Given a string `date` representing a <a href="https://en.wikipedia.org/wiki/Gregorian_calendar" target="_blank">Gregorian calendar</a> date formatted as `YYYY-MM-DD`, return *the day number of the year*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(1)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
