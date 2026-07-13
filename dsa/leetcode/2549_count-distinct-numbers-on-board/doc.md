# Count Distinct Numbers on Board

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2549 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-distinct-numbers-on-board](https://leetcode.com/problems/count-distinct-numbers-on-board/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-distinct-numbers-on-board/).

### Goal
Given an initial integer `n` placed on a board, repeatedly perform a process where for every number `x` currently on the board, you find an integer `i` (where `1 <= i <= n`) such that `x % i == 1`. If such an `i` exists, add `i` to the board. This process continues until no new numbers can be added. The goal is to return the total count of distinct numbers present on the board once the process stabilizes.

### Function Contract
**Inputs**

- `n` (int): The initial integer placed on the board.

**Return value**

- (int): The total number of unique integers present on the board after the process concludes.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `4`
- Explanation: Initially, 5 is on the board. 5 % 4 = 1, so 4 is added. 4 % 3 = 1, so 3 is added. 3 % 2 = 1, so 2 is added. The board contains {5, 4, 3, 2}.

**Example 2**

- Input: `n = 3`
- Output: `2`
- Explanation: Initially, 3 is on the board. 3 % 2 = 1, so 2 is added. The board contains {3, 2}.

**Example 3**

- Input: `n = 1`
- Output: `1`
- Explanation: No integer `i` exists such that 1 % i = 1 for 1 <= i <= 1. The board contains only {1}.

---

## Solution
### Approach
Mathematical observation. For any `n > 2`, the process will eventually add all integers from `2` to `n` to the board. Specifically, `n % (n-1) = 1`, and subsequently `(n-1) % (n-2) = 1`, and so on, down to `3 % 2 = 1`. Thus, for `n > 2`, the answer is `n - 1`. For `n = 1`, the answer is `1`.

### Complexity Analysis
- **Time Complexity**: O(1), as the result is derived from a constant-time mathematical formula.
- **Space Complexity**: O(1), as no additional data structures are required.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int) -> int:
    """
    Calculates the number of distinct integers on the board.
    For n = 1, the result is 1.
    For n > 1, the result is n - 1 because all integers from 2 to n
    will eventually be added to the board.
    """
    if n == 1:
        return 1
    return n - 1
```
</details>
