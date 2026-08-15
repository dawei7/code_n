# Find The K-th Lucky Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2802 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-k-th-lucky-number/) |

## Problem Description

### Goal

The digits `4` and `7` are called lucky digits. A positive integer is a lucky number when every digit in its decimal representation is one of those two digits.

Arrange all lucky numbers in increasing numerical order. Numbers with fewer digits therefore appear before longer ones, while equal-length values follow ordinary decimal ordering. Given a one-based position `k`, return the lucky number occupying that position, represented as a string.

### Function Contract

**Inputs**

- `k`: The one-based position in the ordered lucky-number sequence, with $1 \le k \le 10^9$.

Let $m = \lfloor \log_2(k + 1) \rfloor$, which is the number of digits in the returned lucky number.

**Return value**

Return the $k$-th lucky number as a string containing only `"4"` and `"7"`.

### Examples

#### Example 1

- **Input:** `k = 4`
- **Output:** `"47"`
- **Explanation:** The sequence starts `4`, `7`, `44`, `47`, so its fourth value is `47`.

#### Example 2

- **Input:** `k = 10`
- **Output:** `"477"`
- **Explanation:** The first ten values are `4`, `7`, `44`, `47`, `74`, `77`, `444`, `447`, `474`, and `477`.

#### Example 3

- **Input:** `k = 1000`
- **Output:** `"777747447"`
- **Explanation:** The thousandth value in increasing order is `777747447`.
