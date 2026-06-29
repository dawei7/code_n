# Largest and Second Largest

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LARGESECOND |
| Difficulty Rating | 928 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [LARGESECOND](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/LARGESECOND) |

---

## Problem Statement

You are given an array $A$ of $N$ integers.
Find the **maximum** sum of **two distinct** integers in the array.

**Note:** It is guaranteed that there exist at least two distinct integers in the array.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains single integer $N$ — the size of the array.
    - The next line contains $N$ space-separated integers, denoting the array $A$.

---

## Output Format

For each test case, output on a new line, the maximum sum of two distinct integers in the array.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 1000$
- The sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
4 1 6
7
3 7 2 1 1 5 3
5
8 2 9 4 9
2
1 2
```

**Output**

```text
10
12
17
3
```

**Explanation**

**Test case $1$:** The maximum sum of two distinct elements is $4 + 6 = 10$ .

**Test case $2$:** The maximum sum of two distinct elements is $7 + 5 = 12$.

**Test case $3$:** The maximum sum of two distinct elements is $8 + 9 = 17$.

**Test case $4$:** The maximum sum of two distinct elements is $1 + 2 = 3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
4 1 6
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
7
3 7 2 1 1 5 3
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
5
8 2 9 4 9
```

**Output for this case**

```text
17
```



#### Test case 4

**Input for this case**

```text
2
1 2
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

[Practice](https://www.codechef.com/problems/LARGESECOND)

[Contest: Division 1](https://www.codechef.com/START88A/problems/LARGESECOND)

[Contest: Division 2](https://www.codechef.com/START88B/problems/LARGESECOND)

[Contest: Division 3](https://www.codechef.com/START88C/problems/LARGESECOND)

[Contest: Division 4](https://www.codechef.com/START88D/problems/LARGESECOND)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

928

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A, find the largest possible sum of two distinct elements in it.

#
[](#explanation-5)EXPLANATION:

Clearly, the answer is just the sum of the two largest different elements in A.

There are many ways to find these two elements.

Perhaps the simplest is as follows:

- First, run a loop to find the largest element of A, say M_1.

- Then, run another loop to find the largest element of A that’s not M_1, say M_2.

This can be done by simply ignoring all the occurrences of M_1 in the array.

The answer is then M_1 + M_2.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m1, m2 = max(a), 0
    for x in a:
        if x != m1: m2 = max(m2, x)
    print(m1 + m2)
``

</details>
