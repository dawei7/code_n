# Prime Factorization Method using Sieve O (log n) 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SIEV04 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Sieve of Eratosthenes |
| Official Link | [SIEV04](https://www.codechef.com/learn/course/number-theory/LINTDSA09/problems/SIEV04) |

---

## Problem Statement

The main idea behind this logic is to divide the number repeatedly from its **Smallest Prime factor (SPF)** until the we are left with $1$,with this way we can obtain the occurrence of all the prime factors in a more efficient way ,For this we precompute all the **(SPF)** for all the numbers from 1 to $MAXN$, this precomputation can be done using
**Sieve of Eratosthenes** where we mark each number with index which first time visits this number and due to the monotonous nature of index is assures that the given index is the **(SPF)** of the current number

The function `Sieve()` shows the implementation of the discussed idea.

Now, after we are done with precalculating the smallest prime factor for every number we will divide our number n (whose prime factorization is to be calculated) by its corresponding smallest prime factor till n becomes 1.
This is in the function `getFactorization(int x)`

**Time Complexity:**

The precomputation for the smallest prime factor is done in `O(n log log n)` using a sieve. In the calculation step, we repeatedly divide the number every time by the smallest prime number until it becomes 1. Let's consider a worst-case scenario in which the smallest prime factor is 2. This would result in `log n` division steps. Hence, we can conclude that the time complexity in the worst case is `O(log n)`.

Fill in the blanks in the code on the right which factorizes an integer.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
6
```

**Output**

```text
2
3
```
