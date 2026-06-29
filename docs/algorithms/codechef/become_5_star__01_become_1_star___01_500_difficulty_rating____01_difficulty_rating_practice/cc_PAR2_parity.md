# Parity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PAR2 |
| Difficulty Rating | 295 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PAR2](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PAR2) |

---

## Problem Statement

Ashu and Arvind participated in a coding contest, as a result of which they received $N$ chocolates. Now they want to divide the chocolates between them **equally**.

Can you help them by deciding if it is possible for them to divide all the $N$ chocolates in such a way that they each get an **equal number** of chocolates?

**You cannot break a chocolate in two or more pieces**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer $N$ — the number of chocolates they received.

---

## Output Format

For each test case output the answer on a new line — "Yes" (without quotes) if they can divide chocolates between them equally, and "No" (without quotes) otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, "Yes", "YES", and "yEs" will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
10
4
3
2
```

**Output**

```text
Yes
Yes
No
Yes
```

**Explanation**

**Test case $1$:** They can divide $10$ chocolates such that both of them get $5$ chocolates each.

**Test case $2$:** They can divide $4$ chocolates such that both of them get $2$ chocolates each.

**Test case $3$:** There is no way to divide $3$ chocolates so that they get equal number of chocolates.

**Test case $4$:** They can divide $2$ chocolates such that both of them get $1$ chocolate each.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
No
```



#### Test case 4

**Input for this case**

```text
2
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PAR2)

[Contest: Division 1](https://www.codechef.com/START65A/problems/PAR2)

[Contest: Division 2](https://www.codechef.com/START65B/problems/PAR2)

[Contest: Division 3](https://www.codechef.com/START65C/problems/PAR2)

[Contest: Division 4](https://www.codechef.com/START65D/problems/PAR2)

***Author:*** [Ashu Mittal](https://www.codechef.com/users/khaab_2004)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

295

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N chocolates. Can they be divided equally among two people?

#
[](#explanation-5)EXPLANATION:

The chocolates can be divided equally if and only if there are an even number of them…

So, just check if N is even using an `if` condition and print `Yes` if it is, `No` if it isn’t.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print('Yes' if int(input())%2 == 0 else 'No')
``

</details>
