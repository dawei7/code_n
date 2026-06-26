# Strassen Matrix Multiplication

| | |
|---|---|
| **ID** | `dc_06` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N^2.81)$ Time, $O(N^2)$ Space |
| **Difficulty** | 10/10 |
| **Interview relevance** | 1/10 |
| **Wikipedia** | [Strassen algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm) |

## Problem statement

Given two square matrices `A` and `B` of size N x N, compute their matrix product C = A x B.
Assume N is a power of 2 for simplicity.

**Input:** Two 2D matrices `A` and `B` of dimensions N x N.
**Output:** A 2D matrix representing the product.

## When to use it

- Exclusively an academic algorithm to understand advanced theoretical upper-bounds of computer science.
- It is the 2D matrix equivalent of Karatsuba Multiplication (`dc_04`), proving that $O(N^3)$ is NOT the fastest way to multiply matrices.

## Approach

**1. The Naive Approach ($O(N^3)$):**
Standard matrix multiplication calculates each cell C_{i,j} by computing the dot product of the i-th row of A and the j-th column of B. Since there are N^2 cells, and each dot product requires N multiplications, the time complexity is strictly $O(N^3)$.

**2. Naive Divide and Conquer ($O(N^3)$):**
We can recursively divide the N x N matrices into four smaller (N/2) x (N/2) sub-matrices (quadrants).
$ A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}, B = \begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} 
The resulting matrix C is calculated as:
C_{11} = (A_{11} \times B_{11}) + (A_{12} \times B_{21})
C_{12} = (A_{11} \times B_{12}) + (A_{12} \times B_{22})
C_{21} = (A_{21} \times B_{11}) + (A_{22} \times B_{21})
C_{22} = (A_{21} \times B_{12}) + (A_{22} \times B_{22})

Notice that to calculate the 4 quadrants of C, we must perform **8 recursive multiplications** of (N/2) sized matrices.
By the Master Theorem, T(N) = 8T(N/2) + $O(N^2)$ \implies $O(N^{\log_2(8)$}) = $O(N^3)$. No improvement!

**3. Strassen's Magic Trick ($O(N^{2.81})$):**
In 1969, Volker Strassen discovered an incredibly un-intuitive algebraic formula that computes the exact same 4 quadrants of C using only **7 recursive multiplications** instead of 8!
He defined 7 intermediate matrices (M_1 through M_7):
- M_1 = (A_{11} + A_{22}) \times (B_{11} + B_{22})
- M_2 = (A_{21} + A_{22}) \times B_{11}
- M_3 = A_{11} \times (B_{12} - B_{22})
- M_4 = A_{22} \times (B_{21} - B_{11})
- M_5 = (A_{11} + A_{12}) \times B_{22}
- M_6 = (A_{21} - A_{11}) \times (B_{11} + B_{12})
- M_7 = (A_{12} - A_{22}) \times (B_{21} + B_{22})

Using these 7 matrices, the final 4 quadrants of C are reassembled purely using addition and subtraction (which is $O(N^2)$ fast!):
- C_{11} = M_1 + M_4 - M_5 + M_7
- C_{12} = M_3 + M_5
- C_{21} = M_2 + M_4
- C_{22} = M_1 - M_2 + M_3 + M_6

The new recurrence relation is T(N) = 7T(N/2) + $O(N^2)$.
By the Master Theorem, the time complexity is $O(N^{\log_2(7)$}) \approx $O(N^{2.807})$.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_06: Strassen Matrix Multiplication.

Multiply two 2x2 matrices using Strassen's algorithm
"""


def solve(A, B, n):
    """Strassen 2x2 matrix multiplication.

    Seven products (p1..p7) replace the schoolbook eight,
    trading a few extra additions for one fewer multiply.
    """
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    if n == 2:
        a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
        e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
        p1 = a * (f - h)
        p2 = (a + b) * h
        p3 = (c + d) * e
        p4 = d * (g - e)
        p5 = (a + d) * (e + h)
        p6 = (b - d) * (g + h)
        p7 = (a - c) * (e + f)
        c00 = p5 + p4 - p2 + p6
        c01 = p1 + p2
        c10 = p3 + p4
        c11 = p1 + p5 - p3 - p7
        return [[c00, c01], [c10, c11]]
    return _naive(A, B, n)

def _naive(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```

</details>

## Walk-through

Due to the intense arithmetic complexity, a manual walk-through is omitted. The algebraic expansion of C_{12} = M_3 + M_5 perfectly proves the logic:
M_3 + M_5 = [A_{11} \times (B_{12} - B_{22})] + [(A_{11} + A_{12}) \times B_{22}]
= A_{11}B_{12} - A_{11}B_{22} + A_{11}B_{22} + A_{12}B_{22}
= A_{11}B_{12} + A_{12}B_{22} (The exact definition of C_{12}!)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2.81)$ | $O(N^2)$ |
| **Average** | $O(N^2.81)$ | $O(N^2)$ |
| **Worst** | $O(N^2.81)$ | $O(N^2)$ |

The algorithm eliminates one recursive multiplication call, changing T(N) = 8T(N/2) into T(N) = 7T(N/2). The time drops strictly to $O(N^{2.807})$.
Space complexity is $O(N^2)$ due to the constant allocation of temporary sub-matrices during addition and subtraction operations at every level of the recursive tree.

## Variants & optimizations

- **Coppersmith-Winograd Algorithm:** Strassen was just the beginning. The theoretical limit has been pushed further to $O(N^{2.37})$ by Coppersmith and Winograd (and even further recently). However, these algorithms are known as "Galactic Algorithms" — their constant overhead is so astronomically large that they would only out-perform Strassen on matrices so massive that they couldn't fit into the physical universe.
- **Strassen Threshold:** Like Karatsuba, Strassen has massive overhead due to array allocations and additions. Standard libraries (like BLAS or NumPy) check the matrix size. If N < \text{Threshold} (e.g., 64 or 128), it defaults to highly optimized hardware-level $O(N^3)$ multiplication.

## Real-world applications

- **Deep Learning / Neural Networks:** While standard $O(N^3)$ is heavily optimized on GPUs using Tensor Cores, some highly specialized mathematical computation libraries fallback to Strassen for massive algebraic systems on strict CPU architectures.

## Related algorithms in cOde(n)

- **[dc_04 - Karatsuba Multiplication](dc_04_karatsuba-multiplication.md)** — The 1D integer multiplication equivalent that eliminates 1 out of 4 recursive calls (O(N^{1.58})$).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
