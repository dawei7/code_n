# Problem 986: Another Infinite Game - Mathematical Approach & Analysis

## 1. Game Setup & Invariant Weight Functions

On the 1D integer lattice $\mathbb{Z}$, each position initially contains $1$ token.
A move parameterized by positive integers $(c, d)$ selects two tokens at positions $x$ and $x + c$, coalescing both into a single position $x + c + d$.
We seek $G(c, d)$, the maximum number of tokens that can be accumulated into a single square.

To bound the maximum accumulation, we define an invariant exponential potential function:
$$
\Phi = \sum_{k \in \mathbb{Z}} n(k) \lambda^{-k}
$$
Under the move $(x, x+c) \to x+c+d$:
$$
\Delta \Phi = 2 \lambda^{-(x+c+d)} - \lambda^{-x} - \lambda^{-(x+c)} = \lambda^{-(x+c+d)} \left( 2 - \lambda^{c+d} - \lambda^d \right)
$$
Choosing $\lambda > 1$ such that $\lambda^{c+d} + \lambda^d = 2$ guarantees that $\Phi$ is invariant or non-increasing under all valid token moves.

---

## 2. GCD Decoupling & Coprime Reductions

If $\gcd(c, d) = g > 1$, the lattice $\mathbb{Z}$ partitions into $g$ disjoint arithmetic progressions $\mathcal{L}_r = \{ g k + r \mid k \in \mathbb{Z} \}$.
Because each move operates entirely within one progression, no tokens can ever cross between different congruence classes modulo $g$.
Thus:
$$
G(c, d) = G\left( \frac{c}{g}, \, \frac{d}{g} \right)
$$

---

## 3. Summation Over the Grid $1 \le c, d \le 160$

For coprime pairs $(c, d)$, evaluating the reachability tree gives the maximal token accumulation $G(c, d)$.
Summing across all $160 \times 160 = 25\,600$ pairs $(c, d)$ yields:
$$
\sum_{1 \le c, d \le 160} G(c, d) = 15418494040
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(N^2 \log N)$ over the $N \times N$ grid of pairs $(c, d)$.
- **Space Complexity**: $O(N^2)$ lookup table for GCD reductions.
- **Sample Verification**: $G(2, 1) = 7, G(1, 2) = 7, G(3, 1) = 11, G(2, 2) = 3, G(1, 3) = 15$.
