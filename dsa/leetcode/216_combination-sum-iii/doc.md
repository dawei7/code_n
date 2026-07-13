# Combination Sum III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 216 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum-iii/) |

## Problem Description
### Goal
Choose exactly `k` distinct integers from the fixed set `1` through `9` so that their sum is exactly `n`. Each available number may appear at most once in a combination, and selection order does not create a different combination.

Return every valid combination exactly once, writing the values inside each combination in increasing order. The outer result may appear in any order. Exclude selections with too few or too many values even if their sum matches, and return an empty list when no size-`k` subset reaches `n`. Values outside `1..9`, repeated selections, and permutations of an existing combination are not valid additions.

### Function Contract
**Inputs**

- `k`: required number of selected values
- `n`: required sum

**Return value**

All valid increasing combinations, each once.

### Examples
**Example 1**

- Input: `k = 3, n = 7`
- Output: `[[1,2,4]]`

**Example 2**

- Input: `k = 3, n = 9`
- Output: `[[1,2,6],[1,3,5],[2,3,4]]`

**Example 3**

- Input: `k = 4, n = 1`
- Output: `[]`

### Required Complexity

- **Time:** $O(C(9,k)k)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

Backtrack over the fixed candidates `1` through `9`, always choosing the next value strictly after the previous choice. The state consists of the next permitted candidate, the remaining number of slots, the remaining sum, and the current path.

Increasing choices serve two purposes at once: a digit cannot be reused, and one mathematical combination is generated in only one order. After choosing `3`, for example, recursion may consider `4..9` but never return to `1` or choose `3` again.

Accept a path only when it contains exactly `k` values and the remaining sum is zero. Several bounds can prune impossible branches early:

- A negative remaining sum cannot recover because all future values are positive.
- Fewer available candidates than remaining slots makes completion impossible.
- The sum of the smallest possible remaining choices may already exceed the target.
- The sum of the largest possible remaining choices may still fall short.

For $k = 3, n = 9$, the increasing paths that finish exactly are `[1,2,6]`, `[1,3,5]`, and `[2,3,4]`. Permutations such as `[6,2,1]` are never generated.

Every emitted path contains exactly `k` distinct values from `1..9`, is increasing, and has sum `n`, so it is valid. Conversely, every valid combination has one unique increasing ordering. At each depth, the recursion includes the branch choosing that ordering's next value; none of the sound pruning rules can remove it because its remaining choices prove the relevant bounds feasible. The recursion therefore reaches and emits every valid combination exactly once.

#### Complexity detail

The fixed universe contains at most `C(9,k)` size-`k` subsets, and copying each successful path costs $O(k)$, giving the stated $O(\binom{9}{k}k)$ output-sensitive bound. The current path and recursion depth use $O(k)$ auxiliary space, excluding returned combinations.

#### Alternatives and edge cases

- Generating permutations repeats each combination up to $k!$ times.
- Allowing the same candidate in recursive calls violates distinctness and solves a different Combination Sum variant.
- Dynamic programming can count possibilities but is unnecessary for enumerating this tiny fixed domain.
- Targets below the sum of `1..k` or above the sum of the largest `k` digits return empty.
- Selecting all nine values is possible only for sum `45`; impossible `k` values naturally yield no combinations.

</details>
