# Decompress Run-Length Encoded List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1313 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [decompress-run-length-encoded-list](https://leetcode.com/problems/decompress-run-length-encoded-list/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/decompress-run-length-encoded-list/).

### Goal
Decode a run-length encoded list where each pair `[freq, value]` expands to `freq` copies of `value`.

### Function Contract
**Inputs**

- `nums`: even-length encoded integer array.

**Return value**

The decompressed array.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[2,4,4,4]`

**Example 2**

- Input: `nums = [1,1,2,3]`
- Output: `[1,3,3]`

**Example 3**

- Input: `nums = [2,5,1,9]`
- Output: `[5,5,9]`

---

## Solution
### Approach
Run-length expansion.

### Complexity Analysis
- **Time Complexity**: `O(output length)`
- **Space Complexity**: `O(output length)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    result = []
    for i in range(0, len(nums), 2):
        result.extend([nums[i + 1]] * nums[i])
    return result
```
</details>
