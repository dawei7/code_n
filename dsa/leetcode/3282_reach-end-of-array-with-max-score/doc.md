# Reach End of Array With Max Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3282 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reach-end-of-array-with-max-score](https://leetcode.com/problems/reach-end-of-array-with-max-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reach-end-of-array-with-max-score/).

### Goal
Given an array of integers, you start at the first index and must reach the last index. From any current index `i`, you can jump to any index `j > i`. The score gained from a jump is calculated as `(j - i) * nums[i]`. The objective is to maximize the total score accumulated by the time you reach the final index.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers representing the values at each position.

**Return value**

- An integer representing the maximum possible score to reach the last index.

### Examples
**Example 1**

- Input: `nums = [1, 3, 1, 5]`
- Output: `7`
- Explanation: Jump from index 0 to 1 (score: 1*1=1), then from 1 to 3 (score: 2*3=6). Total = 7.

**Example 2**

- Input: `nums = [4, 3, 1, 3, 2]`
- Output: `16`
- Explanation: Jump from index 0 to 3 (score: 3*4=12), then from 3 to 4 (score: 1*2=2). Total = 14? No, jump 0 to 4 (score: 4*4=16).

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `2`
- Explanation: Jump from 0 to 1 (1*1=1), then 1 to 2 (1*1=1). Total = 2.

---

## Solution
### Approach
The problem is solved using a **Greedy approach**. Since we want to maximize `(j - i) * nums[i]`, we should always aim to jump to the furthest possible index that has a value greater than or equal to our current position's value, or simply keep track of the "best" value seen so far to maximize the jump distance. By iterating through the array and maintaining the maximum value encountered, we can greedily accumulate the score.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform a single pass through the input.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the current score and the maximum value.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    """
    Calculates the maximum score to reach the end of the array.
    We iterate through the array and keep track of the maximum value seen so far.
    Every step, we add the current maximum value to our total score,
    effectively simulating jumps from the best previous position.
    """
    total_score = 0
    current_max = 0

    # We iterate up to the second to last element because
    # we must land on the last index.
    for i in range(len(nums) - 1):
        current_max = max(current_max, nums[i])
        total_score += current_max

    return total_score
```
</details>
