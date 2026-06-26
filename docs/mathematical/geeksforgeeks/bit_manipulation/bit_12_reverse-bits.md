# Formal Mathematical Specification: Reverse Bits

## 1. Definitions and Notation

Let $\mathbb{Z}_{2^k}$ denote the ring of integers modulo $2^k$. In this specification, we define the bit-width $W = 32$. The input space is the set of unsigned 32-bit integers, represented as the set $\mathcal{N} = \{n \in \mathbb{Z} \mid 0 \le n < 2^W\}$.

Any $n \in \mathcal{N}$ can be uniquely represented in its binary positional notation as a vector of bits $b = (b_{W-1}, b_{W-2}, \dots, b_1, b_0)$, where $b_i \in \{0, 1\}$ such that:
$$n = \sum_{i=0}^{W-1} b_i 2^i$$

The objective is to define a function $f: \mathcal{N} \to \mathcal{N}$ such that the output $n' = f(n)$ satisfies:
$$n' = \sum_{i=0}^{W-1} b_i 2^{W-1-i}$$

## 2. Algebraic Characterization

### 2.1 Iterative Formulation
The algorithm constructs $n'$ by iterating through the bit positions of $n$. Let $n^{(k)}$ be the value of the input after $k$ right-shifts, and $r^{(k)}$ be the value of the result after $k$ iterations. 

The state transitions for $k \in \{0, 1, \dots, W-1\}$ are defined by the recurrence:
1. **Extraction:** $b_k = \lfloor n^{(k)} / 2^0 \rfloor \pmod 2$
2. **Shift and Accumulate:** $r^{(k+1)} = (r^{(k)} \cdot 2) + b_k$
3. **Input Reduction:** $n^{(k+1)} = \lfloor n^{(k)} / 2 \rfloor$

Base cases: $n^{(0)} = n$ and $r^{(0)} = 0$. The final result is $r^{(W)}$.

### 2.2 Invariant
At the start of each iteration $k$ (where $0 \le k \le W$), the following invariant holds:
$$r^{(k)} = \sum_{j=0}^{k-1} b_j 2^{k-1-j}$$
This confirms that after $W$ iterations, $r^{(W)} = \sum_{j=0}^{W-1} b_j 2^{W-1-j}$, which is the bit-reversed representation of $n$.

### 2.3 Divide and Conquer (Bit-Masking) Formulation
Alternatively, the transformation can be expressed as a composition of bitwise permutations. Let $M_s$ be a mask of length $W$ consisting of alternating blocks of $s$ ones and $s$ zeros. The reversal is the composition of $m = \log_2 W$ operations:
$$n_{i+1} = \left( (n_i \& M_{2^{m-1-i}}) \gg 2^{m-1-i} \right) \lor \left( (n_i \& \overline{M_{2^{m-1-i}}}) \ll 2^{m-1-i} \right)$$
where $n_0 = n$ and $n_m = f(n)$.

## 3. Complexity Analysis

### 3.1 Time Complexity
The iterative approach performs a fixed number of operations $W = 32$. Each iteration $k$ involves a constant number of bitwise operations (AND, OR, LSHIFT, RSHIFT), each of which is $O(1)$ on a standard word-addressable machine.

The total time $T(W)$ is given by:
$$T(W) = \sum_{k=0}^{W-1} c = c \cdot W$$
Since $W$ is a constant ($W=32$), $T(W) = O(1)$. 

In the divide-and-conquer variant, the number of operations is $T(W) = \sum_{i=0}^{\log_2 W - 1} c = c \log_2 W$. Given $W=32$, $\log_2 32 = 5$, which is also $O(1)$.

### 3.2 Space Complexity
The algorithm maintains a constant number of auxiliary variables ($n, r, i$) regardless of the input value. The memory footprint is independent of the input size $n$ and the bit-width $W$ (assuming $W$ is fixed). 

Let $S(W)$ be the auxiliary space:
$$S(W) = \Theta(1)$$
Thus, the algorithm operates in $O(1)$ space.