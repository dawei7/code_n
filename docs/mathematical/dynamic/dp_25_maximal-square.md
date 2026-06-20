# Formal Mathematical Specification: Maximal Square

## 1. Definitions and Notation

Let $M$ and $N$ be positive integers representing the dimensions of a binary matrix $A \in \{0, 1\}^{M \times N}$. We denote the element at row $i$ and column $j$ as $A_{i,j}$, where $0 \le i < M$ and $0 \le j < N$.

We define the state space $\mathcal{S}$ as a set of side lengths of squares. Let $f(i, j)$ be a function $f: \{0, \dots, M-1\} \times \{0, \dots, N-1\} \to \mathbb{N}_0$, where $f(i, j)$ denotes the side length of the largest square submatrix of $A$ whose bottom-right corner is at index $(i, j)$.

The objective is to compute the area of the maximal square, defined as:
$$\mathcal{A} = \left( \max_{0 \le i < M, 0 \le j < N} f(i, j) \right)^2$$

## 2. Algebraic Characterization

The function $f(i, j)$ is defined by the following recurrence relation:

**Base Cases:**
For the boundary conditions where $i=0$ or $j=0$:
$$f(i, j) = A_{i,j}$$

**Recursive Step:**
For $i > 0$ and $j > 0$:
$$f(i, j) = \begin{cases} 
\min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1 & \text{if } A_{i,j} = 1 \\
0 & \text{if } A_{i,j} = 0 
\end{cases}$$

**Correctness Invariant:**
The recurrence holds because a square of side $k > 1$ ending at $(i, j)$ exists if and only if squares of side at least $k-1$ exist ending at $(i-1, j)$, $(i, j-1)$, and $(i-1, j-1)$. The value $f(i, j)$ represents the largest $k$ such that the submatrix $A[i-k+1 \dots i][j-k+1 \dots j]$ consists entirely of ones.

**Space-Optimized State:**
To reduce space complexity, we define a 1D array $D$ of length $N+1$. Let $D^{(i)}_j$ denote the value of $f(i, j)$ at row $i$. The transition is:
$$D^{(i)}_j = \begin{cases} 
\min(D^{(i)}_j, D^{(i)}_{j-1}, \text{prev}) + 1 & \text{if } A_{i,j} = 1 \\
0 & \text{if } A_{i,j} = 0 
\end{cases}$$
where $\text{prev}$ stores the value of $f(i-1, j-1)$ before the update of $D^{(i)}_j$.

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through each cell of the $M \times N$ matrix exactly once. For each cell $(i, j)$, the algorithm performs a constant number of operations: one comparison, one minimum calculation, one addition, and one assignment. 

The total time complexity $T(M, N)$ is given by the summation:
$$T(M, N) = \sum_{i=1}^{M} \sum_{j=1}^{N} \Theta(1) = \Theta(M \cdot N)$$
Thus, the time complexity is $O(M \cdot N)$.

### Space Complexity
The naive implementation requires an $M \times N$ matrix, resulting in $O(M \cdot N)$ space. However, the optimized implementation utilizes a 1D array $D$ of size $N+1$ and a scalar variable $\text{prev}$ to maintain the state of the diagonal element $(i-1, j-1)$.

The auxiliary space complexity $S(N)$ is:
$$S(N) = \text{size}(D) + \text{size}(\text{prev}) = (N+1) \cdot \text{word\_size} + 1 \cdot \text{word\_size} = O(N)$$
Given that the input matrix is provided, the auxiliary space complexity is $O(N)$, satisfying the requirement.