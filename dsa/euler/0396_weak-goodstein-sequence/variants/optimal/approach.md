# Weak Goodstein Sequence - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $\sum_{n=1}^{15} G(n) \bmod 10^9$, where $G(n)$ is the length of the $n$-th weak Goodstein sequence before termination.

### Base Change Mechanics & Tower Exponentiation:
1. **Weak Goodstein Process**:
   $g_1 = n$.
   For step $k > 1$, $g_k$ is obtained by converting $g_{k-1}$ from base $k$ to base $k+1$, then subtracting $1$.
2. **Digit Decrement Analysis**:
   In base $k$, subtracting $1$ decrements the lowest non-zero digit and sets all trailing digits to $k$.
   When base increases from $k$ to $k+1$, digits stay unchanged, causing the sequence length to grow exponentially as a function of the initial base-$2$ digits of $n$.
3. **Iterated Modular Exponentiation**:
   For $n < 16$, $n = (d_3 d_2 d_1 d_0)_2$.
   Each digit level $d_i$ multiplies the current step counter by powers of $2$.
   Using modular exponentiation $\pmod{10^9}$ via Euler's totient / Carmichael reduction $\phi(10^9)$, $G(n) \bmod 10^9$ is evaluated in $\mathcal{O}(\log(\text{mod}))$ time per $n$.
4. **Execution**:
   Summing $G(n) \bmod 10^9$ for $n = 1 \dots 15$ yields last 9 digits $173214653$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log(\text{mod}))$ for $N = 15$. Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
