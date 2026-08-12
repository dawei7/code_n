# Harshad Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of all strong, right-truncatable Harshad primes less than $10^{14}$.

### Definitions & DFS Tree Backtracking:
1. **Harshad Definitions**:
   - **Harshad Number**: $H$ is divisible by its digit sum $S(H)$.
   - **Right-Truncatable Harshad Number**: Every prefix of $H$ obtained by truncating last digits is a Harshad number.
   - **Strong Harshad Number**: $H$ is Harshad and $H / S(H)$ is prime.
   - **Strong Right-Truncatable Harshad Prime**: A prime $P < 10^{14}$ such that $\lfloor P / 10 \rfloor$ is a strong right-truncatable Harshad number.
2. **DFS Tree Traversal**:
   Starting with single-digit seeds $1 \dots 9$, we recursively append digits $d \in [0, 9]$ to construct right-truncatable Harshad numbers $H' = 10 H + d$.
   Whenever $H$ is strong ($H / S(H)$ is prime), we test candidate primes $P = 10 H + p$ for $p \in \{1, 3, 7, 9\}$.
3. **Miller-Rabin Primality Testing**:
   Candidate primes $P < 10^{14}$ are validated using deterministic Miller-Rabin primality testing.
4. **Execution**:
   Summing all valid strong right-truncatable Harshad primes $< 10^{14}$ yields $696067597313468$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Tree Nodes} \cdot \log^3 N)$ for $N = 10^{14}$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_{10} N)$ stack depth.
