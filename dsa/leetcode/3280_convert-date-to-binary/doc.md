# Convert Date to Binary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3280 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Convert Date to Binary](https://leetcode.com/problems/convert-date-to-binary/) |

## Problem Description

### Goal

A valid Gregorian calendar date is provided as a ten-character string in `yyyy-mm-dd` format. The date lies between January 1, 1900 and December 31, 2100, inclusive, so the year, month, and day components are all positive decimal integers.

Convert each of those three components independently to its base-two representation without leading zeros. Preserve the component order and join the three binary strings with hyphens, producing the binary form `year-month-day`.

### Function Contract

**Inputs**

- `date`: A valid date string of length `10`, with hyphens at indices `4` and `7` and decimal digits elsewhere.

**Return value**

Return the year, month, and day written in binary without leading zeros and separated by `-`.

### Examples

#### Example 1

- **Input:** `date = "2080-02-29"`
- **Output:** `"100000100000-10-11101"`
- **Explanation:** Decimal `2080`, `2`, and `29` become the three displayed binary components.

#### Example 2

- **Input:** `date = "1900-01-01"`
- **Output:** `"11101101100-1-1"`

#### Example 3

- **Input:** `date = "2000-12-31"`
- **Output:** `"11111010000-1100-11111"`
- **Explanation:** Formatting zeros in the decimal month and day do not survive integer conversion.
