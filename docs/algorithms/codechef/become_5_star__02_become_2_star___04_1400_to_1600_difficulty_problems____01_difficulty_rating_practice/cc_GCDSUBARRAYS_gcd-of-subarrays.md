# Gcd of Subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCDSUBARRAYS |
| Difficulty Rating | 1498 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [GCDSUBARRAYS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/GCDSUBARRAYS) |

---

## Problem Statement

You are given positive integers $N$ and $K$.

You have to construct an array $A$ of length $N$ such that :
- $1 \leq A_i \leq 10^{18}$
- $\sum_{i=1}^{N} \sum_{j=i}^{N} F(i,j) = K$, where $F(i,j)$ denotes the [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor) of all elements of the subarray $A[i, j]$.

If multiple such arrays exist, print any.
Report $-1$ if no such array exists.

Note that $A[l, r]$ denotes the subarray $[A_l ,A_{l+1}, \ldots, A_{r-1}, A_r]$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input.
    - The only line of each test case contains two space-separated integers $N$ and $K$ — the number of elements and required sum.

---

## Output Format

For each test case, output on a new line $N$ space-separated integers, denoting array $A$.
Report $-1$ if no such array exists.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq K \leq 10^{18}$
- The sum of $N$ over all test cases won't exceed $1000$.

---

## Examples

**Example 1**

**Input**

```text
3
1 5
2 4
3 1
```

**Output**

```text
5
1 2
-1
```

**Explanation**

**Test case $1$:** The only possible array of size $1$ such that the sum of gcd of all subarrays is $5$ is $A = [5]$.

**Test case $2$:** Consider an array of size $2$ as $A = [1, 2]$. The subarrays of the array are:
- $[1]$: The gcd of this subarray is $1$.
- $[1, 2]$: The gcd of this subarray is $gcd(1, 2) = 1$.
- $[2]$: The gcd of this subarray is $2$.

The sum of gcd of all subarrays is $1+1+2= 4$.

**Test case $3$:** It can be proven that there exists no subarray of size $3$ such that the sum of gcd of all subarrays of the array is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
2 4
```

**Output for this case**

```text
1 2
```



#### Test case 3

**Input for this case**

```text
3 1
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/GCDSUBARRAYS)

[Contest: Division 1](https://www.codechef.com/DEC221A/problems/GCDSUBARRAYS)

[Contest: Division 2](https://www.codechef.com/DEC221B/problems/GCDSUBARRAYS)

[Contest: Division 3](https://www.codechef.com/DEC221C/problems/GCDSUBARRAYS)

[Contest: Division 4](https://www.codechef.com/DEC221D/problems/GCDSUBARRAYS)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tejas10p](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1498

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N and K, construct an array A of length N such that

\sum_{i=1}^N \sum_{j=i}^N \gcd(A_i, A_{i+1}, \ldots, A_j) = K

#
[](#explanation-5)EXPLANATION:

Every subarray has a gcd of at least 1, and an array of length N has \frac{N\cdot (N+1)}{2} subarrays.

So, if K \lt \frac{N\cdot (N+1)}{2}, constructing a valid array is of course impossible.

Now, let K \geq \frac{N\cdot (N+1)}{2}. Constructing an array is always possible in this case, here’s one way.

The number which gives us the most control over the sum is 1, so it’d be nice if we could make most of the subarray gcds 1.

One easy way to do this is to form an array of the form [1, 1, 1, \ldots, 1, x] for some x \geq 1.

If you compute the subarray gcds for this array, you’ll see that except the singleton subarray [x], *every* other subarray has a gcd of 1.

So, the sum of subarray gcds equals x + \frac{N\cdot (N+1)}{2} - 1.

Simply choose x = K+1-\frac{N\cdot (N+1)}{2} and this sum equals K, so we’re done!

Notice that K \geq \frac{N\cdot (N+1)}{2} guarantees that x \geq 1.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
	n, k = map(int, input().split())
	if k < n*(n+1)//2: print(-1)
	else: print(*([1]*(n-1) + [k - n*(n-1)//2 - (n-1)]))
``

</details>
