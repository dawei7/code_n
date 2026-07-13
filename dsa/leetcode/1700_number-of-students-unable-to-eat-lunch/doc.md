# Number of Students Unable to Eat Lunch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1700 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Stack, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-students-unable-to-eat-lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/).

### Goal
Students in a queue prefer either circular or square sandwiches, and sandwiches are served from a stack. A student takes the top sandwich only if it matches their preference; otherwise they move to the back. Count the students who cannot eat.

### Function Contract
**Inputs**

- `students`: a list of `0` and `1` preferences.
- `sandwiches`: a list of `0` and `1` sandwich types from top to bottom.

**Return value**

Return the number of students left unable to take a sandwich.

### Examples
**Example 1**

- Input: `students = [1,1,0,0], sandwiches = [0,1,0,1]`
- Output: `0`

**Example 2**

- Input: `students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]`
- Output: `3`

**Example 3**

- Input: `students = [0,0,1], sandwiches = [1,0,0]`
- Output: `0`

---

## Solution
### Approach
Count how many students prefer each type. Process sandwiches from the top; if no remaining student wants the current type, everyone else is stuck. Otherwise consume one student of that type and continue.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
