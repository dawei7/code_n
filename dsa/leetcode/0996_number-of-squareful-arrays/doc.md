# Number of Squareful Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 996 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-squareful-arrays/) |

## Problem Description

### Goal

An array is squareful when the sum of every pair of adjacent elements is a perfect square. Given an integer array `nums`, count how many distinct permutations of all its elements are squareful.

Two permutations are different only when their values differ at some index. Consequently, exchanging two equal input occurrences does not create another permutation, while placing different values in a different order may do so. Return the number of value sequences that satisfy the adjacency condition throughout.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le12$ and $0\le\texttt{nums[i]}\le10^9$.

Let $U$ be the number of distinct values in `nums`.

**Return value**

- The number of distinct permutations in which every adjacent pair has a perfect-square sum.

### Examples

**Example 1**

- Input: `nums = [1, 17, 8]`
- Output: `2`
- Explanation: `[1, 8, 17]` and `[17, 8, 1]` are the valid permutations.

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `1`
- Explanation: The only distinct permutation is squareful because every adjacent sum is $4$.

**Example 3**

- Input: `nums = [1, 1, 8]`
- Output: `1`
- Explanation: Only `[1, 8, 1]` avoids the nonsquare adjacent sum $1+1$.

### Required Complexity

- **Time:** $O(N!)$
- **Space:** $O(N+U^2)$

<details>
<summary>Approach</summary>

#### General

**Represent equal occurrences by a count:** Build a frequency map instead of choosing among input indices. At each backtracking level, choose one distinct value whose remaining count is positive, decrement that count, recurse, and restore it afterward. Equal occurrences therefore lead through one branch rather than producing duplicate permutations that would need later division or deduplication.

**Precompute legal value transitions:** For every ordered pair of distinct-value keys, use the integer square root of their sum to test whether the sum is a perfect square. Store the values that may follow each value. Once the first position has been chosen, a candidate can be appended only when it is a legal neighbor of the previous value.

Every completed length-$N$ branch is squareful because each extension checked its new adjacent pair. Conversely, every distinct squareful permutation determines exactly one sequence of frequency choices, so the search counts it once. Invalid prefixes stop immediately and cannot become valid after more values are appended.

#### Complexity detail

In the worst case all $N$ values are distinct and every pair is compatible, so the search visits $O(N!)$ completed orders. The recursion stack holds $O(N)$ frames, and frequencies plus the distinct-value transition graph use $O(U^2)$ stored relationships; because $U\le N\le12$, the package reports the dominant working-state bound as $O(N+U^2)$.

#### Alternatives and edge cases

- **Enumerate every index permutation:** Testing all $N!$ index orders counts equal occurrences repeatedly and needs a set or factorial correction to recover distinct value sequences.
- **Bitmask dynamic programming:** A state keyed by used indices and last index can run in $O(N^2 2^N)$ time, but duplicate values require careful symmetry handling.
- **Single element:** The adjacency condition is vacuously true, so the only permutation counts.
- **Repeated values:** A repeated value may follow itself only when twice that value is a perfect square.
- **Zero sum:** Zero is a perfect square, so adjacent zeros are compatible.

</details>
