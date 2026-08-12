# 250250 - Optimal Approach

## Algorithm Explanation

Find the number of non-empty subsets of $\{1^1, 2^2, 3^3, \dots, 250250^{250250}\}$ whose element sum is divisible by $250$, modulo $10^{16}$.

### Modular Frequency Grouping & Circular Convolution DP:
1. **Remainder Frequency Precomputation**:
   For each element $k^k$ ($k \in [1, 250250]$), we compute $r_k = k^k \bmod 250$.
   We tally the frequencies $cnt[r]$ of elements falling into each remainder class $r \in [0, 249]$.
2. **Polynomial Combination / Dynamic Programming**:
   Let `dp[rem]` be the number of subset sums congruent to $rem \bmod 250$.
   We initialize `dp[0] = 1`. For each remainder $r \in [0, 249]$ with frequency $c = cnt[r]$, we incorporate $c$ elements of value $r$ via modular DP convolution:
   $$\text{dp}_{\text{new}}[rem] = (\text{dp}[rem] + \text{dp}[(rem - r) \bmod 250]) \bmod 10^{16}$$
3. **Non-Empty Subset Adjustment**:
   Subtracting $1$ for the empty subset yields the final count.
4. **Execution**:
   The number of valid non-empty subsets modulo $10^{16}$ is $1425480958962864$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N + 250 \cdot N)$ for $N = 250250$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(250)$ array space.
