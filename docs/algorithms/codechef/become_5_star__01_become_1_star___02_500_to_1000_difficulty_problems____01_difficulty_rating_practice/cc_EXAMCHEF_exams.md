# Exams

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXAMCHEF |
| Difficulty Rating | 519 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [EXAMCHEF](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/EXAMCHEF) |

---

## Problem Statement

In Chefland, there are $X$ schools, and each school has $Y$ students.
The year end results are in and a total of $Z$ students passed the exams.

Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was **strictly greater** than $50\%$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $X, Y,$ and $Z$, as mentioned in the statement.

---

## Output Format

For each test case, output on a new line, `YES`, if the total number of students who passed in Chefland was strictly greater than $50\%$, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 2\cdot 10^4$
- $1 \leq X \leq 5$
- $1 \leq Y \leq 50$
- $0 \leq Z \leq X\cdot Y$

---

## Examples

**Example 1**

**Input**

```text
4
2 10 12
2 10 3
1 5 3
3 6 9
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** The total number of students appeared were $2\cdot 10 = 20$. The number of students passed were $12$.
Thus, number of students who passed are $60\%$, which is strictly greater than $50\%$.

**Test case $2$:** The total number of students appeared were $2\cdot 10 = 20$. The number of students passed were $3$.
Thus, number of students who passed are $15\%$, which is less than $50\%$.

**Test case $3$:** The total number of students appeared were $1\cdot 5 = 5$. The number of students passed were $3$.
Thus, number of students who passed are $60\%$, which is strictly greater than $50\%$.

**Test case $4$:** The total number of students appeared were $3\cdot 6 = 18$. The number of students passed were $9$.
Thus, number of students who passed are $50\%$, which is equal to $50\%$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 10 12
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2 10 3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
1 5 3
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3 6 9
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EXAMCHEF)

[Contest: Division 1](https://www.codechef.com/START111A/problems/EXAMCHEF)

[Contest: Division 2](https://www.codechef.com/START111B/problems/EXAMCHEF)

[Contest: Division 3](https://www.codechef.com/START111C/problems/EXAMCHEF)

[Contest: Division 4](https://www.codechef.com/START111D/problems/EXAMCHEF)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

There are X schools with Y students each. Z students in total passed their exams.

Is the pass rate greater than 50\%?

# [](#explanation-5)EXPLANATION:

A pass rate of \gt 50\% means that more than half the students would need to pass the exam.

Since there are X schools and Y students in each of them, there are X\cdot Y students in total.

So, the pass rate is \gt 50\% if and only if

Z\gt \frac{X\cdot Y}{2}

Check this with an `if` condition, and print `Yes` or `No` appropriately.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print('Yes' if 2*z > x*y else 'No')
``

</details>
