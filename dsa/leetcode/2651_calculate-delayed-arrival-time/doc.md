# Calculate Delayed Arrival Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2651 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-delayed-arrival-time/) |

## Problem Description

### Goal

A train was scheduled to arrive at hour `arrivalTime`, but its journey is delayed by `delayedTime` hours. Both quantities use whole hours. Add the complete delay to the original schedule and return the hour at which the train will now reach the station.

Use 24-hour time for the result. Hours wrap after `23`: midnight is represented by `0`, and a delay may move the arrival into the following day without changing the required integer format.

### Function Contract

**Inputs**

- `arrivalTime`: The scheduled hour, where $1 \le \texttt{arrivalTime} < 24$.
- `delayedTime`: The positive delay in hours, where $1 \le \texttt{delayedTime} \le 24$.

**Return value**

- Return the delayed arrival hour as an integer from $0$ through $23$.

### Examples

#### Example 1

- **Input:** `arrivalTime = 15`, `delayedTime = 5`
- **Output:** `20`
- **Explanation:** The sum remains within the same 24-hour cycle.

#### Example 2

- **Input:** `arrivalTime = 13`, `delayedTime = 11`
- **Output:** `0`
- **Explanation:** Hour `24` is midnight, represented by `0` in 24-hour time.
