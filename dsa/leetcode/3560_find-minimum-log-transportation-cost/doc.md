# Find Minimum Log Transportation Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3560 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-log-transportation-cost/) |

## Problem Description

### Goal

Two logs have integer lengths `n` and `m`. They must be carried by three trucks, and each truck can carry exactly one log or log piece whose length is at most `k`. A log that already fits may be transported without modification.

You may cut a log of length $x$ once into two positive integer lengths $a$ and $b$, where $a+b=x$. That cut costs $ab$. The input guarantees that some valid distribution among the three trucks exists. Determine the minimum total cutting cost needed to make every transported piece fit; return zero when neither log needs a cut.

### Function Contract

**Inputs**

- `n`: The positive integer length of the first log.
- `m`: The positive integer length of the second log.
- `k`: The maximum length that one truck can carry.

The bounds are $2 \le k \le 10^5$ and $1 \le n,m \le 2k$. The input always permits a valid arrangement using the three trucks.

**Return value**

Return the minimum total cutting cost as an integer. A cut into lengths $a$ and $b$ contributes $ab$ to that total.

### Examples

**Example 1**

- Input: `n = 6, m = 5, k = 5`
- Output: `5`
- Explanation: Split the length-6 log into pieces of lengths `1` and `5`. Together with the other length-5 log, the three pieces fit in the three trucks, and the cut costs `1 * 5 = 5`.

**Example 2**

- Input: `n = 4, m = 4, k = 6`
- Output: `0`
- Explanation: Both logs already satisfy the truck limit, so no cut is required.

---
