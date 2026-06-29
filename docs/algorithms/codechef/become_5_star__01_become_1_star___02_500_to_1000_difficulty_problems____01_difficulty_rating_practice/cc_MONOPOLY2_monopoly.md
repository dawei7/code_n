# Monopoly

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MONOPOLY2 |
| Difficulty Rating | 578 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MONOPOLY2](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MONOPOLY2) |

---

## Problem Statement

There are $4$ companies in the markets of Chefland, $A$, $B$, $C$, and $D$. $\\$
This year,
- Company $A$ made a profit of $P$ lakh rupees,
- Company $B$ made a profit of $Q$ lakh rupees,
- Company $C$ made a profit of $R$ lakh rupees,
- Company $D$ made a profit of $S$ lakh rupees.

There is said to be a **monopoly** in the market if the profit made by one company is **strictly greater than** the sum of profits made by all other companies. $\\$ Determine if there is a monopoly in the market or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line and only line of each test case contains four space-separated integers $P$, $Q$, $R$ and $S$ — the profits made by companies $A$, $B$, $C$ and $D$ respectively.

---

## Output Format

For each test case, output `YES` if there is a monopoly in the market. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq P, Q, R, S \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 1 1 10
30 20 6 4
100 90 3 4
14 15 16 17
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test Case 1:** Here, company $D$'s profit ($10$) is greater than the sum of profits of all other companies ($1 + 1 + 1 = 3$).

**Test Case 2:** Here, no company's profit is **strictly** greater than the sum of profits of all other companies.

**Test Case 3:** Here, company $A$'s profit ($100$) is greater than the sum of profits of all other companies ($90 + 3 + 4 = 97$).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 10
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
30 20 6 4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
100 90 3 4
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
14 15 16 17
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MONOPOLY2)

[Contest: Division 1](https://www.codechef.com/START89A/problems/MONOPOLY2)

[Contest: Division 2](https://www.codechef.com/START89B/problems/MONOPOLY2)

[Contest: Division 3](https://www.codechef.com/START89C/problems/MONOPOLY2)

[Contest: Division 4](https://www.codechef.com/START89D/problems/MONOPOLY2)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

578

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Four companies — A, B, C,  and D — made profits of rupees P, Q, R,  and S lakh respectively, in the last year.

There’s a monopoly in the market if the profit made by one company is strictly larger than the sum of profits of the others.

Is there a monopoly in the market?

#
[](#explanation-5)EXPLANATION:

Check whether any of the four companies satisfies the monopoly condition, i.e, check if any one of

- A \gt B + C + D

- B \gt A + C + D

- C \gt A + B + D

- D \gt A + B + C

are true.

If at least one of them is true, the answer is `Yes`; else the answer is `No`.

For a slightly simpler solution, notice that it’s enough to check whether the company with *largest* profit satisfies the condition.

This gives us the condition \max(A, B, C, D) \gt A + B + C + D - \max(A, B, C, D), or 2\max(A, B, C, D) \gt A + B + C + D, which is a bit cleaner to implement since it only requires one `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print('Yes' if 2*max(a, b, c, d) > a + b + c + d else 'No')
``

</details>
