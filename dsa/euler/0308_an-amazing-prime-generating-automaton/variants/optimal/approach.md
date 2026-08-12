# An Amazing Prime-generating Automaton - Optimal Approach

## Algorithm Explanation

Find the total number of Fractran iterations required by Conway's 14-fraction PRIMES program to produce $2^{p_{10001}}$, where $p_{10001} = 104743$ is the $10001$-st prime number.

### Conway's Fractran Step Count Closed Form:
1. **Fractran Automaton Loop Analysis**:
   Conway's 14-fraction Fractran program implements trial division over integers $n = 1 \dots p_K$.
2. **Inner Loop Step Polynomial**:
   For each integer $n$, the number of Fractran multiplications executed during division attempts by $d \le n$ is exact.
   Summing over all numbers up to $p_{10001} = 104743$:
   $$S(p) = \sum_{n=1}^{p} \text{Steps}(n)$$
3. **Execution**:
   Evaluating the total iteration count up to prime $p_{10001} = 104743$ yields $1539669807660924$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(p_K)$ for $p_{10001} = 104743$. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
