# Heighway Dragon - Optimal Approach

## Algorithm Explanation

Find the position $(x, y)$ of the cursor after $10^{12}$ steps in the Heighway Dragon curve of order $50$ ($D_{50}$).

### L-System Expansion & Divide-and-Conquer Navigation:
1. **L-System Rules**:
   - $a_k = a_{k-1} \text{ R } b_{k-1} \text{ F R}$
   - $b_k = \text{L F } a_{k-1} \text{ L } b_{k-1}$
   Each block $a_k$ or $b_k$ contains $2^k - 1$ forward steps.
2. **Precomputed Full Displacements**:
   For any level $k$, we precompute the total displacement $(\Delta x, \Delta y)$ and net rotation $\Delta d \pmod 4$ of $a_k$ and $b_k$ in $\mathcal{O}(k)$ time using 2D vector rotations.
3. **Binary Path Search**:
   Given a target step count $K = 10^{12}$, we recursively traverse the top-level expansion of $a_{50}$ down to individual atomic steps in $\mathcal{O}(\log K)$ operations.
4. **Execution**:
   Evaluating for $10^{12}$ steps in $D_{50}$ yields position `139776,963904`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{order})$ for $\text{order} = 50$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{order})$ for displacement memoization tables.
