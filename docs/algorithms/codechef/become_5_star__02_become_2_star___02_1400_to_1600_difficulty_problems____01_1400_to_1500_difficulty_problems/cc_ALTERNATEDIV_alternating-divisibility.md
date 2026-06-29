# Alternating Divisibility

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALTERNATEDIV |
| Difficulty Rating | 1483 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [ALTERNATEDIV](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/ALTERNATEDIV) |

---

## Problem Statement

JJ challenges the Chef to construct an array $A$ of length $N$ such that the following conditions hold:
- $A_i$ divides $A_{i + 1}$ when $i$ is odd and $1 \le i \le N - 1$
- $A_i$ does not divide $A_{i + 1}$ when $i$ is even and $1 \le i \le N - 1$
- $1 \le A_i \le 2 \cdot N$
- All $A_i$ are pairwise **distinct**

Can you help Chef complete JJ's challenge?

If multiple arrays satisfying the above conditions exist print any one of them.

It is guaranteed that under the given constraints, at least one array satisfying the above conditions exists.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - the length of the array $A$ to be constructed.

---

## Output Format

For each test case, output a single line containing $N$ space-separated integers, denoting the elements of the array $A$ you constructed.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1
6
```

**Output**

```text
1 3 2 4
2
1 5 6 12 3 9
```

**Explanation**

**Test case-1:** $[1, 3, 2, 4]$ is a valid array because:
- $A_1 = 1$ divides $A_2 = 3$.
- $A_2 = 3$ does not divide $A_3 = 2$.
- $A_3 = 2$ divides $A_4 = 4$.

**Test case-3:** $[1, 5, 6, 12, 3, 9]$ is a valid array because:
- $A_1 = 1$ divides $A_2 = 5$.
- $A_2 = 5$ does not divide $A_3 = 6$.
- $A_3 = 6$ divides $A_4 = 12$.
- $A_4 = 12$ does not divide $A_5 = 3$.
- $A_5 = 3$ divides $A_6 = 9$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
1 3 2 4
```



#### Test case 2

**Input for this case**

```text
1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
1 5 6 12 3 9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/COOK139C/problems/ALTERNATEDIV)

[Contest - Division 2](https://www.codechef.com/COOK139B/problems/ALTERNATEDIV)

[Contest - Division 1](https://www.codechef.com/COOK139A/problems/ALTERNATEDIV)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

Given an integer N, construct an array A of N elements such that

-
A_i \mid A_{i+1} for all odd i,

-
A_i \nmid A_{i+1} for all even i,

-
A_i \ne A_j for all i\ne j, and

-
1\le A_i \le 2\cdot N for all i.

#
[](#explanation-4)EXPLANATION:

Let x=N-\lceil\frac{N}{2}\rceil+1. Then, the following sequence is valid:

[x, 2\cdot x, x+1,2\cdot(x+1), x+2,\dots]

Proof

It is easy to see that the elements at odd indices are in increasing order from x\to N. Similarly, the elements at even indices are in increasing order from 2\cdot x \to 2\cdot N (from 2\cdot x \to 2\cdot (N-1) when N is odd.)

Then,

2\cdot x = 2\cdot(N-\bigg\lceil\frac{N}{2}\bigg\rceil+1) > N

implies the sets \{x, x+1,\dots, N\} and \{2\cdot x, 2\cdot(x+1), \dots, 2\cdot N\} are disjoint; Therefore, all elements of the above sequence are unique.

A_i\mid A_{i+1} can be trivially verified to be true for all odd i.

A_i\nmid A_{i+1} holds true for all even i, since A_i > A_{i+1} (and a greater number cannot completely divide a smaller one).

Thus, the provided sequence fulfills all requirements of the problem, and is therefore valid!

#
[](#time-complexity-5)TIME COMPLEXITY:

O(N)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/59766540)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
