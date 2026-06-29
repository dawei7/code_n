# Saving Taxes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TAXSAVING |
| Difficulty Rating | 252 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TAXSAVING](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TAXSAVING) |

---

## Problem Statement

In Chefland, everyone who earns **strictly** more than $Y$ rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.

You have earned $X$ $(X \gt Y)$ rupees this year. Find the **minimum** amount of money you have to invest so that you don't have to pay taxes this year.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input consisting of two space separated integers $X$ and $Y$ denoting the amount you earned and the amount above which you will have to pay taxes.

---

## Output Format

For each test case, output a single integer, denoting the minimum amount you need to invest.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq Y \lt X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
4 2
8 7
5 1
2 1
```

**Output**

```text
2
1
4
1
```

**Explanation**

**Test case $1$:** The amount above which you will have to pay taxes is $2$. Since you earn $4$ rupees, you need to invest at least $2$ rupees. After investing $2$ rupees, you will remain with an effective income $4 - 2 = 2$ rupees which will not be taxed.

**Test case $2$:** The amount above which you will have to pay taxes is $7$. Since you earn $8$ rupees, you need to invest at least $1$ rupees.

**Test case $3$:** The amount above which you will have to pay taxes is $1$. Since you earn $5$ rupees, you need to invest at least $4$ rupees.

**Test case $4$:** The amount above which you will have to pay taxes is $1$. Since you earn $2$ rupees, you need to invest at least $1$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
8 7
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 1
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
2 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TAXSAVING)

[Contest: Division 1](https://www.codechef.com/START75A/problems/TAXSAVING)

[Contest: Division 2](https://www.codechef.com/START75B/problems/TAXSAVING)

[Contest: Division 3](https://www.codechef.com/START75C/problems/TAXSAVING)

[Contest: Division 4](https://www.codechef.com/START75D/problems/TAXSAVING)

***Author:*** [tejas10p](https://www.codechef.com/users/tejas10p)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You earned X rupees this year; and anyone who earns strictly more than Y rupees per year must pay taxes.

Given that Y \lt X, how much money must you invest so that you no longer have to pay taxes?

#
[](#explanation-5)EXPLANATION:

Since Y \lt X, it’s clearly optimal to bring our money down to Y (since it only shouldn’t be strictly more than Y).

This can be done by investing X-Y rupees.

So, the answer is simply X-Y.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x - y)
``

</details>
