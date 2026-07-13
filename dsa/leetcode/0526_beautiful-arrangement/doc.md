# Beautiful Arrangement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 526 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/beautiful-arrangement/) |

## Problem Description
### Goal
Given a positive integer `n`, arrange every integer from `1` through `n` exactly once into one-based positions. An arrangement is beautiful when, at every position `i`, either the value stored there is divisible by `i` or `i` is divisible by that value.

Return the number of different beautiful arrangements. Position order matters, so swapping values creates another permutation when the divisibility rules still hold. Every position must satisfy at least one direction of divisibility; meeting the rule only for adjacent pairs or for a subset of positions is insufficient. The function returns the count rather than the permutations themselves.

### Function Contract
**Inputs**

- `n`: the positive upper bound of the values and the permutation length

**Return value**

- The number of permutations satisfying the divisibility condition at every position

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1`

**Example 2**

- Input: `n = 2`
- Output: `2`

**Example 3**

- Input: `n = 4`
- Output: `8`

### Required Complexity

- **Time:** $O(n \cdot 2^n)$
- **Space:** $O(2^n)$

<details>
<summary>Approach</summary>

#### General

**Build only arrangements that can remain valid**

Fill the permutation from position `1` toward position `n`. At a position, try only unused values for which either the value divides the position or the position divides the value. Rejecting an incompatible value immediately avoids generating complete invalid permutations.

**Represent the chosen values with a bitmask**

Bit `value - 1` records whether `value` has already been placed. The number of set bits determines the next position, so the used-value mask completely describes a subproblem; the order that produced the mask cannot affect which continuations are legal.

**Memoize each remaining subproblem**

Different valid prefixes can select the same set of values in different orders. Cache the number of completions for each mask so those prefixes share one calculation. For a mask, sum the cached completion counts reached by placing every compatible unused value. The full mask contributes one completed arrangement.

**Why the sum counts every beautiful arrangement exactly once**

Every explored branch adds one unused value at the next fixed position and checks that position's condition, so a branch reaching the full mask is valid. Conversely, each valid permutation selects one of the explored compatible values at every position and therefore follows a unique root-to-leaf branch. Summing the child counts neither omits nor duplicates a valid permutation.

#### Complexity detail

There are at most $2^{n}$ masks. Each mask examines up to `n` candidate values, giving $O(n \cdot 2^n)$ time. The memo table stores at most one count per mask for $O(2^n)$ space; the recursion depth is $O(n)$ and is dominated by the cache.

#### Alternatives and edge cases

- **Bottom-up subset dynamic programming:** propagates counts between masks with the same $O(n \cdot 2^n)$ bounds, but may visit masks that the divisibility restrictions make unreachable.
- **Backtracking without memoization:** prunes incompatible placements but recomputes identical remaining-value subproblems and can approach factorial time.
- **Generate every permutation:** checks conditions only after or during generation and has an $O(n!)$ search space without state reuse.
- **Place constrained positions first:** can reduce branching in plain backtracking, but the position is no longer implied by the mask and the ordering must be tracked carefully.
- **$n = 1$:** the only permutation is valid because one divides itself.
- **Value equal to position:** always passes both divisibility directions.
- **Divisibility direction:** the condition is inclusive OR; either `value % position = 0` or `position % value = 0` is sufficient.

</details>
