# Tours on a 4 x N Playing Board - Optimal Approach

## Algorithm Explanation

Find the number of Hamiltonian tours $T(10^{12}) \pmod{10^8}$ over a $4 \times 10^{12}$ board starting at $(1, 1)$ and ending at $(4, 1)$.

### Matrix Exponentiation & Linear Recurrence:
1. **4th-Order Linear Recurrence**:
   Boundary connectivity across columns of fixed height $4$ reduces path counts to a 4th-order linear recurrence:
   $$T(n) = 2 T(n-1) + 2 T(n-2) - 2 T(n-3) + T(n-4)$$
2. **Initial Conditions**:
   $T(1) = 1, T(2) = 1, T(3) = 4, T(4) = 8$.
3. **Logarithmic Matrix Exponentiation**:
   Constructing the $4 \times 4$ companion matrix $M$:
   $$M = \begin{pmatrix} 2 & 2 & -2 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$
   Computing $M^{10^{12} - 4} \times [8, 4, 1, 1]^T \pmod{10^8}$ takes $\mathcal{O}(\log(10^{12}))$ operations.
4. **Execution**:
   Evaluating $T(10^{12}) \pmod{10^8}$ yields $15836928$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K^3 \log N)$ for $K = 4$ and $N = 10^{12}$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(K^2)$ for matrix storage.
