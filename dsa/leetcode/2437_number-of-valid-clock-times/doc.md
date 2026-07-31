# Number of Valid Clock Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2437 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Valid Clock Times](https://leetcode.com/problems/number-of-valid-clock-times/) |

## Problem Description

### Goal

You are given a five-character digital-clock pattern `time` in the form `"hh:mm"`. A concrete valid time ranges from `"00:00"` through `"23:59"`. Some digit positions may instead contain `'?'`, meaning that digit is unknown.

Replace every question mark independently with a digit from 0 through 9. Count how many replacements produce a valid 24-hour clock time, and return that count. The colon remains fixed and is not replaced.

### Function Contract

**Inputs**

- `time`: A length-five clock pattern in `"hh:mm"` form whose digit positions contain decimal digits or `'?'`.

The pattern is guaranteed to have at least one valid completion.

**Return value**

- The number of valid clock times matching every fixed digit in the pattern.

### Examples

**Example 1**

- Input: `time = "?5:00"`
- Output: `2`

The leading question mark may be 0 or 1, producing `"05:00"` and `"15:00"`.

**Example 2**

- Input: `time = "0?:0?"`
- Output: `100`

Both unknown positions independently accept all ten digits.

**Example 3**

- Input: `time = "??:??"`
- Output: `1440`

All 24 hour values and all 60 minute values are possible.
