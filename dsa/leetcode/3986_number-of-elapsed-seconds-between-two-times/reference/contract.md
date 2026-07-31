## Function Contract

`solve(startTime, endTime) -> int`

**Inputs**

- `startTime`: A valid 24-hour clock time written as `"HH:MM:SS"`.
- `endTime`: A valid time in the same format that is not earlier than `startTime`.

Both values describe times within the same day. Hours range from `00` through `23`, while minutes and seconds each range from `00` through `59`.

**Output**

Return the number of elapsed seconds from `startTime` to `endTime`. The result lies between `0` and `86399`, inclusive.
