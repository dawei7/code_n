# Nim - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In standard 3-heap normal-play Nim with heap sizes $(n_1, n_2, n_3)$, a position is a losing position for the player about to move ($X(n_1, n_2, n_3) = 0$) if and only if the bitwise XOR sum of the heap sizes is zero:

$$
X(n_1, n_2, n_3) = 0 \iff n_1 \oplus n_2 \oplus n_3 = 0
$$

We are asked to count how many positive integers $n \le 2^{30}$ satisfy:

$$
X(n, 2n, 3n) = 0 \iff n \oplus 2n \oplus 3n = 0
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Linear Sequential Verification
A naive approach loops over all integers $n = 1, 2, \dots, 2^{30}$ and computes `n ^ (2 * n) ^ (3 * n) == 0`:
- Number of operations: $2^{30} \approx 1.07 \times 10^9$ iterations.
- In Python, iterating through $10^9$ integers takes $> 40$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Carry-Free Addition & Consecutive Ones Prohibition
Notice that $3n = n + 2n$.
For any two non-negative integers $A$ and $B$, their arithmetic sum is related to their bitwise XOR sum by:

$$
A + B = (A \oplus B) + 2(A \land B)
$$

Therefore:

$$
A + B = A \oplus B \iff A \land B = 0
$$

Setting $A = n$ and $B = 2n$:

$$
n \oplus 2n = 3n \iff n \land (2n) = 0
$$

Since multiplication by $2$ shifts the binary representation to the left by 1 bit ($(2n)_i = n_{i-1}$), $n \land (2n) = 0$ holds if and only if the binary expansion of $n$ **contains no two consecutive 1s** (Zeckendorf-like binary words).

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Fibonacci Sequence Equivalence
Let $a_k$ be the number of $k$-bit binary words without adjacent 1s:
- Words ending in `0`: obtained by appending `0` to any valid $(k-1)$-bit word ($a_{k-1}$ choices).
- Words ending in `1`: must end in `01`, obtained by appending `01` to any valid $(k-2)$-bit word ($a_{k-2}$ choices).
Thus:

$$
a_k = a_{k-1} + a_{k-2}, \quad a_1 = 2, \quad a_2 = 3 \implies a_k = F_{k+2}
$$

where $F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, \dots$ is the Fibonacci sequence.

### Boundary Enumeration on $[1, 2^{30}]$:
- The range $[0, 2^{30} - 1]$ comprises all 30-bit words, containing $F_{32}$ words without consecutive 1s.
- Subtracting $n = 0$ removes $1$.
- Adding $n = 2^{30} = (1000\dots 0)_2$ (which has no consecutive 1s) adds $1$.
- **Exact Total:** $(F_{32} - 1) + 1 = \mathbf{F_{32} = 2\,178\,309}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Verification on Small Bounds $2^k$:

| $k$ | Range $[1, 2^k]$ | Valid Binary Numbers | Count | Fibonacci Identity |
| :---: | :---: | :--- | :---: | :---: |
| **$1$** | $[1, 2]$ | `1`, `10` | $2$ | $F_3 = 2$ |
| **$2$** | $[1, 4]$ | `1`, `10`, `100` | $3$ | $F_4 = 3$ |
| **$3$** | $[1, 8]$ | `1`, `10`, `100`, `101`, `1000` | $5$ | $F_5 = 5$ |
| **$4$** | $[1, 16]$ | `1`, `2`, `4`, `5`, `8`, `9`, `10`, `16` | $8$ | $F_6 = 8$ |
| **$30$** | $[1, 2^{30}]$ | — | **$2\,178\,309$** | **$F_{32} = 2\,178\,309$** |

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Recurrence Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Base Initialization** | $a = 1, b = 1$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Fibonacci Transition** | Loop $32$ times: $(a, b) \leftarrow (b, a + b)$ | $\mathcal{O}(1)$ |
| **Stage 3** | **Result Output** | Return $F_{32}$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | 32 scalar iterations in $< 0.0001\text{ s}$ |
| **Space Complexity** | $\mathcal{O}(1)$ | Two integer registers |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants & Edge Cases Handled:
1. **$n = 0$ Exclusion:** $n = 0$ is strictly excluded ($n \ge 1$).
2. **Boundary $n = 2^{30}$:** Handled cleanly as the single non-zero bit power of 2.
3. **Carry-Free Equivalence:** $A \land B = 0 \iff A + B = A \oplus B$ holds identically over $\mathbb{Z}_{\ge 0}$.