# Sale Season

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SALESEASON |
| Difficulty Rating | 541 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SALESEASON](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SALESEASON) |

---

## Problem Statement

It's the sale season again and Chef bought items worth a total of $X$ rupees. The sale season offer is as follows:
- if $X \le 100$, no discount.
- if $100 \lt X \le 1000$, discount is $25$ rupees.
- if $1000 \lt X \le 5000$, discount is $100$ rupees.
- if $X \gt 5000$, discount is $500$ rupees.

Find the final amount Chef needs to pay for his shopping.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input containing an integer $X$.

---

## Output Format

For each test case, output on a new line the final amount Chef needs to pay for his shopping.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10000$

---

## Examples

**Example 1**

**Input**

```text
4
15
70
250
1000
```

**Output**

```text
15
70
225
975
```

**Explanation**

**Test case $1$:** Since $X \le 100 $, there is no discount.

**Test case $3$:** Here, $X = 250$. Since $100 \lt 250 \le 1000$, discount is of $25$ rupees. Therefore, Chef needs to pay $250-25 = 225$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
70
```

**Output for this case**

```text
70
```



#### Test case 3

**Input for this case**

```text
250
```

**Output for this case**

```text
225
```



#### Test case 4

**Input for this case**

```text
1000
```

**Output for this case**

```text
975
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SALESEASON)

[Contest: Division 1](https://www.codechef.com/AUG221A/problems/SALESEASON)

[Contest: Division 2](https://www.codechef.com/AUG221B/problems/SALESEASON)

[Contest: Division 3](https://www.codechef.com/AUG221C/problems/SALESEASON)

[Contest: Division 4](https://www.codechef.com/AUG221D/problems/SALESEASON)

***Author:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Nishant Shah](https://www.codechef.com/users/nishant403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

541

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef bought items worth X rupees, and receives some flat discount on them depending on the value of X. What is the final amount paid by Chef?

#
[](#explanation-5)EXPLANATION:

This is a standard application of the `if-else` condition found in most languages. There are 4 conditions and exactly one of them is true, so check all 4, subtract the available discount, and print the answer.

- If X \leq 100, there is no discount so print X

- Else, if 100 \lt X \leq 1000, print X - 25

- Else, if 1000 \lt X \leq 5000, print X - 100

- Else, print X - 500

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's Code (Python)
``for _ in range(int(input())):
    x = int(input())
    if x > 5000:
        x -= 500
    elif x > 1000:
        x -= 100
    elif x > 100:
        x -= 25
    print(x)
``

</details>
