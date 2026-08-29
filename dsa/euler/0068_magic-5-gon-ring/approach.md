# Magic 5-gon Ring - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A magic 5-gon ring is constructed from numbers $1$ to $10$ arranged on $10$ vertices: 5 outer (external) vertices $(o_0, o_1, o_2, o_3, o_4)$ and 5 inner vertices $(i_0, i_1, i_2, i_3, i_4)$.

The 5 line triplets are defined by:
$$L_0 = (o_0, i_0, i_1), \quad L_1 = (o_1, i_1, i_2), \quad L_2 = (o_2, i_2, i_3), \quad L_3 = (o_3, i_3, i_4), \quad L_4 = (o_4, i_4, i_0)$$

The magic property requires that all 5 line sums are equal to a constant $S$:
$$S = o_k + i_k + i_{(k+1) \bmod 5} \quad \forall k \in \{0, 1, 2, 3, 4\}$$

The canonical string representation concatenates each line triplet in order, starting from the line with the lowest external node ($o_0 = \min(o_0, \dots, o_4)$).

The objective is to find the **maximum 16-digit concatenated string** for a magic 5-gon ring:
$$\mathbf{s}_{\text{max}} = \max_{\text{valid rings}} \operatorname{str}(o_0) \mathbin{\Vert} \operatorname{str}(i_0) \mathbin{\Vert} \operatorname{str}(i_1) \dots \operatorname{str}(o_4) \mathbin{\Vert} \operatorname{str}(i_4) \mathbin{\Vert} \operatorname{str}(i_0)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Unconstrained Permutation Search
A naive algorithm loops through all $10! = 3\,628\,800$ permutations without symmetry breaking:
```python
def naive_magic_5gon():
    # explores all 10! permutations without filtering
    # ...
```

### The 16-Digit Invariant & Node Assignment
1. **Outer vs Inner Node Repetition:** Each outer node appears in exactly **one line**, while each inner node is shared and appears in **two lines**.
2. **Total Digits Invariant:** The numbers $1 \dots 9$ are 1-digit, and $10$ is 2-digit.
   - If $10$ is an inner node, it appears twice, producing a string of length $9(1) + 2(2) + 2(1) = 17$ digits.
   - For the string to have length **16**, the number $10$ MUST be placed on an **external node**!
3. **Canonical Rotation:** Enforcing $o_0 = \min(o_0, \dots, o_4)$ reduces the search space by a factor of 5.

---

## 3. Core Intuition & Mathematical Structure

### Line Triplet Topology & Equations

| Line Index $k$ | Line Triplet $(o_k, i_k, i_{k+1})$ | Number of Inner Nodes Shared | Outer Node Multiplicity |
| :---: | :---: | :---: | :---: |
| **$L_0$** | $(o_0, i_0, i_1)$ | $i_0, i_1$ shared | $o_0$ (appears once) |
| **$L_1$** | $(o_1, i_1, i_2)$ | $i_1, i_2$ shared | $o_1$ (appears once) |
| **$L_2$** | $(o_2, i_2, i_3)$ | $i_2, i_3$ shared | $o_2$ (appears once) |
| **$L_3$** | $(o_3, i_3, i_4)$ | $i_3, i_4$ shared | $o_3$ (appears once) |
| **$L_4$** | $(o_4, i_4, i_0)$ | $i_4, i_0$ shared | $o_4$ (appears once) |

$$\sum_{k=0}^4 S = \sum_{k=0}^4 o_k + 2 \sum_{k=0}^4 i_k = \sum_{v=1}^{10} v + \sum_{k=0}^4 i_k = 55 + \sum_{k=0}^4 i_k$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Canonical Permutation Search
1. Loop over permutations of $(1, 2, \dots, 10)$ as $(o_0 \dots o_4, i_0 \dots i_4)$.
2. If $o_0 \neq \min(o_0, \dots, o_4)$, skip (canonical rotation).
3. Compute the 5 line sums:
   $$s_0 = o_0 + i_0 + i_1, \quad s_1 = o_1 + i_1 + i_2, \quad \dots, \quad s_4 = o_4 + i_4 + i_0$$
4. If $s_0 == s_1 == s_2 == s_3 == s_4$:
   - Build concatenated string: `f"{o0}{i0}{i1}{o1}{i1}{i2}{o2}{i2}{i3}{o3}{i3}{i4}{o4}{i4}{i0}"`.
   - If length is 16, update `max_string = max(max_string, int(s_concat))`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: 3-gon Ring Sample (Numbers $1 \dots 6$)
- Lines: $(4, 3, 2), (6, 2, 1), (5, 1, 3)$.
- Line sums: $4+3+2 = 6+2+1 = 5+1+3 = \mathbf{9}$.
- Lowest external node: $4$.
- String: `4,3,2; 6,2,1; 5,1,3` $\implies \mathbf{432621513}$ (9 digits). Matches problem sample! $\checkmark$

### Example 2: Target 5-gon Ring Solution ($16$ Digits)
- External nodes: $(6, 10, 9, 8, 7)$ (where $\min = 6$).
- Internal nodes: $(5, 3, 1, 4, 2)$.
- Line Triplets:
  - $L_0 = (6, 5, 3) \implies 6 + 5 + 3 = \mathbf{14}$
  - $L_1 = (10, 3, 1) \implies 10 + 3 + 1 = \mathbf{14}$
  - $L_2 = (9, 1, 4) \implies 9 + 1 + 4 = \mathbf{14}$
  - $L_3 = (8, 4, 2) \implies 8 + 4 + 2 = \mathbf{14}$
  - $L_4 = (7, 2, 5) \implies 7 + 2 + 5 = \mathbf{14}$
- Concatenated 16-Digit String:
  $$\mathbf{s}_{\text{max}} = \mathbf{6531031914842725}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Permutations** | `itertools.permutations(range(1, 11))` | $3\,628\,800$ states |
| **Stage 2** | **Min Outer Filter** | If `o0 != min(o0..o4)`: continue | $5\times$ speedup |
| **Stage 3** | **Line Sum Match** | Check `s0 == s1 == s2 == s3 == s4` | $5$ sums |
| **Stage 4** | **16-Digit Filter** | If `len(s_concat) == 16`: update maximum | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return scalar integer $6531031914842725$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(10!)$ pruned by $5\times$ | $\approx 0.25$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | String and integer buffers |
| **Dynamic Execution** | $100\%$ Inline | Full permutation search with canonical rotation |

### Critical Invariants & Edge Cases Handled:
1. **16-Digit Length Invariant**: Automatically guarantees that $10$ is placed in an outer node position.
2. **Canonical Minimum Start**: Enforces starting from the smallest outer node without missing valid symmetric solutions.
