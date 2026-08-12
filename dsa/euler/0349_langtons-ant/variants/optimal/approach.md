# Langton's Ant - Optimal Approach

## Algorithm Explanation

Find the number of black squares on an initially all-white 2D grid after $10^{18}$ moves of Langton's Ant.

### 104-Step Highway Periodicity & Linear Extrapolation:
1. **Chaotic Phase & Highway Emergence**:
   Langton's Ant exhibits three distinct behavior phases:
   - Simplicity (initial 200 steps).
   - Chaos (pseudorandom exploration for $\approx 10\,000$ steps).
   - Highway (strictly periodic directional movement).
2. **Period 104 & +12 Net Black Squares**:
   After $\approx 10\,000$ steps, the ant enters an exact period-104 highway loop.
   In every cycle of $104$ steps, the ant advances diagonally by $2$ units and nets $+12$ additional black squares.
3. **Linear Extrapolation Formula**:
   Let $N_0 = 10\,400$ be a base step count in the highway phase with black square count $B(N_0)$.
   For $N = 10^{18}$:
   $$\text{cycles} = \lfloor \frac{N - N_0}{104} \rfloor, \quad \text{rem} = (N - N_0) \bmod 104$$
   $$B(N) = B(N_0) + 12 \cdot \text{cycles} + (B(N_0 + \text{rem}) - B(N_0))$$
4. **Execution**:
   Extrapolating $B(10^{18})$ yields $115384615384614952$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P)$ where $P \approx 10\,400$ initial steps. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ grid hash set.
