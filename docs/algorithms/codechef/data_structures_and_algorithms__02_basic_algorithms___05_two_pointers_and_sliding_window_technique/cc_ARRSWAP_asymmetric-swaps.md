# Asymmetric Swaps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRSWAP |
| Difficulty Rating | 1230 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [ARRSWAP](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/ARRSWAP) |

---

## Problem Statement

Chef has two arrays $A$ and $B$ of the same size $N$.

In one operation, Chef can:
- Choose two integers $i$ and $j$ $(1 \leq i, j \leq N)$ and swap the elements $A_i$ and $B_j$.

Chef came up with a task to find the **minimum** possible value of **($A_{max} - A_{min}$)** after performing the swap operation any (possibly zero) number of times.

Since Chef is busy, can you help him solve this task?

Note that $A_{max}$ and $A_{min}$ denote the maximum and minimum elements of the array $A$ respectively.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains one integer $N$ — the number of elements in each array.
    - The second line consists of $N$ space-separated integers $A_1, A_2,\ldots ,A_N$ denoting the elements of the array $A$.
    - The third line consists of $N$ space-separated integers $B_1, B_2, \ldots ,B_N$ denoting the elements of the array $B$.

---

## Output Format

For each test case, output on a new line, the **minimum** possible value of **($A_{max} - A_{min}$)** in the array $A$ after doing swap operation any number of times.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
2 1 3
1 4 1
4
2 1 4 3
3 2 6 2
5
2 8 4 9 7
7 3 6 8 4
```

**Output**

```text
0
1
2
```

**Explanation**

**Test case $1$:** Chef can make the following operations:
- Operation $1$: Choose $i=1$ and $j=1$ and swap $A_1$ with $B_1$.
- Operation $2$: Choose $i=3$ and $j = 3$ and swap $A_3$ with $B_3$.

By doing the above operations, array $A$ becomes $[1, 1, 1]$. Here **$(A_{max} - A_{min}) = 0$.** It can be shown that this is the minimum value possible.

**Test case $2$:** Chef can make the following operations:
- Operation $1$: Choose $i=2$ and $j=2$ and swap $A_2$ with $B_2$.
- Operation $2$: Choose $i=3$ and $j=1$ and swap $A_3$ with $B_1$.
- Operation $3$: Choose $i=4$ and $j=4$ and swap $A_4$ with $B_4$.

By doing the above operations, array $A$ becomes $[2, 2, 3, 2]$. Here **$(A_{max} - A_{min}) = 1$.** It can be shown that this is the minimum value possible.

**Test case $3$:** Chef can make the following operations:
- Operation $1$: Choose $i=1$ and $j=1$ and swap $A_1$ with $B_1$.
- Operation $2$: Choose $i=3$ and $j=4$ and swap $A_3$ with $B_4$.

By doing the above operations, array $A$ becomes $[7, 8, 8, 9, 7]$. Here **$(A_{max} - A_{min}) = 2$.** It can be shown that this is the minimum value possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 1 3
1 4 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
2 1 4 3
3 2 6 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5
2 8 4 9 7
7 3 6 8 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ARRSWAP)

[Contest: Division 1](https://www.codechef.com/JAN231A/problems/ARRSWAP)

[Contest: Division 2](https://www.codechef.com/JAN231B/problems/ARRSWAP)

[Contest: Division 3](https://www.codechef.com/JAN231C/problems/ARRSWAP)

[Contest: Division 4](https://www.codechef.com/JAN231D/problems/ARRSWAP)

***Author:*** [rkyouwill](https://www.codechef.com/users/rkyouwill)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

You have two arrays A and B. In one move, you can swap any element of A with any element of B.

Find the minimum possible value of \max(A) - \min(A) that you can attain.

#
[](#explanation-5)EXPLANATION:

The fact that any element of A can be swapped with any element of B is quite powerful; in fact, we can pick any N integers out of the 2N we have and put them in A.

Proof

If A already contains the N integers we want, nothing more needs to be done.

Otherwise, B contains one such integer, and A contains one integer we *don’t* want.

Swap these two, and continue.

Now, let C be an array of size 2N containing all the elements of A and B.

Let’s sort C, so C_1 \leq C_2 \leq \ldots \leq C_{2N}.

To minimize the difference, it’s clearly optimal to choose N consecutive elements from this sorted C.

That is, if the smallest element we pick is C_i, then it’s optimal to pick the elements \{C_i, C_{i+1}, \ldots, C_{i+N-1}\}; giving us a difference of C_{i+N-1} - C_i

There are N+1 choices for the smallest element: C_1, C_2, \ldots, C_{N+1}.

Try each one, compute the appropriate maximum element (C_{i+N-1}), and take their difference.

The final answer is the minimum difference among all these.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = sorted(a + b)
    print(min(c[i] - c[i-n+1] for i in range(n-1, 2*n)))
``

</details>
