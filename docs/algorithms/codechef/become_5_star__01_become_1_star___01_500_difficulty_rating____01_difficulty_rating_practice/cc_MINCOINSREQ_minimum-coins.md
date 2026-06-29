# Minimum Coins

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINCOINSREQ |
| Difficulty Rating | 390 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MINCOINSREQ](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MINCOINSREQ) |

---

## Problem Statement

There are only $2$ type of denominations in Chefland:

- Coins worth $1$ rupee each
- Notes worth $10$ rupees each

Chef wants to pay his friend exactly $X$ rupees.
What is the minimum number of **coins** Chef needs to pay exactly $X$ rupees?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing a single integer $X$.

---

## Output Format

For each test case, output on a new line the minimum number of coins Chef needs to pay exactly $X$ rupees.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
53
100
9
11
```

**Output**

```text
3
0
9
1
```

**Explanation**

**Test case $1$:** Chef can use $5$ notes and $3$ coins in the optimal case.

**Test case $2$:** Chef can use $10$ notes and $0$ coins in the optimal case.

**Test case $3$:** Chef can only use $9$ coins.

**Test case $4$:** Chef can use $1$ note and $1$ coin in the optimal case.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
53
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
100
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
9
```

**Output for this case**

```text
9
```



#### Test case 4

**Input for this case**

```text
11
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

[Contest](https://www.codechef.com/START47/)

[Practice](https://www.codechef.com/problems/MINCOINSREQ)

**Setter:** [abhi_inav](https://www.codechef.com/users/abhi_inav)

**Testers:** [inov_360](https://www.codechef.com/users/inov_360), [mexomerf](https://www.codechef.com/users/mexomerf)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

390

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are 2 denominations of coins in Chefland

- Coin worth Rs 1 each

- Notes worth Rs 10 each

Chef wants to pay his friend X rupees. What is the minimum number of coins Chef needs to pay.

#
[](#explanation-5)EXPLANATION:

Chef will have to pay the minimum coins when the value paid via notes is maximised.

Hence, the number of coins he can pay with are **X mod 10** - i.e. the amount remaining when maximum possible possible amount is paid in Rs 10 notes.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    N = int(input())
    print(N%10)
``

</details>
