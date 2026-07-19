# Burst Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 312 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/burst-balloons/) |

## Problem Description
### Goal
Given a row of balloons with nonnegative values, burst every balloon in an order of your choice. When balloon `i` is burst, it awards the product of its own value and the values of its nearest still-unburst neighbors at that moment.

Treat a missing neighbor beyond either end as a virtual balloon of value `1`; virtual balloons cannot be burst. After a real balloon disappears, its surviving neighbors become adjacent for later rewards. Return the maximum total coins obtainable after all balloons are removed. The original adjacent values alone do not determine every reward because the chosen burst order changes future neighborhoods.

### Function Contract
**Inputs**

- `nums`: a nonempty list of nonnegative balloon values

**Return value**

The maximum total coins obtainable after every balloon is burst. Missing neighbors beyond either array edge have value one.

### Examples
**Example 1**

- Input: `nums = [3,1,5,8]`
- Output: `167`

**Example 2**

- Input: `nums = [7,1]`
- Output: `14`

**Example 3**

- Input: `nums = [10,2]`
- Output: `30`
