# Chef and Donation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DNATION |
| Difficulty Rating | 305 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DNATION](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DNATION) |

---

## Problem Statement

In a certain month, Chef earned $X$ rupees while Chefina earned $Y$ rupees such that $Y\gt X$.
Since they want to end up with **exactly** the same amount, they decide to donate the difference between their income to a charity.

Find the amount they donate in the month.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the income of Chef and Chefina in a month, respectively.

---

## Output Format

For each test case, output on a new line, the amount they donate in the month.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X\lt Y \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
1 3
2 5
4 5
2 10
```

**Output**

```text
2
3
1
8
```

**Explanation**

**Test case $1$:** Chef earns $1$ rupees while Chefina earns $3$ rupees. The difference between their income is $3-1 = 2$. Thus, they donate $2$ rupees to charity.

**Test case $2$:** Chef earns $2$ rupees while Chefina earns $5$ rupees. The difference between their income is $5-2 = 3$. Thus, they donate $3$ rupees to charity.

**Test case $3$:** Chef earns $4$ rupees while Chefina earns $5$ rupees. The difference between their income is $5-4 = 1$. Thus, they donate $1$ rupees to charity.

**Test case $4$:** Chef earns $2$ rupees while Chefina earns $10$ rupees. The difference between their income is $10-2 = 8$. Thus, they donate $8$ rupees to charity.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 5
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 5
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
2 10
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DNATION)

[Contest: Division 1](https://www.codechef.com/START84A/problems/DNATION)

[Contest: Division 2](https://www.codechef.com/START84B/problems/DNATION)

[Contest: Division 3](https://www.codechef.com/START84C/problems/DNATION)

[Contest: Division 4](https://www.codechef.com/START84D/problems/DNATION)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [abhidot](https://www.codechef.com/users/abhidot)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

305

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef earned X rupees and Chefina earned Y rupees. It is known that X \lt Y.

The difference between their incomes is donated to charity. How much is donated?

#
[](#explanation-5)EXPLANATION:

The difference between their incomes is exactly Y - X, and hence this is the answer.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y - x)
``

</details>
