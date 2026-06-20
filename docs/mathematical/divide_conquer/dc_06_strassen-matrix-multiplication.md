# Formal Mathematical Specification: Strassen Matrix Multiplication

## 1. Definitions and Notation

Let $\mathcal{R}$ be a ring (typically the field of real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$). We define the set of square matrices of order $n$ over $\mathcal{R}$ as $\mathcal{M}_n(\mathcal{R})$. 

Given two matrices $A, B \in \mathcal{M}_n(\mathcal{R})$, where $n = 2^k$ for some $k \in \mathbb{N}$, we define the block decomposition of $A$ and $B$ as:
$$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}, \quad B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$$
where $A_{ij}, B_{ij} \in \mathcal{M}_{n/2}(\mathcal{R})$. The objective is to compute the product $C = A \cdot B \in \mathcal{M}_n(\mathcal{R})$, where $C$ is partitioned into quadrants $C_{ij} \in \mathcal{M}_{n/2}(\mathcal{R})$.

## 2. Algebraic Characterization

The standard definition of matrix multiplication requires $C_{ij} = \sum_{k=1}^2 A_{ik} B_{kj}$. Strassen’s algorithm replaces the eight standard multiplications with seven intermediate products $M_1, \dots, M_7 \in \mathcal{M}_{n/2}(\mathcal{R})$ defined as:

$$
\begin{aligned}
M_1 &= (A_{11} + A_{22})(B_{11} + B_{22}) \\
M_2 &= (A_{21} + A_{22})B_{11} \\
M_3 &= A_{11}(B_{12} - B_{22}) \\
M_4 &= A_{22}(B_{21} - B_{11}) \\
M_5 &= (A_{11} + A_{12})B_{22} \\
M_6 &= (A_{21} - A_{11})(B_{11} + B_{12}) \\
M_7 &= (A_{12} - A_{22})(B_{21} + B_{22})
\end{aligned}
$$

The quadrants of the resulting matrix $C$ are then reconstructed via linear combinations of these products:

$$
\begin{aligned}
C_{11} &= M_1 + M_4 - M_5 + M_7 \\
C_{12} &= M_3 + M_5 \\
C_{21} &= M_2 + M_4 \\
C_{22} &= M_1 - M_2 + M_3 + M_6
\end{aligned}
$$

**Correctness:** The validity of this construction relies on the distributive property of the ring $\mathcal{R}$. For instance, expanding $C_{12}$:
$$C_{12} = A_{11}(B_{12} - B_{22}) + (A_{11} + A_{12})B_{22} = A_{11}B_{12} - A_{11}B_{22} + A_{11}B_{22} + A_{12}B_{22} = A_{11}B_{12} + A_{12}B_{22}$$
This matches the standard definition of the block matrix product.

## 3. Complexity Analysis

### Time Complexity
The algorithm follows a divide-and-conquer paradigm. Let $T(n)$ denote the number of arithmetic operations required to multiply two $n \times n$ matrices. 

1. **Divide:** Partitioning the matrices takes $O(1)$ time (or $O(n^2)$ if copying is required).
2. **Conquer:** The algorithm performs 7 recursive multiplications of size $n/2$.
3. **Combine:** The additions and subtractions of the $n/2 \times n/2$ matrices require $O(n^2)$ operations.

This yields the recurrence relation:
$$T(n) = 7T(n/2) + \Theta(n^2)$$

Applying the **Master Theorem** for recurrences of the form $T(n) = aT(n/b) + f(n)$, where $a=7, b=2, f(n)=n^2$:
Since $\log_b(a) = \log_2(7) \approx 2.807$, and $f(n) = O(n^{\log_2(7) - \epsilon})$ for $\epsilon \approx 0.807$, the complexity is dominated by the recursive calls:
$$T(n) = \Theta(n^{\log_2 7}) \approx O(n^{2.807})$$

### Space Complexity
Let $S(n)$ be the auxiliary space required. At each level of recursion, we must store the intermediate matrices $M_1, \dots, M_7$ and the sums/differences of sub-matrices. 

The recurrence for space is $S(n) = S(n/2) + O(n^2)$. By the geometric series summation:
$$S(n) = \sum_{i=0}^{\log_2 n} O\left(\left(\frac{n}{2^i}\right)^2\right) = O(n^2) \sum_{i=0}^{\log_2 n} \left(\frac{1}{4}\right)^i = O(n^2)$$
Thus, the total auxiliary space complexity is $O(n^2)$, as the space required at the top level of the recursion dominates the sum of the space required at all subsequent levels.