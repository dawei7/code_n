# XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTM28 |
| Difficulty Rating | 932 |
| Difficulty Band | Bit Manipulation |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Bitwise Operators |
| Official Link | [BTM28](https://www.codechef.com/learn/course/bit-manipulation/BITM04/problems/BTM28) |

---

## Problem Statement

You are given $N$ binary strings of length 10, output the XOR of these strings.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1100101011
0111011001
1110101110
```

**Output**

```text
348
```
