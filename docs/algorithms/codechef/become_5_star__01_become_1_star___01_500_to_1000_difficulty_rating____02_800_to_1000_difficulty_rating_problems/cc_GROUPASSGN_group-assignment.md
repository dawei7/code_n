# Group Assignment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GROUPASSGN |
| Difficulty Rating | 872 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [GROUPASSGN](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/GROUPASSGN) |

---

## Problem Statement

Chef's professor is planning to give his class a group assignment. There are $2N$ students in the class, with distinct roll numbers ranging from $1$ to $2N$. Chef's roll number is $X$.

The professor decided to create $N$ groups of $2$ students each. The groups were created as follows: the first group consists of roll numbers $1$ and $2N$, the second group of roll numbers $2$ and $2N - 1$, and so on, with the final group consisting of roll numbers $N$ and $N+1$.

Chef wonders who his partner will be. Can you help Chef by telling him the roll number of his partner?

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $N$ and $X$, denoting the number of groups that will be formed, and Chef's roll number.

---

## Output Format

For each test case, output the roll number of the student that will be Chef's partner.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^8$
- $1 \leq X \leq 2N$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
3 1
3 4
```

**Output**

```text
3
6
3
```

**Explanation**

**Test case $1$**: The groups will be $\{(1, 4), (2, 3)\}$. Chef's roll number is $2$, so his partner's roll number will be $3$.

**Test case $2$**: The groups will be $\{(1, 6), (2, 5), (3, 4)\}$. Chef's roll number is $1$, so his partner's roll number will be $6$.

**Test case $3$**: The groups will be $\{(1, 6), (2, 5), (3, 4)\}$. Chef's roll number is $4$, so his partner's roll number will be $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 1
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
3 4
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START31A/problems/GROUPASSGN)

[Contest Division 2](https://www.codechef.com/START31B/problems/GROUPASSGN)

[Contest Division 3](https://www.codechef.com/START31C/problems/GROUPASSGN)

[Contest Division 4](https://www.codechef.com/START31D/problems/GROUPASSGN)

Setter: [ Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [ Aryan](https://www.codechef.com/users/aryanc403), [ Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

[Arithemetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression)

#
[](#problem-4)PROBLEM:

Chef’s professor is planning to give his class a group assignment. There are 2N students in the class, with distinct roll numbers ranging from 1 to 2N. Chef’s roll number is X.

The professor decided to create N groups of 2 students each. The groups were created as follows: the first group consists of roll numbers 1 and 2N, the second group of roll numbers 2 and 2N?1, and so on, with the final group consisting of roll numbers N and N+1.

Chef wonders who his partner will be. Can you help Chef by telling him the roll number of his partner?

#
[](#explanation-5)EXPLANATION:

Note that the roll numbers form an [Arithemetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression) with a common difference of 1. Consider the following [Arithemetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression) of roll numbers: 1, 2, 3, 4, . .  X . . . 2N.

Now, the teacher pairs students from the start and end. By the properties of AP, all the pairs will have sum = 2N+1.

Let Chef’s partner have a roll number y. Thus, the pair will look like (X,y).

\implies X+y = 2N+1

\implies y = 2N+1-X

Hence, chef’s partner has a roll number y, i.e 2N+1-X.

#
[](#time-complexity-6)TIME COMPLEXITY:

The above calculation can be done in constant time. Hence, the solution has a time complexity of O(1).

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://pastebin.com/u7dBPwBG)

[Setter’s Solution](http://p.ip.fi/wtk3)

[Tester-1’s Solution](http://p.ip.fi/_7Sb)

[Tester-2’s Solution](http://p.ip.fi/6HyU)

</details>
