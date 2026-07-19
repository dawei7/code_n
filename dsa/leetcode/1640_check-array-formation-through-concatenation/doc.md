# Check Array Formation Through Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1640 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-array-formation-through-concatenation/) |

## Problem Description
### Goal
You are given an array `arr` of distinct integers and a collection `pieces` of non-empty integer arrays. All values across the flattened pieces are distinct, and the pieces contain the same total number of values as `arr`.

Determine whether the pieces can be placed in some order and concatenated to equal `arr`. The pieces themselves may be reordered, but the order of values within any individual piece must remain unchanged.

### Function Contract
**Inputs**

- `arr`: an array of $n$ distinct integers, where $1 \le n \le 100$ and $1 \le \texttt{arr[i]} \le 100$.
- `pieces`: between 1 and $n$ non-empty integer arrays whose total length is $n$.
- Every flattened value in `pieces` is distinct and lies between 1 and 100.

**Return value**

Return `true` exactly when some ordering of all arrays in `pieces`, without reordering any piece internally, concatenates to `arr`; otherwise return `false`.

### Examples
**Example 1**

- Input: `arr = [15,88], pieces = [[88],[15]]`
- Output: `true`

Placing `[15]` before `[88]` forms the target.

**Example 2**

- Input: `arr = [49,18,16], pieces = [[16,18,49]]`
- Output: `false`

The values match as a set, but the sole piece's internal order cannot be changed.

**Example 3**

- Input: `arr = [91,4,64,78], pieces = [[78],[4,64],[91]]`
- Output: `true`

The ordering `[91]`, `[4,64]`, `[78]` reproduces `arr`.
