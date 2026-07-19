# Latest Time by Replacing Hidden Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1736 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/) |

## Problem Description

### Goal

The five-character string `time` has the form `hh:mm`. Each position other than the colon contains either a decimal digit or `?`, which represents one hidden digit that may be replaced independently.

A time is valid when it lies from `00:00` through `23:59`, inclusive. Replace every `?` with a digit so the result is valid and as late as possible within that day, then return the completed string. The input guarantees that at least one valid completion exists.

### Function Contract

**Inputs**

- `time`: a string in `hh:mm` format whose four digit positions may contain `?`.

**Return value**

- Return the lexicographically and chronologically latest valid 24-hour time matching every visible digit.

### Examples

**Example 1**

- Input: `time = "2?:?0"`
- Output: `"23:50"`
- Explanation: The latest hour beginning with `2` is `23`, and the latest minute ending with `0` is `50`.

**Example 2**

- Input: `time = "0?:3?"`
- Output: `"09:39"`
- Explanation: The fixed leading zero limits the hour to `00` through `09`.

**Example 3**

- Input: `time = "1?:22"`
- Output: `"19:22"`
- Explanation: Only the hidden hour digit changes, and `9` gives the latest valid match.
