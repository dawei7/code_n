# The Chase - Optimal Approach

## Algorithm Explanation

Find the expected number of turns for a game of The Chase played with $100$ players sitting around a circular table, starting with two opposite dice.

### Markov Chain Distance State & Gaussian Elimination:
1. **Distance State Space**:
   By circular symmetry, the distance between the two dice is $d \in \{0, 1, 2, \dots, 50\}$.
   $d = 0$ is the absorbing state ($E(0) = 0$).
2. **Transition Probabilities**:
   On each turn, both players roll:
   - Relative distance change $\Delta d = 0$ with probability $18/36 = 1/2$.
   - $\Delta d = \pm 1$ with probability $8/36 = 2/9$.
   - $\Delta d = \pm 2$ with probability $1/36$.
3. **Linear Equation System**:
   For each $d \in [1, 50]$, expected turns $E(d)$ satisfies:
   $$18 E(d) - 8 E(|d-1|) - E(|d-2|) - 8 E(\text{wrap}(d+1)) - E(\text{wrap}(d+2)) = 36$$
   where $\text{wrap}(x) = N - x$ for $x > 50$.
4. **Execution**:
   Solving the $50 \times 50$ tridiagonal-like linear system via Gaussian elimination yields $E(50) = 3780.618622$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}((N/2)^3)$ for $N = 100$. Runs in $\approx 0.007\text{s}$.
- **Space Complexity:** $\mathcal{O}((N/2)^2)$ to store the matrix.
