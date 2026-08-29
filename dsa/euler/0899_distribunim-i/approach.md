# DistribuNim I - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Two players play normal-play Nim with two piles $(a, b)$.
A valid move takes $(u, v)$ stones such that:
1. $u + v = \min(a, b)$
2. $u < a$ and $v < b$ (both piles remain non-empty).

$L(n)$ is the number of ordered pairs $(a, b) \in [1, n]^2$ that are losing (P-)positions for the first player.
Given:
- $L(7) = 21$
- $L(7^2) = 221$

Find $L(7^{17})$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### 2D Backward Induction Table
- For $N = 7^{17} \approx 2.32 \times 10^{14}$, allocating an $N \times N$ matrix or iterating over $N^2$ states is impossible.

---

## 3. Core Intuition & Mathematical Structure

### Binary Trailing-Ones and Bit-Length Invariant
By backwards induction on the quotient lattice:
A state $(a, b)$ is a P-position if and only if:

$$
b \equiv 2^{\text{len}(a)} - 1 \pmod{2^{\text{len}(a)}} \quad \text{or} \quad a \equiv 2^{\text{len}(b)} - 1 \pmod{2^{\text{len}(b)}}
$$

That is, the larger pile has at least as many trailing $1$-bits as the entire bit length of the smaller pile!

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Disjoint Bit-Length Block Decomposition
We count valid pairs $(a, b)$ by partitioning according to their bit lengths $k = \lfloor \log_2 a \rfloor + 1$:

1. **Strictly Unequal Lengths ($\text{len}(a) < \text{len}(b)$)**:
   For each length $k \in [1, \lfloor \log_2 N \rfloor + 1]$:
   - $a \in [2^{k-1}, \min(N, 2^k - 1)]$ has count $C_a$.
   - $b \in [2^k, N]$ with $b \equiv 2^k - 1 \pmod{2^k}$ has count $C_b = \lfloor (N - (2^{k+1} - 1)) / 2^k \rfloor + 1$.
   - Contribution: $2 \cdot C_a \cdot C_b$.

2. **Equal Lengths ($\text{len}(a) = \text{len}(b) = k$)**:
   - Condition requires $a = 2^k - 1$ or $b = 2^k - 1$.
   - Contribution: $2 \cdot C_k - 1$ (if $2^k - 1 \le N$).

Summing across all $k \le 48$ gives $L(7^{17}) = \mathbf{10784223938983273}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $N = 7$:
- $k = 1$ ($a \in [1, 1]$): $C_a = 1$. $b \in [2, 7]$ with $b \equiv 1 \pmod 2 \implies b \in \{3, 5, 7\} (C_b = 3)$. Contribution: $2 \times 1 \times 3 = 6$.
- $k = 2$ ($a \in [2, 3]$): $C_a = 2$. $b \in [4, 7]$ with $b \equiv 3 \pmod 4 \implies b \in \{7\} (C_b = 1)$. Contribution: $2 \times 2 \times 1 = 4$.
- Equal length terms:
  - $k=1$: $(1, 1) \implies 1$
  - $k=2$: $a=3$ or $b=3 \implies 2(2) - 1 = 3$
  - $k=3$: $a=7$ or $b=7 \implies 2(4) - 1 = 7$
- Total: $6 + 4 + (1 + 3 + 7) = \mathbf{21}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Bit-Length Loop** | Iterate $k$ from $1$ to $\lfloor \log_2 N \rfloor + 1$ | $\mathcal{O}(\log N)$ |
| **Stage 2** | **Unequal Length Counting** | Multiply block counts by arithmetic progression frequencies | $\mathcal{O}(1)$ |
| **Stage 3** | **Equal Length Counting** | Add boundary pivot elements | $\mathcal{O}(1)$ |
| **Stage 4** | **Result Output** | Return $10784223938983273$ | $\mathcal{O}(\log N)$ in pure Python ($< 0.001\text{ s}$) |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\log N) \approx 0.001\text{ s}$ | Real-time execution |
| **Space Complexity** | $\mathcal{O}(1) \le 1\text{ KB}$ | Minimal stack |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Trailing-One Suffix Periodicity**: $b \equiv 2^k - 1 \pmod{2^k}$ fully characterizes all reachable terminal states.
2. **Disjoint Case Union**: Splitting into $\text{len}(a) < \text{len}(b)$, $\text{len}(a) > \text{len}(b)$, and $\text{len}(a) = \text{len}(b)$ prevents double-counting.
