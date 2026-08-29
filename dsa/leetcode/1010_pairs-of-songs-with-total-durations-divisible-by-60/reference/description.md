### 1. Description

You are given a list of songs where the $i^{\text{th}}$ song has a duration of $\text{time}[i]$ seconds.

Return *the number of pairs of songs for which their total duration in seconds is divisible by* `60`. Formally, we want the number of indices `i`, `j` such that `i < j` with $(\text{time}[i] + \text{time}[j]) \% 60 = 0$.

### 2. Function Contract

**Inputs**

- `time`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $time = [30,20,150,100,40]$
- **Output:** `3`
- **Explanation:** Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

#### Example 2

- **Input:** $time = [60,60,60]$
- **Output:** `3`
- **Explanation:** All three pairs have a total duration of 120, which is divisible by 60.

### 4. Constraints

- $1 \le \text{time.length} \le 6 * 10^{4}$

- $1 \le \text{time}[i] \le 500$
