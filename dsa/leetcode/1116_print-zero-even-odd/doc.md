# Print Zero Even Odd

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1116 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [print-zero-even-odd](https://leetcode.com/problems/print-zero-even-odd/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/print-zero-even-odd/).

### Goal
Coordinate three threads so they print the sequence `010203...0n`. One thread prints zeros, one prints odd numbers, and one prints even numbers.

### Concurrency Contract
**Inputs**

- `n`: Highest number to print.
- `zero(printNumber)`: Method that prints `0` before every number.
- `odd(printNumber)`: Method that prints odd numbers.
- `even(printNumber)`: Method that prints even numbers.

**Required output order**

For each number from `1` to `n`, print `0` followed by that number.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `"0102"`

**Example 2**

- Input: `n = 5`
- Output: `"0102030405"`

**Example 3**

- Input: `n = 1`
- Output: `"01"`

---

## Solution
### Approach
Use three synchronization signals: one for `zero`, one for `odd`, and one for `even`. Initially only `zero` may run. After printing `0`, the zero thread opens the odd or even signal depending on the next number. The number-printing thread prints that number and then reopens the zero signal.

This handoff repeats until all numbers from `1` through `n` have been printed.

### Complexity Analysis
- **Time Complexity**: `O(n)` total number-printing rounds.
- **Space Complexity**: `O(1)` synchronization state.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
