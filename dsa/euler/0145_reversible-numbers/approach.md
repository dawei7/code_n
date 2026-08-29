# Reversible Numbers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Some positive integers $n$ have the property that the sum:

$$
n + \operatorname{reverse}(n)
$$

consists entirely of **odd decimal digits**. For instance:

$$
36 + 63 = 99 \quad \text{and} \quad 409 + 904 = 1313
$$

We will call such numbers **reversible**; so $36, 63, 409,$ and $904$ are reversible. Leading zeroes are not allowed in either $n$ or $\operatorname{reverse}(n)$ (so $n$ cannot be a multiple of 10).

There are $120$ reversible numbers below one-thousand ($1000$).

The objective is to find **how many reversible numbers there are below one-billion ($10^9$)**:

$$
N_{\text{rev}} = \left| \left\{ n < 10^9 \;\middle|\; n \not\equiv 0 \pmod{10} \land \forall d \in \operatorname{digits}(n + \operatorname{reverse}(n)), \, d \equiv 1 \pmod 2 \right\} \right|
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Iteration over 1 Billion Integers
A naive approach loops from 1 to $10^9$, reversing digits and testing parity:
```python
def naive_reversible_numbers():
    # Testing 10^9 numbers with string reversals takes > 40 seconds
    # ...
```

### Exact Combinatorial Digit Carry Classification
Let $L$ be the digit length of $n$ ($1 \le L \le 8$ for $n < 10^9$).
1. **Case $L \equiv 1 \pmod 4$ ($L \in \{1, 5\}$):**
   - The middle digit has no partner and its sum is $2 d_{\text{mid}}$.
   - Any carry into the middle digit forces an adjacent parity mismatch, making valid sums **impossible**:

$$
N(L) = 0
$$

2. **Case $L$ is Even ($L \in \{2, 4, 6, 8\}$):**
   - No carries can propagate across digit pairs without ruining parity.
   - The outermost pair $(d_1, d_L)$ must satisfy $d_1 + d_L \in \{1, 3, 5, 7, 9\}$ with $d_1, d_L \ge 1 \implies 20$ valid pairs.
   - Each internal pair $(d_i, d_{L-i+1})$ allows $d_i, d_{L-i+1} \in [0, 9] \implies 30$ valid pairs.

$$
N(L) = 20 \times 30^{L/2 - 1}
$$

3. **Case $L \equiv 3 \pmod 4$ ($L \in \{3, 7\}$):**
   - A carry is required into the middle digit:

$$
N(L) = 100 \times 500^{(L-3)/4}
$$

4. Summing across $L = 1 \dots 8$ evaluates the answer in $\approx 0.0000$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Combinatorial Count Breakdown by Digit Length $L$

| Digit Length $L$ | Modulo Class | Combinatorial Formula | Sub-Counts | Count $N(L)$ | Cumulative Count |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$L = 1$** | $L \equiv 1 \bmod 4$ | $0$ | — | **$0$** | $0$ |
| **$L = 2$** | $L$ Even | $20 \times 30^0$ | $20 \times 1$ | **$20$** | $20$ |
| **$L = 3$** | $L \equiv 3 \bmod 4$ | $100 \times 500^0$ | $100 \times 1$ | **$100$** | **$120$ ($< 1000$ Sample)** |
| **$L = 4$** | $L$ Even | $20 \times 30^1$ | $20 \times 30$ | **$600$** | $720$ |
| **$L = 5$** | $L \equiv 1 \bmod 4$ | $0$ | — | **$0$** | $720$ |
| **$L = 6$** | $L$ Even | $20 \times 30^2$ | $20 \times 900$ | **$18\,000$** | $18\,720$ |
| **$L = 7$** | $L \equiv 3 \bmod 4$ | $100 \times 500^1$ | $100 \times 500$ | **$50\,000$** | $68\,720$ |
| **$L = 8$** | $L$ Even | $20 \times 30^3$ | $20 \times 27000$ | **$540\,000$** | **$608\,720$ (Total)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Length-by-Length Closed-Form Evaluation
Summing all digit lengths below $10^9$ ($L = 1 \dots 8$):

$$
N_{\text{rev}} = 0 + 20 + 100 + 600 + 0 + 18\,000 + 50\,000 + 540\,000 = \mathbf{608\,720}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample for $n < 1000$ ($L \le 3$)
- $L = 1$: $0$.
- $L = 2$: $20$.
- $L = 3$: $100$.
- Total below 1000: $0 + 20 + 100 = \mathbf{120}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $n < 10^9$ ($L \le 8$)
- Summing all 8 lengths:

$$
N_{\text{rev}} = \mathbf{608\,720}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Length Loop** | For $L \in [1, 8]$ | $8$ steps |
| **Stage 2** | **Class $L \equiv 1 \bmod 4$**| Return $0$ | $\mathcal{O}(1)$ |
| **Stage 3** | **Class $L$ Even** | Return $20 \times 30^{L/2 - 1}$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Class $L \equiv 3 \bmod 4$**| Return $100 \times 500^{(L-3)/4}$ | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Sum** | Return `sum(...) = 608720` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\text{max\_len})$ where $\text{max\_len} = 8$ | $\approx 0.0000$ seconds ($8$ arithmetic operations) |
| **Space Complexity** | $\mathcal{O}(1)$ | Constant auxiliary space |
| **Dynamic Execution** | $100\%$ Inline | Closed-form combinatorial carry analysis |

### Critical Invariants & Edge Cases Handled:
1. **No Leading Zeros Invariant**: Outer pair formula restricts $d_1 \ge 1, d_L \ge 1$, ensuring both $n$ and $\operatorname{reverse}(n)$ have no leading zeros.
2. **Modulo 4 Parity Impossibility**: Carry propagation from the center in odd lengths $L \equiv 1 \pmod 4$ inevitably creates an even digit, correctly yielding 0.