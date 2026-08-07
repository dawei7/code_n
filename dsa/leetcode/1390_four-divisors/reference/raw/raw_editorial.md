### Approach 1: Enumeration

#### Intuition

We can traverse each element in the array $\textit{nums}$ and sequentially check whether each element has exactly four factors. For any element $x$, we can determine the number of its factors using a method similar to prime number checking. The key idea is that if an integer $x$ has a factor $y$, then it must also have a factor $x/y$, and at least one of $y$ and $x/y$ is no greater than $\sqrt{x}$. Therefore, we only need to enumerate possible factors $y$ within the interval $[1, \sqrt{x}]$ and obtain the other factors of $x$ through $x/y$, resulting in a time complexity of $O(\sqrt{x})$.

If $x$ has exactly four factors, we add the sum of its factors to the answer.

#### Implementation


```python
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            # factor_cnt: number of factors
            # factor_sum: sum of factors
            factor_cnt = factor_sum = 0
            i = 1
            while i * i <= num:
                if num % i == 0:
                    factor_cnt += 1
                    factor_sum += i
                    if (
                        i * i != num
                    ):  # check if i and num/i are equal; if not, consider num/i as a new factor.
                        factor_cnt += 1
                        factor_sum += num // i
                i += 1
            if factor_cnt == 4:
                ans += factor_sum
        return ans
```


#### Complexity Analysis

Let $N$ be the length of the array $\textit{nums}$, and let $C$ be the range of elements in the array $\textit{nums}$, which does not exceed $10^5$.

- Time complexity: $O(N\sqrt{C})$.

- Space complexity: $O(1)$.

### Approach 2: Preprocessing

#### Intuition

Our intuition tells us that integers with exactly four factors are not very common. Can we find them in advance?

According to the "Fundamental Theorem of Arithmetic" (also known as the "Unique Factorization Theorem"), if an integer $x$ can be decomposed as:

$$
x = p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k}
$$

where $p_i$ are distinct prime numbers, the number of divisors of $x$ is:

$$
\textit{factor\_count}(x) = \prod_{i=1}^k (\alpha_i + 1)
$$

If the value of $\textit{factor\_count}(x)$ is $4$, then there are only two possibilities:

- An integer $x$ has only one prime factor with an exponent of $3$. In this case, $\textit{factor\_count}(x) = (3+1) = 4$.

- An integer $x$ has two prime factors, each with an exponent of $1$. In this case, $\textit{factor\_count}(x) = (1+1)(1+1) = 4$.

For the first case, we need to find all primes not exceeding $C^{1/3}$. For the second case, we need to find all primes not exceeding $C$, then multiply them pairwise and remove the results that exceed $C$. Here, the definition of $C$ is consistent with that in the complexity analysis section of Approach 1. In summary, we need to find all primes not exceeding $C$.

How can we find all primes not greater than $C$? At this point, the "Sieve of Eratosthenes" or "Euler's sieve" can be used. They help us efficiently find all such primes. The detailed algorithms of these two sieves are not the focus of this solution, so they are not discussed here. After finding these primes, we can construct all $x$ that satisfy the above two conditions. We store $x$ and the sum of its factors in a hash map (HashMap), allowing us to check in $O(1)$ time whether each element in the array $\textit{nums}$ meets the requirements and to compute the sum of factors for the elements that do.

#### Implementation


```python
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # C is the upper bound of the array nums, and C3 is the cube root of C.
        C, C3 = 100000, 46

        isprime = [True] * (C + 1)
        primes = list()

        # Sieve of Eratosthenes
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for j in range(i + i, C + 1, i):
                isprime[j] = False

        # Sieve of Euler
        """
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if i * prime > C:
                    break
                isprime[i * prime] = False
                if i % prime == 0:
                    break
        """

        # Construct all four factors using the prime table
        factor4 = dict()
        for prime in primes:
            if prime <= C3:
                factor4[prime**3] = 1 + prime + prime**2 + prime**3
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                if primes[i] * primes[j] <= C:
                    factor4[primes[i] * primes[j]] = (
                        1 + primes[i] + primes[j] + primes[i] * primes[j]
                    )
                else:
                    break

        ans = 0
        for num in nums:
            if num in factor4:
                ans += factor4[num]
        return ans
```


#### Complexity Analysis

Let $\pi(X)$ be the prime-counting function, representing the number of primes not exceeding $X$.

- Time complexity: $O(\pi^2(C) + C\log\log C + N)$ or $O(\pi^2(C) + C + N)$.
  
  The time complexity of the Sieve of Eratosthenes is $O(C\log\log C)$, and the time complexity of the Sieve of Euler is $O(C)$. The time complexity of constructing all four-factor numbers using the prime table is $O(\pi(C^{1/3})) + O(\pi^2(C)) = O(\pi^2(C))$, and the time complexity of traversing all elements in the array $\textit{nums}$ and checking whether they have four factors is $O(N)$.

- Space complexity: $O(C + \pi(C))$.
  
  Regardless of which sieve method is used, an array of length $C$ is required to record whether each number is prime, and an array of length $\pi(C)$ is required to store all the primes.

---