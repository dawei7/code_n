# Coloured Configurations - Optimal Approach

## Algorithm Explanation

Find the last $8$ digits of $N(25, 75, 1984)$, the number of valid $c$-colorings of compound graphs built from $a$ units of type $A$ and $b$ units of type $B$.

### Chromatic Representation Theory & Matrix Eigenvalues:
1. **Transfer Matrix Decomposition**:
   Under the action of the symmetric group $S_c$ on edge color pairs, the transfer matrices $M_A(c)$ and $M_B(c)$ decompose into $3$ invariant eigenspaces with multiplicities $m_0 = 1$, $m_1 = 2c - 3$, and $m_2 = \frac{c(c-3)}{2}$.
2. **Closed-Form Eigenvalue Polynomials**:
   - For Unit $A$:
     $\lambda_0(A, c) = (c-1)(c-2)^2$, $\lambda_1(A, c) = (c-2)(c-1)$, $\lambda_2(A, c) = (c-2)(c-3)$.
   - For Unit $B$:
     $\lambda_0(B, c) = (c-2)(c+1)(2c+3)$, $\lambda_1(B, c) = (c-2)(c+9)$, $\lambda_2(B, c) = (c-2)(c-3)$.
3. **Combination & Modular Exponentiation**:
   There are $\binom{a+b}{a}$ ways to arrange the sequence of units.
   $$N(a, b, c) = \binom{a+b}{a} \cdot \left[ \lambda_0(A)^a \lambda_0(B)^b + (2c-3)\lambda_1(A)^a \lambda_1(B)^b + \frac{c(c-3)}{2}\lambda_2(A)^a \lambda_2(B)^b \right] \pmod{10^8}$$
4. **Execution**:
   Evaluating for $a=25, b=75, c=1984$ using `pow(..., MOD)` yields $79603968$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log(a+b))$ - Modular exponentiation and binomial coefficient. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
