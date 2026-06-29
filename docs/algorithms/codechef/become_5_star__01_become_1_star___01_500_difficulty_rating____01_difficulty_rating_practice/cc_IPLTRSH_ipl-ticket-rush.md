# IPL Ticket Rush

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IPLTRSH |
| Difficulty Rating | 273 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [IPLTRSH](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/IPLTRSH) |

---

## Problem Statement

DAIICT college students want to attend an IPL match.

A total of $N$ students from the college want to go while only $M$ tickets are available for the match.

Determine how many students won't be able to book tickets.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $M$ — the number of students wants to go and the total number of tickets available, respectively.

---

## Output Format

For each test case, output on a new line the number of students who won't be able to book tickets.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N , M \leq 10^{5}$

---

## Examples

**Example 1**

**Input**

```text
4
5 3
5 7
4 1
8 8
```

**Output**

```text
2
0
3
0
```

**Explanation**

**Test case $1$:** There are $5$ students who want to go, and only $3$ tickets are available. Hence $2$ students won't be able to get tickets.

**Test case $2$:** There are $5$ students who want to go, and $7$ tickets are available. So, every one of them will get the tickets.

**Test case $3$:** There are $4$ students who want to go, and only $1$ ticket is available. Hence $3$ students won't be able to get tickets.

**Test case $4$:** There are $8$ students who want to go, and $8$ tickets are available. So, every one of them will get the tickets.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 7
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4 1
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
8 8
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/IPLTRSH)

[Contest: Division 1](https://www.codechef.com/START85A/problems/IPLTRSH)

[Contest: Division 2](https://www.codechef.com/START85B/problems/IPLTRSH)

[Contest: Division 3](https://www.codechef.com/START85C/problems/IPLTRSH)

[Contest: Division 4](https://www.codechef.com/START85D/problems/IPLTRSH)

***Authors:*** [d_k_7386](https://www.codechef.com/users/d_k_7386)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

273

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

N students want to attend a cricket match that has M tickets available. How many of them will miss out?

#
[](#explanation-5)EXPLANATION:

If M \geq N, then all the students can buy tickets, so the answer is 0.

If M \lt N, then N-M of the students won’t be able to buy tickets.

This can be succinctly represented by the formula \max(0, N-M).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    print(max(0, n - m))
``

</details>
