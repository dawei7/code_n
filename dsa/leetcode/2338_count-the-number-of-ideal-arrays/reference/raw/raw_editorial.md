[TOC]

## Solution

--- 

### Approach: Combinatorial Mathematics

#### Intuition

We're given an integer `n` and a maximum allowed value `maxValue`, and we want to count how many arrays `arr` of length `n` exist such that:

* Each element of the array is between `1` and `maxValue`
* Every element divides the next one, meaning $\text{arr}[i-1] \mid \text{arr}[i]$ for all $i$ from `1` to `n - 1`

To approach this, let's fix the **last** element of the array to be some number $x$ (where $x \in [1, \text{maxValue}]$), and count how many valid arrays of length `n` can end with $x$. The key idea is that if each element divides the next, then the entire array is a chain of divisors ending in $x$.

Now, we can represent each element in the array as a product of multiplicative steps. That is, we can write:

$$
\text{arr}[0] = k_0,\quad \text{arr}[1] = k_0k_1,\quad \ldots,\quad \text{arr}[n-1] = k_0k_1\cdots k_{n-1} = x
$$

So we’re looking for sequences of $n$ natural numbers $k_0, k_1, \dots, k_{n-1}$ whose product is exactly $x$.

This means: for a given $x$, how many ways can we split its prime factors across `n` multiplicative positions?

Let’s say the prime factorization of $x$ is:

$$
x = p_1^{a_1} \cdot p_2^{a_2} \cdots p_m^{a_m}
$$

Each exponent $a_j$ needs to be split into $n$ parts — one for each slot in the sequence. This is a classic "stars and bars" problem in combinatorics, where we’re placing $a_j$ indistinguishable items into $n$ buckets:

$$
\text{Number of ways} = \binom{a_j + n - 1}{a_j}
$$

Because different prime factors are independent, we multiply the counts for each:

$$
\text{Total sequences ending in } x = \prod_{j=1}^{m} \binom{a_j + n - 1}{a_j}
$$

Finally, we go through all $x \in [1, \text{maxValue}]$, compute the number of valid arrays that end in each $x$, and add them all up.

#### Implementation


```python
MOD = 10**9 + 7
MAX_N = 10**4 + 10
MAX_P = 15  # At most 15 prime factors

sieve = [0] * MAX_N  # Smallest prime factor

for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

ps = [[] for _ in range(MAX_N)]

for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)

c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]

c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for x in range(1, maxValue + 1):
            mul = 1
            for p in ps[x]:
                mul = mul * c[n + p - 1][p] % MOD
            ans = (ans + mul) % MOD
        return ans
```


#### Complexity Analysis

Let $m$ be the $\textit{maxValue}$, and $n$ be the length of the $\textit{arr}$ array. $\omega(m)$ represents the number of distinct prime factors of $m$, and its average order in number theory is $\log\log m$. For more details, please refer to the [Prime omega function](https://en.wikipedia.org/wiki/Prime_omega_function#Average_order_and_summatory_functions).

- Time complexity: $O((n+\omega(m))\cdot\omega(m)+m\omega(m))$.

In preprocessing, the minimum prime factor is sieved out with $O(n\log\log n)$, prime factorization requires $O(n\log n)$, and the combination number calculation requires $O((n+\omega(m))\cdot\omega(m))$. In the formal solution, the time complexity for finding the number of elements in an array is $O(m\omega(m))=O(m\log\log m)$.

- Space complexity: $O((n+\log(m))\cdot\log(m))$.

We need to save the preprocessed results of the combination numbers and the prime factorizations needed for selecting $\log(m)$ positions from $(n + \log(m) - 1)$ positions. Since the code allocates an array of fixed length, the number of factors is taken as the maximum value rather than the average, so the space complexity factor is $\log(m)$ rather than $\omega(m)$.