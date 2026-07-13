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

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The version predicate changes only once**

Maintain an inclusive interval containing the first bad version. If the midpoint is bad, keep it and search left; otherwise discard it and everything earlier.

The first bad version always lies in `[left, right]`. A bad midpoint makes `[left, mid]` the only relevant half; a good midpoint makes `[mid + 1, right]` the only relevant half.

**Keeping a bad midpoint preserves the boundary candidate**

If the midpoint is good, monotonicity proves every earlier version is good and the boundary must be to its right. If it is bad, the midpoint might itself be the first bad version, so the search retains it while discarding only later candidates. Each update preserves the transition point until the interval contains one version, which must be the answer.

#### Complexity detail

Each API call halves the remaining interval, so there are $O(\log n)$ calls and only constant local state.

#### Alternatives and edge cases

- **Scan from version one:** may make $O(n)$ API calls.
- The first or only version may already be bad; overflow-safe midpoint arithmetic avoids fixed-width issues.

</details>
