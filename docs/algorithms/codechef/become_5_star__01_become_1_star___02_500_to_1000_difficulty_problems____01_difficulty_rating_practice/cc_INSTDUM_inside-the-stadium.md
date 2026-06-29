# Inside The Stadium

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INSTDUM |
| Difficulty Rating | 895 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [INSTDUM](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/INSTDUM) |

---

## Problem Statement

Shubman Gill is playing an international match.
He played a total of $N$ balls, where, in the $i^{th}$ ball, he scored $A_{i}$ runs.

The *strike rate* of a player is calculated as : $\frac{\text{no. of runs}}{\text{no. of balls played}}\times 100$.

Preet, a math enthusiast, is currently watching the match. Help him find the number of times, Shubman's *strike rate* became **exactly** $100$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ - the total number of balls played by Gill.
    - The second line of each test case contains $N$ space-separated integers where $A_{i}$ denotes runs scored on $i^{th}$ ball.

---

## Output Format

For each test case, output on a new line, the total number of times the strike rate of Gill became $100$.

---

## Constraints

- $1 \leq T \leq 10^{5}$
- $1 \leq N \leq 10^{5}$
- $0 \leq A_i \leq 6$
- The sum of $N$ over all test cases won't exceed $10^{6}$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 0 2 3
5
2 6 0 1 0
3
1 1 1
```

**Output**

```text
2
0
3
```

**Explanation**

**Test case $1$:** Shubhman's strike rate would be:
- After $1$ ball: $\frac{\text{1}}{\text{1}}\times 100 = 100$.
- After $2$ balls: $\frac{\text{1}}{\text{2}}\times 100 = 50$.
- After $3$ balls: $\frac{\text{3}}{\text{3}}\times 100 = 100$.
- After $4$ balls: $\frac{\text{6}}{\text{4}}\times 100 = 150$.

Thus, the strike rate was exactly $100$ twice.

**Test case $2$:** Shubhman's strike rate would be:
- After $1$ ball: $\frac{\text{2}}{\text{1}}\times 100 = 200$.
- After $2$ balls: $\frac{\text{8}}{\text{2}}\times 100 = 400$.
- After $3$ balls: $\frac{\text{8}}{\text{3}}\times 100 = 266.66$.
- After $4$ balls: $\frac{\text{9}}{\text{4}}\times 100 = 225$.
- After $5$ balls: $\frac{\text{9}}{\text{5}}\times 100 = 180$.

Thus the strike rate was never exactly $100$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 0 2 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
2 6 0 1 0
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3
1 1 1
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

[Practice](https://www.codechef.com/problems/INSTDUM)

[Contest: Division 1](https://www.codechef.com/START85A/problems/INSTDUM)

[Contest: Division 2](https://www.codechef.com/START85B/problems/INSTDUM)

[Contest: Division 3](https://www.codechef.com/START85C/problems/INSTDUM)

[Contest: Division 4](https://www.codechef.com/START85D/problems/INSTDUM)

***Authors:*** [d_k_7386](https://www.codechef.com/users/d_k_7386), [preet_25](https://www.codechef.com/users/preet_25)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

895

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the runs scored in each of N balls, find the number of times when the strike rate was exactly 100.

#
[](#explanation-5)EXPLANATION:

Recall that the strike rate is defined as

\frac{ \text{total runs scored} } { \text{balls faced} } \cdot 100

This equals 100 if and only if the number of runs scored equals the number of balls faced.

After i balls, the number of runs scored is exactly A_1 + A_2 + \ldots + A_i.

So, the answer is simply the number of i such that A_1 + A_2 + \ldots + A_i = i.

This can be easily computed in \mathcal{O}(N) with a simple loop.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    runs, ans = 0, 0
    for i in range(n):
        runs += a[i]
        if runs == i+1: ans += 1
    print(ans)
``

</details>
