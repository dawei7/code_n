# Check If N and Its Double Exist

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1346 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-n-and-its-double-exist/) |

## Problem Description

### Goal

Given an integer array `arr`, determine whether it contains two elements at different indices such that one element is exactly twice the other. More precisely, decide whether there are indices `i` and `j` with $i \ne j$ and `arr[i] == 2 * arr[j]`.

Return `true` when such a pair exists and `false` otherwise. The distinct-index requirement matters for zero and duplicate values: one occurrence cannot be paired with itself.

### Function Contract

**Inputs**

- `arr`: an integer array. Let $n$ be its length.

**Return value**

- Return `true` if two different indices hold values related by an exact factor of two; otherwise return `false`.

### Examples

**Example 1**

- Input: `arr = [10, 2, 5, 3]`
- Output: `true`
- Explanation: The values `10` and `5` occur at different indices and `10 == 2 * 5`.

**Example 2**

- Input: `arr = [3, 1, 7, 11]`
- Output: `false`

**Example 3**

- Input: `arr = [0, 0]`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Match against earlier values.** Scan `arr` once while keeping a set of values already encountered. For a current value `value`, a qualifying earlier partner can have either of two roles: it may equal `2 * value`, or it may be the number whose double is `value`.

The first role is checked directly with `2 * value in seen`. The second is possible only when `value` is even, in which case its exact integer half is `value // 2`. If either partner is present, the current position and the earlier position are distinct by construction, so returning `true` is valid.

Only after both checks fail is `value` inserted into the set. This ordering prevents a single zero from matching itself, while a second zero correctly finds the first. If the scan ends without a match, every pair has been considered when its later member was processed, so no qualifying pair exists.

#### Complexity detail

Each of the $n$ values performs a constant expected number of hash-set operations, giving $O(n)$ expected time. The set can hold $n$ distinct values, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Exhaustive pair search:** Testing every pair uses only constant auxiliary space but requires $O(n^2)$ time when no match exists.
- **Sorting with two pointers or binary search:** Sorting supports an $O(n \log n)$ solution, but it is slower than the direct hash-set scan and may alter the input if done in place.
- **One zero:** A single zero cannot use itself as both indices and must not produce a match.
- **Two zeroes:** Two occurrences satisfy `0 == 2 * 0`.
- **Equal nonzero values:** Duplicate values such as `[5, 5]` do not form a double pair.
- **Negative values:** The same factor-of-two relation applies without any special sign handling.

</details>
