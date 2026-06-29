# Read Pages

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | READPAGES |
| Difficulty Rating | 343 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [READPAGES](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/READPAGES) |

---

## Problem Statement

Chef has started studying for the upcoming test. The textbook has $N$ pages in total. Chef wants to read at most $X$ pages a day for $Y$ days.

Find out whether it is possible for Chef to complete the whole book.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains three space-separated integers $N, X,$ and $Y$ — the number of pages, the number of pages Chef can read in a day, and the number of days.

---

## Output Format

For each test case, output on a new line, `YES`, if Chef can complete the whole book in given time, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase. For example, `Yes`, `YES`, `yes`, and `yES` are all considered identical.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq X, Y \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
5 2 3
10 3 3
7 7 1
3 2 1
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** Chef can read two pages on the first day, two on the second day, and the remaining one on the third day.

**Test case $2$:** Chef cannot complete all ten pages in three days.

**Test case $3$:** Chef can read all seven pages in one day.

**Test case $4$:** Chef cannot complete all three pages in one day.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
10 3 3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
7 7 1
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3 2 1
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

[Practice](https://www.codechef.com/problems/READPAGES)

[Contest: Division 1](https://www.codechef.com/START76A/problems/READPAGES)

[Contest: Division 2](https://www.codechef.com/START76B/problems/READPAGES)

[Contest: Division 3](https://www.codechef.com/START76C/problems/READPAGES)

[Contest: Division 4](https://www.codechef.com/START76D/problems/READPAGES)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef can read upto X pages a day for Y days. Can he read N pages in total?

#
[](#explanation-5)EXPLANATION:

Chef can read a maximum of X\cdot Y pages in total.

So, the answer is `Yes` if X\cdot Y \geq N; and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x, y = map(int, input().split())
    print('Yes' if n <= x*y else 'No')
``

</details>
