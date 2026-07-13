# Distribute Candies to People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1103 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [distribute-candies-to-people](https://leetcode.com/problems/distribute-candies-to-people/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/distribute-candies-to-people/).

### Goal
Distribute candies to `num_people` people in rounds. Give `1` candy to the first person, `2` to the second, and so on, wrapping back to the first person and increasing the gift size each time. If fewer candies remain than the next gift size, give all remaining candies to that person.

### Function Contract
**Inputs**

- `candies`: Total number of candies.
- `num_people`: Number of people in the distribution cycle.

**Return value**

List where index `i` contains the candies received by person `i`.

### Examples
**Example 1**

- Input: `candies = 7, num_people = 4`
- Output: `[1, 2, 3, 1]`

**Example 2**

- Input: `candies = 10, num_people = 3`
- Output: `[5, 2, 3]`

**Example 3**

- Input: `candies = 1, num_people = 1`
- Output: `[1]`

---

## Solution
### Approach
Simulate the distribution. Keep the next gift size and the current person index. Each step gives `min(next_gift, remaining_candies)` to the current person, then advances both the gift size and person index.

The loop ends once no candies remain.

### Complexity Analysis
- **Time Complexity**: `O(s)`, where `s` is the number of gifts actually made.
- **Space Complexity**: `O(num_people)` for the answer.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
