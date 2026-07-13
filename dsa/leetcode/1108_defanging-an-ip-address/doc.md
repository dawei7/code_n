# Defanging an IP Address

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1108 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [defanging-an-ip-address](https://leetcode.com/problems/defanging-an-ip-address/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/defanging-an-ip-address/).

### Goal
Return a defanged version of an IPv4 address by replacing every period `.` with `[.]`.

### Function Contract
**Inputs**

- `address`: Valid IPv4 address string.

**Return value**

Address string with each `.` replaced by `[.]`.

### Examples
**Example 1**

- Input: `address = "1.1.1.1"`
- Output: `"1[.]1[.]1[.]1"`

**Example 2**

- Input: `address = "255.100.50.0"`
- Output: `"255[.]100[.]50[.]0"`

**Example 3**

- Input: `address = "0.0.0.0"`
- Output: `"0[.]0[.]0[.]0"`

---

## Solution
### Approach
Scan the string and build a new string, appending `[.]` when the character is a period and appending the character itself otherwise.

Most languages also provide a direct string replacement method that expresses the same transformation.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the address length.
- **Space Complexity**: `O(n)` for the returned string.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
