# Calculate Money in Leetcode Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1716 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) |

## Problem Description
### Goal

Hercy deposits money every day. On the first Monday he deposits one dollar, then increases the daily deposit by one dollar from Tuesday through Sunday. Each later Monday starts one dollar higher than the preceding Monday, and that week again increases by one dollar each day.

Given a day count `n`, return the total money deposited from the first Monday through the end of day `n`.

### Function Contract
**Inputs**

- `n`: the inclusive number of saving days, with $1 \le n \le 1000$

**Return value**

The sum of the deposits made on days $1$ through $n$ under the weekly increasing pattern.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `10`

The first four deposits are 1, 2, 3, and 4 dollars.

**Example 2**

- Input: `n = 10`
- Output: `37`

The first week contributes 28 dollars; the next Monday through Wednesday contribute 2, 3, and 4 dollars.

**Example 3**

- Input: `n = 20`
- Output: `96`

Two complete weeks contribute 28 and 35 dollars, and the following six days contribute 3 through 8 dollars.
