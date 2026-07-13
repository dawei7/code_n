# Get the Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1537 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [get-the-maximum-score](https://leetcode.com/problems/get-the-maximum-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/get-the-maximum-score/).

### Goal
Walk through two strictly increasing arrays, switching from one array to the
other only at shared values, and maximize the sum of visited values.

### Function Contract
**Inputs**

- `nums1`: the first strictly increasing array.
- `nums2`: the second strictly increasing array.

**Return value**

The maximum score modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums1 = [2, 4, 5, 8, 10], nums2 = [4, 6, 8, 9]`
- Output: `30`

**Example 2**

- Input: `nums1 = [1, 3, 5, 7, 9], nums2 = [3, 5, 100]`
- Output: `109`

**Example 3**

- Input: `nums1 = [1, 2, 3, 4, 5], nums2 = [6, 7, 8, 9, 10]`
- Output: `40`

---

## Solution
### Approach
Use two pointers and accumulate segment sums between common values. When a common
value is reached, add the larger of the two segment sums plus the shared value,
then reset both segment sums. After the scan, add the larger remaining segment.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1, nums2):
    mod = 10**9 + 7
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    a = sorted(nums1)
    b = sorted(nums2)
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sum1 += a[i]
            i += 1
        elif a[i] > b[j]:
            sum2 += b[j]
            j += 1
        else:
            value = a[i]
            block1 = 0
            while i < len(a) and a[i] == value:
                block1 += a[i]
                i += 1
            block2 = 0
            while j < len(b) and b[j] == value:
                block2 += b[j]
                j += 1
            best = max(sum1, sum2) + max(block1, block2)
            sum1 = best
            sum2 = best
    sum1 += sum(a[i:])
    sum2 += sum(b[j:])
    return max(sum1, sum2) % mod
```
</details>
