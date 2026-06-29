# Broken Phone

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BROKENPHONE |
| Difficulty Rating | 451 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BROKENPHONE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BROKENPHONE) |

---

## Problem Statement

Uttu broke his phone. He can get it repaired by spending $X$ rupees or he can buy a new phone by spending $Y$ rupees. Uttu wants to spend as little money as possible. Find out if it is better to get the phone repaired or to buy a new phone.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the cost of getting the phone repaired and the cost of buying a new phone.

---

## Output Format

For each test case,
- output `REPAIR` if it is better to get the phone repaired.
- output `NEW PHONE` if it is better to buy a new phone.
- output `ANY` if both the options have the same price.

You may print each character of `REPAIR`, `NEW PHONE` and `ANY` in uppercase or lowercase (for example, `any`, `ANy`, `Any` will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \le X, Y \le 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
100 1000
10000 5000
3000 3000
```

**Output**

```text
REPAIR
NEW PHONE
ANY
```

**Explanation**

**Test Case 1:** It is better to get the phone repaired since $100 \lt 1000$.

**Test Case 2:** It is better to buy a new phone since $10000 \gt 5000$.

**Test Case 3:** Uttu can choose either of the two options since $3000 = 3000$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 1000
```

**Output for this case**

```text
REPAIR
```



#### Test case 2

**Input for this case**

```text
10000 5000
```

**Output for this case**

```text
NEW PHONE
```



#### Test case 3

**Input for this case**

```text
3000 3000
```

**Output for this case**

```text
ANY
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BROKENPHONE)

[Contest: Division 1](https://www.codechef.com/START55A/problems/BROKENPHONE)

[Contest: Division 2](https://www.codechef.com/START55B/problems/BROKENPHONE)

[Contest: Division 3](https://www.codechef.com/START55C/problems/BROKENPHONE)

[Contest: Division 4](https://www.codechef.com/START55D/problems/BROKENPHONE)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/JeevanJyot)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

451

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Uttu broke his phone. He can get it fixed for X rupees or buy a new one for Y rupees. Which option is cheaper?

#
[](#explanation-5)EXPLANATION:

There are three cases:

- If X \lt Y, print “Repair”

- If X \gt Y, print “New phone”

- If X = Y, print “Any”

The three cases can be checked using `if` conditions.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('repair' if x < y else ('new phone' if x > y else 'any'))
``

</details>
