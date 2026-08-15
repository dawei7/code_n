# Number of Employees Who Met the Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2798 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-employees-who-met-the-target/) |

## Problem Description

### Goal

A company has $n$ employees numbered from $0$ through $n - 1$. The 0-indexed array `hours` records how many hours each employee worked: employee $i$ worked `hours[i]` hours.

Every employee is expected to work at least `target` hours. Determine how many entries in `hours` meet or exceed that inclusive threshold, and return that count. Both worked hours and the target are non-negative, so zero is a valid threshold as well as a valid recorded value.

### Function Contract

**Inputs**

- `hours`: A list of $n$ non-negative integers, where `hours[i]` is employee $i$'s worked time and $1 \le n \le 50$.
- `target`: The non-negative minimum required number of hours.

Every value in `hours` and `target` lies between $0$ and $10^5$, inclusive.

**Return value**

Return the number of employees whose recorded hours are at least `target`.

### Examples

#### Example 1

- **Input:** `hours = [0, 1, 2, 3, 4]`, `target = 2`
- **Output:** `3`
- **Explanation:** The values `2`, `3`, and `4` meet the inclusive threshold.

#### Example 2

- **Input:** `hours = [5, 1, 4, 2, 2]`, `target = 6`
- **Output:** `0`
- **Explanation:** No employee worked at least six hours.
