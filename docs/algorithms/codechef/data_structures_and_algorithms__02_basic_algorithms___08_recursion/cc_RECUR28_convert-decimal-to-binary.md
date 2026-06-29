# Convert Decimal To Binary

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR28 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR28](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR28) |

---

## Problem Statement

Write a recursive function to convert a non-negative integer $n$ into its binary representation.

Given a non-negative integer $n$, the binary representation of $n$ can be obtained by repeatedly dividing the number by $2$ and recording the remainder. The remainder forms the binary digits from the least significant bit (LSB) to the most significant bit (MSB).

---

## Input Format

- The only line of input contains a single non-negative integers $n$.

---

## Output Format

- Output the binary form of $n$.

---

## Constraints

- $0 \leq n \leq 1000000000$

---

## Examples

**Example 1**

**Input**

```text
5
```

**Output**

```text
101
```

**Explanation**

5 ÷ 2 = 2 with remainder 1(LSB) \
2 ÷ 2 = 1 with remainder 0 \
1 ÷ 2 = 0 with remainder 1 (MSB)
