# Count Number of Maximum Bitwise-OR Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2044 |
| Difficulty | Medium |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) |

## Problem Description

### Goal

Choose any nonempty subset of the integer array `nums` and compute the bitwise
OR of its selected elements. A subset is determined by selected indices, so
equal values at different indices still create different subsets.

Find the greatest bitwise OR attainable by any subset, then return how many
different nonempty index subsets attain that value. Selected indices need not
be adjacent, and their original relative order is preserved within a subset.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: an array of positive integers with $1 \le N \le 16$ and
  $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- The number of nonempty index subsets whose bitwise OR equals the maximum
  possible subset OR.

### Examples

**Example 1**

- Input: `nums = [3, 1]`
- Output: `2`
- Explanation: Subsets selecting `[3]` and `[3, 1]` both have OR `3`.

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `7`
- Explanation: Every one of the $2^3-1$ nonempty index subsets has OR `2`.

**Example 3**

- Input: `nums = [3, 2, 1, 5]`
- Output: `6`

### Required Complexity

- **Time:** $O(2^N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Derive the maximum OR without searching**

Adding an element to a subset can only set additional bits; it never clears an
already set bit. Therefore the OR of all input elements is an upper bound on
every subset OR, and the full set attains it. Compute this target once.

**Explore each include-or-exclude choice**

Backtracking at index $i$ keeps the OR accumulated from earlier selected
indices. One branch excludes `nums[i]` and preserves that value; the other
includes it and updates the state with `current | nums[i]`. At the end, count
the branch exactly when its OR equals the target.

Each index subset corresponds to one unique sequence of include/exclude
decisions, so the recursion visits every subset once and cannot double-count.
The leaf comparison accepts exactly the subsets with maximum OR. Because all
values are positive, the empty subset's OR `0` cannot equal the positive
target.

**Count all remaining choices after reaching the target**

Once `current` already equals the target, OR-ing more values cannot change it.
Every combination of the remaining $N-i$ indices is valid, contributing
$2^{N-i}$ subsets immediately. Returning this count is an optional pruning
that preserves the worst-case bound while avoiding redundant recursion when
the target is reached early.

#### Complexity detail

In the worst case, the target is reached only at leaves and the recursion visits
$O(2^N)$ states. Each state performs constant bitwise work. The recursion depth
is $N$, so auxiliary stack space is $O(N)$.

#### Alternatives and edge cases

- **Iterative bitmask enumeration:** Compute the OR for every mask; updating
  incrementally can retain $O(2^N)$ time, while recomputing each mask from all
  indices takes $O(N2^N)$.
- **Count dynamic programming by OR value:** Maintain a frequency map of
  reachable OR values after each element. This can merge equal states but may
  store many distinct OR values.
- A single element creates exactly one nonempty subset.
- Equal values at different indices remain independently selectable and
  multiply the count.
- If every element already equals the target OR, every nonempty subset
  qualifies.
- Distinct single-bit powers may require selecting every element, leaving only
  one qualifying subset.
- The answer counts index subsets, not distinct value sequences or distinct OR
  values.

</details>
