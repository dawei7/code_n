# K-th Smallest in Lexicographical Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 440 |
| Difficulty | Hard |
| Topics | Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/) |

## Problem Description
### Goal
Given positive integers `n` and `k`, arrange every integer from `1` through `n` by lexicographical order of its decimal representation. This is dictionary order, so a prefix such as `1` appears before `10`, and the complete `1` prefix subtree appears before `2`.

Return the integer at the valid one-based position `k`. Do not materialize or sort all `n` values, because the range may be large. Count how many valid integers lie beneath each decimal prefix and skip whole prefix subtrees until the target rank is reached, never including zero or values above `n`.

### Function Contract
**Inputs**

- `n`: the inclusive upper bound of the integer range
- `k`: a one-based position in lexicographic order

**Return value**

- Return the integer occupying position `k` without materializing the full sorted range.

### Examples
**Example 1**

- Input: `n = 13, k = 2`
- Output: `10`

**Example 2**

- Input: `n = 1, k = 1`
- Output: `1`

**Example 3**

- Input: `n = 100, k = 10`
- Output: `17`

### Required Complexity

- **Time:** $O(d^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**View decimal prefixes as an implicit ten-way trie**

Lexicographic order is preorder traversal of prefixes: visit `1`, then everything beginning with `10`, then `11`, and eventually move to prefix `2`. The integers themselves need not be stored; multiplying a prefix by ten descends to its first child, while adding one moves to its next sibling.

**Count how many valid integers lie below a prefix**

For adjacent prefixes `first` and `next = first + 1`, each decimal depth contributes the clipped interval `[first, next)` within $[1,n+1)$. Add `min(n + 1, next) - first`, then multiply both boundaries by ten. The sum is exactly the number of integers whose decimal form begins with the prefix.

**Skip a whole subtree or descend into it**

Start at prefix `1` and convert `k` to the number of remaining preorder moves by subtracting one. If the current subtree contains at most `k` remaining positions, skip it with `prefix += 1` and subtract its size. Otherwise the answer lies inside it: descend with `prefix *= 10` and subtract one for visiting that child prefix.

**Why the remaining rank stays correct**

The prefix count partitions lexicographic preorder into contiguous subtrees. Skipping subtracts exactly every value preceding the next sibling. Descending consumes exactly the current prefix and preserves the rank within its child subtree. Each action therefore keeps the desired value at the maintained remaining offset until that offset reaches zero.

#### Complexity detail

Let `d` be the number of decimal digits in `n`. Counting one prefix subtree takes $O(d)$, and at most $O(d)$ skip-or-descend decisions are needed per digit frontier, giving the conventional $O(d^2)$ bound. Only numeric counters are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Materialize and sort decimal strings:** straightforward but takes $O(n \log n)$ time and $O(n)$ space.
- **Explicit trie:** reproduces the same ordering but stores all numbers and defeats the large-`n` constraint.
- **Depth-first enumeration until rank `k`:** avoids sorting but still takes $O(k)$ time.
- **$k = 1$:** the answer is always `1`.
- **Prefix clipped by `n`:** use $n + 1$ as the exclusive upper bound in subtree counts.
- **Powers of ten:** descending from `1` correctly visits `10`, `100`, and deeper prefixes before sibling `2`.

</details>
