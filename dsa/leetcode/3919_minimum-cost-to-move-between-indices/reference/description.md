## Description

You are given an integer array `nums` where `nums` is **strictly increasing**.

For each index `x`, let `closest(x)` be the **adjacent** index `y` such that $abs(\text{nums}[x] - \text{nums}[y])$ is **minimized**. If both **adjacent** indices exist and give the same difference, choose the **smaller** index.

From any index `x`, you can move in two ways:

- To any index `y` with cost $abs(\text{nums}[x] - \text{nums}[y])$, or

- To `closest(x)` with cost 1.

You are also given a 2D integer array `queries`, where each $\text{queries}[i] = [l_{i}, r_{i}]$.

For each query, calculate the **minimum total cost** to move from index $l_{i}$ to index $r_{i}$.

Return an integer array `ans`, where $\text{ans}[i]$ is the answer for the $$i^{\text{th}}$$ query.

The **absolute difference** between two values `x` and `y` is defined as $abs(x - y)$.
### Function Contract

**Inputs**

- `nums`: A strictly increasing list of integers. Its indices are the positions between which moves are made.
- `queries`: A list of pairs `[l, r]`, each asking for the minimum cost to travel from index `l` to index `r`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. For an interior index, equal gaps select its smaller, left-hand neighbor as `closest(x)`; either endpoint has only one possible adjacent index.

**Return value**

Return a list of $q$ integers in the same order as `queries`. Entry `i` is the minimum total cost of moving from `queries[i][0]` to `queries[i][1]`. A query whose endpoints are equal has cost `0`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]

**Output:** [6,2,5]

**Explanation:**​​​​​​​​​​​​​​​​​​​​

- The closest indices are `[1, 0, 1]` respectively.

- For `[0, 2]`, the path `0 → 1 → 2` uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost $|-2 - 3| = 5$, giving total $1 + 5 = 6$.

- For `[2, 0]`, the path `2 → 1 → 0` uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2.

- For `[1, 2]`, the direct move from index 1 to index 2 has cost $|-2 - 3| = 5$, which is optimal.

Thus, $ans = [6, 2, 5]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]

**Output:** [4,1,3]

**Explanation:**

- The closest indices are `[1, 2, 1, 2]` respectively.

- For `[3, 0]`, the path `3 → 2 → 1 → 0` uses closest moves from index 3 to 2 and from 2 to 1, each with cost 1, and a move from 1 to 0 with cost $|2 - 0| = 2$, giving total $1 + 1 + 2 = 4$.

- For `[1, 2]`, the closest move from index 1 to 2 has cost 1.

- For `[2, 0]`, the path `2 → 1 → 0` uses a closest move from index 2 to 1 with cost 1 and a move from 1 to 0 with cost $|2 - 0| = 2$, giving total $1 + 2 = 3$.

Thus, $ans = [4, 1, 3]$.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- `nums` is strictly increasing

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i] = [l_{i}, r_{i}]$​​​​​​​

- $0 \le l_{i}, r_{i} < \text{nums.length}$