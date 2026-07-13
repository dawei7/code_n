# Sum of All Odd Length Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1588 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-all-odd-length-subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/).

### Goal
Sum the values of every odd-length contiguous subarray.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

The total sum across all odd-length subarrays.

### Examples
**Example 1**

- Input: `arr = [1, 4, 2, 5, 3]`
- Output: `58`

**Example 2**

- Input: `arr = [1, 2]`
- Output: `3`

**Example 3**

- Input: `arr = [10, 11, 12]`
- Output: `66`

---

## Solution
### Approach
For index `i`, count how many subarrays include it:
`(i + 1) * (n - i)`. Half of those, rounded up, have odd length. Multiply that
odd-subarray count by `arr[i]` and add the contribution.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
