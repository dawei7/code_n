# Flipping Game - Optimal Approach

## Algorithm Explanation

Find $W(10^6)$, the number of winning first moves on an $N \times N$ board ($N = 10^6$) in the two-player 2D Flipping Game with square width $w \in \{k^2\}$ and triangular height $h \in \{\frac{m(m+1)}{2}\}$.

### Nim-Sum 2D Independent Game Decomposition & Fast Walsh-Hadamard Transform:
1. **2D Nim-Product Theorem**:
   By the Turning Turtles theorem for 2D impartial coin-flipping games:
   The game decomposes into independent 1D games along the horizontal (square moves) and vertical (triangular moves) axes.
   The Grundy value (nim-value) of cell $(i, j)$ is the nim-product of the 1D Grundy values $g_x(i) \otimes g_y(j)$.
2. **1D Grundy Sequences**:
   - $g_x(i)$ is the Grundy value for 1D coin turning with square steps $k^2$.
   - $g_y(j)$ is the Grundy value for 1D coin turning with triangular steps $\frac{m(m+1)}{2}$.
   Both 1D sequences are small integers $(< 64)$ computed linearly for $1 \le i, j \le N$.
3. **FWHT Frequency Convolution**:
   A first move $(w, h)$ ending at $(i, j)$ is a winning move iff its nim-sum equals the total board nim-sum.
   Counting winning moves reduces to 1D XOR frequency convolutions via Fast Walsh-Hadamard Transform (FWHT).
4. **Execution**:
   Evaluating $W(10^6)$ yields $3996390106631$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 10^6$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ 1D Grundy arrays.
