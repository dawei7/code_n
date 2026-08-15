# Number of Senior Citizens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2678 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-senior-citizens/) |

## Problem Description

### Goal

You receive a 0-indexed array `details` containing compact passenger records. Every record is a 15-character string with four consecutive fields: the first ten characters are the passenger's phone number, character 10 records gender, characters 11 and 12 encode a two-digit age, and the final two characters identify the assigned seat.

Count the passengers whose encoded age is strictly greater than 60. A passenger aged exactly 60 does not qualify.

### Function Contract

**Inputs**

- `details`: A list of 1 through 100 passenger strings, each exactly 15 characters long. Apart from the gender position, each character is a decimal digit; the gender is `M`, `F`, or `O`. Phone numbers and seat numbers are distinct.

**Return value**

Return the number of records whose two-digit age field represents a value greater than 60.

### Examples

#### Example 1

- **Input:** `details = ["7868190130M7522","5303914400F9211","9273338290F4010"]`
- **Output:** `2`
- **Explanation:** The three ages are 75, 92, and 40, so two exceed 60.

#### Example 2

- **Input:** `details = ["1313579440F2036","2921522980M5644"]`
- **Output:** `0`
- **Explanation:** Ages 20 and 56 are not greater than 60.
