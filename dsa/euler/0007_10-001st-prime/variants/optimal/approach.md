# 10001st Prime - Optimal Approach

## Algorithm Explanation

By the Prime Number Theorem, the $n$-th prime $p_n$ satisfies $p_n \sim n \ln n$.
For $n = 10001$:
$$p_{10001} < 10001 (\ln 10001 + \ln \ln 10001) \approx 114319$$

We set a conservative upper bound $L = 120000$ and run the **Sieve of Eratosthenes**:
1. Allocate boolean array `is_prime` up to $L$.
2. Mark multiples of each prime starting from $p^2$.
3. Maintain a prime counter and return immediately when the $10001^{\text{st}}$ prime is reached.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \log \log L)$ - Sieve bound where $L = 120000$.
- **Space Complexity:** $\mathcal{O}(L)$ - Sieve boolean array.
