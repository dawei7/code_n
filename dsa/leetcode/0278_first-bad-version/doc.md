# First Bad Version

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 278 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/first-bad-version/) |

## Problem Description
### Goal
Versions are numbered from `1` through `n`. A supplied boolean API `isBadVersion(version)` reports whether a version is bad, and the statuses are monotone: once the first bad version appears, every later version is also bad.

Return the smallest version number for which the API is true. A bad version is guaranteed to exist within the range. Use as few API calls as possible by exploiting the good-to-bad boundary rather than checking versions sequentially, and avoid arithmetic overflow when selecting a midpoint. The app supplies the boundary directly only to emulate the same predicate offline.

### Function Contract
**Inputs**

- `n`: versions numbered `1` through `n`
- `bad`: the offline app's first bad version

**Return value**

The first bad version. The native interface receives only `n` and calls the provided `isBadVersion(version)` API.

### Examples
**Example 1**

- Input: `n = 5, bad = 4`
- Output: `4`

**Example 2**

- Input: `n = 1, bad = 1`
- Output: `1`

**Example 3**

- Input: `n = 10, bad = 2`
- Output: `2`
