# Unstable Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COUNTSUB |
| Difficulty Rating | 1545 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [COUNTSUB](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/COUNTSUB) |

---

## Problem Statement

You are given an array $A$ of size $N$.

We define the function $f(l, r) = \sum_{i=l}^{r-1}(A_i-A_{i+1})$, where $1\le l \le r \le N$.
Note that $f(i, i)$ is defined as $0$.

A subarray $A[l, r]$ is considered *unstable* if $f(l,r) \neq (A_r-A_l)$.

Count the number of *unstable* subarrays in the array.

Note that the subarray $A[l, r]$ consists of $A_l, A_{(l+1)}, \ldots, A_{(r-1)}, A_r$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line, the count of *unstable* subarrays.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
10 20 30
4
1 2 1 2
5
1 2 3 4 5
```

**Output**

```text
3
4
10
```

**Explanation**

**Test case $1$:** There are $3$ unstable subarrays:
- $A[1, 2]$: Here $f(1, 2) = 10-20 = -10$ and $A_2 - A_1 = 10$.
- $A[1, 3]$: Here $f(1, 3) = (10-20) + (20-30) = -10-10 = -20$ and $A_3 - A_1 = 20$.
- $A[2, 3]$: Here $f(2, 3) = 20-30 = -10$ and $A_3 - A_2 = 10$.

**Test case $2$:** There are $4$ unstable subarrays:
- $A[1, 2]$: Here $f(1, 2) = 1-2 = -1$ and $A_2 - A_1 = 1$.
- $A[1, 4]$: Here $f(1, 4) = (1-2) + (2-1) + (1-2) = -1+1-1 = -1$ and $A_4 - A_1 = 1$.
- $A[2, 3]$: Here $f(2, 3) = 2-1 =  1$ and $A_3 - A_2 =-1$.
- $A[3, 4]$: Here $f(3, 4) = 1-2 = -1$ and $A_4 - A_3 = 1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
10 20 30
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COUNTSUB)

[Contest: Division 1](https://www.codechef.com/START88A/problems/COUNTSUB)

[Contest: Division 2](https://www.codechef.com/START88B/problems/COUNTSUB)

[Contest: Division 3](https://www.codechef.com/START88C/problems/COUNTSUB)

[Contest: Division 4](https://www.codechef.com/START88D/problems/COUNTSUB)

***Author:*** [ro27](https://www.codechef.com/users/ro27)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1545

# [](#prerequisites-3)PREREQUISITES:

Knowledge of maps/dictionaries OR sorting

# [](#problem-4)PROBLEM:

You’re given an array A. Define the function f as

f(L, R) = \sum_{i=L}^{R-1} (A_i - A_{i+1})

with f(i, i) = 0.

Count the number of unstable subarrays, i.e, subarrays (L, R) such that f(L, R) \neq A_R - A_L.

# [](#explanation-5)EXPLANATION:

Notice that if you expand it out, f(L, R) is a telescoping sum. That is,

\begin{aligned}
f(L, R) &= \sum_{i=L}^{R-1} (A_i - A_{i+1}) \\
&= (A_L - A_{L+1}) + (A_{L+1} - A_{L+2}) + \dots + (A_{R-1} - A_R) \\
&= A_L + (-A_{L+1} + A_{L+1}) + (-A_{L+2} + A_{L+2}) + \dots + (-A_{R-1} + A_{R-1}) - A_R \\
&= A_L - A_R
\end{aligned}

So, f(L, R) = A_L - A_R, which means a subarray is unstable if A_L - A_R \neq A_R - A_L.

Let’s instead count the number of subarrays that *aren’t* unstable, i.e, which satisfy A_L - A_R = A_R - A_L. We can then subtract this from the total number of subarrays, which equals \frac{N\cdot (N+1)}{2}

Notice that this equality simply translates to A_L = A_R.

So, our objective is count the number of subarrays whose endpoints are equal.

This is the same as counting the number of pairs of equal elements in the array!

We do need an algorithm to do this quickly, since \mathcal{O}(N^2) won’t cut it.

There are several ways of doing this faster, here’s one:

- Let \text{freq} be a `map`/`dict`, such that \text{freq}[x] denotes the number of times we’ve seen x *so far*.

Initially, \text{freq} is empty.

- Iterate i from 1 to N. When processing index i:

- Increase \text{freq}[A_i] by 1.

- Then, add \text{freq}[A_i] to the answer, since that’s the number of indices to the left of i whose value equals A_i.

Depending on the kind of map used, this is \mathcal{O}(N\log N) or (expected) \mathcal{O}(N) time, which is fast enough.

There are other implementations that don’t need maps; for example using sorting.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) or \mathcal{O}(N\log N) per test case.

# [](#code-7)CODE:

Editorialist's code (Python, dict)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    ans = n*(n+1)//2
    for x in a:
        if x not in freq: freq[x] = 0
        freq[x] += 1
        ans -= freq[x]
    print(ans)
``

Editorialist's code (Python, sorting)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = n*(n+1)//2
    cur = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]: cur = 1
        else: cur += 1
        ans -= cur
    print(ans)
``

</details>
