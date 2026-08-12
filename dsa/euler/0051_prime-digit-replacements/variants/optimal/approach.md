# Prime Digit Replacements - Optimal Approach

## Algorithm Explanation

Find the smallest prime that is part of an $8$-prime family obtained by replacing part of the number with the same digit.

### Mathematical Reduction
If we replace $k$ digits with $0 \dots 9$:
- If $k$ is not a multiple of $3$, the sum of replaced digits modulo $3$ covers $0, 1, 2$ equally. This forces at least $3$ generated numbers to be divisible by $3$ (composite), making an $8$-prime family mathematically impossible.
- Thus, the number of replaced digits $k$ **must be $3$**.
- The replaced digits cannot be the last digit (since even digits or $5$ make numbers composite).

### Strategy:
1. Generate primes up to $N = 1000000$ using Sieve of Eratosthenes.
2. Iterate primes $p$: if $p$ contains digit `'0'`, `'1'`, or `'2'` exactly $3$ times (excluding the last position), replace those digits with $0 \dots 9$.
3. Count valid prime results and return the smallest prime in the first $8$-member family.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ where $N = 1000000$. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Prime set and sieve table.
