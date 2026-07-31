## General

**Only the extreme prime positions can maximize the distance.** Suppose the indices containing prime values are $p_1 < p_2 < \dots < p_k$. Every pair lies inside the interval from $p_1$ to $p_k$, so its distance is at most $p_k-p_1$. It is therefore sufficient to locate the first and last prime-valued elements; the intervening prime positions cannot improve the answer.

The values are restricted to the fixed range from $1$ through $100$. Store the 25 primes in that range in a constant lookup set. Scan from the left until finding the first value in the set, then scan from the right until finding the last one. The contract guarantees at least one prime value, so both searches always succeed.

The left search returns $p_1$ because it examines indices in increasing order and stops at the first qualifying value. The right search analogously returns $p_k$. Their difference is attainable by choosing those two indices and, by the extreme-position argument, no other pair can have a greater distance. When there is only one prime position, both searches return the same index and the valid answer is zero.

## Complexity detail

Let $n$ be the length of `nums`. The two searches inspect at most $n$ positions each, and membership in the fixed prime set is constant time, giving $O(n)$ time. The set always contains exactly the primes through $100$, independent of $n$, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Single full scan:** Track the first prime index and update the last prime index whenever another is found. This has the same $O(n)$ time and $O(1)$ auxiliary space.
- **Trial division:** Test each value with divisors through its square root instead of using a set. This is source-general, but the fixed value bound makes a lookup simpler and faster.
- **Sieve of Eratosthenes:** Precompute primality through $100$ in a Boolean array. It provides the same constant-size lookup but adds initialization machinery for a tiny fixed domain.
- **Enumerate all prime pairs:** Collect prime indices and compare every pair. It is correct but can take $O(n^2)$ time even though only the two extreme positions matter.
- **Value one:** The integer $1$ is not prime and must never establish either boundary.
- **Exactly one prime:** The same index may be selected twice, so the answer is $0$.
- **Duplicate prime values:** Primality applies to values, while distance applies to their distinct indices; equal prime values at different positions can determine the maximum.
- **Prime values at both ends:** The maximum possible answer is $n-1$.
