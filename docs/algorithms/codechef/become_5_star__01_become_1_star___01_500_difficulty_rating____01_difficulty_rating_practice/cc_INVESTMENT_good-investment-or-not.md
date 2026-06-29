# Good Investment or Not

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INVESTMENT |
| Difficulty Rating | 357 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [INVESTMENT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INVESTMENT) |

---

## Problem Statement

Chef has invested his money at an interest rate of $X$ percent per annum while the current inflation rate is $Y$ percent per annum.

An investment is called *good* if and only if the interest rate of the investment is **at least twice** of the inflation rate.
Determine whether the investment made by Chef is *good* or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $X$ and $Y$, the interest rate and the current inflation rate respectively.

---

## Output Format

For each test case, output `YES` if the investment is good, `NO` otherwise.

You can output any letter in any case. For example `YES`, `yes`, `yES` are all considered same.

---

## Constraints

- $1 \leq T \leq 400$
- $1 \leq X, Y \leq 20$

---

## Examples

**Example 1**

**Input**

```text
5
7 4
6 3
2 4
10 10
20 1
```

**Output**

```text
NO
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** The interest rate is $7$ and the current inflation rate is $4$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

**Test case $2$:** The interest rate is $6$ and the current inflation rate is $3$. Since the interest rate is equal to twice of current inflation rate, the investment is good.

**Test case $3$:** The interest rate is $2$ and the current inflation rate is $4$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

**Test case $4$:** The interest rate is $10$ and the current inflation rate is $10$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

**Test case $5$:** The interest rate is $20$ and the current inflation rate is $1$. Since the interest rate is greater than twice of current inflation rate, the investment is good.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 4
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
6 3
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
2 4
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
10 10
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
20 1
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/INVESTMENT)

[Contest: Division 1](https://www.codechef.com/DEC221A/problems/INVESTMENT)

[Contest: Division 2](https://www.codechef.com/DEC221B/problems/INVESTMENT)

[Contest: Division 3](https://www.codechef.com/DEC221C/problems/INVESTMENT)

[Contest: Division 4](https://www.codechef.com/DEC221D/problems/INVESTMENT)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tejas10p](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

357

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef invested money at a rate of X percent per annum, while inflation is Y percent.

An investment is *good* if its interest rate is at least twice the inflation rate.

Is Chef’s investment good?

#
[](#explanation-5)EXPLANATION:

According to the statement, the investment is good if and only if X (the interest rate) is at least twice of Y (the inflation rate), i.e, X \geq 2Y.

So, check whether X \geq 2Y using an `if` condition, and print the answer appropriately.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if 2*y <= x else 'No')
``

</details>
