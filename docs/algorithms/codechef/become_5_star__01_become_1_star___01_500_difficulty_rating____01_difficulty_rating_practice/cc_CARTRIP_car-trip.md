# Car Trip

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CARTRIP |
| Difficulty Rating | 374 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CARTRIP](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CARTRIP) |

---

## Problem Statement

Chef rented a car for a day.

Usually, the cost of the car is Rs $10$ per km. However, since Chef has booked the car for the whole day, he needs to pay for **at least** $300$ kms even if the car runs less than $300$ kms.

If the car ran $X$ kms, determine the cost Chef needs to pay.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$ - denoting the number of kms Chef travelled.

---

## Output Format

For each test case, output the cost Chef needs to pay.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
5
800
3
299
301
300
```

**Output**

```text
8000
3000
3000
3010
3000
```

**Explanation**

**Test case $1$:** The car runs for $800$ kms. Thus, he needs to pay $800\cdot 10 = 8000$ rupees.

**Test case $2$:** The car runs for $3$ kms. However, since Chef booked the car for whole day, he needs to pay for at least $300$ kms. Thus, he needs to pay $300\cdot 10 = 3000$ rupees.

**Test case $3$:** The car runs for $299$ kms. However, since Chef booked the car for whole day, he needs to pay for at least $300$ kms. Thus, he needs to pay $300\cdot 10 = 3000$ rupees.

**Test case $4$:** The car runs for $301$ kms. Thus, he needs to pay $301\cdot 10 = 3010$ rupees.

**Test case $5$:** The car runs for $300$ kms. Thus, he needs to pay $300\cdot 10 = 3000$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
800
```

**Output for this case**

```text
8000
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
3000
```



#### Test case 3

**Input for this case**

```text
299
```

**Output for this case**

```text
3000
```



#### Test case 4

**Input for this case**

```text
301
```

**Output for this case**

```text
3010
```



#### Test case 5

**Input for this case**

```text
300
```

**Output for this case**

```text
3000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CARTRIP)

[Contest: Division 1](https://www.codechef.com/START53A/problems/CARTRIP)

[Contest: Division 2](https://www.codechef.com/START53B/problems/CARTRIP)

[Contest: Division 3](https://www.codechef.com/START53C/problems/CARTRIP)

[Contest: Division 4](https://www.codechef.com/START53D/problems/CARTRIP)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

374

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has booked a car at a rate of rupees 10 per kilometer. He has to pay for at least 300 kilometers no matter what.

If Chef travels for X kilometers, how much will he pay?

#
[](#explanation-5)EXPLANATION:

Chef will pay for 300 kilometers if X \leq 300, and X kilometers otherwise. Each kilometer costs 10 rupees, so the answer is simply 10\cdot \max(X, 300).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print(10 * max(300, int(input())))
``

</details>
