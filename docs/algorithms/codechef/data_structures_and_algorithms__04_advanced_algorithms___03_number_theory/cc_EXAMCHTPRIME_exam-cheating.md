# Exam Cheating

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXAMCHTPRIME |
| Difficulty Rating | 1639 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Prime Factorization |
| Official Link | [EXAMCHTPRIME](https://www.codechef.com/learn/course/number-theory/LINTDSA02/problems/EXAMCHTPRIME) |

---

## Problem Statement

Ram and Shyam are sitting next to each other, hoping to cheat on an exam. However, the examination board has prepared $p$ different sets of questions (numbered $0$ through $p-1$), which will be distributed to the students in the following way:
- The students are assigned roll numbers — pairwise distinct positive integers.
- If a student's roll number is $r$, this student gets the $((r-1)\%p)$-th set of questions.

Obviously, Ram and Shyam can cheat only if they get the same set of questions.

You are given the roll numbers of Ram and Shyam: $A$ and $B$ respectively. Find the number of values of $p$ for which they can cheat, or determine that there is an infinite number of such values.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.

### Output
For each test case, print a single line — the number of values of $p$ for which Ram and Shyam can cheat, or $-1$ if there is an infinite number of such values.

### Constraints
- $1 \le T \le 100$
- $1 \le A, B \le 10^8$

---

## Examples

**Example 1**

**Input**

```text
1
2 6
```

**Output**

```text
3
```

**Explanation**

**Example case 1:** They can cheat for $p = 1$, $p = 2$ or $p = 4$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Exam Cheating in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA02/problems/EXAMCHTPRIME?tab=statement)

### [](#problem-statement-1)Problem Statement:

This problem asks us to find out how many values of p (the number of different sets of exam questions) will allow Ram and Shyam to cheat by getting the same set of questions.

### [](#approach-2)Approach:

- **Assignment Rule**: The student with roll number r receives set number (r−1)%p.

- **Objective**: Ram and Shyam can only cheat if they receive the same set. This means that: (A−1)%p = (B−1)%p. A is Ram’s roll number and B is Shyam’s roll number.

- **Condition Simplification**: We can simplify the equation:

(A−1)%p = (B−1)%p ⇒ (A−B)%p = 0. Thus, p must divide (A−B). Now we have to find the divisors of (A-B), because p must be one of those divisors.

Now there are two scenarios:

- When A=B: In this case, (A-B)=0 and p can be any value. Thus, there are infinitely many values of p, so result is -1.

- When A≠B: In this case, the number of valid values for p is equal to the number of divisors of |A-B|

- **Find Divisors**: The approach to counting divisors of a number n is based on the fact that divisors come in pairs. For every divisor i of n, there exists a corresponding divisor \frac{n}{i} ​. By iterating only up to \sqrt{n} ​​, we efficiently find all divisors, as any divisor greater than \sqrt{n} ​ ​ would have already been paired with a divisor smaller than \sqrt{n} ​ .

### [](#complexity-3)Complexity:

- **Time Complexity:** O(\sqrt{A-B} ) We are iterating through \sqrt{A-B}  to find the divisors.

- **Space Complexity:** `O(1)` No extra space is  required.

</details>
