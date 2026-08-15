# Integral Fusion - Optimal Approach

## 1. Problem Statement & Mathematical Formulation

For a positive integer $n > 1$, the factor tree $T(n)$ is built by recursively splitting $n$ into the closest-to-$\sqrt{n}$ divisor pair $a \times b$ with $a \le b$ and $|b - a|$ minimal. Given the tree shape of $n!!$, $M(n)$ is the smallest positive integer whose factor tree has the same shape as $T(n!!)$.

We seek $\sum_{n=2}^{31} M(n)$.

---

## 2. Naive Approach & Computational Impossibility

### Sequential Integer Scan
Enumerate $x = 1, 2, 3, \dots$, factor each $x$ into its closest-factor tree, and check if the shape matches $T(n!!)$. Since $M(31) = 26\,129\,782\,224\,000 \approx 2.6 \times 10^{13}$, scanning every integer up to this bound for all 30 values of $n$ requires $> 10^{14}$ trial factorizations, taking centuries.

---

## 3. Mathematical Breakthrough & Applied Theorems

### Bottom-Up Beam Search DP on Tree Shapes
1. **Topology Extraction**: Recursively factor $n!!$ using closest-to-$\sqrt{n}$ divisor pairs to obtain the binary tree shape $T(n!!)$. Each leaf is a prime factor; each internal node records left/right subtree shapes.

2. **Candidate Synthesis via Prime Signatures**: For each distinct subtree shape, maintain a sorted beam of the $K$ smallest valid integers along with their prime factorizations. Leaf shapes map to the first $K$ primes $\{2, 3, 5, 7, \dots\}$. Internal shapes are synthesized by taking the Cartesian product of left and right candidate lists, enforcing $A \le B$, combining prime signatures, and verifying the closest-factor constraint.

3. **Divisor Verification from Prime Signatures**: For a candidate $N = A \times B$ with known factorization, generate all divisors directly from the prime signature and check that no divisor $D$ satisfies $A < D \le \lfloor\sqrt{N}\rfloor$. This ensures $A$ is genuinely the closest factor.

4. **Dynamic Beam Scaling**: If the root shape yields no valid candidates at beam width $K$, clear the memoization cache and retry with $K \in \{100, 300, 1000, 3000\}$ until a valid minimum is found.

---

## 4. Step-by-Step Mathematical Algorithm

1. Compute $n!!$ as an exact integer for each $n = 2, \dots, 31$.
2. Recursively extract the binary tree shape $T(n!!)$ using closest-factor splitting.
3. For each subtree shape (bottom-up, memoized):
   - **Leaf**: Return the first $K$ primes as candidates.
   - **Internal node $(L, R)$**: Form all pairs $(a, b)$ from $L$-candidates $\times$ $R$-candidates with $a \le b$. Compute $N = a \times b$, merge prime signatures, generate all divisors of $N$, find the largest divisor $\le \lfloor\sqrt{N}\rfloor$, and accept $N$ only if this divisor equals $a$.
4. Sort accepted candidates by value and keep the smallest $K$.
5. If the root returns an empty list, clear cache and retry with larger $K$.
6. $M(n)$ is the smallest root candidate. Accumulate $\sum_{n=2}^{31} M(n)$.

---

## 5. Implementation Architecture & Mechanics

The solution is implemented in `solution.py`:
- **`factor_tree(n)`**: Recursive closest-factor tree shape extraction.
- **`get_divisors(factors)`**: Generate all divisors from a prime signature dictionary.
- **`get_cands(t, max_cands)`**: Memoized bottom-up DP returning the $K$ smallest valid candidates for subtree shape $t$.
- **`solve(limit)`**: Outer loop over $n = 2, \dots, 31$ with dynamic beam scaling retry.

---

## 6. Mathematical Complexity Analysis

- **Time Complexity**: $\mathcal{O}(30 \times K^2 \times d)$ where $K \le 3000$ is the beam width and $d$ is the average divisor count per candidate. Total work $\sim 10^8$ operations.
- **Space Complexity**: $\mathcal{O}(K \times T)$ where $T$ is the number of distinct subtree shapes, each storing up to $K$ candidate pairs with their prime signatures.
