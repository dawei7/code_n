# Shuffle an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 384 |
| Difficulty | Medium |
| Topics | Array, Math, Design, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/shuffle-an-array/) |

## Problem Description
### Goal
Construct an object from an integer array whose elements are unique, and preserve an immutable copy of its original order. `shuffle()` returns a random permutation of all positions, with every possible permutation equally likely.

`reset()` restores and returns the original ordering exactly as supplied at construction. Repeated shuffle and reset calls operate on the same object without corrupting that baseline, and returned arrays must contain the complete original multiset. Use an unbiased shuffling process rather than repeatedly choosing positions in a way that gives some permutations greater probability.

### Function Contract
**Inputs**

- `nums`: the initial integer array
- `operations`: for the app adapter, a chronological list containing `"shuffle"` and `"reset"`

**Return value**

- The app adapter returns one array for each operation. A reset returns the initial order; a shuffle returns a uniformly random permutation. Native LeetCode invokes the corresponding methods directly.

### Examples
**Example 1**

- Input: `nums = [1,2,3], operations = ["shuffle","reset"]`
- Output: one valid result is `[[2,3,1],[1,2,3]]`

**Example 2**

- Input: `nums = [5], operations = ["shuffle","reset","shuffle"]`
- Output: `[[5],[5],[5]]`

**Example 3**

- Input: `nums = [1,1,2], operations = ["shuffle"]`
- Output: one valid result is `[[1,2,1]]`
