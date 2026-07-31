## General

Only two entries in each row can affect the answer: `nums[i][i]` from the primary diagonal and `nums[i][n - 1 - i]` from the secondary diagonal. Visit those values directly instead of scanning the other $n^2-2n$ matrix positions.

For a candidate value $x$, test divisibility only through $\lfloor\sqrt{x}\rfloor$. If $x$ had a factor larger than its square root, the paired factor would be smaller than the square root and would already have been found. Handle $2$ separately, reject other even values, and test only odd divisors thereafter.

Maintain the largest prime found so far. A value no larger than that answer cannot improve the result, so it does not need another primality test. The center of an odd-sized matrix is visited twice, but this comparison skips the duplicate after its first visit.

Every value eligible for the answer is one of the two positions inspected in its row. The primality test accepts exactly values greater than $1$ with no divisor through their square root. Updating only with larger accepted values therefore leaves the maximum diagonal prime in the accumulator, or $0$ if none is accepted.

## Complexity detail

Let $n$ be the matrix side length and let $m$ be the largest diagonal value. At most $2n$ values are inspected, and trial division for one value costs $O(\sqrt{m})$ in the worst case. Total time is $O(n\sqrt{m})$. The scan and primality test use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sieve of Eratosthenes:** Precomputing primality through the largest matrix value gives fast lookups, but uses $O(m)$ time and space even though only $O(n)$ values matter.
- **Scan the whole matrix:** Checking whether every cell lies on a diagonal is correct, but wastes $O(n^2)$ position visits.
- **One-cell matrix:** Its only value belongs to both diagonals and must be considered once logically.
- **Shared center:** In an odd-sized matrix, the center is on both diagonals; duplicate inspection does not change the maximum.
- **Value one:** $1$ is not prime and must be rejected.
- **Off-diagonal primes:** They never qualify, even when they exceed every diagonal value.
- **No prime:** The initial answer of $0$ is returned unchanged.
