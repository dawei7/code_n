# Netflix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NETFLIX |
| Difficulty Rating | 493 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [NETFLIX](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/NETFLIX) |

---

## Problem Statement

Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netfix allows only two users to share a subscription.

Given that Alice, Bob, and Charlie have $A, B,$ and $C$ rupees respectively and a Netflix subscription costs $X$ rupees, find whether any two of them can contribute to buy a subscription.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains four space-separated integers $A, B, C,$ and $X$ — the amount that Alice, Bob, and Charlie have, and the cost of a Netflix subscription respectively.

---

## Output Format

For each test case, output `YES`, if any two of Alice, Bob, and Charlie can contribute to buy a Netflix subscription or `NO` otherwise.

You may print each character in uppercase or lowercase. For example, `NO`, `no`, `No`, and `nO` are all considered identical.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, C, X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 1 1 3
2 3 1 5
4 2 3 4
2 1 4 7
```

**Output**

```text
NO
YES
YES
NO
```

**Explanation**

**Test case $1$:** No two people can contribute to collect enough money to buy a Netflix subscription.

**Test case $2$:** Alice and Bob can contribute and collect a total of $5$ rupees which is enough to buy a Netflix subscription of $5$ rupees.

**Test case $3$:** One possible way is, Bob and Charlie can contribute and collect a total of $5$ rupees which is enough to buy a Netflix subscription of $4$ rupees.
Note that there are other possible ways as well.

**Test case $4$:** No two people can contribute to collect enough money to buy a Netflix subscription.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 3
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
2 3 1 5
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
4 2 3 4
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
2 1 4 7
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

[Practice](https://www.codechef.com/problems/NETFLIX)

[Contest: Division 1](https://www.codechef.com/COOK144A/problems/NETFLIX)

[Contest: Division 2](https://www.codechef.com/COOK144B/problems/NETFLIX)

[Contest: Division 3](https://www.codechef.com/COOK144C/problems/NETFLIX)

[Contest: Division 4](https://www.codechef.com/COOK144D/problems/NETFLIX)

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

Alice, Bob, and Charlie have A, B, C rupees respectively.

A Netflix subscription costs X rupees.

Is it possible for exactly two of them to purchase a subscription?

#
[](#explanation-5)EXPLANATION:

There are three possible sums of two people: A+B, A+C, B+C.

If any of these three is \geq X, the answer is “Yes”. Otherwise, the answer is “No”.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c, x = map(int, input().split())
    print('Yes' if max(a+b, a+c, b+c) >= x else 'No')
``

</details>
