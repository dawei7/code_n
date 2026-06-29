# Decrement OR Increment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DECINC |
| Difficulty Rating | 722 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [DECINC](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DECINC) |

---

## Problem Statement

Write a program to obtain a number $N$ and increment its value by 1 if the number is divisible by 4 $otherwise$ decrement its value by 1.

---

## Input Format

First line will contain a number $N$.

---

## Output Format

Output a single line, the new value of the number.

---

## Constraints

- $0 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
5
```

**Output**

```text
4
```

**Explanation**

Since 5 is not divisible by 4 hence, its value is decreased by 1.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Decrement OR Increment Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DECINC)

### [](#problem-statement-1)Problem Statement:

Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by 1.

### [](#approach-2)Approach:

- If `N` modulo `4` equals `0 (N%4==0)` - add `1` in `N` and return it.

- else subtract `1` from `N` and return it.

### [](#complexity-3)Complexity:

- **Time Complexity:** O(1)

- **Space Complexity:** O(1)

</details>
