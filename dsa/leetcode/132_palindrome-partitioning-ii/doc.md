# Palindrome Partitioning II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 132 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/) |

## Problem Description
### Goal
Given a nonempty string, insert cuts between selected adjacent characters so that every resulting contiguous substring is a palindrome. Each character must belong to exactly one piece, the pieces retain their original order, and no rearrangement is permitted.

Return the minimum number of cuts needed for any valid palindrome partition. The answer counts boundaries rather than substrings, so a string that is already a palindrome requires `0` cuts, while separating all `n` characters would use $n - 1$. Only the best partition matters; the function does not return the pieces or enumerate alternative minimum-cut divisions.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase string

**Return value**

The minimum number of boundaries inserted so every resulting substring is a palindrome.

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `1`

**Example 2**

- Input: `s = "a"`
- Output: `0`

**Example 3**

- Input: `s = "ab"`
- Output: `1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Palindrome preprocessing turns every cut candidate into constant-time validation**

Fill a table in dependency order: `s[left:right+1]` is palindromic when its endpoints match and its interior is empty, one character, or already marked palindromic. Processing shorter interiors first makes each candidate suffix test constant time during cut optimization.

**Every optimal prefix partition has one final palindrome**

Let `cuts[end]` be the minimum cuts for `s[:end+1]`. If `s[0:end+1]` is a palindrome, assign zero. Otherwise try each `start` from `1` through `end` for which `s[start:end+1]` is palindromic, and minimize `cuts[start - 1] + 1`.

Initialize a conservative bound such as `end`, corresponding to cutting between every character. Starting suffixes at one in the non-whole-prefix case avoids an invalid `cuts[-1]` dependency.

**Prefix order guarantees every preceding optimum is final**

When computing `cuts[end]`, all smaller prefixes are optimal and the palindrome table is complete for every candidate suffix ending at `end`.

**Trace a whole-palindrome prefix followed by one suffix**

Prefix `aa` is a palindrome and needs zero cuts. For the final `b`, suffix `b` combines with that optimal prefix and one boundary, producing `aa | b` with one cut.

**The final palindromic suffix determines each cut candidate**

Every partition of a prefix ends with one palindrome `s[start:end]`. Removing that suffix leaves a partition of the preceding prefix, whose minimum cut count is already known. Adding the boundary before the suffix constructs a valid candidate, with the whole-prefix palindrome handled as zero cuts.

Trying every table-confirmed suffix start includes the final suffix used by an optimal partition. Taking the minimum therefore cannot miss the optimum, and every compared candidate is itself a valid palindromic partition.

#### Complexity detail

There are $O(n^2)$ substrings and prefix-suffix transitions, each handled in constant time after table entries exist. The palindrome table uses $O(n^2)$ space and cuts use $O(n)$.

#### Alternatives and edge cases

- **Enumerate all palindrome partitions:** may generate exponentially many partitions when only one minimum is needed.
- **Check each substring by scanning:** adds another factor and can take $O(n^3)$ time.
- **Center expansion with cut updates:** can achieve $O(n)$ space but has a more delicate update order.
- A fully palindromic string needs zero cuts; a string with no multi-character palindrome needs $n - 1$.
- Cuts count boundaries, not pieces. A partition with `p` substrings uses $p - 1$ cuts.

</details>
