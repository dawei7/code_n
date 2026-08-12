# Prime Frog - Optimal Approach

## Algorithm Explanation

Find the exact probability $p/q$ in reduced fraction form that Susan hears the $15$-croak sequence `"PPPPNNPPPNPPNPN"` from a frog jumping uniformly at random among $500$ squares.

### Exact Rational Markov Chain Dynamic Programming:
1. **Transition Rules**:
   - Starting square $x \in \{1 \dots 500\}$ is uniform with probability $1/500$.
   - Interior squares $x \in [2, 499]$ jump to $x-1$ or $x+1$ with probability $1/2$.
   - Boundary squares $x = 1$ and $x = 500$ jump inward with probability $1$.
2. **Emission Probabilities**:
   - If $x$ is prime: emits `'P'` with prob $2/3$, `'N'` with prob $1/3$.
   - If $x$ is non-prime: emits `'P'` with prob $1/3$, `'N'` with prob $2/3$.
3. **Exact Fraction Propagation**:
   Using `fractions.Fraction` in Python, we propagate exact probability vectors over $15$ time steps across all $500$ positions.
4. **Execution**:
   Summing final state probabilities for `"PPPPNNPPPNPPNPN"` yields $199740353 / 29386561536000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot L)$ for $N = 500$ squares and sequence length $L = 15$. Runs in $\approx 0.02\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ rational probability array.
