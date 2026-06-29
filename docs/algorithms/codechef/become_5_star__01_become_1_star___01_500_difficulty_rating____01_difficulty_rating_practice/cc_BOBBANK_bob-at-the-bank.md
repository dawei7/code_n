# Bob at the Bank

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BOBBANK |
| Difficulty Rating | 481 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BOBBANK](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BOBBANK) |

---

## Problem Statement

Bob has an account in the Bobby Bank. His current account balance is $W$ rupees.

Each month, the office in which Bob works deposits a fixed amount of $X$ rupees to his account.
$Y$ rupees is deducted from Bob's account each month as bank charges.

Find his final account balance after $Z$ months. Note that the account balance can be negative as well.

---

## Input Format

- The first line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing four integers $W,X,Y,$ and $Z$ — the initial amount, the amount deposited per month, the amount deducted per month, and the number of months.

---

## Output Format

For each test case, output in a single line the final balance in Bob's account after $Z$ months.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq W,X,Y,Z \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
100 11 1 10
999 25 36 9
2500 100 125 101
```

**Output**

```text
200
900
-25
```

**Explanation**

**Test case $1$:** Bob's current account balance is $100$. At the end of each month Bob gets Rs $11$ and pays Rs $1$, thus gaining $10$ per month. Thus, at the end of $10$ months, Bob will have $100 + 10 \times 10 = 200$.

**Test case $2$:** Bob's current account balance is $999$. At the end of each month Bob gets Rs $25$ and pays Rs $36$, thus losing $11$ per month. Thus, at the end of $9$ months, Bob will have $999 - 11 \times 9 = 900$.

**Test case $3$:** Bob's current account balance is $2500$. At the end of each month Bob gets Rs $100$ and pays Rs $125$, thus losing $25$ per month. Thus, at the end of $101$ months, Bob will have $2500 - 25 \times 101 = -25$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 11 1 10
```

**Output for this case**

```text
200
```



#### Test case 2

**Input for this case**

```text
999 25 36 9
```

**Output for this case**

```text
900
```



#### Test case 3

**Input for this case**

```text
2500 100 125 101
```

**Output for this case**

```text
-25
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BOBBANK)

[Contest: Division 1](https://www.codechef.com/SEP221A/problems/BOBBANK)

[Contest: Division 2](https://www.codechef.com/SEP221B/problems/BOBBANK)

[Contest: Division 3](https://www.codechef.com/SEP221C/problems/BOBBANK)

[Contest: Division 4](https://www.codechef.com/SEP221D/problems/BOBBANK)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Preparer:*** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

481

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Bob’s current bank balance is W rupees. Each month, rupees X is deposited into it and Y is deducted. How much remains in it after Z months?

#
[](#explanation-5)EXPLANATION:

Each month, X rupees is added and Y is deducted, leading to an overall change of X-Y in his balance.

In Z months, this amounts to a total change of Z\times(X-Y).

So, the final balance is W + Z\times(X-Y).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    print(w + z*(x-y))
``

</details>
