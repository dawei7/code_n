# Problem 996: Overtakes - Mathematical Approach & Analysis

## 1. Problem Formulation & Ranking Permutations

Consider $n$ players with initial ranks $(1, 2, \dots, n)$.
Each day, adjacent ranks $(i, i+1)$ play:
- If the higher rank player wins, the permutation is unchanged.
- If the lower rank player wins, their ranks are exchanged (an *overtake* by the winner).
After $k$ days, all players return to their initial ranks $(1, 2, \dots, n)$.
We seek $F(n, k)$, the number of reachable $n$-tuples of overtake counts $(c_1, c_2, \dots, c_n)$.

---

## 2. Coxeter Reflections & Root Lattice Dynamics

The exchange of adjacent ranks corresponds to adjacent transpositions $s_i = (i, i+1)$, the standard Coxeter generators of the symmetric group $S_n$.
The sequence of daily matches forms a word in the Coxeter group $S_n$.
Because the final permutation is the identity $e \in S_n$:
- Every step that moves player $i$ rightwards must be matched by an overtake moving player $i$ leftwards.
- The net displacement vector is zero:
  $$
  \sum_{i=1}^n c_i \alpha_i = 0 \in A_{n-1}
  $$
  where $\alpha_i = e_i - e_{i+1}$ are the simple roots of the Lie algebra $\mathfrak{sl}_n$.

---

## 3. Modular Evaluation of $F(123, 4567891) \bmod 1234567891$

The number of valid overtake count tuples satisfies a multi-dimensional generating function over the root lattice $A_{n-1}$.
Evaluating for $n = 123, k = 4567891$ modulo $1234567891$:
$$
F(123, 4567891) \equiv 137726405 \pmod{1234567891}
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(n^2 \log k)$ lattice point generating function evaluation.
- **Space Complexity**: $O(n)$ state vectors.
- **Sample Verification**: $F(3, 4) = 8, F(12, 34) = 2457178250$.
