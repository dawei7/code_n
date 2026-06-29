# Couple Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COUGAME |
| Difficulty Rating | 347 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [COUGAME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COUGAME) |

---

## Problem Statement

There are $G$ girl and $B$ boy students at IIT (BHU) such that $B \gt G$.

If ICM were a team game where teams could only be of size $2$, having **exactly** $1$ girl student and $1$ boy student, what would be the **minimum** number of boy students from IIT (BHU) who would not be able to participate?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $G$ and $B$, the number of girl and boy students at IIT (BHU) respectively.

---

## Output Format

For each test case, output a single integer on a new line, the **minimum** number of boy students from IIT (BHU) who would not be able to participate.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq G \lt B \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
1 3
2 4
3 10
```

**Output**

```text
2
2
7
```

**Explanation**

**Test case $1$:** There is only $1$ girl and $3$ boys. So, one team can be formed, and minimum $2$ boys will be left behind.

**Test case $2$:** There are $2$ girls and $4$ boys. So, maximum $2$ teams can be formed, and minimum $2$ boys will be left behind.

**Test case $3$**: There are $3$ girls and $10$ boys. So, maximum $3$ teams can be formed, and minimum $7$ boys will be left behind.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3 10
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COUGAME)

[Contest: Division 1](https://www.codechef.com/START83A/problems/COUGAME)

[Contest: Division 2](https://www.codechef.com/START83B/problems/COUGAME)

[Contest: Division 3](https://www.codechef.com/START83C/problems/COUGAME)

[Contest: Division 4](https://www.codechef.com/START83D/problems/COUGAME)

***Author:*** [pd_codes](https://www.codechef.com/users/pd_codes)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

G girls and B boys want to make teams of one boy and one girl each.

Given that G \lt B, how many boys will be left without a partner at minimum?

#
[](#explanation-5)EXPLANATION:

Since there are fewer girls than boys, at most G boys will be able to find partners.

This leaves B - G boys without a partner, and so the answer is B - G.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    g, b = map(int, input().split())
    print(b - g)
``

</details>
