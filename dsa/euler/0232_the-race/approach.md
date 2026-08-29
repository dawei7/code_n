# The Race - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Two players share an unbiased coin and take turns playing **The Race** to $N = 100$ points:
1. **Player 1's Turn**: The coin is tossed once. If Heads, Player 1 scores $1$ point; if Tails, $0$ points.
2. **Player 2's Turn**: Player 2 chooses an integer $T \ge 1$ and tosses the coin $T$ times. If all $T$ tosses are Heads, Player 2 scores $2^{T-1}$ points; otherwise $0$ points.
3. **Winning Condition**: Player 1 goes first. The first player to reach $\ge N$ points wins immediately.
4. **Optimal Policy**: Player 2 chooses $T$ dynamically at each state to maximize their probability of winning.

What is the probability that **Player 2 wins**, rounded to eight decimal places?

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Monte Carlo Simulation Bottlenecks
A naive simulation attempts to estimate winning probabilities through random rollouts:
```python
def naive_monte_carlo_race():
    # Estimating 8 decimal places requires > 10^17 game simulations
    # Computationally infeasible
    # ...
```

### Backward Induction in a Finite Markov Decision Process
1. **State Definition:**
   Let $P(i, j)$ be Player 2's win probability when it is **Player 2's turn** with scores $(i, j)$.
   Let $Q(i, j)$ be Player 2's win probability when it is **Player 1's turn** with scores $(i, j)$.
2. **Turn Transitions:**
   - On Player 1's turn at $(i, j)$:

$$
Q(i, j) = \frac{1}{2} P(i, j) + \frac{1}{2} P(i+1, j)
$$

     where $P(i+1, j) = 0$ if $i+1 \ge N$.
   - On Player 2's turn at $(i, j)$ choosing $T \ge 1$:
     Success probability is $2^{-T}$ with reward state $j + 2^{T-1}$.

$$
P_T(i, j) = 2^{-T} S_T(i, j) + (1 - 2^{-T}) Q(i, j)
$$

     where $S_T(i, j) = 1$ if $j + 2^{T-1} \ge N$, else $Q(i, j + 2^{T-1})$.
3. **Resolving Self-Loops:**
   Substituting $Q(i, j) = \frac{1}{2} P(i, j) + \frac{1}{2} P(i+1, j)$ and solving for $P(i, j)$:

$$
P(i, j) = \max_{T \ge 1} \frac{2 S_T(i, j) + (2^T - 1) P(i+1, j)}{2^T + 1}
$$

---

## 3. Core Intuition & Mathematical Structure

### Parameter Matrix for Player 2 Choices $T \in \{1, 2, 3, 4\}$

| $T$ | Success Probability $p = 2^{-T}$ | Score Gain $g = 2^{T-1}$ | Success Value $S_T(i, j)$ | Recurrence Numerator $2 S_T + (2^T - 1) P(i+1, j)$ | Recurrence Denominator $2^T + 1$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$1$** | $1/2 = 0.500$ | $1$ | $Q(i, j+1)$ | $2 Q(i, j+1) + 1 \cdot P(i+1, j)$ | $3$ |
| **$2$** | $1/4 = 0.250$ | $2$ | $Q(i, j+2)$ | $2 Q(i, j+2) + 3 \cdot P(i+1, j)$ | $5$ |
| **$3$** | $1/8 = 0.125$ | $4$ | $Q(i, j+4)$ | $2 Q(i, j+4) + 7 \cdot P(i+1, j)$ | $9$ |
| **$4$** | $1/16 = 0.0625$ | $8$ | $Q(i, j+8)$ | $2 Q(i, j+8) + 15 \cdot P(i+1, j)$ | $17$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Backward Induction Algorithm
```python
def solve(target_score: int = 100) -> str:
    N = target_score
    P = [[0.0] * (N + 1) for _ in range(N + 1)]
    Q = [[0.0] * (N + 1) for _ in range(N + 1)]

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            best_p = 0.0
            for T in range(1, 9):
                gain = 1 << (T - 1)
                p2 = 1 << T
                S_T = 1.0 if j + gain >= N else Q[i][j + gain]
                P_next = 0.0 if i + 1 >= N else P[i + 1][j]
                val = (2.0 * S_T + (p2 - 1.0) * P_next) / (p2 + 1.0)
                if val > best_p:
                    best_p = val
            P[i][j] = best_p
            Q[i][j] = 0.5 * P[i][j] + 0.5 * (0.0 if i + 1 >= N else P[i + 1][j])

    return f"{Q[0][0]:.8f}"
```

Evaluating for $N = 100$:

$$
\text{Winning Probability } Q(0, 0) = \mathbf{0.83648556}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Boundary State $(99, 99)$
- Player 1 scores $1$ on Heads ($\text{prob } 1/2$) and wins immediately.
- On Player 2's turn, choosing $T=1$ gives score gain $1 \ge 100$ on Heads with probability $1/2$.
- $P(99, 99) = \frac{2(1.0) + (1)(0)}{3} = \frac{2}{3}$.
- $Q(99, 99) = \frac{1}{2}\left(\frac{2}{3}\right) + \frac{1}{2}(0) = \frac{1}{3} \approx 0.33333333$.

### Example 2: Target Evaluation for $N = 100$
- Starting at $(0, 0)$ with Player 1 tossing first:

$$
Q(0, 0) = \mathbf{0.83648556}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **DP Grid Init** | Allocate matrices $P, Q \in \mathbb{R}^{(N+1) \times (N+1)}$ | $\mathcal{O}(N^2)$ |
| **Stage 2** | **Backward Sweeps** | Nested loops $i = N-1 \dots 0$ and $j = N-1 \dots 0$ | $\mathcal{O}(N^2)$ |
| **Stage 3** | **Optimal Action** | Compute $P(i, j) = \max_{T=1}^8 \frac{2 S_T + (2^T-1) P(i+1, j)}{2^T+1}$ | $\mathcal{O}(\log N)$ |
| **Stage 4** | **Turn Expectation**| $Q(i, j) = 0.5 P(i, j) + 0.5 P(i+1, j)$ | $\mathcal{O}(1)$ |
| **Stage 5** | **Format Result** | Return `f"{Q[0][0]:.8f}"` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2 \log_2 N)$ | $< 0.01$ seconds for $N = 100$ |
| **Space Complexity** | $\mathcal{O}(N^2)$ | Table storage $\approx 100$ KB |
| **Dynamic Execution** | $100\%$ Inline | Exact backward induction Markov decision process |

### Critical Invariants & Edge Cases Handled:
1. **Immediate Win Invariant**: Player 1 reaching $N$ terminates the game without allowing Player 2 a response in that round.
2. **Optimal Strategy Invariant**: Because $2^{8-1} = 128 > 100$, checking $T \in [1, 8]$ covers all possible non-redundant actions.