# Recurring Digit Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR26 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR26](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR26) |

---

## Problem Statement

Given a non-negative integer $N$, repeatedly sum its digits until the result has only one digit.

---

## Input Format

- The only line of input contains a single a non-negative integers $N$.

---

## Output Format

- Print the desired output.

---

## Constraints

- $0 \leq N \leq 1000000000$

---

## Examples

**Example 1**

**Input**

```text
38
```

**Output**

```text
2
```

**Explanation**

Sum of digits of 38: 3 + 8 = 11

Sum of digits of 11: 1 + 1 = 2

Hence the result is 2.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Recurring Digit Sum in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR26)

### [](#problem-statement-1)Problem Statement:

Given a non-negative integer N, repeatedly sum its digits until the result has only one digit.

### [](#approach-2)Approach:

We can solve this problem using recursion by repeatedly summing the digits of N and then checking if the sum has more than one digit. If so, we call the same function recursively with this sum until the result is a single-digit number.

- **Base Case**: If N is a single-digit number (i.e., N<10), return N.

- **Recursive Case**: If N has more than one digit, calculate the sum of its digits and recursively call the function with the new sum.

### [](#complexity-3)Complexity:

-

**Time Complexity:** `O(log N)` since the number of digits in `N` reduces significantly with each recursion (from multiple digits to just one).

-

**Space Complexity:** `O(log⁡ N)` for the recursion stack because each recursion call processes the sum of digits of a progressively smaller number.

</details>
