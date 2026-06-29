# Majin Vegeta

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VEGETA |
| Difficulty Rating | 1477 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [VEGETA](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/VEGETA) |

---

## Problem Statement

Babidi has summoned Majin Vegeta. He orders him to kill Supreme Kai. But Vegeta wants to get out of his control.

Babidi has laid out a trap. Vegeta is standing at the $nth$ level of mind control. In order to defeat Babidi's trap, he needs to reach $mth$ level. The levels are continuous increasing integers. At each increment of level, $nth$ to $(n+1)th$ level, for example, the energy used is - number of distinct prime factors of $n$.

Vegeta needs your help in order to figure out how much total minimum energy he needs to defeat Babidi's trap. The total energy is the sum of energy used at each increment of a level.In the calculation of energy, $n$ and $m$ are inclusive.

###Input:
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follow.
- The first and only line of each test case contains the two integers $n$ and $m$, separated by a single space.

###Output:
For each test case, print a single line containing one integer denoting the energy needed by Vegeta to escape Babidi's mind control and continue his battle with Kakarot.

###Constraints
- $1 \leq T \leq 2$
- $1 \leq n \leq m \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
2
3 7
1 1023
```

**Output**

```text
5
2177
```

**Explanation**

Example case 1: Vegeta is standing at $n$=3. As he moves from 3 to 4, energy used is 1. From 4 to 5, energy used is 1. Similarly, as he continues to move towards m=7, the total energy used is 1+1+1+2=5.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 7
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
1 1023
```

**Output for this case**

```text
2177
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Majin Vegeta Practice Problem in 1400 to 1600 difficulty problems](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/VEGETA)

### [](#problem-statement-1)Problem Statement:

Given an integer range `[n, m]` for each test case, the energy required to move between two consecutive levels `n` and `n+1` is determined by the number of distinct prime factors of `n`. So, for each level `n`, we need to compute the number of distinct prime factors and sum them up for all levels between `n` and `m` inclusive.

### [](#approach-2)Approach:

**Prime Factorization**:

- The energy used to move from level `n` to `n+1` is equal to the number of distinct prime factors of `n`. For example: For `n = 6`, the prime factors are `{2, 3}`, so the energy used is 2.

**Sieve of Eratosthenes** is typically used for finding primes, but here we will modify it to count the number of distinct prime factors for each number.

**Precompute the number of distinct prime factors for all numbers up to `10^6`**:

- Create an array `prime_factors_count` where `prime_factors_count[i]` holds the number of distinct prime factors of `i`.

- Initialize the array as zero, then for each prime `i`, increment the count of prime factors for all multiples of `i`.

**Sum the Distinct Prime Factors**:

- For each test case, simply sum the values in `prime_factors_count` from `n` to `m`.

### [](#complexity-3)Complexity:

- **Time Complexity:** The modified Sieve of Eratosthenes runs in `O(MAX log log MAX)` time, which is efficient for `MAX = 10^6`. For each test case, we simply sum the values from `prime_factors_count[n]` to `prime_factors_count[m]`, which takes `O(m - n + 1)` time. In the worst case, this is `O(MAX)` for a single test case.

- **Space Complexity:** We use an array `prime_factors_count` of size `MAX + 1`, so the space complexity is `O(MAX)`.

</details>
