# Chef and Chapters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEMCOURSES |
| Difficulty Rating | 350 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SEMCOURSES](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SEMCOURSES) |

---

## Problem Statement

This semester, Chef took $X$ courses. Each course has $Y$ units and each unit has $Z$ chapters in it.

Find the total number of chapters Chef has to study this semester.

---

## Input Format

- The first line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers $X, Y,$ and $Z$.

---

## Output Format

For each test case, output in a single line the total number of chapters Chef has to study this semester.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y, Z \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1
2 1 2
1 2 3
```

**Output**

```text
1
4
6
```

**Explanation**

**Test case $1$:** There is only $1$ course with $1$ unit. The unit has $1$ chapter. Thus, the total number of chapters is $1$.

**Test case $2$:** There are $2$ courses with $1$ unit each. Thus, there are $2$ units. Each unit has $2$ chapters. Thus, the total number of chapters is $4$.

**Test case $3$:** There is only $1$ course with $2$ units. Each unit has $3$ chapters. Thus, the total number of chapters is $6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 1 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START36A/problems/SEMCOURSES)

[Contest Division 2](https://www.codechef.com/START36B/problems/SEMCOURSES)

[Contest Division 3](https://www.codechef.com/START36C/problems/SEMCOURSES)

[Contest Division 4](https://www.codechef.com/START36D/problems/SEMCOURSES)

Setter: [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

Testers: [Felipe Mota](https://www.codechef.com/users/fmota), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

350

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

This semester, Chef took X courses. Each course has Y units and each unit has Z chapters in it.

Find the total number of chapters Chef has to study this semester.

#
[](#explanation-5)EXPLANATION:

For each test case, the total number of chapters would be the product of X, Y and Z.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/yy02)

[Setter’s Solution](https://p.ip.fi/Q-nC)

[Tester 1’s Solution](https://p.ip.fi/hS9s)

[Tester 2’s Solution](https://p.ip.fi/ZJjk)

</details>
