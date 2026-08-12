# Square Root Convergents - Optimal Approach

## Algorithm Explanation

Count how many of the first $1000$ convergents of $\sqrt{2} = 1 + \frac{1}{2 + \dots}$ have a numerator with more decimal digits than denominator.

### Recurrence Relation
Let the fraction at expansion $k$ be $\frac{N_k}{D_k}$. The expansion step is:
$$1 + \frac{1}{1 + \frac{N_k}{D_k}} = 1 + \frac{D_k}{N_k + D_k} = \frac{N_k + 2D_k}{N_k + D_k}$$

Hence:
- $N_{k+1} = N_k + 2 D_k$
- $D_{k+1} = N_k + D_k$

Starting with $N_1 = 3, D_1 = 2$, we iterate $1000$ steps and increment the counter whenever $\text{len}(\text{str}(N_k)) > \text{len}(\text{str}(D_k))$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ where $K = 1000$ steps. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
