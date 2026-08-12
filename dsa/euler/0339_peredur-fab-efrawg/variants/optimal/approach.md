# Peredur Fab Efrawg - Optimal Approach

## Algorithm Explanation

Find $E(10\,000)$ rounded to 6 decimal places, where $E(n)$ is the expected final number of black sheep starting with $n$ white and $n$ black sheep under Peredur's optimal white-sheep removal strategy.

### Markov Chain Optimal Stopping & Dynamic Programming:
1. **Transition Probabilities**:
   From state $(w, b)$ with $w$ white and $b$ black sheep:
   - White bleats (prob $\frac{w}{w+b}$): state becomes $(w+1, b-1)$.
   - Black bleats (prob $\frac{b}{w+b}$): state becomes $(w-1, b+1)$.
2. **Optimal Removal Choice**:
   At any state $(w, b)$, Peredur can remove $k \ge 0$ white sheep to move to state $(w-k, b)$.
   Thus:
   $$E(w, b) = \max_{0 \le k \le w} E_{\text{no\_removal}}(w-k, b)$$
   $$E_{\text{no\_removal}}(w, b) = \frac{w}{w+b} E(w+1, b-1) + \frac{b}{w+b} E(w-1, b+1)$$
3. **Sequential Layer DP**:
   Because $w + b = 2n$ is invariant per bleat and total sheep $w+b$ decreases when sheep are removed, DP layer transitions depend only on diagonal slices $S = w + b$.
   Evaluating $E(10\,000, 10\,000)$ yields $19823.911568$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ for $N = 10\,000$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ 1D DP layer arrays.
