# Missing Number In Arithmetic Progression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1228 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/missing-number-in-arithmetic-progression/) |

## Problem Description

### Goal

An array originally formed an arithmetic progression: the difference between every pair of consecutive values was the same. Exactly one value that was neither the first nor the last was removed from that array.

You are given the remaining values in their original order as `arr`. Return the removed value. The input is guaranteed to come from such a valid removal, and the progression may be increasing, decreasing, or constant.

### Function Contract

**Inputs**

- `arr`: The $n$ remaining progression values, where $3\le n\le1000$ and $0\le\texttt{arr[i]}\le10^5$.

**Return value**

- The unique interior value removed from the original arithmetic progression.

### Examples

**Example 1**

- Input: `arr = [5,7,11,13]`
- Output: `9`

The original progression was `[5,7,9,11,13]` with common difference `2`.

**Example 2**

- Input: `arr = [15,13,12]`
- Output: `14`

The original progression was decreasing by `1`.

**Example 3**

- Input: `arr = [0,0,0,0,0]`
- Output: `0`

Removing one value from a constant progression leaves the same values.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recover the common difference from the endpoints.** The original progression contains `n + 1` values and therefore has `n` equal gaps from the unchanged first value to the unchanged last value. Compute `difference = (arr[-1] - arr[0]) // n`. This works for positive and negative differences because the input guarantee makes the division exact.

**Locate the first shifted index.** Without a missing earlier value, index `i` should contain `arr[0] + i * difference`. Before the removed position, actual and expected values agree. From the removed position onward, every actual value is the next progression term and disagrees with its index's expectation. Binary-search this monotone match/mismatch boundary.

**Return the term at that boundary.** If `left` is the first mismatching index, the missing value is `arr[0] + left * difference`. For a constant progression, every value and the missing value equal `arr[0]`; return it directly because no mismatch boundary is observable.

The removal is guaranteed to be interior, so both endpoints used to derive the difference are authentic. The binary-search invariant keeps all indices before `left` matched and the missing position at or after `left`, which proves the returned expected term is exactly the removed one.

#### Complexity detail

Binary search halves the $n$-element index range each iteration, taking $O(\log n)$ time. Only bounds and scalar arithmetic values are stored, so space is $O(1)$.

#### Alternatives and edge cases

- **Linear adjacent-gap scan:** The first gap different from `difference` reveals the missing term, but it takes $O(n)$ time.
- **Compare total sums:** The expected progression sum minus the observed sum gives the missing value in $O(n)$ time and requires care with fixed-width overflow.
- **Decreasing progression:** A negative `difference` preserves the same expected-index boundary.
- **Constant progression:** Every observed and missing value is identical, so return the common value directly.
- **Missing near either end:** The guarantee excludes the original endpoints but permits the second or penultimate value; binary search still finds the first shifted index.
- **Integer division:** Exact progression endpoints guarantee no rounding ambiguity.

</details>
