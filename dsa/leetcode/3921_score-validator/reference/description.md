## Description

Process a list of string events while maintaining `score = 0` and `counter = 0` initially.

- A numeric event—`"0"`, `"1"`, `"2"`, `"3"`, `"4"`, or `"6"`—adds its integer value to `score`.
- `"W"` adds `1` to `counter` and adds nothing to `score`.
- Either `"WD"` or `"NB"` adds `1` to `score` without changing `counter`.

Read events from left to right. Processing ends after the whole list or immediately after an event makes `counter` equal to `10`, whichever happens first. Return the final score and counter together as `[score, counter]`.
