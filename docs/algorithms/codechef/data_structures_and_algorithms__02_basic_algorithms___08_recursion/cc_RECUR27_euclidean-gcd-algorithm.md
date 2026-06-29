# Euclidean GCD Algorithm

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR27 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR27](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR27) |

---

## Problem Statement

You are required to write a recursive function to find the Greatest Common Divisor (GCD) of two non-negative integers $a$ and $b$ using the **Euclidean Algorithm**.

The Euclidean Algorithm is based on the following recurrence relation:

Given two non-negative integers $a$ and $b$, the GCD of $a$ and $b$ is defined by the following properties:

1. **Base Case:**
   - If ($b$ = $0$), then GCD($a$, $b$) = $a$.

2. **Recursive Case:**
   - If ($b$ != $0$), then GCD($a$, $b$) = GCD($b$, $a$ % $b$).

---

## Input Format

- The only line of input contains two space separated non-negative integers $a$ and $b$.

---

## Output Format

- Output the GCD of the two numbers.

---

## Constraints

- $0 \leq a, b \leq 1000000000$

---

## Examples

**Example 1**

**Input**

```text
48 18
```

**Output**

```text
6
```

**Explanation**

GCD(48, 18) = GCD(18, 48 % 18) = GCD(18, 12)
GCD(18, 12) = GCD(12, 18 % 12) = GCD(12, 6)
GCD(12, 6) = GCD(6, 12 % 6) = GCD(6, 0)
Since \(b = 0\), \(GCD(6, 0) = 6
