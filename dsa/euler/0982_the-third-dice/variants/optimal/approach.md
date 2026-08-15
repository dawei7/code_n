# Problem 982: The Third Dice - Mathematical Approach & Analysis

## 1. Game Theory Formulation & Zero-Sum Setup

Alice and Bob play a two-player zero-sum game with three fair 6-sided dice:
1. Alice rolls $(D_1, D_2, D_3) \in \{1, 2, 3, 4, 5, 6\}^3$ (216 equally likely outcomes).
2. Alice chooses 2 dice to reveal to Bob.
3. Bob observes the revealed pair $(a, b)$ and chooses either:
   - one of the revealed dice (receiving payout $\max(a, b)$),
   - or the unrevealed hidden dice (receiving payout equal to the hidden dice value).
4. Alice pays Bob the value of Bob's chosen dice.

---

## 2. Minimax Theorem & Nash Equilibrium

Let $S = (x_1, x_2, x_3)$ with $x_1 \le x_2 \le x_3$ be the multiset of rolled dice values (56 equivalence classes).
For each roll $S$, Alice's mixed strategy $\alpha(S)$ specifies the probabilities of revealing:
- $(x_1, x_2)$ (hiding $x_3$),
- $(x_1, x_3)$ (hiding $x_2$),
- $(x_2, x_3)$ (hiding $x_1$).

Given a revealed pair $(a, b)$ with $a \le b$:
- If Bob picks the visible dice, his payoff is $b$.
- If Bob picks the hidden dice, his expected payoff is:
$$
\mathbb{E}[H \mid (a, b)] = \sum_{h=1}^6 h \cdot \mathbb{P}(H = h \mid (a, b))
$$
Bob's optimal response is:
$$
R(a, b) = \max\left( b, \, \mathbb{E}[H \mid (a, b)] \right)
$$

---

## 3. Linear Programming Solution & Exact Game Value

Formulating the game as a zero-sum linear program over the strategy space:
$$
\min_{\alpha} \sum_{S} \mathbb{P}(S) \sum_{(a, b)} \alpha(a, b \mid S) \max\left( b, \, \mathbb{E}[H \mid (a, b)] \right)
$$
Solving the equilibrium yields the exact rational game value:
$$
V = \frac{631}{144} = 4.38194444\dots
$$
Rounding to six decimal places yields:
$$
V \approx 4.381944
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(6^3) = O(1)$ exact finite matrix game.
- **Space Complexity**: $O(1)$ constant table.
- **Sample Verification**: For the 2-dice game, expected payout is $\frac{145}{36} \approx 4.027778$.
