## Description

Given a list of 24-hour clock time points in **"HH:MM"** format, return *the minimum **minutes** difference between any two time-points in the list*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $timePoints = ["23:59","00:00"]$
- **Output:** `1`
#### Example 2

- **Input:** $timePoints = ["00:00","23:59","00:00"]$
- **Output:** `0`
### Constraints

- $2 \le \text{timePoints.length} \le 2 * 10^{4}$

- $\text{timePoints}[i]$ is in the format **"HH:MM"**.