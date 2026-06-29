# Positive or Negative Subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POSITNEG |
| Difficulty Rating | 1526 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [POSITNEG](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/POSITNEG) |

---

## Problem Statement

Consider an array $A$ having length $N$ such that $A_i = 2^{i-1}$ for all $1 \le i \le N$.

You are given an integer array $B$ having length $N$ such that $B_i = +1$ or $B_i = -1$ for all $1 \le i \le N$.

We create another array $C$ of length $N$ such that $C_i = B_i \cdot A_i$

- Let the number of subarrays of $C$ having sum **strictly** greater than $0$ be $P$ and
- Let the number of subarrays of $C$ having sum **strictly** less than $0$ be $Q$

Determine the value of $|P - Q|$. (Here $|x|$ denotes the absolute value of $x$)

Note: An array $X$ is a subarray of an array $Y$ if $X$ can be obtained from $Y$ by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $B$.
- The second line of each test case contains $N$ space-separated integers $B_1, B_2, \dots, B_N$ denoting the array $B$.

---

## Output Format

For each test case, output the absolute difference between the number of subarrays of $C$ having sum strictly greater than $0$ and the number of subarrays of $C$ having sum strictly less than $0$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $B_i = +1$ or $B_i = -1$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 -1 1 1
3
-1 -1 -1
2
1 -1
2
1 1
```

**Output**

```text
6
6
1
3
```

**Explanation**

In the first test case:-
the given array $B$ is $[1, -1, 1, 1]$ and the given array  $A$ is $[1, 2, 4, 8]$,.
We need to create array $C$ by multiplying corresponding elements of $A$ and $B$.
Thus, $C = [1, -2, 4, 8]$.

The subarrays of the array $[1, -2, 4, 8]$ and their corresponding sum are:

$[1]$: sum $= 1$
$[1, -2]$: sum $= -1$
$[1, -2, 4]$: sum $= 3$
$[1, -2, 4, 8]$: sum $= 11$
$[-2]$: sum $= -2$
$[-2, 4]$: sum $= 2$
$[-2, 4, 8]$: sum $= 10$
$[4]$: sum $= 4$
$[4, 8]$: sum $= 12$
$[8]$: sum $= 8$

So, the number of subarrays having sum strictly greater than $0$ is $8$, and the number of subarrays having sum strictly less than $0$ is $2$. Therefore, the answer is $|8-2|=6$.

In the 4th test case:-
Given the array $A = [1, 2]$ and the array $B = [1, 1]$, we need to create an array $C$ by multiplying corresponding elements of $A$ and $B$. Thus, we have:

C=[1,2]

The subarrays of the array $C$ and their corresponding sum are:

$[1]$: sum $= 1$
$[2]$: sum $= 2$
$[1, 2]$: sum $= 3$

So, the number of subarrays having sum strictly greater than $0$ is $3$, and the number of subarrays having sum strictly less than $0$ is $0$. Therefore, the answer is $|3-0|=3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 -1 1 1
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
3
-1 -1 -1
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
2
1 -1
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
2
1 1
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

[Practice](https://www.codechef.com/problems/POSITNEG)

[Contest: Division 1](https://www.codechef.com/START89A/problems/POSITNEG)

[Contest: Division 2](https://www.codechef.com/START89B/problems/POSITNEG)

[Contest: Division 3](https://www.codechef.com/START89C/problems/POSITNEG)

[Contest: Division 4](https://www.codechef.com/START89D/problems/POSITNEG)

***Author:*** [rajat397](https://www.codechef.com/users/rajat397)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1526

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You’re given an array B of length N consisting of 1's and -1's.

Consider a new array C, such that C_i = 2^{i-1}\cdot B_i for each 1\leq i \leq N.

Suppose P subarrays of C have a strictly positive sum and Q of them have a strictly negative sum.

Find |P - Q|.

#
[](#explanation-5)EXPLANATION:

Consider a subarray [L, R]. A little observation should tell you that:

- If B_R = 1, then C_L + C_{L+1} + \ldots + C_R \gt 0

- If B_R = -1, then C_L + C_{L+1} + \ldots + C_R \lt 0

Proof

Suppose B_R = 1, so C_R = 2^{R-1}

Recall that the powers of two satisfy 2^0 + 2^1 + \ldots + 2^{R-2} \lt 2^{R-1}, which (by removing a few terms) also means 2^{L-1} + \ldots + 2^{R-2} \lt 2^{R-1}.

This can be rearranged to 2^{R-1} - 2^{R-2} - 2^{R-3} - \ldots - 2^{L-1} \gt 0, and the LHS of this equation is the minimum possible sum of C_L + C_{L+1} + \ldots + C_R (attained when B_L = B_{L+1} = \ldots = B_{R-1} = -1)

The minimum possible sum is positive, so clearly any sum is also going to be positive.

A similar proof holds for the B_R = -1 case.

This makes the problem quite simple:

- If B_i = 1, then all the subarrays ending at i have positive sum. There are exactly i such subarrays (in 1-indexing).

- Similarly, if B_i = -1, then all i subarrays ending at this index have a negative sum.

This allows us to compute P and Q both in \mathcal{O}(N) time (if B_i = 1, add i to P; otherwise add i to Q), after which |P - Q| is easily found.

You may also note that, if we let d = P - Q, then each index i adds exactly B_i \cdot i to d.

So, a simple way to write down the answer is \displaystyle\left|\sum_{i=1}^N i\cdot B_i\right|.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * (i+1)
    print(abs(ans))
``

</details>
