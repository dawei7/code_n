# Build Array Where You Can Find The Maximum Exactly K Comparisons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1420 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/) |

## Problem Description

### Goal

Consider arrays of length `n` whose elements are integers from $1$ through `m`. Scan one such array from left to right while maintaining the largest value seen. Its search cost increases whenever the current element is strictly greater than every earlier element, including the first element.

Count how many possible arrays have search cost exactly `k`. Arrays are distinguished by their complete sequence of values, and the answer must be returned modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: the array length, where $1 \le n \le 50$.
- `m`: the largest allowed element value, where $1 \le m \le 50$.
- `k`: the required search cost, where $1 \le k \le n$.

**Return value**

- The number of length-`n` arrays over values $1$ through `m` whose running maximum changes exactly `k` times, modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 2, m = 3, k = 1`
- Output: `6`

**Example 2**

- Input: `n = 5, m = 2, k = 3`
- Output: `0`

**Example 3**

- Input: `n = 9, m = 1, k = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(nkm)$
- **Space:** $O(km)$

<details>
<summary>Approach</summary>

#### General

**Retain cost and current maximum.** After a fixed number of positions, let `dp[c][x]` count arrays with search cost `c` and current maximum exactly `x`. For length one, every choice from $1$ through $m$ creates its first maximum, so `dp[1][x] = 1`.

When appending another value to a state ending at maximum `x`, there are `x` choices from $1$ through `x` that keep both maximum and cost unchanged. This contributes `x * dp[c][x]`.

A new maximum `x` can instead follow any state with cost `c - 1` and previous maximum smaller than `x`. Its contribution is

$$
\sum_{y=1}^{x-1} \texttt{dp[c - 1][y]}.
$$

**Accumulate the transition prefix.** While visiting `x` in increasing order for a fixed cost, maintain the sum of the preceding `dp[c - 1]` values. This supplies the displayed transition in constant time rather than summing all smaller maxima again. Apply the recurrence for each added position and reduce modulo $10^9 + 7$.

The state records exactly the information that affects the next search comparison. Every appended value is either at most the current maximum or is a unique new maximum, so the two transition terms are disjoint and exhaustive. Induction over array length proves the final sum of `dp[k][x]` over all maxima counts exactly the requested arrays.

#### Complexity detail

There are $n$ length layers, $k$ relevant costs, and $m$ possible maxima. Prefix accumulation makes every transition constant time, giving $O(nkm)$ time. Keeping only the previous and next layers uses $O(km)$ space.

#### Alternatives and edge cases

- **Direct smaller-maximum summation:** Evaluate the transition sum separately for every `x`. It is correct but takes $O(nkm^2)$ time.
- **Enumerate all arrays:** Testing all $m^n$ arrays is infeasible.
- **Cost exceeds value range:** No array can create more than $m$ distinct increasing maxima, so the count is zero when `k > m`.
- **Length one:** Every one-element array has cost one, yielding `m` valid arrays when `k = 1`.
- **Single allowed value:** Exactly one array exists, and its cost is one regardless of `n`.
- **Strict comparison:** Repeating the current maximum does not increase cost.
- **Modulo:** Reduce multiplication, prefix sums, and state additions at every layer.

</details>
