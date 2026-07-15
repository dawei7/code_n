# Diet Plan Performance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1176 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/diet-plan-performance/) |

## Problem Description

### Goal

A dieter consumes `calories[i]` calories on day $i$. For every consecutive sequence of exactly `k` days, let $T$ be the total calories consumed in that window. The dieter loses one point when $T<\texttt{lower}$, gains one point when $T>\texttt{upper}$, and receives no point change when $\texttt{lower}\leq T\leq\texttt{upper}$.

The score begins at zero. Evaluate every `k`-day window whose start is between `0` and `calories.length - k`, inclusive, and return the final score after all days. The result may be negative.

### Function Contract

**Inputs**

- `calories`: An array of daily calorie counts with $1 \leq \lvert\texttt{calories}\rvert \leq 10^5$ and $0 \leq \texttt{calories[i]} \leq 20000$.
- `k`: The exact window length, with $1 \leq \texttt{k} \leq \lvert\texttt{calories}\rvert$.
- `lower`: The inclusive lower boundary for a no-change window.
- `upper`: The inclusive upper boundary for a no-change window, with $0 \leq \texttt{lower} \leq \texttt{upper}$.
- Let $n=\lvert\texttt{calories}\rvert$.

**Return value**

- The sum of the point changes from all $n-k+1$ consecutive windows of length `k`.

### Examples

**Example 1**

- Input: `calories = [1,2,3,4,5]`, `k = 1`, `lower = 3`, `upper = 3`
- Output: `0`

The first two days lose one point each, the middle day changes nothing, and the last two days gain one point each.

**Example 2**

- Input: `calories = [3,2]`, `k = 2`, `lower = 0`, `upper = 1`
- Output: `1`

**Example 3**

- Input: `calories = [6,5,0,0]`, `k = 2`, `lower = 1`, `upper = 5`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compute the first complete window.** Sum `calories[:k]` once. Compare that total with the two thresholds: subtract one only when it is strictly below `lower`, add one only when it is strictly above `upper`, and otherwise leave the score unchanged.

**Slide without resumming.** When the window moves one position right, add the entering value `calories[right]` and subtract the leaving value `calories[right - k]`. This updates the total in constant time while preserving exactly the sum of the current consecutive `k` days.

Score each updated window with the same strict comparisons. The first window and the $n-k$ subsequent slides cover every valid start exactly once, so the accumulated score matches the required evaluation and can be negative when losses outnumber gains.

#### Complexity detail

The initial sum examines `k` values and the sliding loop processes each remaining value once. Since $k\leq n$, total time is $O(n)$. The running sum, score, and loop index use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Resum every window:** Calling `sum(calories[start:start + k])` is correct but takes $O(nk)$ time and becomes quadratic when $k$ grows with $n$.
- **Prefix sums:** A length-$n+1$ prefix array gives each window sum in $O(1)$ time and $O(n)$ total time, but uses $O(n)$ extra space.
- **Equality with a threshold:** A total equal to `lower` or `upper` is inside the inclusive no-change range.
- **One-day windows:** With `k = 1`, each array element is scored independently.
- **Whole-array window:** With `k = n`, exactly one total is evaluated.
- **Zero calories:** Zero values participate normally and can make the final score negative.

</details>
