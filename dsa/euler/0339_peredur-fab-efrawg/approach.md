# Peredur Fab Efrawg - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Two flocks of sheep contain $B$ black sheep and $W$ white sheep, initially starting with $(B, W) = (n, n)$.
At each step, a sheep bleats uniformly at random from the total $T = B + W$ sheep:
- If a white sheep bleats (probability $\frac{W}{T}$): $B \to B - 1, W \to W + 1$.
- If a black sheep bleats (probability $\frac{B}{T}$): $B \to B + 1, W \to W - 1$.
After a conversion occurs, Peredur may remove any number of white sheep ($W \to W - k$, $0 \le k \le W$) to maximize the expected final number of black sheep (which terminates with $B$ black sheep when $W = 0$).

Let $E(n)$ be the optimal expected final number of black sheep starting from $(n, n)$.
We are given sample values:
- $E(1) = 1.0$
- $E(2) = \frac{55}{24} \approx 2.291667$
- $E(3) = \frac{1981}{528} \approx 3.751894$
- $E(5) = 6.871346$

Find $E(10\,000)$ rounded to $6$ decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Value Iteration on 2D State Space
A naive Markov Decision Process (MDP) models states $(B, W)$ with $0 \le B, W \le 2n$:
- State space size: $\approx (2n)^2 = 4 \times 10^8$ states for $n = 10\,000$.
- Each value iteration pass takes $\mathcal{O}(n^2)$ operations. Reaching numerical convergence to $10^{-10}$ requires hundreds of iterations, consuming $> 10^{11}$ floating-point operations and gigabytes of memory.

---

## 3. Core Intuition & Mathematical Structure

### Martingale Scale Function on Birth-Death Chains
For a fixed total number of sheep $m = B + W$, the number of black sheep $b$ evolves as a 1D birth-death process on $\{0, 1, \dots, m\}$ with transition probabilities:
$$p_b = \frac{b}{m} \quad (\text{up}), \quad q_b = \frac{m - b}{m} \quad (\text{down})$$
Using potential theory and scale functions:
- The scale increment is $\Delta x_m(b) \propto \frac{1}{\binom{m - 1}{b}}$.
- The optimal value function $S_m(b)$ at the decision stage is the least concave majorant with respect to the scale function.
- By symmetry and concavity, the optimal stopping threshold is precisely $b \le \lfloor m / 2 \rfloor$.
- Whenever $b$ black sheep are present, Peredur removes white sheep to enforce $W = b - 1$ (for $b \ge 2$) or $W = 0$ (for $b = 1$).

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### The $O(n)$ Boundary Recurrence
Let $B[b]$ denote the value at the threshold state once it becomes stoppable:
$$B[b] = B[b - 1] + (2b - 1 - B[b - 1]) \cdot r_b$$
where $r_b = \frac{2p_b}{1 + p_b}$ and $p_b = \frac{1}{4^{b-1}} \binom{2b - 2}{b - 1}$ is the central binomial coefficient probability, updated via:
$$p_{b+1} = p_b \cdot \frac{2b - 1}{2b}$$

### Evaluation from Initial State $(n, n)$
From $(n, n)$ before the first bleat:
1. With probability $\frac{1}{2}$, white bleats $\implies (n - 1, n + 1)$, which is reduced to the threshold state with value $B[n - 1]$.
2. With probability $\frac{1}{2}$, black bleats $\implies (n + 1, n - 1)$ on total sheep $2n$.
   By linear interpolation under the scale function:
   $$V(2n, n + 1) = B[n] + (2n - B[n]) \cdot R_n$$
   where:
   $$R_n = \frac{1}{\sum_{k=0}^{n-1} \prod_{j=1}^k \frac{n - j}{n + j}}$$
3. Total expected value:
   $$\mathbf{E(n) = \frac{1}{2} B[n - 1] + \frac{1}{2} V(2n, n + 1)}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Verification on Small $n$:

| $n$ | $B[n]$ | $R_n$ | $V(2n, n+1)$ | $E(n)$ Formula | Exact $E(n)$ |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$1$** | $1.000000$ | $1.000000$ | $2.000000$ | $0.5(0) + 0.5(2.0)$ | $\mathbf{1.000000}$ |
| **$2$** | $2.333333$ | $0.750000$ | $3.583333$ | $0.5(1.0) + 0.5(3.583333)$ | $\mathbf{2.291667} = \frac{55}{24}$ |
| **$3$** | $3.787879$ | $0.625000$ | $5.170455$ | $0.5(2.333333) + 0.5(5.170455)$ | $\mathbf{3.751894} = \frac{1981}{528}$ |
| **$5$** | $6.898919$ | $0.492188$ | $8.425232$ | $0.5(5.317460) + 0.5(8.425232)$ | $\mathbf{6.871346}$ (Sample verified) |

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Boundary Array $B[b]$** | Recurrence $B[b] = B[b-1] + (2b-1-B[b-1]) \frac{2p}{1+p}$ | $\mathcal{O}(n)$ |
| **Stage 2** | **Scale Ratio $R_n$** | Sum product ratios $\prod_{j=1}^k \frac{n-j}{n+j}$ | $\mathcal{O}(n)$ |
| **Stage 3** | **Black Continuation $V$** | Compute $V(2n, n+1) = B[n] + (2n - B[n]) R_n$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Expectation Combination** | $E(n) = 0.5 B[n-1] + 0.5 V(2n, n+1)$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(n)$ | $\approx 2 \times 10^4$ operations in $< 0.003\text{ s}$ |
| **Space Complexity** | $\mathcal{O}(n)$ | Array `B` of length $n + 1$ ($< 0.1\text{ MB}$) |
| **Implementation Standard** | $100\%$ Pure Python | Zero native compiler dependencies |

### Critical Invariants & Edge Cases Handled:
1. **$n = 1$ Base Condition:** $B[0] = 0, B[1] = 1.0 \implies E(1) = 1.0$.
2. **Exponential Tail Truncation:** Scale terms with value $< 10^{-18}$ are safely early-stopped.
3. **Double Precision Stability:** Scale products strictly decrease, maintaining full 64-bit float precision.
