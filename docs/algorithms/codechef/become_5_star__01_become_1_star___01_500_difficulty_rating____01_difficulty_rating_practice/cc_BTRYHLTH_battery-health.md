# Battery Health

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTRYHLTH |
| Difficulty Rating | 296 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BTRYHLTH](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BTRYHLTH) |

---

## Problem Statement

Apple considers any iPhone with a battery health of $80\%$ or above, to be in *optimal* condition.

Given that your iPhone has $X\%$ battery health, find whether it is in *optimal* condition.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains an integer $X$ — the battery health.

---

## Output Format

For each test case, output on a new line, `YES`, if the battery is in *optimal* condition, and `NO` otherwise.

You may print each character in uppercase or lowercase. For example, `NO`, `no`, `No` and `nO`, are all considered identical.

---

## Constraints

- $1 \leq T \leq 100$
- $0 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
97
42
80
10
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** The battery health is $97 \%$ which is greater than equal to $80 \%$. Thus, the battery is in optimal condition.

**Test case $2$:** The battery health is $42 \%$ which is less than $80 \%$. Thus, the battery is not in optimal condition.

**Test case $3$:** The battery health is $80 \%$ which is greater than equal to $80 \%$. Thus, the battery is in optimal condition.

**Test case $4$:** The battery health is $10 \%$ which is less than $80 \%$. Thus, the battery is not in optimal condition.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
97
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
42
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
80
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
10
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

[Practice](https://www.codechef.com/problems/BTRYHLTH)

[Contest: Division 1](https://www.codechef.com/COOK144A/problems/BTRYHLTH)

[Contest: Division 2](https://www.codechef.com/COOK144B/problems/BTRYHLTH)

[Contest: Division 3](https://www.codechef.com/COOK144C/problems/BTRYHLTH)

[Contest: Division 4](https://www.codechef.com/COOK144D/problems/BTRYHLTH)

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

An iPhone with at least 80\% battery health is in optimal condition.

Your iPhone’s battery health is X\%. Is it in optimal condition?

#
[](#explanation-5)EXPLANATION:

The answer is “Yes” if X \geq 80 and “No” otherwise.

This can be checked using `if` conditions.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Yes' if x >= 80 else 'No')
``

</details>
