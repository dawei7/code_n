# Count and Say

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 38 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-and-say/) |

## Problem Description
### Goal
The count-and-say sequence starts with the string `"1"`. To obtain the next term, read the current term from left to right, divide it into maximal runs of equal digits, and describe each run by writing its length followed by the repeated digit.

Given `n` from `1` through `30`, return the `n`th term as a string. Descriptions concern consecutive groups rather than total frequency: `"21"` is read as one `2` followed by one `1`, not as a combined inventory of the whole string.

### Function Contract
**Inputs**

- `n`: `int` in `[1, 30]`

**Return value**

The nth count-and-say term as a `str`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `"1"`

**Example 2**

- Input: `n = 4`
- Output: `"1211"`

**Example 3**

- Input: `n = 5`
- Output: `"111221"`
