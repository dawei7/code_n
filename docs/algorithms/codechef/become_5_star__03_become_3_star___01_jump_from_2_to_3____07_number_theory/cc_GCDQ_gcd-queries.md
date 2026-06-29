# Gcd Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCDQ |
| Difficulty Rating | 1674 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [GCDQ](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/GCDQ) |

---

## Problem Statement

You are given an array **A** of integers of size **N**. You will be given **Q** queries where each query is represented by two integers **L, R**. You have to find the [gcd](http://en.wikipedia.org/wiki/Greatest_common_divisor)(Greatest Common Divisor) of the array after excluding the part from range **L** to **R** inclusive (1 Based indexing). You are guaranteed that after excluding the part of the array
remaining array is non empty.

### Input

- First line of input contains an integer **T** denoting number of test cases.

- For each test case, first line will contain two space separated integers **N, Q**.

-  Next line contains **N** space separated integers denoting array **A**.

- For next **Q** lines, each line will contain a query denoted by two space separated integers **L, R**.

### Output
For each query, print a single integer representing the answer of that query.

### Constraints

**Subtask #1: 40 points**

- **2 ≤ T, N ≤ 100, 1 ≤ Q ≤ N, 1 ≤ A[i] ≤ 105**

- **1 ≤ L, R ≤ N and L ≤ R**

**Subtask #2: 60 points**

- **2 ≤ T, N ≤ 105, 1 ≤ Q ≤ N, 1 ≤ A[i] ≤ 105**

- **1 ≤ L, R ≤ N and L ≤ R**

-  Sum of **N** over all the test cases will be less than or equal to **106**.

**Warning : ** Large IO(input output), please use faster method for IO.

---

## Examples

**Example 1**

**Input**

```text
1
3 3
2 6 9
1 1
2 2
2 3
```

**Output**

```text
3
1
2
```

**Explanation**

**Test case $1$:** The given array is $[2, 6, 9]$.
- Query $1$: On excluding the range $[1,1]$, the remaining elements are $[6, 9]$. The *gcd* of $6$ and $9$ is $3$.
- Query $2$: On excluding the range $[2,2]$, the remaining elements are $[2, 9]$. The *gcd* of $2$ and $9$ is $1$.
- Query $3$: On excluding the range $[2,3]$, the remaining elements are $[2]$. The *gcd* of $2$ is $2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/GCDQ)

[Contest](http://www.codechef.com/JAN15/problems/GCDQ)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

EASY

### PRE-REQUISITES:

GCD, Precomputation

### PROBLEM:

You are given an array **A** of integers of size **N**. You will be given **Q** queries where each query is represented by two integers **L**, **R**. You have to find the **gcd**(Greatest Common Divisor) of the array after excluding the part from range **L** to **R** inclusive (1 Based indexing). You are guaranteed that after excluding the part of the array remaining array is non empty.

1 ? **N**, **Q** ? 100000

### EXPLANATION:

If you do it naively(ie. calculating GCD of remaining array for each query), the worstcase complexity will be **O(N * Q)**.

Let’s denote by **G(L, R)**, the GCD of **AL, AL+1 … AR**. We can observe that for query **[L, R]**, we need GCD of **G(1, L-1)** and **G(R+1, N)**.

So, we precalculate prefix and suffix gcd arrays.

If we have:

**Prefixi** = GCD of **A1, A2 … Ai**

**Suffixi** = GCD of **AN, AN-1 … Ai**

answer to query **[L, R]**, would be GCD of **PrefixL-1** and **SuffixR+1**.

We can calculate prefix and suffix arrays in **O(N)** if we notice that:

**Prefixi** = GCD(**Prefixi-1**, **Ai**)

**Suffixi** = GCD(**Suffixi+1**, **Ai**)

Pseudo Code for building prefix and suffix arrays:

``n,a=input
pre[n],suf[n]

//base case
pre[1]=a[1]
suf[n]=a[n]

for i=2 to n:
    pre[i] = gcd(pre[i-1], a[i])

for i=n-1 to 1:
    suf[i] = gcd(suf[i+1], a[i])
``

So, overall complexity would be **O((N + Q) * K)**, where **K** is a constant factor for gcd calculation.

### ALTERNATIVE SOLUTION:

Use segment trees for range gcd queries. But note that a factor of **log N** will be increased in complexity.

### SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/JAN15/Setter/GCDQ.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/JAN15/Tester/GCDQ.cpp)

</details>
