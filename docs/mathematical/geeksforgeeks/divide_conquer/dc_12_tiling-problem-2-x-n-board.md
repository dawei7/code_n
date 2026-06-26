# Formal Mathematical Specification: Tiling Problem (2 x N Board)

## 1. Definitions and Notation

Let $N \in \mathbb{N}_0$ denote the width of a board of dimensions $2 \times N$. We define the set of all valid tilings of a $2 \times N$ board as $\mathcal{T}_N$. The objective is to determine the cardinality of this set, denoted by $f(N) = |\mathcal{T}_N|$.

The tiles available are of dimension $2 \times 1$ (dominoes). A tiling is a partition of the $2 \times N$ grid into $N$ disjoint sets of cells, where each set corresponds to the area covered by a single tile. 

We define the domain of our function as:
- $N \in \{0, 1, 2, \dots\}$
- $f: \mathbb{N}_0 \to \mathbb{N}_1$
- Modulo arithmetic: All calculations are performed in the ring $\mathbb{Z}_m$, where $m = 10^9 + 7$.

## 2. Algebraic Characterization

The problem exhibits optimal substructure, allowing us to define $f(N)$ via a linear homogeneous recurrence relation with constant coefficients.

Consider the leftmost column of a $2 \times N$ board. There are two mutually exclusive and exhaustive ways to cover the cells $(1,1)$ and $(2,1)$:

1. **Vertical Placement:** A single $2 \times 1$ tile covers both $(1,1)$ and $(2,1)$. The remaining area is a $2 \times (N-1)$ board, which can be tiled in $f(N-1)$ ways.
2. **Horizontal Placement:** Two $2 \times 1$ tiles are placed horizontally, covering $(1,1), (1,2)$ and $(2,1), (2,2)$. The remaining area is a $2 \times (N-2)$ board, which can be tiled in $f(N-2)$ ways.

This yields the recurrence relation:
$$f(N) = f(N-1) + f(N-2), \quad \forall N \ge 2$$

With the base cases:
- $f(0) = 1$ (The empty set is the unique tiling of a $2 \times 0$ board).
- $f(1) = 1$ (Only one vertical tile is possible).

This is isomorphic to the Fibonacci sequence $F_{n+1}$, where $F_0=0, F_1=1, F_2=1, F_3=2, \dots$. Thus, $f(N) = F_{N+1}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm employs an iterative approach to compute the $N$-th term of the sequence. Let $T(N)$ be the number of operations.
The algorithm performs a single loop from $i = 2$ to $N$. Within each iteration, we perform a constant number of additions and assignments in $\mathbb{Z}_m$.

The total work is given by the summation:
$$T(N) = c_1 + \sum_{i=2}^{N} c_2 = \Theta(N)$$
where $c_1$ represents initialization and $c_2$ represents the constant-time arithmetic operations per iteration. Thus, the time complexity is $O(N)$.

### Space Complexity
The algorithm maintains a fixed number of scalar variables to store the state of the recurrence: $a$ (representing $f(i-2)$) and $b$ (representing $f(i-1)$). 

Let $S(N)$ be the auxiliary space complexity. Since the memory usage is independent of the input size $N$:
$$S(N) = O(1)$$
The space complexity is strictly constant, as we only require storage for two integers regardless of the magnitude of $N$.