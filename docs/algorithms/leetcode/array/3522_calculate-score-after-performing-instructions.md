# Calculate Score After Performing Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3522 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Simulation |
| Official Link | [calculate-score-after-performing-instructions](https://leetcode.com/problems/calculate-score-after-performing-instructions/) |

## Problem Description & Examples
### Goal
Given a string of instructions consisting of 'L', 'R', and 'U', calculate the final score based on a stack-based mechanism. When 'L' or 'R' is encountered, push the character onto a stack. When 'U' is encountered, remove the most recently added 'L' or 'R' from the stack (if any exist) and add the numerical value associated with that character (L=1, R=2) to the total score.

### Function Contract
**Inputs**

- `s`: A string containing only the characters 'L', 'R', and 'U'.

**Return value**

- An integer representing the total accumulated score after processing all instructions.

### Examples
**Example 1**

- Input: `s = "LRU"`
- Output: `2`
- Explanation: 'L' is pushed, 'R' is pushed. 'U' removes 'R' (value 2). Total = 2.

**Example 2**

- Input: `s = "UL"`
- Output: `0`
- Explanation: 'U' has no preceding 'L' or 'R' to remove. 'L' is pushed but never removed. Total = 0.

**Example 3**

- Input: `s = "LLRU"`
- Output: `2`
- Explanation: 'L', 'L', 'R' are pushed. 'U' removes 'R' (value 2). Total = 2.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Stack** data structure. By treating the string as a sequence of operations, we maintain a stack of characters. 'L' and 'R' are pushed onto the stack, while 'U' acts as a pop operation that triggers a score update based on the popped element's value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the string, as we iterate through the string exactly once and perform constant-time stack operations.
- **Space Complexity**: `O(n)` in the worst case where all characters are 'L' or 'R' and are pushed onto the stack.
