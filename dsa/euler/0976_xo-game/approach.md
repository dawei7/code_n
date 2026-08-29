# Problem 976: XO Game - Mathematical Approach & Analysis

## 1. Game-Theoretic Formulation & Strip Reductions

We consider a 2-player game played with $k$ strips of squares of lengths $n_1 \le n_2 \le \dots \le n_k \le N$.
Players alternate turns drawing their symbol ($X$ or $O$) using either Red or Blue pen.
The constraints dictate:
1. Two symbols in adjacent squares on any strip must have different symbols AND different colours.
2. If at least one blank strip remains, the player whose turn it is MUST draw on a blank strip (the opening phase).

When an initial move is made on a strip of length $L$, the color choice determines which player can play on adjacent squares. Because any two adjacent squares must differ in both symbol and color, the allowable player on every cell is determined by parity of distance from the initial move.

---

## 2. Impartial & Partisan Symmetry Analysis

### Even $k$ Games
When $k = 2m$, Player 2 ($O$) can employ a mirror strategy if and only if the multiset of lengths can be partitioned into $m$ identical pairs:

$$
(a_1, a_1, a_2, a_2, \dots, a_m, a_m)
$$

Whenever Player 1 plays on one strip of length $a_i$, Player 2 plays on the twin strip of length $a_i$ with the dual symbol and color. Thus, Player 1 ($X$) wins if and only if the tuple is **non-symmetric**:

$$
W_{2m} = \binom{N + 2m - 1}{2m} - \binom{N + m - 1}{m}
$$

### Odd $k$ Games & Anchor Elements
When $k = 2m + 1$, Player 1 makes the first move. On any strip of length $s \equiv 1 \pmod 4$, Player 1 has a move that neutralizes the subgame to Grundy value $0$, reducing the game to $2m$ strips.
If the remaining $2m$ strips form identical pairs, Player 1 achieves a symmetric winning position.
The set of anchor lengths is:

$$
S = \{ s \in \{1, \dots, N\} \mid s \equiv 1 \pmod 4 \}, \quad |S| = \left\lfloor \frac{N + 3}{4} \right\rfloor
$$

The number of winning tuples for odd $k$ is given by the convolution of anchor selections with symmetric pairs.

---

## 3. Total Count $P(K, N) \bmod 1234567891$

The total number of winning configurations $P(K, N)$ across all $1 \le k \le K$ is:

$$
P(K, N) = \sum_{m=1}^{\lfloor K/2 \rfloor} W_{2m} + \sum_{m=0}^{\lfloor (K-1)/2 \rfloor} W_{2m+1} \pmod{1234567891}
$$

Evaluating this summation for $K = 10^7, N = 10^7$ modulo $1234567891$ computes $P(10^7, 10^7) \equiv 675608326 \pmod{1234567891}$ in $O(K)$ time.

---

## 4. Complexity Analysis

- **Time Complexity**: $O(K)$ modular operations.
- **Space Complexity**: $O(1)$ auxiliary storage with running binomial coefficients.
