# Lychrel Numbers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For an initial positive integer $n_0 \in \mathbb{N}$, the reverse-and-add algorithm generates a sequence $\{n_k\}_{k=0}^{\infty}$ via:

$$
n_{k+1} = n_k + \operatorname{rev}(n_k)
$$

where $\operatorname{rev}(m)$ is the integer formed by reversing the decimal digits of $m$.

A number $n$ is defined as a **Lychrel number candidate** if it does not produce a palindrome within 50 iterations:

$$
\forall k \in \{1, 2, \dots, 49\}, \quad n_k \neq \operatorname{rev}(n_k)
$$

The objective is to find the total count of Lychrel numbers strictly below $10\,000$:

$$
N_{\text{Lychrel}} = \sum_{n=1}^{9999} \mathbb{I}\left( n \text{ is a Lychrel candidate} \right)
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Unbounded While Loops
A naive implementation loops indefinitely until a palindrome appears:
```python
def naive_is_lychrel(n):
    # Runs into infinite loops on true Lychrel numbers (e.g. 196, 4994)
    # ...
```

### The 50-Iteration Cutoff Bound
1. Problem specification establishes that every non-Lychrel number below $10\,000$ either becomes a palindrome immediately or within 50 iterations.
2. Capping the reverse-and-add loop at $49$ additions guarantees deterministic $\mathcal{O}(1)$ termination per candidate with zero infinite loops.

---

## 3. Core Intuition & Mathematical Structure

### Reverse-and-Add Trajectories for Example Numbers

| Initial Number $n_0$ | Step 1 ($n_1 = n_0 + \operatorname{rev}(n_0)$) | Step 2 ($n_2 = n_1 + \operatorname{rev}(n_1)$) | Step 3 ($n_3 = n_2 + \operatorname{rev}(n_2)$) | Palindrome Reached? | Lychrel Status |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$47$** | $47 + 74 = \mathbf{121}$ | — | — | Yes (Step 1) | **Not Lychrel** |
| **$349$** | $349 + 943 = 1292$ | $1292 + 2921 = 4213$ | $4213 + 3124 = \mathbf{7337}$ | Yes (Step 3) | **Not Lychrel** |
| **$196$** | $196 + 691 = 887$ | $887 + 788 = 1675$ | $1675 + 5761 = 7436$ | No (after 50 steps) | **Lychrel** |
| **$4994$** | $4994 + 4994 = 9988$ | $9988 + 8899 = 18887$ | $\dots$ | No (after 50 steps) | **Lychrel** |

*(Note: Even though $4994$ is itself already palindromic, the problem specifies that the first addition must be performed before testing for palindromicity).*

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Deterministic Bounded Testing
1. For each integer $n \in [1, 9999]$:
   - Initialize $c = n$.
   - For $\text{step} = 1 \dots 49$:
     - $c \leftarrow c + \operatorname{rev}(c)$.
     - If $\operatorname{str}(c) == \operatorname{str}(c)^R$, return `False`.
   - Return `True` (Lychrel).
2. Count instances where `is_lychrel(n)` is True across all $n < 10\,000$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $47$ and $349$
- $n = 47 \implies 47 + 74 = 121$ (palindrome at step 1) $\implies$ Not Lychrel. Matches problem sample! $\checkmark$
- $n = 349 \implies 349 + 943 = 1292 \implies 1292 + 2921 = 4213 \implies 4213 + 3124 = 7337$ (palindrome at step 3) $\implies$ Not Lychrel. Matches problem sample! $\checkmark$

### Example 2: Target Evaluation for $1 \le n < 10\,000$
- Testing all 9999 integers up to $49$ additions:

$$
N_{\text{Lychrel}} = \mathbf{249}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Helper Function** | `is_lychrel(n)`: runs loop for 49 additions | $\le 49$ steps |
| **Stage 2** | **Palindrome Check** | `s = str(curr); if s == s[::-1]: return False` | $\mathcal{O}(\text{digits})$ |
| **Stage 3** | **Generator Counter** | `sum(1 for i in range(1, 10000) if is_lychrel(i))` | $9999$ numbers |
| **Stage 4** | **Return Value** | Return scalar integer $249$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \cdot K)$ where $N = 10\,000, K = 50$ | $\approx 0.04$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | String buffers $\le 30$ digits |
| **Dynamic Execution** | $100\%$ Inline | Reverse-and-add arithmetic |

### Critical Invariants & Edge Cases Handled:
1. **Initial Palindromes Handled Properly**: Numbers that are already palindromes (e.g. $4994$) must undergo at least one addition before checking palindromicity.
2. **Arbitrary-Precision BigInt Addition**: Python naturally handles intermediate values that grow to dozens of decimal digits without overflow.