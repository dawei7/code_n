# Self Crossing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 335 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/self-crossing/) |

## Problem Description
### Goal
Start at the origin and draw axis-aligned segments with the given positive lengths. The first segment travels north, then directions rotate counterclockwise through west, south, east, and back to north for all later segments.

Return `True` when the path ever crosses itself, overlaps a previous segment, or touches a nonconsecutive segment at an endpoint; otherwise return `False`. Consecutive segments naturally share their connecting endpoint and do not by themselves count as self-crossing. Detect intersections anywhere during the walk without expanding each unit of distance, since segment lengths may be large. The input path cannot change its turn direction.

### Function Contract
**Inputs**

- `distance`: the positive length of each consecutive segment

**Return value**

`True` if the path crosses, overlaps, or touches itself; otherwise `False`.

### Examples
**Example 1**

- Input: `distance = [2,1,1,2]`
- Output: `True`

**Example 2**

- Input: `distance = [1,2,3,4]`
- Output: `False`

**Example 3**

- Input: `distance = [1,1,1,1]`
- Output: `True`
