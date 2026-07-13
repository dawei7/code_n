# Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 46 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutations/) |

## Problem Description
### Goal
You are given an array `nums` whose integers are all unique. A permutation is an ordering that contains every input value exactly once and introduces no additional values.

Return the complete collection of permutations. For `n` values there are $n!$ results, and each distinct ordering must appear once. The permutations and the collection itself may be listed in any order. A one-element input has one permutation containing that element.

### Function Contract
**Inputs**

- `nums`: `List[int]` of distinct values

**Return value**

A `List[List[int]]` containing all $n!$ permutations.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

**Example 2**

- Input: `nums = [0, 1]`
- Output: `[[0, 1], [1, 0]]`

**Example 3**

- Input: `nums = [1]`
- Output: `[[1]]`

### Required Complexity

- **Time:** $O(n \cdot n!)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Fix one array position at each recursion depth**

At recursion position `first`, swap each value from indices `first` onward into that position, recursively permute the suffix, then swap back. Swapping selects a value without allocating a separate remaining-values list. When `first = len(nums)`, copy the complete ordering into the result.

Distinct input values guarantee every choice at a depth creates a different prefix, so no duplicate tracking is needed.

**Swap-back restores the parent's exact choice set**

On entry to depth `first`, positions before `first` are fixed to a unique chosen prefix, while the suffix contains exactly the unused values in some order. Swapping selects one unused value, recursion completes the remaining positions, and swapping back restores both values to their original parent-state positions before the next sibling branch.

The leaf must append a copy. Appending the mutable working array itself would make every result entry refer to the same object and eventually show the final restored order.

**Trace the first-position branches**

For `[1, 2, 3]`, fixing 1 first produces suffix orders `[2, 3]` and `[3, 2]`. Backtracking then fixes 2 and 3 first in turn, each with both suffix orders, yielding all six permutations.

**Each permutation determines one swap path**

At recursion depth `i`, the prefix before `i` is fixed and the suffix contains exactly the unused distinct values. Swapping one suffix value into position `i` preserves that partition; reaching depth `n` therefore produces a valid arrangement containing every input once.

Any target permutation uniquely determines which remaining value must be swapped into each successive position. The search enumerates that choice at every depth, so it follows the target's path and emits it. Distinct input values prevent two different swap-choice paths from producing the same permutation.

#### Complexity detail

There are $n!$ outputs and copying each length-`n` permutation costs $O(n)$, so $O(n \cdot n!)$ time is output-optimal. The recursion depth is `n` and swaps are in place, using $O(n)$ auxiliary stack space; output storage is $O(n \cdot n!)$.

#### Alternatives and edge cases

- **Build a path with a used set:** has the same complexity but stores an additional $O(n)$ membership structure.
- **Generate all length-n sequences then filter repeats:** explores $n^{n}$ sequences and wastes substantial work.
- **Lexicographic next-permutation iteration:** can enumerate permutations iteratively after sorting, but still must copy all outputs and is less direct for arbitrary input order.
- A one-value input has one permutation. Under the mathematical convention, an empty input has one empty permutation, though the challenge constraints determine whether that case occurs.
- Distinctness is what makes every swap choice at a depth unique; duplicate inputs require the additional canonical-choice logic of problem 47.

</details>
