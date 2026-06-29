# Running Comparison

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RUNCOMPARE |
| Difficulty Rating | 899 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [RUNCOMPARE](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/RUNCOMPARE) |

---

## Problem Statement

Alice and Bob recently got into running, and decided to compare how much they ran on different days.

They each ran for $N$ days — on the $i^{th}$ day, Alice ran $A_i$ meters and Bob ran $B_i$ meters.

On each day,
- Alice is *unhappy* if Bob ran **strictly more than twice** her distance, and *happy* otherwise.
- Similarly, Bob is *unhappy* if Alice ran **strictly more than twice** his distance, and *happy* otherwise.

For example, on a given day
- If Alice ran $200$ meters and Bob ran $500$, Alice would be unhappy but Bob would be happy.
- If Alice ran $500$ meters and Bob ran $240$, Alice would be happy and Bob would be unhappy.
- If Alice ran $300$ meters and Bob ran $500$, both Alice and Bob would be happy.

On how many of the $N$ days were **both** Alice and Bob happy?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$ — the number of days.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the distances run by Alice on the $N$ days.
    - The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$ — the distances run by Bob on the $N$ days.

---

## Output Format

For each test case, output on a new line the number of days when **both** Alice and Bob were happy.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq A_i, B_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
3
100 200 300
300 200 100
4
1000 1000 1000 1000
400 500 600 1200
4
800 399 1400 532
2053 2300 3400 23
5
800 850 900 950 1000
600 800 1000 1200 1400
```

**Output**

```text
1
3
0
5
```

**Explanation**

**Test case $1$:** Alice is unhappy on the first day, since she ran $100$ meters but Bob ran $300$; and $300$ is more than twice of $100$.
Similarly, Bob is unhappy on the third day.
Both Alice and Bob are happy on the second day, so the answer is $1$.

**Test case $2$:** Bob is unhappy on day $1$ and happy on every other day, while Alice is happy on every day. So, they're both happy on three days — the second, third, and fourth.

**Test case $3$:** Alice is unhappy on days $1, 2, 3$ and Bob is unhappy on day $4$.

**Test case $4$:** Alice and Bob are both happy on all five days.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
100 200 300
300 200 100
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
1000 1000 1000 1000
400 500 600 1200
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4
800 399 1400 532
2053 2300 3400 23
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
5
800 850 900 950 1000
600 800 1000 1200 1400
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RUNCOMPARE)

[Contest: Division 1](https://www.codechef.com/START80A/problems/RUNCOMPARE)

[Contest: Division 2](https://www.codechef.com/START80B/problems/RUNCOMPARE)

[Contest: Division 3](https://www.codechef.com/START80C/problems/RUNCOMPARE)

[Contest: Division 4](https://www.codechef.com/START80D/problems/RUNCOMPARE)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Testers:*** [wuhudsm](https://www.codechef.com/users/wuhudsm), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice and Bob ran for N days each, with distances A_i and B_i on the i-th day, respectively.

On a given day, each person is unhappy if the other one ran more than twice their distance; and happy otherwise.

On how many of the days were both Alice and Bob happy?

#
[](#explanation-5)EXPLANATION:

On the i-th day,

- Alice is happy if B_i \leq 2\cdot A_i

- Bob is happy if A_i \leq 2\cdot B_i

So, they’re *both* happy only when both conditions are true simultaneously.

This leads to a rather simple solution: using a loop and a conditional statement, simply count the number of i such that (A_i \leq 2\cdot B_i) and (B_i \leq 2\cdot A_i).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	ans = 0
	for i in range(n):
	    if a[i] <= 2*b[i] and b[i] <= 2*a[i]: ans += 1
	print(ans)
``

</details>
