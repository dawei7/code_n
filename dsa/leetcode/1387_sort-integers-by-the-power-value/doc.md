# Sort Integers by The Power Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1387 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Memoization, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/sort-integers-by-the-power-value/) |

## Problem Description

### Goal

For a positive integer `x`, repeatedly replace it with `x / 2` when it is even and with `3 * x + 1` when it is odd. Its power value is the number of replacements required to reach `1`; the values in the given range are guaranteed to reach `1`.

List every integer from `lo` through `hi`, inclusive, ordered first by increasing power value and then by increasing integer value when powers tie. Return the `k`th integer in this one-indexed order.

### Function Contract

**Inputs**

- `lo`: the inclusive lower bound, with $1 \le \texttt{lo} \le \texttt{hi}$.
- `hi`: the inclusive upper bound, at most $1000$.
- `k`: a one-indexed position within the $R = \texttt{hi} - \texttt{lo} + 1$ integers.
- Let $U$ be the number of distinct Collatz values encountered while evaluating the whole interval.

**Return value**

- The integer occupying position `k` after sorting by `(power value, integer value)`.

### Examples

**Example 1**

- Input: `lo = 12, hi = 15, k = 2`
- Output: `13`

**Example 2**

- Input: `lo = 7, hi = 11, k = 4`
- Output: `7`

**Example 3**

- Input: `lo = 1, hi = 1, k = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(U + R log R)$
- **Space:** $O(U + R)$

<details>
<summary>Approach</summary>

#### General

**Memoize complete sequence suffixes.** Start with power `0` for `1`. To evaluate a number, follow its Collatz sequence while recording previously unknown states until reaching a memoized value. Walk the recorded path backward, assigning each state one more step than its successor.

Every later sequence that meets any cached state can stop immediately. Thus shared suffixes across the interval are evaluated once rather than rediscovered for every starting integer.

**Sort with both ordering keys.** Evaluate the power of each integer from `lo` through `hi`, then sort using the pair `(power, value)`. Including the value as the second key implements the required tie rule directly. Return index `k - 1` from the sorted list.

#### Complexity detail

Each of the $U$ distinct Collatz states is transitioned and memoized once, costing $O(U)$ time and space. Sorting the $R$ interval values costs $O(R \log R)$ time and stores $O(R)$ values. Together the bounds are $O(U + R \log R)$ time and $O(U + R)$ space.

#### Alternatives and edge cases

- **Recompute every sequence:** Calculate each starting value's full power independently. It is correct but repeats shared Collatz suffixes.
- **Comparator recomputation:** Invoke uncached power calculations during every sort comparison. This can multiply sequence work by $O(R \log R)$ comparisons.
- **Bottom-up only to `hi`:** Collatz sequences can rise above `hi`, so a fixed array limited to the input interval is insufficient.
- **Power tie:** Place the smaller integer first.
- **Range containing one:** The power of `1` is zero.
- **Single-value range:** The only value is returned for `k = 1`.
- **One-indexed rank:** Convert `k` to list index `k - 1`.

</details>
