### 1. Description

You are given two valid times `startTime` and `endTime`, each represented as a string in the format `"HH:MM:SS"`.

Return the number of seconds that have elapsed from `startTime` to `endTime`.

### 2. Function Contract

`solve(startTime, endTime) -> int`

**Inputs**

- `startTime`: A valid 24-hour clock time written as `"HH:MM:SS"`.
- `endTime`: A valid time in the same format that is not earlier than `startTime`.

Both values describe times within the same day. Hours range from `00` through `23`, while minutes and seconds each range from `00` through `59`.

**Output**

Return the number of elapsed seconds from `startTime` to `endTime`. The result lies between `0` and `86399`, inclusive.

### 3. Examples

#### Example 1

- **Input:** startTime = "01:00:00", endTime = "01:00:25"

- **Output:** 25

- **Explanation:** `endTime` is 25 seconds ahead of `startTime`.

#### Example 2

- **Input:** startTime = "12:34:56", endTime = "13:00:00"

- **Output:** 1504

- **Explanation:** `endTime` is 25 minutes and 4 seconds ahead of `startTime`, which equals 1504 seconds.

### 4. Constraints

- $\text{startTime.length} = 8$

- $\text{endTime.length} = 8$

- `startTime` and `endTime` are valid times in the format `"HH:MM:SS"`

- $00 \le HH \le 23$

- $00 \le MM \le 59$

- $00 \le SS \le 59$

- `endTime` is not earlier than `startTime`
