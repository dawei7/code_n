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

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Let $n$ be the number of log entries.

Only the current depth matters; the names of ancestor folders are never needed. Start a counter at zero. A child-folder operation increases it by one, `"./"` leaves it unchanged, and `"../"` decreases it only when it is positive. Clamping the decrement at zero implements the rule that the crawler cannot move above the main folder.

After each processed prefix, the counter equals the number of parent links from the crawler's current folder to the main folder. This is initially true at depth zero, and each of the three operation types changes both the real location and the counter identically. Therefore it remains true after the complete log. Each return operation can traverse only one parent link, so exactly that many operations are both necessary and sufficient.

#### Complexity detail

The algorithm examines each of the $n$ log entries once and performs constant work, for $O(n)$ time. It stores only the integer depth, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Explicit folder stack:** Pushing child names and popping for parent moves is correct and also linear, but stores $O(n)$ folder names that the requested count does not need.
- **Rebuild a textual path:** Repeated insertion, removal, or splitting can introduce quadratic copying and parsing work.
- Parent operations at depth zero have no effect, even when several occur consecutively.
- `"./"` is distinct from a child folder name and never changes depth.
- A log containing only child moves returns its full length.
- Folder names themselves do not affect the answer; only the operation category matters.

</details>
