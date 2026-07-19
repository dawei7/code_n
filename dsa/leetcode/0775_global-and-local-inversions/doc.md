# Global and Local Inversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 775 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/global-and-local-inversions/) |

## Problem Description

### Goal

Given a permutation `nums` of the integers from `0` through $n - 1$, a global inversion is a pair of indices $i < j$ with `nums[i] > nums[j]`. A local inversion is a global inversion whose indices are adjacent, so $j = i + 1$.

Return `True` if the number of global inversions equals the number of local inversions, and `False` otherwise. Since every local inversion is already global, equality means that no inversion may span a distance greater than one index.

### Function Contract

**Inputs**

- `nums`: a nonempty permutation of `0, 1, ..., len(nums) - 1`.

**Return value**

- `True` when every global inversion is local; otherwise `False`.

### Examples

**Example 1**

- Input: `nums = [1,0,2]`
- Output: `True`
- Explanation: The only inversion is the adjacent pair `(1,0)`.

**Example 2**

- Input: `nums = [1,2,0]`
- Output: `False`
- Explanation: `(1,0)` spans two indices and is a nonlocal global inversion.

**Example 3**

- Input: `nums = [1,0,3,2]`
- Output: `True`
- Explanation: Both inversions are disjoint adjacent swaps.
