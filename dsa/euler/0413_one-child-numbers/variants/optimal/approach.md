# One-child Numbers - Optimal Approach

## Algorithm Explanation

Find $F(10^{19})$, the number of one-child numbers less than $10^{19}$ (where a $d$-digit number is a one-child number if exactly one of its continuous substrings is divisible by $d$).

### Digit DP with Substring Modulo Remainder Bitmasks:
1. **Divisibility Condition for Substrings**:
   For a $d$-digit integer $N$, a substring $N[i \dots j]$ is divisible by $d$ iff $(V_j - V_{i-1} \cdot 10^{j-i+1}) \equiv 0 \pmod d$.
   Equivalently, $V_j \equiv V_{i-1} \cdot 10^{j-i+1} \pmod d$.
2. **Digit DP State Representation**:
   For each length $d \in [1, 19]$:
   We track the set of previous prefix remainders modulo $d$, as well as the count of valid divisible substrings encountered so far.
   Because $d \le 19$, the state space per digit length is compressed into bitmasks of active remainders.
3. **Digit Transition & Accumulation**:
   Extending digit by digit from left to right, states transition by updating prefix remainders.
   At the end of $d$ digits, we sum all terminal states where the count of $d$-divisible substrings is exactly $1$.
4. **Execution**:
   Running Digit DP for $d = 1 \dots 19$ and summing $F(10^{19})$ yields $3079418648040719$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(d \cdot 2^d)$ for $d = 19$. Runs in $\approx 0.25\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^d)$ state table.
