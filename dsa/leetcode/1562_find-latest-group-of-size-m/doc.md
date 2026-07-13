# Find Latest Group of Size M

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1562 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-latest-group-of-size-m](https://leetcode.com/problems/find-latest-group-of-size-m/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-latest-group-of-size-m/).

### Goal
Bits are turned from `0` to `1` in the order given by `arr`. Find the latest step
where there exists a contiguous group of exactly `m` ones.

### Function Contract
**Inputs**

- `arr`: the 1-based positions turned on at each step.
- `m`: the target group length.

**Return value**

The latest step containing a group of exactly `m` ones, or `-1` if it never
happens.

### Examples
**Example 1**

- Input: `arr = [3, 5, 1, 2, 4], m = 1`
- Output: `4`

**Example 2**

- Input: `arr = [3, 1, 5, 4, 2], m = 2`
- Output: `-1`

**Example 3**

- Input: `arr = [1, 2, 3], m = 3`
- Output: `3`

---

## Solution
### Approach
Maintain the lengths of one-groups at their boundary positions and a count of
how many groups currently have each length. When turning on position `x`, merge
the group ending at `x - 1` and the group starting at `x + 1`, update the length
counts, and record the step whenever the count for length `m` is positive.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr, m):
    n = len(arr)
    if m <= 0:
        return -1
    if m == n:
        return n
    length = [0] * (n + 2)
    active = [False] * (n + 2)
    count = 0
    answer = -1
    for step, raw_pos in enumerate(arr, 1):
        if not 1 <= raw_pos <= n or active[raw_pos]:
            if count > 0:
                answer = step
            continue
        active[raw_pos] = True
        left = length[raw_pos - 1]
        right = length[raw_pos + 1]
        merged = left + 1 + right
        if left == m:
            count -= 1
        if right == m:
            count -= 1
        if merged == m:
            count += 1
        length[raw_pos - left] = merged
        length[raw_pos + right] = merged
        length[raw_pos] = merged
        if count > 0:
            answer = step
    return answer
```
</details>
