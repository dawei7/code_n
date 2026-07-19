# Find the Celebrity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 277 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, Graph Theory, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-celebrity/) |

## Problem Description
### Goal
Among `n` people labeled `0` through $n - 1$, a celebrity is known by every other person but does not know any other person. Relationship information is available only through the boolean API `knows(a, b)` in the native problem.

Return the celebrity's index when exactly one person satisfies both conditions, or `-1` when nobody does. A popular person who knows someone else is not a celebrity, and a private person whom someone does not know is not one either. Minimize API calls by eliminating impossible candidates before verifying both directions; the app matrix models the same relationships offline.

### Function Contract
**Inputs**

- `n`: people numbered `0` through $n - 1$
- `knows_matrix`: offline app data where `knows_matrix[a][b]` represents `knows(a,b)`

**Return value**

The celebrity index, or `-1` if no celebrity exists. The native interface receives only `n` and calls the provided `knows(a,b)` API.

### Examples
**Example 1**

- Input: `n = 3, knows_matrix = [[false,true,false],[false,false,false],[false,true,false]]`
- Output: `1`

**Example 2**

- Input: `n = 2, knows_matrix = [[false,true],[true,false]]`
- Output: `-1`

**Example 3**

- Input: `n = 1, knows_matrix = [[false]]`
- Output: `0`
