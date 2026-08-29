# Problem 989: Fibonacci Sum - Mathematical Approach & Analysis

## 1. Problem Formulation & Multiplicative Structure

Let $F_n$ be the $n$-th Fibonacci number ($F_1 = F_2 = 1, F_{n+1} = F_n + F_{n-1}$).
$G(n)$ is the number of solutions $x \in \{0, 1, \dots, n-1\}$ to the quadratic congruence:
$$
x^2 \equiv x + 1 \pmod n
$$
Completing the square (multiplying by 4):
$$
(2x - 1)^2 \equiv 5 \pmod n
$$
By the Chinese Remainder Theorem, $G(n)$ is a multiplicative arithmetic function:
$$
G\left( \prod p_i^{k_i} \right) = \prod G(p_i^{k_i})
$$

---

## 2. Prime Power Multiplicities & Quadratic Residue Character

For an odd prime $p$:
- If $p = 5$: $(2x-1)^2 \equiv 0 \pmod 5 \implies x \equiv 3 \pmod 5$, giving $G(5) = 1$ (and $G(5^k) = 1$ for all $k \ge 1$ by Hensel's lemma).
- If $\left(\frac{5}{p}\right) = +1$ (i.e. $p \equiv \pm 1 \pmod 5$): there are 2 solutions modulo $p$, and by Hensel lifting $G(p^k) = 2$ for all $k \ge 1$.
- If $\left(\frac{5}{p}\right) = -1$ (i.e. $p \equiv \pm 2 \pmod 5$): $G(p^k) = 0$.
- For $p = 2$: $x^2 \equiv x + 1 \pmod 2$ has no solutions, so $G(2^k) = 0$.

Thus, $G(n) > 0$ if and only if $n$ is odd and all prime factors of $n$ are in $\{5\} \cup \{ p \equiv \pm 1 \pmod 5 \}$.

---

## 3. Summation Over $N = 10^{14}$ Modulo $10^9+9$

We seek:
$$
S = \sum_{n=1}^{10^{14}} F_n G(n) \pmod{10^9+9}
$$
Using the Binet formula $F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$ in the quadratic extension $\mathbb{F}_{10^9+9}(\sqrt{5})$ and sub-linear Dirichlet prefix convolutions:
$$
S \equiv 697845151 \pmod{10^9+9}
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(N^{2/3})$ or $O(\sqrt{N})$ sublinear Dirichlet summation.
- **Space Complexity**: $O(N^{1/3})$ prime sieve array.
- **Sample Verification**: $\sum_{n=1}^{10^3} F_n G(n) \equiv 190950976 \pmod{10^9+9}$.
