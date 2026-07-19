# Average Salary Excluding the Minimum and Maximum Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1491 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) |

## Problem Description
### Goal

An array `salary` contains the distinct integer salaries of a group of employees. Remove exactly two entries from consideration: the unique minimum salary and the unique maximum salary.

Return the arithmetic mean of all remaining salaries. The array always contains at least three values, so at least one salary remains after the two extremes are excluded. A floating-point result within absolute error $10^{-5}$ of the exact average is accepted.

### Function Contract
**Inputs**

Let $N$ be the length of `salary`.

- `salary`: a list of unique integers with $3 \le N \le 100$.
- Every salary satisfies $1000 \le \texttt{salary[i]} \le 10^6$.
- Input order has no semantic meaning; the minimum and maximum may occur at any positions.

**Return value**

Return the sum of the $N-2$ non-extreme salaries divided by $N-2$. The result is a floating-point number, and an absolute error of at most $10^{-5}$ is accepted.

### Examples
**Example 1**

- Input: `salary = [4000,3000,1000,2000]`
- Output: `2500.0`
- Explanation: Removing `1000` and `4000` leaves `2000` and `3000`, whose average is `2500`.

**Example 2**

- Input: `salary = [1000,2000,3000]`
- Output: `2000.0`
- Explanation: With three employees, only the middle salary remains after both extremes are excluded.

**Example 3**

- Input: `salary = [1000,2000,3001,9000]`
- Output: `2500.5`
- Explanation: The two retained salaries sum to `5001`, so the requested average need not be an integer.
