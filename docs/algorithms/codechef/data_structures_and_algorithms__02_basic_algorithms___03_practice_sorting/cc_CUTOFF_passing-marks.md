# Passing Marks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CUTOFF |
| Difficulty Rating | 855 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [CUTOFF](https://www.codechef.com/practice/course/sorting/SORTING/problems/CUTOFF) |

---

## Problem Statement

In a class of $N$ students, a class test was held. The $i^{th}$ student scored $A_i$ marks. It is also known that the scores of all students were **distinct**.

A student passes the test if their score is **strictly greater** than the passing mark.
Given that exactly $X$ students pass in the test, find the **maximum** value of the passing mark of the test.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $X$ — the number of students in the class and the number of students that passed in the test.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$, where the $i^{th}$ integer denotes the marks of the $i^{th}$ student.

---

## Output Format

For each test case, output on a new line, the **maximum** value of the passing mark of the test.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq X \leq N$
- $1 \leq A_i \leq 100$
- All elements of array $A$ are **distinct**.

---

## Examples

**Example 1**

**Input**

```text
3
2 2
5 1
4 1
5 1 7 4
4 3
15 70 100 31
```

**Output**

```text
0
6
30
```

**Explanation**

**Test case $1$:** Since both students pass the test, both students scored greater than passing marks. The maximum value of passing marks can be $0$, as both students have marks greater than $0$.

**Test case $2$:** Only one student passes the test. Thus, the third student has passed the test by scoring $7$ marks. The passing marks of the test is $6$.

**Test case $3$:** Since three students pass the test, students $2, 3,$ and $4$ scored greater than passing marks. The maximum value of passing marks can be $30$, three students have marks greater than $30$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
5 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 1
5 1 7 4
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
4 3
15 70 100 31
```

**Output for this case**

```text
30
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CUTOFF)

[Contest: Division 1](https://www.codechef.com/START78A/problems/CUTOFF)

[Contest: Division 2](https://www.codechef.com/START78B/problems/CUTOFF)

[Contest: Division 3](https://www.codechef.com/START78C/problems/CUTOFF)

[Contest: Division 4](https://www.codechef.com/START78D/problems/CUTOFF)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

N students took a test, the i-th of them scored A_i marks. All the A_i are distinct.

It is known that exactly X children passed the test.

A student is said to have passed if their score is strictly more than the passing mark.

Find the highest possible passing mark.

#
[](#explanation-5)EXPLANATION:

The constraints are small, so it is possible to simply brute force the answer.

Clearly, the pass mark is between 0 and 100.

Simply try each one, and then iterate across the entire array to count the number of children who passed if this were to be the pass mark.

Among them, print the maximum value such that exactly X students passed.

This has a complexity of \mathcal{O}(100\cdot N), which is good enough.

It is possible (but unnecessary) to solve the problem with a better complexity.

#
[](#time-complexity-6)TIME COMPLEXITY

Between \mathcal{O}(N) and \mathcal{O}(100\cdot N) per test case, depending on implementation.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(101):
        passed = 0
        for y in a: passed += y > i
        if passed >= x: ans = i
    print(ans)
``

</details>
