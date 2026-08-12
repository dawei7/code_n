# Step Numbers - Optimal Approach

## Algorithm Explanation

Find the total number of pandigital step numbers less than $10^{40}$.
A **step number** has $|d_i - d_{i-1}| = 1$ for all consecutive digits. A **pandigital** number contains every digit $0 \dots 9$ at least once.

### Bitmask Dynamic Programming:
Construct step numbers digit by digit for length $L = 1 \dots 40$.

1. **State Definition**:
   Maintain DP state `dp[(d, mask)]` representing the count of valid step number prefixes ending in digit $d \in [0, 9]$ with accumulated digit bitmask `mask` $\in [1, 1023]$.
2. **Base Case ($L = 1$)**:
   For $d_1 \in [1, 9]$ (no leading zero), initialize `dp[(d1, 1 << d1)] = 1`.
3. **Transition Step ($L = 2 \dots 40$)**:
   For each state $(d, \text{mask})$ and adjacent digit $d_{\text{next}} \in \{d-1, d+1\} \cap [0, 9]$:
   $$\text{new\_dp}[(d_{\text{next}}, \text{mask} \mid (1 \ll d_{\text{next}}))] += \text{dp}[(d, \text{mask})]$$
4. **Pandigital Accumulation**:
   For each step $L$, accumulate counts for all states with $\text{mask} = 1023$ ($1111111111_2$, indicating all $10$ digits have been visited).

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \cdot 10 \cdot 2^{10})$ where $L = 40$ (at most $10,240$ active states per step). Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(10 \cdot 2^{10}) = \mathcal{O}(10,240)$ active DP state dictionary memory.
