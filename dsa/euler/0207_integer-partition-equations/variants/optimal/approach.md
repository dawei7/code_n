# Integer Partition Equations - Optimal Approach

## Algorithm Explanation

Find the smallest $m$ for which $P(m) < \frac{1}{12345}$, where $P(m)$ is the proportion of valid partitions $4^t = 2^t + k$ ($k \le m$) that are perfect ($t \in \mathbb{Z}$).

### Quadratic Factorization & Logarithmic Counting:
1. **Partition Characterization**:
   Setting $x = 2^t > 0$, the equation becomes $x^2 - x - k = 0$.
   For $x$ to be an integer, $1 + 4k$ must be a square, leading to $k = h(h + 1)$ for integers $h \ge 1$, with $x = 2^t = h + 1$.
2. **Perfect Partitions**:
   A partition is perfect if $t = \log_2(h + 1)$ is an integer $\implies h = 2^p - 1$.
   The total number of partitions for a maximum $h$ is $h$, of which $p = \lfloor \log_2(h + 1) \rfloor$ are perfect.
3. **Threshold Calculation**:
   We require $\frac{p}{h} < \frac{1}{12345} \implies h > 12345 p$.
   Checking increasing values of $p$, $p = 17$ yields $h = 209866$ and $m = h(h + 1) = 44043947822$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_2(\text{target\_denom}))$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
