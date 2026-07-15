# Prime Arrangements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1175 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-arrangements/) |

## Problem Description

### Goal

Consider every permutation of the integers from $1$ through $n$, placed at positions numbered from $1$ through $n$. A permutation is valid when every prime number appears at a prime-numbered position. Equivalently, all prime values must occupy the prime positions, while all non-prime values occupy the remaining positions.

Count the valid permutations. Because the count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The inclusive upper bound of the values and positions, with $1 \leq n \leq 100$.
- Let $p$ be the number of primes not greater than $n$.

**Return value**

- The number of permutations of $1,2,\ldots,n$ in which prime values occupy prime-numbered positions, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `12`

There are three prime values and prime positions, so the count is $3!\times 2!=12$.

**Example 2**

- Input: `n = 100`
- Output: `682289015`

**Example 3**

- Input: `n = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(n\log\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count the prime positions.** Use the Sieve of Eratosthenes on the integers through $n$. Initially mark every value at least `2` as prime. For each still-prime candidate whose square is at most `n`, mark its multiples beginning at `candidate * candidate` as composite. Earlier multiples already have a smaller prime factor.

**Reduce the arrangement rule to two independent permutations.** There are exactly $p$ prime values and exactly $p$ prime-numbered positions. Any ordering of those prime values among those positions is valid, producing $p!$ choices. The other $n-p$ values are all non-prime—including `1`—and can be ordered freely among the other positions in $(n-p)!$ ways.

Multiplying the independent choices gives $p!(n-p)!$. Compute both factorials modulo $10^9+7$ so intermediate values stay bounded; modular multiplication preserves the required final remainder.

#### Complexity detail

The sieve takes $O(n\log\log n)$ time and stores $n+1$ Boolean flags. Counting flags and multiplying the two factorial ranges take $O(n)$ additional time. Total time is $O(n\log\log n)$ and auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Trial division for every value:** Testing divisors only through each square root uses $O(n\sqrt n)$ time and $O(1)$ auxiliary space, which is acceptable for the small public bound but asymptotically slower.
- **Test every possible divisor:** Checking all smaller integers for every candidate is correct but takes $O(n^2)$ time.
- **One is not prime:** Value `1` and position `1` belong to the non-prime group.
- **Smallest input:** For `n = 1`, the sole permutation is valid.
- **Modulo timing:** Reducing after each multiplication avoids constructing enormous factorial integers in languages with fixed-width arithmetic.
- **Symmetric counts:** Prime values cannot enter non-prime positions because the $p$ prime positions already must contain all $p$ prime values.

</details>
