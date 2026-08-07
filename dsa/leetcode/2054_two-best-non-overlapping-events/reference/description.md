### 1. Description

You are given a **0-indexed** 2D integer array of `events` where $\text{events}[i] = [\text{startTime}_{i}, \text{endTime}_{i}, \text{value}_{i}]$. The $$i^{\text{th}}$$ event starts at $\text{startTime}_{i}$_ and ends at $\text{endTime}_{i}$, and if you attend this event, you will receive a value of $\text{value}_{i}$. You can choose **at most** **two** **non-overlapping** events to attend such that the sum of their values is **maximized**.

Return *this **maximum** sum.*

Note that the start time and end time is **inclusive**: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time `t`, the next event must start at or after $t + 1$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/untitled-diagramdrawio.png)

- **Input:** $events = [[1,3,2],[4,5,2],[2,4,3]]$
- **Output:** `4`
- **Explanation:** Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
#### Example 2

![Example 1 Diagram](images/2054b.png)

- **Input:** $events = [[1,3,2],[4,5,2],[1,5,5]]$
- **Output:** `5`
- **Explanation:** Choose event 2 for a sum of 5.
#### Example 3

![](images/2054c.png)

- **Input:** $events = [[1,5,3],[1,5,1],[6,6,5]]$
- **Output:** `8`
- **Explanation:** Choose events 0 and 2 for a sum of 3 + 5 = 8.

### 4. Constraints

- $2 \le \text{events.length} \le 10^{5}$

- $\text{events}[i].length = 3$

- $1 \le \text{startTime}_{i} \le \text{endTime}_{i} \le 10^{9}$

- $1 \le \text{value}_{i} \le 10^{6}$