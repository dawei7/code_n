# Candy Division

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CANDIVIDE |
| Difficulty Rating | 289 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CANDIVIDE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CANDIVIDE) |

---

## Problem Statement

There are **three** friends and a total of $N$ candies.
There will be a fight amongst the friends if all of them do **not** get the same number of candies.

Chef wants to divide **all** the candies such that there is **no fight**. Find whether such distribution is possible.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$ - the number of candies.

---

## Output Format

For each test case, output `YES`, if we can distribute all the candies between the three friends equally. Otherwise output `NO`.

You can output each character of the answer in uppercase or lowercase. For example, the strings `yEs`, `yes`, `Yes`, and YES are considered the same.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
3
4
2
6
```

**Output**

```text
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** Chef can distribute all $3$ candies such that each friend gets $1$ candy. Since all three friends have same number of candies, there is no fight.

**Test case $2$:** There exist no way of distributing **all** candies such that all three friends have same number of candies.

**Test case $3$:** There exist no way of distributing **all** candies such that all three friends have same number of candies.

**Test case $4$:** Chef can distribute all $6$ candies such that each friend gets $2$ candies. Since all three friends have same number of candies, there is no fight.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
6
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

[Practice](https://www.codechef.com/problems/CANDIVIDE)

[Contest: Division 1](https://www.codechef.com/START82A/problems/CANDIVIDE)

[Contest: Division 2](https://www.codechef.com/START82B/problems/CANDIVIDE)

[Contest: Division 3](https://www.codechef.com/START82C/problems/CANDIVIDE)

[Contest: Division 4](https://www.codechef.com/START82D/problems/CANDIVIDE)

***Authors:*** [krypto_ray](https://www.codechef.com/users/krypto_ray)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has three friends and N candies. Can he distribute all the candies equally to them?

#
[](#explanation-5)EXPLANATION:

Since each candy should be distributed, and each friend should receive an equal number, the total number of candies should be divisible by 3.

So, the answer is “Yes” if N is divisible by 3, and “No” otherwise.

In most programming languages, this can be checked using the statement `if (N%3 == 0)`

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    print('Yes' if n%3 == 0 else 'No')
``

</details>
