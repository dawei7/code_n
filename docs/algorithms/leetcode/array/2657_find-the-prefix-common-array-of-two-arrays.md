# Find the Prefix Common Array of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2657 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Bit Manipulation |
| Official Link | [find-the-prefix-common-array-of-two-arrays](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) |

## Problem Description & Examples
### Goal
Given two integer arrays, `A` and `B`, of the same length `n`, both of which are permutations of integers from `1` to `n`. The task is to construct a result array `C` of length `n`. For each index `i` from `0` to `n-1`, `C[i]` should represent the count of unique integers that are present in both the prefix subarray `A[0...i]` and the prefix subarray `B[0...i]`.

### Function Contract
**Inputs**

- `A`: `List[int]` - An array of `n` integers. `A` is a permutation of `[1, ..., n]`.
- `B`: `List[int]` - An array of `n` integers. `B` is a permutation of `[1, ..., n]`.
  - Constraints:
    - `n == A.length == B.length`
    - `1 <= n <= 50`
    - `1 <= A[i], B[i] <= n`

**Return value**

- `List[int]` - An array `C` of length `n`, where `C[i]` is the count of common unique elements in `A[0...i]` and `B[0...i]`.

### Examples
**Example 1**

- Input: `A = [1,2,3,6,5,4]`, `B = [2,3,1,4,5,6]`
- Output: `[0,1,3,3,4,6]`
  - Explanation:
    - `i = 0`: `A[0...0] = {1}`, `B[0...0] = {2}`. Common: `{}`. Count = 0.
    - `i = 1`: `A[0...1] = {1,2}`, `B[0...1] = {2,3}`. Common: `{2}`. Count = 1.
    - `i = 2`: `A[0...2] = {1,2,3}`, `B[0...2] = {2,3,1}`. Common: `{1,2,3}`. Count = 3.
    - `i = 3`: `A[0...3] = {1,2,3,6}`, `B[0...3] = {2,3,1,4}`. Common: `{1,2,3}`. Count = 3.
    - `i = 4`: `A[0...4] = {1,2,3,6,5}`, `B[0...4] = {2,3,1,4,5}`. Common: `{1,2,3,5}`. Count = 4.
    - `i = 5`: `A[0...5] = {1,2,3,6,5,4}`, `B[0...5] = {2,3,1,4,5,6}`. Common: `{1,2,3,4,5,6}`. Count = 6.

**Example 2**

- Input: `A = [2,3,4,5,1]`, `B = [1,2,3,4,5]`
- Output: `[0,1,2,3,5]`
  - Explanation:
    - `i = 0`: `A[0...0] = {2}`, `B[0...0] = {1}`. Common: `{}`. Count = 0.
    - `i = 1`: `A[0...1] = {2,3}`, `B[0...1] = {1,2}`. Common: `{2}`. Count = 1.
    - `i = 2`: `A[0...2] = {2,3,4}`, `B[0...2] = {1,2,3}`. Common: `{2,3}`. Count = 2.
    - `i = 3`: `A[0...3] = {2,3,4,5}`, `B[0...3] = {1,2,3,4}`. Common: `{2,3,4}`. Count = 3.
    - `i = 4`: `A[0...4] = {2,3,4,5,1}`, `B[0...4] = {1,2,3,4,5}`. Common: `{1,2,3,4,5}`. Count = 5.

**Example 3**

- Input: `A = [1,2,3]`, `B = [1,2,3]`
- Output: `[1,2,3]`
  - Explanation:
    - `i = 0`: `A[0...0] = {1}`, `B[0...0] = {1}`. Common: `{1}`. Count = 1.
    - `i = 1`: `A[0...1] = {1,2}`, `B[0...1] = {1,2}`. Common: `{1,2}`. Count = 2.
    - `i = 2`: `A[0...2] = {1,2,3}`, `B[0...2] = {1,2,3}`. Common: `{1,2,3}`. Count = 3.

---

## Underlying Base Algorithm(s)
The core idea is to iterate through the arrays from left to right, maintaining the set of unique elements encountered so far in `A`'s prefix and `B`'s prefix. Since the problem constraints specify that `A` and `B` contain integers from `1` to `n`, we can use boolean arrays (or frequency arrays) instead of hash sets for efficient O(1) lookups and updates.

The algorithm proceeds as follows:
1.  Initialize two boolean arrays, `seen_A` and `seen_B`, of size `n+1` (to accommodate 1-indexed values up to `n`), all set to `False`. These arrays will track which numbers have appeared in the current prefix of `A` and `B`, respectively.
2.  Initialize a counter `common_count` to `0`. This counter will store the number of unique elements common to both prefixes `A[0...i]` and `B[0...i]`.
3.  Initialize an empty list `C` of size `n` to store the results.
4.  Iterate `i` from `0` to `n-1`:
    a.  Get `val_A = A[i]` and `val_B = B[i]`.
    b.  **Process `val_A`**:
        i.  If `val_A` has not been seen in `A`'s prefix yet (`seen_A[val_A]` is `False`):
            1.  Mark `seen_A[val_A]` as `True`.
            2.  If `val_A` has already been seen in `B`'s prefix (`seen_B[val_A]` is `True`), it means `val_A` is now present in both prefixes. Increment `common_count`.
    c.  **Process `val_B`**:
        i.  If `val_B` has not been seen in `B`'s prefix yet (`seen_B[val_B]` is `False`):
            1.  Mark `seen_B[val_B]` as `True`.
            2.  If `val_B` has already been seen in `A`'s prefix (`seen_A[val_B]` is `True`), it means `val_B` is now present in both prefixes. Increment `common_count`.
    d.  Store the current `common_count` in `C[i]`.
5.  Return the array `C`.

This approach ensures that `common_count` is correctly updated when a number appears for the first time in either `A`'s or `B`'s prefix, and that number is already present in the other array's prefix.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
  - The algorithm iterates through the arrays `A` and `B` once, from `i = 0` to `n-1`.
  - Inside the loop, operations like array access, boolean checks, and assignments (`seen_A[val] = True`, `seen_B[val] = True`, `common_count += 1`) all take constant time, `O(1)`.
  - Therefore, the total time complexity is `n * O(1) = O(n)`.
- **Space Complexity**: `O(n)`
  - Two boolean arrays, `seen_A` and `seen_B`, are used, each of size `n+1`. This contributes `O(n)` space.
  - The result array `C` also stores `n` integers, contributing `O(n)` space.
  - Thus, the total space complexity is `O(n)`.
