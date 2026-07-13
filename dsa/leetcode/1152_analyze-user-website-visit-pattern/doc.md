# Analyze User Website Visit Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1152 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [analyze-user-website-visit-pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/analyze-user-website-visit-pattern/).

### Goal
Given parallel visit logs, find the 3-website sequence visited by the largest number of distinct users. Visits for each user are ordered by timestamp, and the three websites in a sequence do not need to be consecutive. If several sequences have the same user count, return the lexicographically smallest one.

### Function Contract
**Inputs**

- `username`: User name for each visit.
- `timestamp`: Time for each visit.
- `website`: Website visited in the corresponding log entry.

**Return value**

List of three website names representing the best pattern.

### Examples
**Example 1**

- Input: `username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]`, `timestamp = [1,2,3,4,5,6,7,8,9,10]`, `website = ["home","about","career","home","cart","maps","home","home","about","career"]`
- Output: `["home", "about", "career"]`

**Example 2**

- Input: `username = ["ua","ua","ua","ub","ub","ub"]`, `timestamp = [1,2,3,4,5,6]`, `website = ["a","b","a","a","b","c"]`
- Output: `["a", "b", "a"]`

**Example 3**

- Input: `username = ["u","u","u"]`, `timestamp = [3,1,2]`, `website = ["c","a","b"]`
- Output: `["a", "b", "c"]`

---

## Solution
### Approach
Sort all visits by timestamp, then collect each user's website history in chronological order. For every user, generate the set of unique 3-sequences from that history so the same user contributes at most once to a pattern.

Count how many users produced each pattern. Track the pattern with the highest count, breaking ties by tuple lexicographic order.

### Complexity Analysis
- **Time Complexity**: `O(m log m + u * l^3)`, where `m` is the number of visits, `u` is the number of users, and `l` is the largest visit count for one user.
- **Space Complexity**: `O(m + p)`, where `p` is the number of generated 3-sequences.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
