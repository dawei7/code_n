## Problem Description & Examples
### Goal
You have `n` versions `[1..n]`, and one version is first bad. Given `isBadVersion(version)` returns whether a version is bad, find the first bad version. Minimize API calls.

In this simulation, `solve(n, first_bad)` finds the first bad version.

### Function Contract
**Inputs**

- `n`: int - number of versions
- `first_bad`: int - first bad version

**Return value**

int - the first bad version

### Examples
**Example 1**

- Input: `n = 5, first_bad = 4`
- Output: `4`

**Example 2**

- Input: `n = 10, first_bad = 7`
- Output: `7`

**Example 3**

- Input: `n = 20, first_bad = 5`
- Output: `5`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
