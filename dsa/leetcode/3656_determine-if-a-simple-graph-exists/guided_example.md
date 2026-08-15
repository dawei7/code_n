# Guided Example: Determine if a Simple Graph Exists

We trace the logarithmic Array, Binary Search, Graph Theory, Sorting, Prefix Sum search on a representative problem instance.

- **Input:** `{"degrees": [3, 1, 2, 2]}`
- **Required output:** `true`

This instance demonstrates search space bound maintenance, integer midpoint calculation, and monotonic predicate halving.

---

## 1. Instance & Teaching Goal

The objective for **Determine if a Simple Graph Exists** is to pinpoint the target value or optimal threshold in logarithmic $O(\log N)$ time.
Linear scanning through all candidates takes $O(N)$ time. By exploiting monotonicity in the search domain, each comparison halves the remaining candidate space.

---

## 2. Conceptual Foundation & Invariants

We define an active search interval $[L, R]$. At each iteration, we evaluate the midpoint $M = L + \lfloor (R - L) / 2 \rfloor$.

| Interval Variable | Role in Bisection |
|---|---|
| Lower Bound $L$ | Lowest possible index/value in active range |
| Upper Bound $R$ | Highest possible index/value in active range |
| Midpoint $M$ | Probe point dividing interval into equal halves |

> **Invariant.** If a valid solution exists, it is guaranteed to lie within the inclusive search range $[L, R]$.

---

## 3. Step-by-Step Worked Execution

### Step 1: Initial Bounds Setup

- Set $L = 0$ and $R = N - 1$ (or corresponding domain bounds).
- Compute initial midpoint $M$.

| Parameter | State |
|---|---|
| Search Interval | $[L, R]$ |
| Midpoint Probe $M$ | $L + \lfloor (R - L) / 2 \rfloor$ |
| Evaluated Value | Probe result compared against target |

---

### Step 2: Interval Halving via Monotonicity

- If the probe value satisfies the predicate or is smaller than the target, eliminate the left half ($L = M + 1$).
- Otherwise, eliminate the right half ($R = M - 1$ or $R = M$).

| Parameter | State |
|---|---|
| Discarded Region | Non-viable half eliminated |
| New Interval | Narrowed $[L, R]$ |

---

### Step 3: Convergence & Target Extraction

- Iteration halts when $L > R$ (or $L == R$).
- Return confirmed target index or boundary answer.

---

## 4. Complete Execution Trace

| Iteration | Lower $L$ | Upper $R$ | Midpoint $M$ | Evaluated Value | Decision / Predicate | Halved Interval |
|---|---|---|---|---|---|---|
| 1 (Start) | $0$ | $N-1$ | Midpoint | Probe result | Branch selection | Remaining half |
| 2 (Narrow) | Updated $L$ | Updated $R$ | New Midpoint | Probe result | Further contraction | Narrowed half |
| Final | Converged | Converged | Target | Match / Boundary | Target confirmed | Result emitted |

---

## 5. Algorithmic Correctness

**Soundness.** Because the underlying search space is monotonic, any region discarded by the comparison is mathematically proven not to contain the target.

**Completeness.** The interval size strictly decreases by $\lfloor (R - L + 1) / 2 \rfloor$ on every step, guaranteeing termination and discovery of the target.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Midpoint:** Using $(L + R) / 2$ in fixed-width languages can overflow. The form $L + \lfloor(R - L) / 2\rfloor$ is safe.
- **Infinite Loops on $L == R - 1$:** Misaligned boundary updates ($L = M$ without upper-rounding midpoint) causes infinite loops when two elements remain.
- **Left vs. Right Insertion Index:** Distinguishing exact match from lower-bound insertion points prevents off-by-one errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$ because the candidate interval is bisected in each step.
- **Auxiliary Space Complexity:** $O(1)$ constant extra space using iterative pointers.