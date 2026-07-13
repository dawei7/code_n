# Earliest Second to Mark Indices I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3048 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [earliest-second-to-mark-indices-i](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/earliest-second-to-mark-indices-i/).

### Goal
Given an array of target values representing the number of decrements required for each index and a sequence of indices to be marked, determine the earliest second (1-indexed) by which all indices can be marked. At each second, you can either decrement a target value at a specific index or mark an index if its target value has reached zero.

### Function Contract
**Inputs**

- `nums`: A list of integers where `nums[i]` is the number of decrements needed for index `i+1`.
- `changeIndices`: A list of integers representing the index to be potentially marked at each second.

**Return value**

- An integer representing the minimum time (1-indexed) required to mark all indices, or -1 if it is impossible.

### Examples
**Example 1**

- Input: `nums = [2, 2, 0], changeIndices = [2, 2, 2, 2, 3, 2, 2, 1]`
- Output: `8`

**Example 2**

- Input: `nums = [1, 3], changeIndices = [1, 1, 1, 2, 1, 1, 1]`
- Output: `6`

**Example 3**

- Input: `nums = [0, 1], changeIndices = [2, 2, 2, 1]`
- Output: `4`

---

## Solution
### Approach
The problem exhibits a monotonic property: if it is possible to mark all indices by time `T`, it is also possible for any time `T' > T`. This allows the use of **Binary Search on the Answer**. For a fixed time `T`, we verify feasibility by greedily processing the `changeIndices` in reverse: we prioritize marking an index as late as possible to maximize the time available for decrements.

### Complexity Analysis
- **Time Complexity**: `O(M log M)`, where `M` is the length of `changeIndices`. The binary search runs in `O(log M)` steps, and each check takes `O(M)` time.
- **Space Complexity**: `O(N + M)`, where `N` is the length of `nums` and `M` is the length of `changeIndices`, used to store the last occurrence of each index and the state during the check.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], changeIndices: list[int]) -> int:
    n = len(nums)
    m = len(changeIndices)

    def check(time: int) -> bool:
        # last_occurrence stores the latest second an index can be marked
        last_occurrence = [-1] * (n + 1)
        for i in range(time):
            last_occurrence[changeIndices[i]] = i

        # If any index never appears in the first 'time' seconds, we can't mark it
        if -1 in last_occurrence[1:]:
            return False

        # Sort indices by their last occurrence to process greedily
        # We need to perform nums[i] decrements before the last_occurrence[i+1]
        needed = list(nums)
        events = sorted([(last_occurrence[i + 1], i) for i in range(n)])

        decrements_available = 0
        current_time = 0

        for deadline, idx in events:
            # Time available for decrements before this deadline
            # is the time elapsed minus time spent marking previous indices
            time_to_use = deadline - current_time
            if time_to_use < needed[idx]:
                return False

            # We use 'needed[idx]' seconds to decrement, and 1 second to mark
            current_time += needed[idx] + 1

        return True

    low = 1
    high = m
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```
</details>
