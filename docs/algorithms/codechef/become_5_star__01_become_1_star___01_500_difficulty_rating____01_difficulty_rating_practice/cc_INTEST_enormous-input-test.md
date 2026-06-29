# Enormous Input Test

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INTEST |
| Difficulty Rating | 464 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [INTEST](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTEST) |

---

## Problem Statement

You are given $N$ integers. Find the count of numbers divisible by $K$.

---

## Input Format

The input begins with two positive integers $N$, $K$. The next $N$ lines contains one positive integer each denoted by $A_i$.

---

## Output Format

Output a single number denoting how many integers are divisible by $K$.

---

## Constraints

- $1 \leq N, K \leq 10^7$
- $1 \leq A_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
7 3
1
51
966369
7
9
999996
11
```

**Output**

```text
4
```

**Explanation**

The integers divisible by $3$ are $51, 966369, 9,$ and $999996$. Thus, there are $4$ integers in total.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Enormous Input Test Practice Problem in 500 difficulty rating](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTEST)

### [](#problem-statement-1)Problem Statement:

You are given N integers. Find the count of numbers divisible by K.

### [](#approach-2)Approach:

- **Simple Division Check**: For each number A_i, check if A_i mod K == 0 to determine if it’s divisible by K.

- **Count the Divisibles**: Maintain a counter to count how many numbers are divisible by K.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(N)`, where `N` is the number of integers. Each integer is processed in constant time `O(1)`.

- **Space Complexity**: `O(1)` for counting and checking

</details>
