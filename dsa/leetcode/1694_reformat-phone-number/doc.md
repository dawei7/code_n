# Reformat Phone Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1694 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reformat-phone-number/) |

## Problem Description
### Goal

The string `number` contains decimal digits together with spaces and dashes. First discard every space and dash while preserving the digits' original left-to-right order. Then partition the clean digit sequence into blocks and join consecutive blocks with a single dash.

Take blocks of three digits from the left while more than four digits remain. Format the final suffix according to its length: two or three remaining digits form one block, while four remaining digits become two blocks of two. The result must never contain a one-digit block and can contain at most two two-digit blocks. Return the reformatted phone number.

### Function Contract
**Inputs**

- `number`: a string of length $N$, where $2 \le N \le 100$, containing only digits, spaces, and dashes and containing at least two digits

**Return value**

The digits in their original order, grouped under the three-digit and final-suffix rules with dashes between blocks.

### Examples
**Example 1**

- Input: `number = "1-23-45 6"`
- Output: `"123-456"`

Removing separators leaves six digits, which form two blocks of three.

**Example 2**

- Input: `number = "123 4-567"`
- Output: `"123-45-67"`

After the first three-digit block, the four-digit suffix is divided into two equal blocks.

**Example 3**

- Input: `number = "123 4-5678"`
- Output: `"123-456-78"`

The first six digits form two blocks of three and the last two digits remain together.
