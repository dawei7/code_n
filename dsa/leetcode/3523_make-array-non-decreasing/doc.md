# Make Array Non-decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3523 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [make-array-non-decreasing](https://leetcode.com/problems/make-array-non-decreasing/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/make-array-non-decreasing/).

### Goal
Determine the minimum number of rounds required to transform an array into a non-decreasing sequence. In each round, every element that is strictly smaller than the element immediately preceding it is removed from the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial sequence.

**Return value**

- An integer representing the total number of rounds needed until the array becomes non-decreasing.

### Examples
**Example 1**

- Input: `nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]`
- Output: `3`

**Example 2**

- Input: `nums = [4, 5, 7, 7, 13]`
- Output: `0`

**Example 3**

- Input: `nums = [10, 1, 2, 3, 4, 5]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Monotonic Stack**. Each element in the stack stores a pair: the value itself and the number of rounds it takes for that specific element to be "eliminated" (or survive). For each element, we determine how many rounds it would take to be removed by comparing it with the elements currently in the stack. If an element is greater than the top of the stack, it will be removed in the next round, and we calculate the maximum rounds needed based on the elements it "covers."

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is pushed and popped from the stack at most once.
- **Space Complexity**: `O(n)` to store the stack in the worst-case scenario where the array is strictly decreasing.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    # The stack stores tuples of (value, rounds_to_be_removed)
    # rounds_to_be_removed is the number of rounds until this element is deleted.
    stack = []
    max_rounds = 0

    for x in nums:
        rounds = 0
        # While the current element is smaller than the top of the stack,
        # it will be removed by the element at the top of the stack.
        while stack and stack[-1][0] <= x:
            rounds = max(rounds, stack.pop()[1])

        if stack:
            # If the stack is not empty, the current element will be removed
            # in (rounds + 1) steps because it is smaller than the element
            # currently at the top of the stack.
            rounds += 1
        else:
            # If the stack is empty, this element will never be removed.
            rounds = 0

        max_rounds = max(max_rounds, rounds)
        stack.append((x, rounds))

    return max_rounds
```
</details>
