# Last Visited Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2899 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [last-visited-integers](https://leetcode.com/problems/last-visited-integers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/last-visited-integers/).

### Goal
Given a list of strings representing either integers or the string "prev", process the list to track previously encountered integers. When an integer is encountered, store it in a history list. When "prev" is encountered, retrieve the $k$-th most recently added integer, where $k$ is the number of consecutive "prev" strings seen so far. If no such integer exists in the history, return -1.

### Function Contract
**Inputs**

- `nums`: A list of strings where each element is either a string representation of a positive integer or the literal string "prev".

**Return value**

- A list of integers representing the results of each "prev" operation.

### Examples
**Example 1**

- Input: `["1", "2", "prev", "prev", "prev"]`
- Output: `[2, 1, -1]`

**Example 2**

- Input: `["1", "prev", "2", "prev", "prev"]`
- Output: `[1, 2, 1]`

**Example 3**

- Input: `["7", "prev", "prev", "3", "prev"]`
- Output: `[7, -1, 3]`

---

## Solution
### Approach
The problem is solved using a **Simulation** approach with a **Stack** (or a dynamic list) to maintain the history of integers. We maintain a counter for consecutive "prev" occurrences to determine the index of the target integer in the history stack.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input list. We iterate through the list once, and each operation (appending to history or accessing the stack) is $O(1)$.
- **Space Complexity**: $O(n)$ in the worst case, as we may store all integers from the input list in our history stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[str]) -> List[int]:
    history = []
    results = []
    consecutive_prev = 0

    for item in nums:
        if item == "prev":
            consecutive_prev += 1
            # Check if the k-th last element exists
            if consecutive_prev <= len(history):
                # The k-th last element is at index len(history) - k
                results.append(history[-consecutive_prev])
            else:
                results.append(-1)
        else:
            # Reset consecutive count and add integer to history
            consecutive_prev = 0
            history.append(int(item))

    return results
```
</details>
