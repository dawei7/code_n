# Codechef Airlines

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AIRLINES |
| Difficulty Rating | 475 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [AIRLINES](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AIRLINES) |

---

## Problem Statement

Chef has opened a new airline. Chef has $10$ airplanes where each airplane has a capacity of $X$ passengers.
On the first day itself, $Y$ people are willing to book a seat in **any one** of Chef's airplanes.

Given that Chef charges $Z$ rupees for each ticket, find the **maximum** amount he can earn on the first day.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $X, Y,$ and $Z$ — the capacity of each airplane, the number of people willing to book a seat in any one of Chef's airplanes on the first day, and the cost of each seat respectively.

---

## Output Format

For each test case, output on a new line, the **maximum** amount Chef can earn on the first day.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y, Z \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
2 15 10
1 10 1
5 60 100
1 11 7
```

**Output**

```text
150
10
5000
70
```

**Explanation**

**Test case $1$:** Chef has $10$ airplanes and each airplane has a capacity of $2$ passengers. Thus, there are $20$ seats available in total.
There are $15$ people who want to book a seat. Since we have enough seats for everyone, all $15$ people can book their seats and pay $10$ rupees each. The total money Chef earns is $15\cdot 10 = 150$.

**Test case $2$:** Chef has $10$ airplanes and each airplane has a capacity of $1$ passenger. Thus, there are $10$ seats available in total.
There are $10$ people who want to book a seat. Since we have enough seats for everyone, all $10$ people can book their seats and pay $1$ rupee each. The total money Chef earns is $10\cdot 1 = 10$.

**Test case $3$:** Chef has $10$ airplanes and each airplane has a capacity of $5$ passengers. Thus, there are $50$ seats available in total.
There are $60$ people who want to book a seat. Since we have only $50$ seats, only $50$ people can book their seats and pay $100$ rupees each. The total money Chef earns is $50\cdot 100 = 5000$.

**Test case $4$:** Chef has $10$ airplanes and each airplane has a capacity of $1$ passenger. Thus, there are $10$ seats available in total.
There are $11$ people who want to book a seat. Since we have only $10$ seats, only $10$ people can book their seats and pay $7$ rupees each. The total money Chef earns is $10\cdot 7 = 70$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 15 10
```

**Output for this case**

```text
150
```



#### Test case 2

**Input for this case**

```text
1 10 1
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
5 60 100
```

**Output for this case**

```text
5000
```



#### Test case 4

**Input for this case**

```text
1 11 7
```

**Output for this case**

```text
70
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AIRLINES)

[Contest: Division 1](https://www.codechef.com/START77A/problems/AIRLINES)

[Contest: Division 2](https://www.codechef.com/START77B/problems/AIRLINES)

[Contest: Division 3](https://www.codechef.com/START77C/problems/AIRLINES)

[Contest: Division 4](https://www.codechef.com/START77D/problems/AIRLINES)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has 10 airplanes, each with X seats.

Y passengers want to book a seat, and each seat costs rupees Z.

How much money can Chef earn?

#
[](#explanation-5)EXPLANATION:

10 airplanes with X seats each gives Chef a total of 10\cdot X seats.

Since Y people want to book a seat, the best Chef can do is to sell \min(Y, 10\cdot X) seats.

With each seat costing Z rupees, Chef thus earns

Z\times \min(Y, 10\cdot X)

rupees.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(z * min(y, 10*x))
``

</details>
