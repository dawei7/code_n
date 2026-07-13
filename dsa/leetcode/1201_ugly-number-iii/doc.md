# Ugly Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Binary Search, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [ugly-number-iii](https://leetcode.com/problems/ugly-number-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/ugly-number-iii/).

### Goal
Return the `n`th positive integer that is divisible by at least one of `a`, `b`, or `c`.

### Function Contract
**Inputs**

- `n`: 1-indexed position to find.
- `a`, `b`, `c`: Positive divisors.

**Return value**

The `n`th number divisible by `a`, `b`, or `c`.

### Examples
**Example 1**

- Input: `n = 3`, `a = 2`, `b = 3`, `c = 5`
- Output: `4`

**Example 2**

- Input: `n = 4`, `a = 2`, `b = 3`, `c = 4`
- Output: `6`

**Example 3**

- Input: `n = 5`, `a = 2`, `b = 11`, `c = 13`
- Output: `10`

---

## Solution
### Approach
Binary search the answer. For a candidate value `x`, count how many positive integers `<= x` are divisible by at least one of `a`, `b`, or `c`.

Use inclusion-exclusion with least common multiples:

- `x/a + x/b + x/c`
- subtract counts divisible by pairwise lcms
- add the count divisible by the lcm of all three

The smallest `x` whose count is at least `n` is the answer.

### Complexity Analysis
- **Time Complexity**: `O(log answer)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
