# Crawler Log Folder

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1598 |
| Difficulty | Easy |
| Topics | Array, String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/crawler-log-folder/) |

## Problem Description
### Goal
A file-system crawler records each folder-change operation in `logs`. Operation `"../"` moves from the current folder to its parent, except that attempting it in the main folder leaves the crawler there. Operation `"./"` keeps the current folder unchanged. Any other entry has the form `"x/"` and moves into an existing child folder named `x`.

The crawler begins in the main folder and performs the log entries in order. After every recorded operation is complete, return the minimum number of folder-change operations needed to get back to the main folder.

### Function Contract
**Inputs**

- `logs`: a list of $n$ valid operations with $1 \le n \le 1000$; child-folder names contain lowercase English letters and digits.

**Return value**

Return the crawler's final depth below the main folder, which equals the minimum number of parent moves needed to return.

### Examples
**Example 1**

- Input: `logs = ["d1/", "d2/", "../", "d21/", "./"]`
- Output: `2`

**Example 2**

- Input: `logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]`
- Output: `3`

**Example 3**

- Input: `logs = ["d1/", "../", "../", "../"]`
- Output: `0`
