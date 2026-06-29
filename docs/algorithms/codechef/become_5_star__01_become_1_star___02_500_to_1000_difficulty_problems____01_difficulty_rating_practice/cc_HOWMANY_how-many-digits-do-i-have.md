# HOW MANY DIGITS DO I HAVE

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HOWMANY |
| Difficulty Rating | 908 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [HOWMANY](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/HOWMANY) |

---

## Problem Statement

Write a program to obtain a number $(N)$ from the user and display whether the number is a one digit number, 2 digit number, 3 digit number or more than 3 digit number

---

## Input Format

First line will contain the number $N$,

---

## Output Format

Print "1" if N is a 1 digit number.

Print "2" if N is a 2 digit number.

Print "3" if N is a 3 digit number.

Print "More than 3 digits" if N has more than 3 digits.

---

## Constraints

- $0 \leq N \leq 1000000$

---

## Examples

**Example 1**

**Input**

```text
9
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [HOW MANY DIGITS DO I HAVE Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/HOWMANY)

### [](#problem-statement-1)Problem Statement:

Write a program to obtain a number N from the user and display whether the number is a one digit number, 2 digit number, 3 digit number or more than 3 digit number.

### [](#approach-2)Approach:

**Conditional Checks**:

- We check the value of `N`:

- If `1 <= N <= 9`, it’s a one-digit number.

- If `10 <= N <= 99`, it’s a two-digit number.

- If `100 <= N <= 999`, it’s a three-digit number.

- Otherwise, if `N` is greater than `999`, it’s considered “More than 3 digits.”

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(1)` Simple conditional statements

- **Space Complexity:** `O(1)` No extra space used.

</details>
