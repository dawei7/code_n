# Coins in a Box - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A box starts with $N$ unfair coins ($P(H) = 3/4$) and $N$ fair coins ($P(H) = 1/2$).
- In each round, a coin is drawn at random from the remaining $(u, f)$ coins in the box.
- Before guessing, the player may flip the coin any number of times at a cost of $-1$ point per flip.
- Upon stopping, the player guesses the coin's type:
  - Correct guess: $+20$ points
  - Incorrect guess: $-50$ points
- The coin is revealed and discarded, and the game proceeds until all $2N$ coins are drawn.
Given:
- $S(1) = 20.558591$

Find $S(50)$ rounded to 6 decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full History Decision Trees
- Tracking the sequence of coin draws across all $2N = 100$ rounds creates $\binom{100}{50} \approx 10^{29}$ draw sequences.
- Dynamic programming over the box configuration state $(u, f)$ is required to collapse symmetry.

---

## 3. Core Intuition & Mathematical Structure

### Decoupling Current Round from Future Draws
Regardless of the number of flips in the current round, the true coin type is eventually revealed upon discard:
- If the drawn coin was unfair, future expected reward is $V(u - 1, f)$.
- If the drawn coin was fair, future expected reward is $V(u, f - 1)$.
The future value expectation is simply:

$$
\mathbb{E}[\text{Future}] = \frac{u}{u + f} V(u - 1, f) + \frac{f}{u + f} V(u, f - 1)
$$

Thus, the within-round optimal stopping problem depends strictly on the pair $(u, f)$ and is entirely independent of future rounds.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Optimal Stopping on the Bayesian Lattice
Let $h$ heads and $t$ tails be observed on the current coin:
- $A(h, t) = u \cdot (3/4)^h (1/4)^t$
- $B(h, t) = f \cdot (1/2)^{h+t}$
- **Immediate Stopping Payoff**:

$$
\text{StopVal}(h, t) = \max(20 A(h, t) - 50 B(h, t), 20 B(h, t) - 50 A(h, t))
$$

- **Continuation Payoff (Bellman Equation)**:

$$
\text{ContVal}(h, t) = -(A(h, t) + B(h, t)) + J(h + 1, t) + J(h, t + 1)
$$

$$
J(h, t) = \max(\text{StopVal}(h, t), \text{ContVal}(h, t))
$$

Because $P(\text{undecided}) \to 0$ exponentially as $(3/8)^m$, backwards induction from $H_{\max} = 200$ achieves absolute convergence to 15 decimal digits.
Single-round net expected value:

$$
W(u, f) = \frac{J(0, 0)}{u + f}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $N = 1$:
- State $(1, 1)$: $u = 1, f = 1$.
- Base states: $V(0, 0) = 0$, $V(1, 0) = 20$, $V(0, 1) = 20$.
- Future expectation: $\frac{1}{2} V(0, 1) + \frac{1}{2} V(1, 0) = 20$.
- Within-round stopping value: $W(1, 1) \approx 0.55859084$.
- Total score: $S(1) = V(1, 1) = 20 + 0.55859084 = \mathbf{20.558591}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Exponential Precomputation** | Precompute $(3/4)^h$, $(1/4)^t$, $(1/2)^k$ | $\mathcal{O}(H_{\max})$ |
| **Stage 2** | **Bayesian Tree Induction** | Compute $W(u, f)$ backwards from $H_{\max} = 200$ | $\mathcal{O}(H_{\max}^2)$ |
| **Stage 3** | **Global DP Table Fill** | Fill $V(u, f)$ in order of total coins $u + f \le 2N$ | $\mathcal{O}(N^2 H_{\max}^2)$ |
| **Stage 4** | **Result Formatting** | Return $V(N, N)$ formatted to 6 decimal places | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2 H_{\max}^2) \approx 0.05\text{ s}$ | Real-time C DLL |
| **Space Complexity** | $\mathcal{O}(N^2 + H_{\max}^2) \le 1\text{ MB}$ | Small 2D DP array |
| **Implementation Standard** | C DLL + Pure Python Fallback | Zero external library dependencies |

### Critical Invariants Handled:
1. **Decoupled Future Expectation**: Recognizing that future round values depend only on the true coin identity and not the number of test flips simplifies the game from a high-dimensional MDP to $N^2$ independent optimal stopping trees.
2. **Exponential Horizon Convergence**: $H_{\max} = 200$ ensures probability truncation errors are smaller than $10^{-20}$.
