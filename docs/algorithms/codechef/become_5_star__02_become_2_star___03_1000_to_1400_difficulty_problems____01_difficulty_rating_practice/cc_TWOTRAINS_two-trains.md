# Two Trains

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWOTRAINS |
| Difficulty Rating | 1230 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [TWOTRAINS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/TWOTRAINS) |

---

## Problem Statement

There are $2$ trains $A$ and $B$ and $N$ stations in a line from $1$ to $N$ in order. There is also an array $P$ of length $N-1$ such that $P_i$ $(1\le i \lt N)$ denotes the amount of time any train takes to go from the $i$-th station to the $(i+1)$-th station.

Initially, both trains are at station $1$. Train $A$ departs from station $1$ and stops directly at station $N$. For safety purposes, it is maintained that train $B$ cannot depart from station $i$ unless train $A$ has already reached station $(i+1)$ $(1 \le i \lt N)$.

Find the **minimum** time after which train $B$ reaches station $N$, once train $A$ departs from station $1$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$, denoting number of stations.
    - The next line contains $N-1$ space-separated integers, $P_1,P_2,\ldots ,P_{N-1}$.

---

## Output Format

For each test case, output on a new line the minimum time after which train $B$ reaches station $N$.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $1 \leq P_i \leq 10^3$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
4
3
3 5
4
5 2 6
```

**Output**

```text
8
13
19
```

**Explanation**

**Test case $1$:** $A$ reaches station $2$ at $t=4$ and at this time $B$ departs from station $1$ and reaches station $2$ at $t=4+4=8$.

**Test case $2$:** Following is the timeline of two trains-
- At $t=3$, $A$ reaches station $2$ and $B$ departs from station $1$.
- At $t=6$, $B$ reaches station $2$ but $A$ has not yet reached station $3$, so train $B$ will wait at station $2$.
- At $t=8$, $A$ reaches station $3$ and $B$ departs from station $2$.
- At $t=8+5=13$, train $B$ reaches station $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
4
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
3
3 5
```

**Output for this case**

```text
13
```



#### Test case 3

**Input for this case**

```text
4
5 2 6
```

**Output for this case**

```text
19
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TWOTRAINS)

[Contest: Division 1](https://www.codechef.com/AUG221A/problems/TWOTRAINS)

[Contest: Division 2](https://www.codechef.com/AUG221B/problems/TWOTRAINS)

[Contest: Division 3](https://www.codechef.com/AUG221C/problems/TWOTRAINS)

[Contest: Division 4](https://www.codechef.com/AUG221D/problems/TWOTRAINS)

***Author:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Nishant Shah](https://www.codechef.com/users/nishant403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1230

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are two trains A and B, and N stations. A train takes time P_i to go from station i to station (i+1).

Train B can depart from station i only after train A has reached station (i+1). What is the minimum amount of time needed for train B to reach station N?

#
[](#explanation-5)EXPLANATION:

Let S = P_1 + P_2 + \ldots + P_{N-1}, i.e, the sum of all the elements of P.

Let M = \max(P_1, P_2, \ldots, P_{N-1}), i.e, the maximum element  of P.

Then the answer is just S + M.

How?

The journey of train B can be broken into two separate parts: time taken by it when travelling from one station to another, and time taken while waiting for train A to reach the next station.

The time taken while travelling is clearly just P_1 + P_2 + \ldots + P_{N-1}, by definition.

Now, let M = \max(P_1, P_2, \ldots, P_{N-1}).

The minimum waiting time is definitely at least M, since while train A crosses the section that needs M time, train B cannot move along that section at all, and hence must wait for a total of \geq M units of time already.

Conversely, suppose train B just waits for M seconds at the very beginning before even starting, and starts moving at the end of the M-th second. It is easy to see that, since M = \max(P_1, P_2, \ldots, P_{N-1}), whenever train B is at station i, train A has already reached station (i+1) (and may have gone even further). So, no more waiting time is needed.

Thus, the minimum waiting time is exactly M, and hence the answer is S + M as claimed.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case

#
[](#code-7)CODE:

Editorialist's Code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) + max(a))
``

</details>
