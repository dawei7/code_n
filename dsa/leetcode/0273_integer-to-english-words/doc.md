# Integer to English Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 273 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-to-english-words/) |

## Problem Description
### Goal
Given a nonnegative 32-bit integer, write its value using conventional English number words. Compose groups for hundreds and the larger scales `Thousand`, `Million`, and `Billion`, omitting any group whose numerical value is zero.

Return a capitalized string with words separated by single spaces, no leading or trailing whitespace, no hyphens, and no inserted word `and`. The value zero is represented exactly as `"Zero"`. Within each nonzero three-digit group, use the standard forms from `One` through `Nineteen` and the tens through `Ninety`, preserving their numerical order without spelling individual digits.

### Function Contract
**Inputs**

- `num`: a nonnegative integer

**Return value**

Capitalized English number words separated by single spaces, without `and`; zero becomes `"Zero"`.

### Examples
**Example 1**

- Input: `num = 123`
- Output: `"One Hundred Twenty Three"`

**Example 2**

- Input: `num = 12345`
- Output: `"Twelve Thousand Three Hundred Forty Five"`

**Example 3**

- Input: `num = 1234567`
- Output: `"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`

### Required Complexity

- **Time:** $O(\log num)$
- **Space:** $O(\log num)$

<details>
<summary>Approach</summary>

#### General

**English scale words align with base-1000 chunks**

Split the number into base-1000 chunks. Convert each nonzero chunk below 1000, append its scale name (`Thousand`, `Million`, or `Billion`), and combine chunks from largest to smallest.

**Name one chunk with exhaustive local cases**

For a value below 1000, emit a hundreds phrase when needed, then handle a remainder below 20 directly or combine a tens word with an optional ones word.

At scale index `i`, the current chunk is exactly the coefficient of $1000^{i}$. Its local words plus scale name therefore represent that chunk's contribution without affecting any other digits.

**Unique chunk decomposition preserves value and order**

Base-1000 decomposition uniquely expresses the number as a sum of coefficients times $1000^{i}$. The helper covers every coefficient from 1 through 999 through disjoint hundreds, sub-twenty, tens, and ones cases. Appending the corresponding scale word restores its place value, and joining nonzero chunks from largest scale to smallest produces the exact English representation.

#### Complexity detail

The algorithm processes one chunk per three decimal digits, giving $O(\log num)$ time and word storage. Under the native 32-bit bound there are at most four chunks.

#### Alternatives and edge cases

- **Large lookup table:** is bulky and obscures the repeated structure.
- Zero needs an explicit result; zero-valued internal chunks are skipped without adding a scale word.

</details>
