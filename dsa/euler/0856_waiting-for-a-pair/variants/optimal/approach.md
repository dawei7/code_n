# Waiting for a Pair - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In a standard 52-card deck (13 ranks, 4 suits), cards are drawn without replacement until two consecutive cards have the same rank (or until the 52 cards are exhausted).
Find the expected number of cards drawn, rounded to 8 decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full Permutation Search
- There are $52! \approx 8.07 \times 10^{67}$ shuffle permutations.
- Direct tree search or Monte Carlo simulation cannot provide the 8 requested decimal places of exact precision.

---

## 3. Core Intuition & Mathematical Structure

### Symmetry Reduction via Rank Frequencies
The identities of individual ranks (e.g. Ace vs King) are mathematically indistinguishable.
The composition of the remaining deck is uniquely determined by the tuple $(c_4, c_3, c_2, c_1)$, where $c_k$ is the number of ranks having $k$ cards remaining.
To evaluate the stopping probability on the next draw, we only need to track $\text{last} \in \{0, 1, 2, 3\}$, the remaining card count of the rank drawn in the immediate preceding step.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Markov Chain Dynamic Programming
For a state $S = (c_4, c_3, c_2, c_1, \text{last})$ with total cards $N = 4c_4 + 3c_3 + 2c_2 + c_1$:
1. **Consecutive Pair Match**:
   With probability $\frac{\text{last}}{N}$, the next card matches the previous rank. The process terminates immediately with 0 additional draws.
2. **Transition to Rank with $k$ Cards**:
   For each $k \in \{1, 2, 3, 4\}$, the number of eligible ranks is $c_k - \mathbb{I}(\text{last} = k)$.
   Drawing a card from an eligible rank occurs with probability $\frac{k(c_k - \mathbb{I}(\text{last}=k))}{N}$, transitioning to $(c - e_k + e_{k-1}, k - 1)$.
3. **Bellman Expectation**:
   $$E(S) = 1 + \sum_{k=1}^4 \frac{k(c_k - \mathbb{I}(\text{last}=k))}{N} E(c - e_k + e_{k-1}, k - 1)$$

Total reachable state space:
$$|\mathcal{S}| \le 4 \times \binom{13 + 4}{4} = 4 \times 2380 = \mathbf{9520} \text{ states}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for 2 Ranks with 2 Cards ($N=4$ cards):
- Start at $(c_2 = 2, c_1 = 0, \text{last} = 0)$, $N = 4$.
- Draw 1: Any rank with 2 cards $\implies (1, 1, \text{last} = 1)$.
- State $(1, 1, 1)$, $N = 3$:
  - Match previous rank (prob $1/3$): Stop! ($0$ future draws).
  - Draw from other rank with 2 cards (prob $2/3$): Transitions to $(0, 2, \text{last} = 1)$, $N = 2$.
- The expected draws evaluate to exact rational values in a handful of subproblems.

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Tuple Representation** | Index states via $(c_4, c_3, c_2, c_1, \text{last})$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Memoized Backward Induction** | Recursively evaluate expected draws with memoization | $\mathcal{O}(|\mathcal{S}|) \le 9520$ |
| **Stage 3** | **Result Formatting** | Round initial state expectation $E(13, 0, 0, 0, 0)$ to 8 decimals | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(|\mathcal{S}|) \approx 0.01\text{ s}$ | Real-time execution |
| **Space Complexity** | $\mathcal{O}(|\mathcal{S}|) \le 1\text{ MB}$ | Hash map of 9520 entries |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Exclusion of Previous Rank**: Correctly subtracting $\mathbb{I}(\text{last} = k)$ prevents double-counting the matching rank as a generic continuation branch.
2. **Terminal Deck Exhaustion**: When $N = 0$, expected future draws equal 0, properly representing the 52-card limit.
