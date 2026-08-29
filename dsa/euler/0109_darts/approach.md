# Darts - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered $1$ to $20$.
The score of a dart is determined by the number of the region of the board it lands in:
- **Singles ($S1 \dots S20$, $S25$):** $1$ to $20$, and outer bull $25$.
- **Doubles ($D1 \dots D20$, $D25$):** $2, 4 \dots 40$, and inner bull $50$.
- **Trebles ($T1 \dots T20$):** $3, 6 \dots 60$.
- **Miss ($M$):** $0$ points.

A checkout is a sequence of up to 3 darts where the **last dart must land on a double** ($D1 \dots D20$ or $D25$) to finish on exactly the target score.
The order of the first two darts does NOT matter (e.g. $S1 + S2 + D1$ is identical to $S2 + S1 + D1$).

The objective is to find how many **distinct ways there are of checking out with a score of less than 100**:

$$
N_{\text{checkout}} = \left| \left\{ (\{d_1, d_2\}, d_3) \in \mathcal{D}_{\text{all}}^2 \times \mathcal{D}_{\text{double}} \;\middle|\; v(d_1) + v(d_2) + v(d_3) < 100 \right\} \right|
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Ordered Tuple Cartesian Explosion
A naive approach loops over ordered triples $(d_1, d_2, d_3)$ and overcounts transposed pairs $(d_1, d_2)$ and $(d_2, d_1)$:
```python
def naive_darts():
    # Permutes 3-dart tuples overcounting symmetric pairs
    # ...
```

### Unordered First Two Darts Symmetry Breaking
1. There are $63$ possible single dart outcomes in $\mathcal{D}_{\text{all}}$:

$$
\text{Miss } (0) + 20 \text{ Singles} + 20 \text{ Doubles} + 20 \text{ Trebles} + S25 + D25 = 63 \text{ outcomes}
$$

2. There are $21$ double checkout outcomes in $\mathcal{D}_{\text{double}}$:

$$
20 \text{ Doubles } (D1 \dots D20) + D25 = 21 \text{ outcomes}
$$

3. The number of unordered pairs $\{d_1, d_2\}$ with $i \le j$ is:

$$
\frac{63 \times 64}{2} = 2016 \text{ pairs}
$$

4. Total 3-dart checkout combinations to evaluate:

$$
2016 \times 21 = 42\,336 \text{ combinations}
$$

5. Evaluating 42,336 combinations takes $\approx 0.01$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Dartboard Outcome Classification

| Category | Notation | Count | Score Values |
| :---: | :---: | :---: | :--- |
| **Miss** | $M$ | $1$ | $0$ |
| **Singles** | $S1 \dots S20, S25$ | $21$ | $1, 2, \dots, 20, 25$ |
| **Doubles** | $D1 \dots D20, D25$ | $21$ | $2, 4, \dots, 40, 50$ |
| **Trebles** | $T1 \dots T20$ | $20$ | $3, 6, \dots, 60$ |
| **All Possible Darts $\mathcal{D}_{\text{all}}$** | — | **$63$** | Entire target board + Miss |
| **Valid Finish Darts $\mathcal{D}_{\text{double}}$** | — | **$21$** | Doubles and Bullseye only |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Checkout Combination Pipeline
1. Construct array of 63 dart values:

$$
\mathcal{D}_{\text{all}} = [0, S_1 \dots S_{20}, D_1 \dots D_{20}, T_1 \dots T_{20}, S_{25}, D_{25}]
$$

2. Construct array of 21 double values:

$$
\mathcal{D}_{\text{double}} = [D_1 \dots D_{20}, D_{25}]
$$

3. Initialize `checkout_count = 0`.
4. Loop $i = 0 \dots 62$:
   - Loop $j = i \dots 62$:
     - Loop $d_3 \in \mathcal{D}_{\text{double}}$:
       - Total $= v_i + v_j + v_{d3}$.
       - If Total $< 100$: `checkout_count += 1`.
5. Return `checkout_count`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Checkouts for Score 6 (From Problem Description)
- 1 Dart: $D3$.
- 2 Darts: $D1 + D2$, $S2 + D2$, $S4 + D1$.
- 3 Darts: $S1 + S1 + D2$, $S1 + D1 + D1$, $M + S2 + D2$, etc.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for Score $< 100$
- Testing all $42\,336$ unordered checkout combinations:

$$
N_{\text{checkout}} = \mathbf{38\,182}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Board Generation** | Build 63 normal darts and 21 doubles | $\mathcal{O}(1)$ |
| **Stage 2** | **First Dart $d_1$** | For $i \in [0, 62]$ | $63$ choices |
| **Stage 3** | **Second Dart $d_2$**| For $j \in [i, 62]$ (Unordered symmetry) | $2016$ pairs |
| **Stage 4** | **Finish Dart $d_3$**| For $d_3 \in \text{doubles}$ | $21$ choices |
| **Stage 5** | **Score Filter** | If $v_1 + v_2 + v_3 < 100$: count $+1$ | $\mathcal{O}(1)$ |
| **Stage 6** | **Return Total** | Return `checkout_count = 38182` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(|\mathcal{D}_{\text{all}}|^2 \cdot |\mathcal{D}_{\text{double}}|)$ | $\approx 0.01$ seconds ($42\,336$ total checks) |
| **Space Complexity** | $\mathcal{O}(1)$ | Small constant arrays |
| **Dynamic Execution** | $100\%$ Inline | Combinatorial double checkout search |

### Critical Invariants & Edge Cases Handled:
1. **Miss ($0$ points) Representation**: Representing a 1-dart or 2-dart checkout as $(M, M, D)$ or $(d_1, M, D)$ allows a single unified 3-level loop to handle 1-dart, 2-dart, and 3-dart checkouts seamlessly.
2. **Unordered Dart Symmetry**: Iterating $j$ from $i$ to $62$ counts unordered subsets of the first two throws $\{d_1, d_2\}$, preventing identical duplicate checkouts.