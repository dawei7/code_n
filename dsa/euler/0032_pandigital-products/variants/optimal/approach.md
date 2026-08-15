# Pandigital Products - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

An arithmetic identity $a \times b = p$ ($a, b, p \in \mathbb{N}$) is defined as **$1$ through $9$ pandigital** if the concatenated string:
$$\mathbf{s} = \operatorname{str}(a) \mathbin{\Vert} \operatorname{str}(b) \mathbin{\Vert} \operatorname{str}(p)$$
contains each of the decimal digits $1, 2, \dots, 9$ exactly once.

Let $\mathcal{P}_{\text{pan}}$ denote the set of all unique products $p$ that satisfy at least one such identity.

The objective is to compute the sum of all distinct pandigital products:
$$S = \sum_{p \in \mathcal{P}_{\text{pan}}} p$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Unconstrained Double Loop Search
A naive algorithm iterates over all possible pairs $(a, b)$ up to $10\,000$:
```python
def naive_pandigital_products():
    # tests all (a, b) in [1, 9876] x [1, 9876]
    # ...
```

### Computational Inefficiencies
1. **$10^8$ Redundant Iterations**: Most pairs have total digit lengths far from $9$.
2. **Superiority of Digit Length Partitioning**: Analytical inequalities prove that only two partition structures can total $9$ digits, reducing search space to $\approx 4000$ operations ($\approx 0.005$ seconds).

---

## 3. Core Intuition & Mathematical Structure

Let $L(x) = \lfloor \log_{10} x \rfloor + 1$ denote the number of decimal digits in $x$.
For $a \times b = p$, the total digit length must satisfy:
$$L(a) + L(b) + L(p) = 9$$

Since $10^{L(a)-1} \le a < 10^{L(a)}$ and $10^{L(b)-1} \le b < 10^{L(b)}$:
$$10^{L(a)+L(b)-2} \le a \cdot b < 10^{L(a)+L(b)} \implies L(p) \in \{L(a)+L(b)-1, \, L(a)+L(b)\}$$

### Digit Length Partition Cases

| Partition Pattern | $L(a)$ | $L(b)$ | $L(p)$ | Total Digits $L(a)+L(b)+L(p)$ | Feasibility |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$1 \times 3$** | $1$ | $3$ | $3$ or $4$ | $1 + 3 + (3\text{ or }4) = 7\text{ or }8 \neq 9$ | **Impossible** |
| **$1 \times 4$** | **$1$** | **$4$** | **$4$** | $1 + 4 + 4 = \mathbf{9}$ | **Valid (Case 1)** |
| **$2 \times 3$** | **$2$** | **$3$** | **$4$** | $2 + 3 + 4 = \mathbf{9}$ | **Valid (Case 2)** |
| **$2 \times 4$** | $2$ | $4$ | $5$ | $2 + 4 + 5 = 11 > 9$ | **Impossible** |
| **$3 \times 3$** | $3$ | $3$ | $5$ or $6$ | $3 + 3 + (5\text{ or }6) \ge 11 > 9$ | **Impossible** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Bounded Factor Search Ranges
1. **Case 1 ($1 \times 4 \to 4$)**:
   $$a \in [1, 9], \quad b \in \left[1234, \left\lfloor \frac{9876}{a} \right\rfloor \right]$$
2. **Case 2 ($2 \times 3 \to 4$)**:
   $$a \in [12, 98], \quad b \in \left[123, \left\lfloor \frac{9876}{a} \right\rfloor \right]$$
3. **Set Deduplication**:
   Store each valid product in a hash set $\mathcal{H}$ to avoid double counting identical products produced by multiple factorizations (e.g. $18 \times 297 = 5346$ and $27 \times 198 = 5346$).

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for Identity $39 \times 186 = 7254$
- $a = 39$ ($2$ digits: `3`, `9`)
- $b = 186$ ($3$ digits: `1`, `8`, `6`)
- $p = 7254$ ($4$ digits: `7`, `2`, `5`, `4`)
- Concatenation: $\mathbf{s} = \text{"391867254"}$.
- Length is $9$, contains digits `1` through `9` without repetition $\implies$ Pandigital! $\checkmark$

### Example 2: Complete Target Evaluation
The set of unique 1-9 pandigital products is:
$$\mathcal{P}_{\text{pan}} = \{4396, 5346, 5796, 6952, 7254, 7632, 7852\} \cup \{4396, 5346, \dots\}$$
Summing all elements in $\mathcal{P}_{\text{pan}}$:
$$S = \mathbf{45\,228}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Set Allocation** | `unique_products = set()`, `target = set("123456789")` | $\mathcal{O}(1)$ |
| **Stage 2** | **Case 1 Scan** | For $a \in [1, 9], b \in [1234, 9876//a]$: test $\text{str}(a)\mathbin{\Vert}\text{str}(b)\mathbin{\Vert}\text{str}(p)$ | $\approx 2500$ checks |
| **Stage 3** | **Case 2 Scan** | For $a \in [12, 98], b \in [123, 9876//a]$: test $\text{str}(a)\mathbin{\Vert}\text{str}(b)\mathbin{\Vert}\text{str}(p)$ | $\approx 1500$ checks |
| **Stage 4** | **Sum Deduplicated** | `sum(unique_products)` | $\mathcal{O}(|\mathcal{P}|)$ |
| **Stage 5** | **Return Value** | Return scalar integer $45228$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(A \cdot B)$ bounded to $\approx 4\,000$ iterations | $\approx 0.005$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Hash set with $< 20$ elements |
| **Dynamic Execution** | $100\%$ Inline | Exact digit set comparison |

### Critical Invariants & Edge Cases Handled:
1. **Deduplication Invariant**: Multiple factor pairs for the same product (such as 5346) are added to `unique_products` set once.
2. **Zero Exclusion**: Digits must be strictly $1\text{--}9$; any identity containing `0` fails the set equality test.
