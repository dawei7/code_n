# Greater Average

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGPROBLEM |
| Difficulty Rating | 500 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [AVGPROBLEM](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AVGPROBLEM) |

---

## Problem Statement

You are given $3$ numbers $A, B,$ and $C$.

Determine whether the **average** of $A$ and $B$ is **strictly greater** than $C$ or not?

**NOTE:** Average of $A$ and $B$ is defined as $\frac{(A+B)}{2}$. For example, average of $5$ and $9$ is $7$, average of $5$ and $8$ is $6.5$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $3$ integers $A, B,$ and $C$.

---

## Output Format

For each test case, output `YES` if average of $A$ and $B$ is strictly greater than $C$, `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YeS`, `yEs`, `yes` and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, C \leq 10$

---

## Examples

**Example 1**

**Input**

```text
5
5 9 6
5 8 6
5 7 6
4 9 8
3 7 2
```

**Output**

```text
YES
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** The average value of $5$ and $9$ is $7$ which is strictly greater than $6$.

**Test case $2$:** The average value of $5$ and $8$ is $6.5$ which is strictly greater than $6$.

**Test case $3$:** The average value of $5$ and $7$ is $6$ which is not strictly greater than $6$.

**Test case $4$:** The average value of $4$ and $9$ is $6.5$ which is not strictly greater than $8$.

**Test case $5$:** The average value of $3$ and $7$ is $5$ which is strictly greater than $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 9 6
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5 8 6
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5 7 6
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
4 9 8
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
3 7 2
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

[Practice](https://www.codechef.com/problems/AVGPROBLEM)

[Contest: Division 1](https://www.codechef.com/START53A/problems/AVGPROBLEM)

[Contest: Division 2](https://www.codechef.com/START53B/problems/AVGPROBLEM)

[Contest: Division 3](https://www.codechef.com/START53C/problems/AVGPROBLEM)

[Contest: Division 4](https://www.codechef.com/START53D/problems/AVGPROBLEM)

***Author:*** [ Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

500

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given A, B, and C, determine whether the average of A and B is strictly greater than C.

#
[](#explanation-5)EXPLANATION:

The average of A and B is \frac{A+B}{2}. Compute this value and check whether it is greater than C using an `if` condition.

Make sure to compute \frac{A+B}{2} using floats, since the standard `/` division in most languages is integer (floor) division. You should use something like `(A+B)/2.0` instead of `(A+B)/2`.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('yes' if a+b > 2*c else 'no')
``

</details>
