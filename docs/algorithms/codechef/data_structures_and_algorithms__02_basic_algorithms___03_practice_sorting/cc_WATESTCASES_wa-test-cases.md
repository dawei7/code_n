# WA Test Cases

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATESTCASES |
| Difficulty Rating | 976 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [WATESTCASES](https://www.codechef.com/practice/course/sorting/SORTING/problems/WATESTCASES) |

---

## Problem Statement

*Chef has recently introduced a [feature](https://discuss.codechef.com/t/new-feature-wa-test-cases/101838), called WA Test Cases, which allows you to see the smallest test case that your WA code has failed in. For example, you can go to any relevant problem in [Practice](https://www.codechef.com/practice?end_rating=499&group=unattempted&hints=0&limit=20&page=0&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=&video_editorial=0&wa_enabled=1), make a submission which gets a WA verdict, and then click on the "Debug My Code" button to see the test case.*

Your job now is to find that smallest test case that a particular submission fails on. That problem has $N$ test cases, and you are given the size of each of those test cases as $S_1, S_2, \ldots, S_N$. You are also given a binary string $V$, which tells whether the submission has passed a particular test case or not. That is, if the $i^{th}$ bit of $V$ is $1$, that means that the submission has passed the $i^{th}$ test case. If it is $0$, then it has failed that test case. Your job is the output the size of the smallest test case where the submission has failed.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer, $N$.
    - The second line contains $N$ integers - $S_1, S_2, \ldots, S_N$
    - The third line contains a binary string - $V$.

---

## Output Format

For each test case, output on a new line, a single integer, which should be the size of the smallest test case where the submission has failed.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq S_i \leq 100$
- Length of $V = N$
- Each element of $V$ is either $0$ or $1$
- At least one element of $V$ will be $0$

---

## Examples

**Example 1**

**Input**

```text
5
3
5 10 3
000
3
5 10 3
001
3
5 5 3
001
3
5 5 3
101
5
10 100 100 10 10
00001
```

**Output**

```text
3
5
5
5
10
```

**Explanation**

**Test case 1:** There are $3$ test cases, and the submission has failed all the $3$ test cases. The sizes of the test cases on which it has failed are $\{5, 10, 3\}$. The smallest among these is $3$, and so the answer is $3$.

**Test case 2:** There are $3$ test cases, and the submission has failed on $2$ test cases. The sizes of the test cases on which it has failed are $\{5, 10\}$. The smallest among these is $5$, and so the answer is $5$.

**Test case 3:** There are $3$ test cases, and the submission has failed on $2$ test cases. The sizes of the test cases on which it has failed are $\{5, 5\}$. The smallest among these is $5$, and so the answer is $5$.

**Test case 4:** There are $3$ test cases, and the submission has failed on $1$ test case. The sizes of the test case on which it has failed is $\{5\}$. The smallest among these is $5$, and so the answer is $5$.

**Test case 5:** There are $5$ test cases, and the submission has failed on $4$ test cases. The sizes of the test cases on which it has failed are $\{10, 100, 100, 10\}$. The smallest among these is $10$, and so the answer is $10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
5 10 3
000
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
5 10 3
001
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
3
5 5 3
001
```

**Output for this case**

```text
5
```



#### Test case 4

**Input for this case**

```text
3
5 5 3
101
```

**Output for this case**

```text
5
```



#### Test case 5

**Input for this case**

```text
5
10 100 100 10 10
00001
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WATESTCASES)

[Contest: Division 1](https://www.codechef.com/START52A/problems/WATESTCASES)

[Contest: Division 2](https://www.codechef.com/START52B/problems/WATESTCASES)

[Contest: Division 3](https://www.codechef.com/START52C/problems/WATESTCASES)

[Contest: Division 4](https://www.codechef.com/START52D/problems/WATESTCASES)

***Author:*** [CodeChef Admin](https://www.codechef.com/users/admin)

***Preparer:*** [Souradeep Paul](https://www.codechef.com/users/souradeep1999)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

976

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the results (pass/fail) and sizes of N test cases that a submission is run on. Find the smallest test case that fails this submission.

#
[](#explanation-5)EXPLANATION

It is enough to implement what the statement asks for, using a loop.

Keep a variable mn, which will hold our answer. Initialize it to some large value (anything \geq 100).

Now, run a loop of i from 1 to N, and if V_i = 0, set mn \gets \min(mn, S_i). Finally, print the value of mn.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    s = input()
    ans = 101
    for i in range(n):
        if s[i] == '0':
            ans = min(ans, v[i])
    print(ans)
``

</details>
