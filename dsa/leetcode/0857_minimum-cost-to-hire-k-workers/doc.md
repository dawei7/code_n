# Minimum Cost to Hire K Workers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 857 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) |

## Problem Description
### Goal
There are $n$ workers. Worker `i` has quality `quality[i]` and will accept no less than `wage[i]`. Hire exactly $k$ workers and assign their pay subject to two rules: every hired worker receives at least their minimum wage, and all hired workers are paid directly proportionally to their quality.

Find the least total amount that can satisfy both rules for some group of exactly $k$ workers. A result within $10^{-5}$ of the exact minimum is accepted.

### Function Contract
**Inputs**

- `quality`: an array of $n$ positive worker qualities.
- `wage`: an equally long array of positive minimum wages, paired by index with `quality`.
- `k`: the required group size, where $1 \leq k \leq n \leq 10^4$ and $1 \leq \texttt{quality[i]}, \texttt{wage[i]} \leq 10^4$.

**Return value**

Return the minimum total cost as a floating-point number, within absolute error $10^{-5}$.

### Examples
**Example 1**

- Input: `quality = [10,20,5], wage = [70,50,30], k = 2`
- Output: `105.0`

Paying at a rate of $7$ per unit of quality gives the selected workers payments $70$ and $35$.

**Example 2**

- Input: `quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3`
- Output: `30.6666666667`

**Example 3**

- Input: `quality = [5,10,2], wage = [30,20,8], k = 1`
- Output: `8.0`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**A group is determined by one pay ratio**

If every selected worker is paid at a common rate $r$ per unit of quality, worker $i$ receives $r \cdot \texttt{quality[i]}$. Meeting that worker's minimum requires

$$
r \geq \frac{\texttt{wage[i]}}{\texttt{quality[i]}}.
$$

For a fixed group, the cheapest valid rate is therefore the largest wage-to-quality ratio among its members. Its cost is that ratio multiplied by the group's total quality.

**Sweep possible maximum ratios**

Sort workers by their individual required ratio in ascending order. When processing a worker with ratio $r$, all workers seen so far can be paid legally at rate $r$. Among them, the cheapest $k$-worker quality total is obtained by choosing the $k$ smallest qualities.

Maintain those qualities in a max-heap represented by negative values, along with their sum. Push each new quality; whenever the heap exceeds $k$, remove its largest quality. With exactly $k$ entries, `quality_sum * ratio` is the best cost using the current ratio as an upper pay threshold.

Every feasible group appears when its largest required ratio is reached. At that step all its workers are available, and the heap's quality sum is no larger than that group's sum. The recorded candidate is therefore no worse. Conversely, each recorded candidate selects $k$ available workers and pays them all at a sufficient ratio, so it is feasible. The minimum candidate is exactly optimal.

#### Complexity detail

Sorting $n$ workers takes $O(n\log n)$ time. Each worker causes one heap insertion and at most one removal, each $O(\log k)$, so sorting dominates and total time is $O(n\log n)$. The sorted worker list and heap use $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate worker groups:** Checking all $inom{n}{k}$ subsets is correct but exponential in the worst case.
- **Keep a sorted quality list:** It can identify the largest selected quality, but insertion and deletion may take linear time.
- **Min-heap of qualities:** The algorithm must evict the largest quality, so a max-heap is the direct choice.
- **One worker:** The minimum is simply the smallest individual wage.
- **Hire everyone:** The maximum individual ratio fixes the rate for the sum of all qualities.
- **Equal ratios:** The heap keeps the $k$ smallest qualities at that shared rate.
- **Large minimum wage, low quality:** Such a worker's high ratio may make otherwise small total quality expensive.
- **Floating-point output:** The accepted tolerance covers ordinary division rounding; all heap decisions use integer qualities.
- **Exactly $k$ workers:** Candidates are evaluated only when the heap contains exactly $k$ qualities.

</details>
