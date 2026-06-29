# Multivitamin Tablets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TABLETS |
| Difficulty Rating | 376 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TABLETS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TABLETS) |

---

## Problem Statement

The doctor prescribed Chef to take a multivitamin tablet $3$ times a day for the next $X$ days.

Chef already has $Y$ multivitamin tablets.

Determine if Chef has enough tablets for these $X$ days or not.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the number of days Chef needs to take tablets and the number of tablets Chef already has.

---

## Output Format

For each test case, output `YES` if Chef has enough tablets for these $X$ days. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \le X \le 100$
- $0 \le Y \le 1000$

---

## Examples

**Example 1**

**Input**

```text
4
1 10
12 0
10 29
10 30
```

**Output**

```text
YES
NO
NO
YES
```

**Explanation**

**Test Case 1:** Chef has $10$ tablets and Chef needs $3$ tablets for $1$ day. Therefore Chef has enough tablets.

**Test Case 2:** Chef has $0$ tablets and Chef needs $36$ tablets for $12$ days. Therefore Chef does not have enough tablets.

**Test Case 3:** Chef has $29$ tablets and Chef needs $30$ tablets for $10$ days. Therefore Chef does not have enough tablets.

**Test Case 4:** Chef has $30$ tablets and Chef needs $30$ tablets for $10$ days. Therefore Chef has enough tablets.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
12 0
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
10 29
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
10 30
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TABLETS)

[Contest: Division 1](https://www.codechef.com/START73A/problems/TABLETS)

[Contest: Division 2](https://www.codechef.com/START73B/problems/TABLETS)

[Contest: Division 3](https://www.codechef.com/START73C/problems/TABLETS)

[Contest: Division 4](https://www.codechef.com/START73D/problems/TABLETS)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [mexomerf](https://www.codechef.com/users/mexomerf), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has Y multivitamin tablets, and needs to take 3 of them each day for the next X days.

Does Chef have enough tablets in stock?

#
[](#explanation-5)EXPLANATION:

Chef needs 3 tablets a day for X days, making a total of 3X tablets.

So, the answer is `Yes` if 3X \leq Y and `No` otherwise; which can be checked using an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if y >= 3*x else 'No')
``

</details>
