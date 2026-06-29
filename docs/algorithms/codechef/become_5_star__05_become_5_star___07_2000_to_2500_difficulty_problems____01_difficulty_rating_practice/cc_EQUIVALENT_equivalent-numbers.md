# Equivalent Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQUIVALENT |
| Difficulty Rating | 2087 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [EQUIVALENT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/EQUIVALENT) |

---

## Problem Statement

Chef calls a pair of integers $(A, B)$ *equivalent* if there exist some **positive** integers $X$ and $Y$ such that $A^X = B^Y$.

Given $A$ and $B$, determine whether the pair is *equivalent* or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $A$ and $B$, as mentioned in statement.

---

## Output Format

For each test case, output `YES` if $(A, B)$ is an *equivalent* pair, `NO` otherwise.

The output is case-insensitive. Thus, the strings `Yes`, `YES`, `yes`, and `yeS` are all considered identical.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq A, B \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
2 3
8 4
12 24
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Test case $1$:** There are no positive integers $X$ and $Y$ which satisfy $A^X = B^Y$.

**Test case $2$:** Let $X = 2$ and $Y = 3$. Thus, $A^X = 8^2 = 64$ and $B^Y = 4^3 = 64$. Thus, the pair $(8, 4)$ is *equivalent*.

**Test case $3$:** There are no positive integers $X$ and $Y$ which satisfy $A^X = B^Y$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
8 4
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
12 24
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

[Contest Division 1](https://www.codechef.com/START58A/problems/EQUIVALENT)

[Contest Division 2](https://www.codechef.com/START58B/problems/EQUIVALENT)

[Contest Division 3](https://www.codechef.com/START58C/problems/EQUIVALENT)

[Contest Division 4](https://www.codechef.com/START58D/problems/EQUIVALENT)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Satyam](https://www.codechef.com/users/satyam_343), [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

2087

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef calls a pair of integers (A, B) *equivalent* if there exist some **positive** integers X and Y such that A^X = B^Y.

Given A and B, determine whether the pair is *equivalent* or not.

#
[](#explanation-5)EXPLANATION:

In order for two number A and B to satisfy the relation

A^x = B^y

where x and y are two positive integers, it needs to satisfy the following conditions:

1.) Both the number should have the same prime factors.

2.) The ratio of frequency of each prime factors of the two numbers should be the same.

Thus we would first check if both the numbers have same prime factors and if yes then we would calculate the frequency of each prime factor for the two numbers and then check if each pair of frequencies have the same ratio.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(\sqrt{max(A,B)}), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/3cMJ)

[Setter’s Solution](http://p.ip.fi/WNDp)

[Tester1’s Solution](http://p.ip.fi/xcWy)

[Tester2’s Solution](http://p.ip.fi/an6J)

</details>
