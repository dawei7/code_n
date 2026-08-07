### 1. Description

You are given a **0-indexed** 2D integer array `tires` where $\text{tires}[i] = [f_{i}, r_{i}]$ indicates that the $$i^{\text{th}}$$ tire can finish its $$x^{\text{th}}$$ successive lap in $f_{i} * r_{i}^(x-1)$ seconds.

- For example, if $f_{i} = 3$ and $r_{i} = 2$, then the tire would finish its $1^st$ lap in `3` seconds, its $2^nd$ lap in $3 * 2 = 6$ seconds, its $3^rd$ lap in $3 * 2^{2} = 12$ seconds, etc.

You are also given an integer `changeTime` and an integer `numLaps`.

The race consists of `numLaps` laps and you may start the race with **any** tire. You have an **unlimited** supply of each tire and after every lap, you may **change** to any given tire (including the current tire type) if you wait `changeTime` seconds.

Return* the **minimum** time to finish the race.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4$
- **Output:** `21`
- **Explanation:**
Lap 1: Start with tire 0 and finish the lap in 2 seconds.
Lap 2: Continue with tire 0 and finish the lap in 2 * 3 = 6 seconds.
Lap 3: Change tires to a new tire 0 for 5 seconds and then finish the lap in another 2 seconds.
Lap 4: Continue with tire 0 and finish the lap in 2 * 3 = 6 seconds.
Total time = 2 + 6 + 5 + 2 + 6 = 21 seconds.
The minimum time to complete the race is 21 seconds.
#### Example 2

- **Input:** $tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5$
- **Output:** `25`
- **Explanation:**
Lap 1: Start with tire 1 and finish the lap in 2 seconds.
Lap 2: Continue with tire 1 and finish the lap in 2 * 2 = 4 seconds.
Lap 3: Change tires to a new tire 1 for 6 seconds and then finish the lap in another 2 seconds.
Lap 4: Continue with tire 1 and finish the lap in 2 * 2 = 4 seconds.
Lap 5: Change tires to tire 0 for 6 seconds then finish the lap in another 1 second.
Total time = 2 + 4 + 6 + 2 + 4 + 6 + 1 = 25 seconds.
The minimum time to complete the race is 25 seconds.

### 4. Constraints

- $1 \le \text{tires.length} \le 10^{5}$

- $\text{tires}[i].length = 2$

- $1 \le f_{i}, changeTime \le 10^{5}$

- $2 \le r_{i} \le 10^{5}$

- $1 \le numLaps \le 1000$