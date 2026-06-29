# Recent contest problems

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECENTCONT |
| Difficulty Rating | 793 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [RECENTCONT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/RECENTCONT) |

---

## Problem Statement

*CodeChef recently revamped its [practice page](https://www.codechef.com/practice) to make it easier for users to identify the next problems they should solve by introducing some new features:*
- *Recent Contest Problems - Contains only problems from the last 2 contests*
- *Separate Un-Attempted,  Attempted, and All tabs*
- *Problem Difficulty Rating - The Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience*
- *Popular Topics and Tags*

Chef has been participating regularly in rated contests but missed the last two contests due to his college exams. He now wants to solve them and so he visits the practice page to view these [problems](https://www.codechef.com/practice/recent).

Given a list of $N$ contest codes, where each contest code is either `START38` or `LTIME108`, help Chef count how many problems were featured in each of the contests.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of two lines of input.
- First line of input contains the total count of problems that appeared in the two recent contests - $N$.
- Second line of input contains the list of $N$ contest codes. Each code is either `START38` or `LTIME108`, to which each problem belongs.

---

## Output Format

For each test case, output two integers in a single new line - the first integer should be the number of problems in `START38`, and the second integer should be the number of problems in `LTIME108`.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 1000$
- Each of the contest codes will be either `START38` or `LTIME108`.

---

## Examples

**Example 1**

**Input**

```text
4
3
START38 LTIME108 START38
4
LTIME108 LTIME108 LTIME108 START38
2
LTIME108 LTIME108
6
START38 LTIME108 LTIME108 LTIME108 START38 LTIME108
```

**Output**

```text
2 1
1 3
0 2
2 4
```

**Explanation**

**Test case $1$:** There are $2$ `START38`s in the input, which means that there were $2$ problems in `START38`. Similarly, there was $1$ problem in `LTIME108`.

**Test case $2$:** There is $1$ `START38` in the input, which means that there was $1$ problem in `START38`. Similarly, there were $3$ problems in `LTIME108`.

**Test case $3$:** There are no `START38`s in the input, which means that were $0$ problems in `START38`. Similarly, there were $2$ problems in `LTIME108`.

**Test case $4$:** There are $2$ `START38`s in the input, which means that there were $2$ problems in `START38`. Similarly, there were $4$ problems in `LTIME108`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
START38 LTIME108 START38
```

**Output for this case**

```text
2 1
```



#### Test case 2

**Input for this case**

```text
4
LTIME108 LTIME108 LTIME108 START38
```

**Output for this case**

```text
1 3
```



#### Test case 3

**Input for this case**

```text
2
LTIME108 LTIME108
```

**Output for this case**

```text
0 2
```



#### Test case 4

**Input for this case**

```text
6
START38 LTIME108 LTIME108 LTIME108 START38 LTIME108
```

**Output for this case**

```text
2 4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START39A/problems/RECENTCONT)

[Contest Division 2](https://www.codechef.com/START39B/problems/RECENTCONT)

[Contest Division 3](https://www.codechef.com/START39C/problems/RECENTCONT)

[Contest Division 4](https://www.codechef.com/START39D/problems/RECENTCONT)

Setter: [Hrishikesh](https://www.codechef.com/users/hrishik85)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

793

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

*CodeChef recently revamped its [practice page](https://www.codechef.com/practice) to make it easier for users to identify the next problems they should solve by introducing some new features:*

- *Recent Contest Problems - Contains only problems from the last 2 contests*

- *Separate Un-Attempted,  Attempted, and All tabs*

- *Problem Difficulty Rating - The Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience*

- *Popular Topics and Tags*

Chef has been participating regularly in rated contests but missed the last two contests due to his college exams. He now wants to solve them and so he visits the practice page to view these [problems](https://www.codechef.com/practice/recent).

Given a list of N problem codes, where each problem code is either `START38` or `LTIME108`, help Chef count how many problems were featured in each of the contests.

#
[](#explanation-5)EXPLANATION:

This is a simple array traversal problem. Just keep two counts, start and ltime to keep the count of problems having problem code as `START38` and  `LTIME108` respectively.

Traverse through the array of strings and if current word is `START38`, then increment start by 1 else increment ltime by 1.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/AlDH)

[Tester1’s Solution](http://p.ip.fi/7VPJ)

[Tester2’s Solution](http://p.ip.fi/MLSW)

</details>
