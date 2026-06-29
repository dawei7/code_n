# Monopoly in Chefland

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MONOPOLY |
| Difficulty Rating | 482 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MONOPOLY](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MONOPOLY) |

---

## Problem Statement

Chef is the financial incharge of Chefland and one of his duties is identifying if any company has gained a monopolistic advantage in the market.

There are exactly $3$ companies in the market each of whose revenues are denoted by $R_1$, $R_2$ and $R_3$ respectively. A company is said to have a monopolistic advantage if its revenue is **strictly** greater than the sum of the revenues of its competitors.

Given the revenue of the $3$ companies, help Chef determine if any of them has a monopolistic advantage.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing three space separated integers $R_1$, $R_2$ and $R_3$ denoting the revenue of the three companies respectively.

---

## Output Format

For each test case, output $\texttt{YES}$ if any of the companies has a monopolistic advantage over its competitors, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq R_1, R_2, R_3 \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
1 1 1
1 2 4
2 10 3
1 2 3
```

**Output**

```text
No
Yes
Yes
No
```

**Explanation**

**Test case 1:** All the companies have equal revenue so none have a monopolistic advantage.

**Test case 2:** The third company has a monopolistic advantage as $1 + 2 < 4$.

**Test case 3:** The second company has a monopolistic advantage as $2 + 3 < 10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
No
```



#### Test case 2

**Input for this case**

```text
1 2 4
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
2 10 3
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MONOPOLY)

[Contest: Division 1](https://www.codechef.com/START66A/problems/MONOPOLY)

[Contest: Division 2](https://www.codechef.com/START66B/problems/MONOPOLY)

[Contest: Division 3](https://www.codechef.com/START66C/problems/MONOPOLY)

[Contest: Division 4](https://www.codechef.com/START66D/problems/MONOPOLY)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

482

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the revenue of three companies R_1, R_2, R_3, does any company have strictly higher revenue than the sum of the other two?

#
[](#explanation-5)EXPLANATION:

There are only three cases to check:

- R_1 \gt R_2 + R_3

- R_2 \gt R_1 + R_3

- R_3 \gt R_1 + R_2

Check all three using `if` conditions, then print “Yes” if any one of them is true.

A little observation can also reduce this to a single observation: the answer is “Yes” if and only if

2\cdot\max(R_1, R_2, R_3) \gt R_1+R_2+R_3

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('Yes' if 2*max(a, b, c) > a+b+c else 'No')
``

</details>
