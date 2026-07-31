# Count Houses in a Circular Street II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2753 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Uncategorized |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-houses-in-a-circular-street-ii/) |

## Problem Description

### Goal

A circular street contains an unknown number $n$ of houses. From any house, moving right advances to the next house, and moving right from the last house wraps to the first. You begin at an arbitrary house and know only a positive upper bound $k$, where $1 \le n \le k \le 10^5$.

Each house has a door that may initially be open or closed, with at least one door guaranteed open. The restricted `Street` interface lets you inspect the current door, close it if it is open, and move one house to the right. It does not expose house identities, permit opening a door, or reveal your position.

Use only that interface to determine and return the exact number of houses.

### Function Contract

Let $n$ be the length of the circular street.

**Inputs**

- `street`: A circular `Street` object whose initial door states contain at least one open door. The app judge constructs this object from the nonempty array of `0` and `1` values shown in a case input.
- `k`: A positive integer upper bound satisfying $n \le k \le 10^5$.

The interactive object provides `closeDoor()`, `isDoorOpen()`, and `moveRight()`.

**Return value**

Return the integer $n$, the exact number of houses in the circle.

### Examples

**Example 1**

- Input: `street = [1,1,1,1], k = 10`
- Output: `4`
- Explanation: Four houses form the cycle; the bound may be larger than the answer.

**Example 2**

- Input: `street = [1,0,1,1,0], k = 5`
- Output: `5`
- Explanation: Door states do not change the number of houses, and the bound is tight.

**Example 3**

- Input: `street = [0,0,1,0,0,0,0], k = 20`
- Output: `7`
- Explanation: Even one initially open door is sufficient as a reference point.
