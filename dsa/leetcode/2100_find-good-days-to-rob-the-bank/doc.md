# Find Good Days to Rob the Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) |

## Problem Description

### Goal

The days are numbered from $0$, and `security[i]` gives the number of guards working on day `i`. A day is considered good only if it has at least `time` earlier days and `time` later days available for inspection.

Across the `time` days leading into a good day, including the comparison with that day, guard counts must be non-increasing. Starting from that day and continuing through the following `time` days, guard counts must be non-decreasing. In other words, day `i` is good exactly when

$$
\texttt{security[i-time]} \ge \cdots \ge \texttt{security[i]}
\le \cdots \le \texttt{security[i+time]}.
$$

Return all zero-based indices that satisfy these conditions. Their output order does not matter.

### Function Contract

Let $n$ be the number of days.

**Inputs**

- `security`: a list of $n$ non-negative guard counts, where $1 \le n \le 10^5$ and $0 \le \texttt{security[i]} \le 10^5$.
- `time`: the number of required days on each side, where $0 \le \texttt{time} \le 10^5$.

**Return value**

Return every index whose preceding `time` comparisons are non-increasing and whose following `time` comparisons are non-decreasing.

### Examples

**Example 1**

- Input: `security = [5,3,3,3,5,6,2]`, `time = 2`
- Output: `[2,3]`
- Explanation: Around day `2`, $5 \ge 3 \ge 3 \le 3 \le 5$; around day `3`, $3 \ge 3 \ge 3 \le 5 \le 6$.

**Example 2**

- Input: `security = [1,1,1,1,1]`, `time = 0`
- Output: `[0,1,2,3,4]`
- Explanation: With no required days on either side, every index qualifies.

**Example 3**

- Input: `security = [1,2,3,4,5,6]`, `time = 2`
- Output: `[]`
- Explanation: No eligible center has two non-increasing days leading into it.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Summarizing the left condition**

For each day, record how many consecutive non-increasing transitions end there. If `security[day - 1] >= security[day]`, extend the previous count by one; otherwise reset it to zero. A day has the required left window exactly when this count is at least `time`.

**Summarizing the right condition**

Scan from right to left and similarly record how many consecutive non-decreasing transitions begin at each day. If `security[day] <= security[day + 1]`, extend the count from the next day. This count reaches `time` exactly when the required right window is valid.

**Combining both windows**

Only indices from `time` through `n - time - 1` have enough surrounding days. Return those whose left and right counts are both at least `time`.

Each recorded count describes the entire required monotonic chain through its endpoint, not merely one comparison. Therefore a selected index satisfies every inequality on both sides. Conversely, any good day has `time` consecutive valid transitions in each direction, so both counts reach the threshold and the scan includes it.

#### Complexity detail

The forward scan, backward scan, and final filtering scan each process $n$ positions once, giving $O(n)$ time. The two run-length arrays use $O(n)$ space, and the output can also contain $O(n)$ indices.

#### Alternatives and edge cases

- **Direct window checks:** Test all `time` comparisons on both sides of every candidate. This is straightforward but costs $O(n \cdot \texttt{time})$ in the worst case.
- **Prefix counts of violations:** Mark each increasing transition for the left rule and each decreasing transition for the right rule, then use prefix sums to test whether a window contains a violation. This also runs in $O(n)$ time and space.
- **Constant-extra-space streaming:** With carefully maintained windows, the auxiliary arrays can be reduced, but the two directional summaries are simpler and less error-prone.
- When `time = 0`, every day is good, including both endpoints.
- If $2 \cdot \texttt{time} + 1 > n$, no day has enough positions on both sides.
- Equality satisfies both non-increasing and non-decreasing requirements, so flat plateaus may yield several adjacent good days.
- A globally increasing array can fail every positive-time left window, while a globally decreasing array can fail every positive-time right window.

</details>
