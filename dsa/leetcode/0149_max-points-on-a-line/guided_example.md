# Guided Example: Max Points on a Line

We trace the step-by-step slope frequency hashing and coprime fraction reduction on representative 2D coordinate plane instances:

- **Input:** $\text{points} = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]$
- **Required output:** $4$ (Collinear line $y = -x + 5$ connects $4$ points: $[1, 4], [2, 3], [3, 2], [4, 1]$)
- **Base Collinear Instance:** $\text{points} = [[1, 1], [2, 2], [3, 3]] \implies 3$

This instance demonstrates anchor-based slope grouping, eliminating floating-point precision hazards via reduced coprime integer pairs $(\Delta y / \gcd, \Delta x / \gcd)$, handling vertical and horizontal lines uniformly, and achieving optimal $O(N^2)$ time and $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given $n = 6$ points on a 2D Cartesian plane:
$$
\text{points} = [P_0(1, 1), \, P_1(3, 2), \, P_2(5, 3), \, P_3(4, 1), \, P_4(2, 3), \, P_5(1, 4)]
$$
Find the maximum number of points that lie on the same straight line.

In this instance:
- Points $P_5(1, 4), P_4(2, 3), P_1(3, 2),$ and $P_3(4, 1)$ all lie on the straight line $x + y = 5$ (slope $m = -1$).
- No line contains $5$ or more points.
The maximum points collinear on any straight line is $4$.

A naive brute-force checks all $\binom{N}{3}$ triplets, resulting in $O(N^3)$ runtime.
By selecting each point $P_i$ as an **anchor** in turn, all lines passing through $P_i$ are partitioned into equivalence classes based on their slope $m$.
Using a hash map to tally slope occurrences from $P_i$ identifies the maximum collinear cluster through $P_i$ in $O(N)$ operations, lowering total runtime to $O(N^2)$.

---

## 2. Conceptual Foundation & Invariants

### Exact Slope Representation via Coprime Reduction
Computing slope as a float $m = \frac{\Delta y}{\Delta x}$ introduces IEEE-754 precision issues (e.g. $1/3 \ne 0.3333333333333333$) and division-by-zero on vertical lines ($\Delta x = 0$).
To achieve exact, collision-free hashing, represent each slope as a canonical reduced pair of coprime integers:
$$
g = \gcd(|\Delta x|, \, |\Delta y|)
$$
$$
dx = \frac{\Delta x}{g}, \quad dy = \frac{\Delta y}{g}
$$

### Canonical Sign Normalization Rules
1. **Vertical Lines ($\Delta x = 0$):** Canonical key is $(0, 1)$.
2. **Horizontal Lines ($\Delta y = 0$):** Canonical key is $(1, 0)$.
3. **General Slopes:** Ensure the denominator $dx > 0$. If $dx < 0$, invert both signs:
   $$
   dx \leftarrow -dx, \quad dy \leftarrow -dy
   $$
Canonical slope key: $(dx, dy)$.

The four normalization situations, each instantiated with a pair that actually occurs in this input, show why the canonical key and not the raw difference must be hashed:

| Geometry | Pair from this instance | Raw $(\Delta x, \Delta y)$ | What the raw measure gets wrong | Canonical key |
|:---|:---|:---:|:---|:---:|
| Vertical | $P_0(1, 1) \to P_5(1, 4)$ | $(0, 3)$ | A float slope is undefined because the division by $\Delta x = 0$ has no value | $(0, 1)$ |
| Horizontal | $P_0(1, 1) \to P_3(4, 1)$ | $(3, 0)$ | Slope $0$ collapses every horizontal direction into one number and still needs a separate sentinel from the vertical case | $(1, 0)$ |
| Reducible fraction | $P_0(1, 1) \to P_2(5, 3)$ | $(4, 2)$ | Unreduced, $(4, 2)$ and $(2, 1)$ describe the same slope but land in different buckets | $(2, 1)$ |
| Negative denominator | $P_4(2, 3) \to P_5(1, 4)$ | $(-1, 1)$ | $(-1, 1)$ and $(1, -1)$ are one line, yet they are two distinct tuples | $(1, -1)$ |
| Reduction and sign together | $P_1(3, 2) \to P_5(1, 4)$ | $(-2, 2)$ | Dividing by $g = 2$ yields $(-1, 1)$, which is still on the wrong side of the denominator rule | $(1, -1)$ |

### Algorithm Protocol
If $N \le 2$, return $N$.
Initialize $\text{max\_pts} = 2$.
For $i$ from $0$ to $N - 1$:
- Initialize `slopes = defaultdict(int)`.
- For $j$ from $i + 1$ to $N - 1$:
  - Compute canonical slope $(dx, dy)$ between $P_i$ and $P_j$.
  - $\text{slopes}[(dx, dy)] \leftarrow \text{slopes}[(dx, dy)] + 1$.
- Local max through anchor $P_i$ is $1 + \max(\text{slopes.values}())$ (the $+1$ accounts for anchor $P_i$ itself).
- $\text{max\_pts} \leftarrow \max(\text{max\_pts}, \, \text{local\_max})$.

> **Invariant.** For an anchor point $P_i$, two points $P_j$ and $P_k$ have identical canonical slope keys if and only if $P_i, P_j,$ and $P_k$ are collinear.

---

## 3. Step-by-Step Worked Execution

We trace the slope counts when anchor is selected as $P_4(2, 3)$:
Candidate points to compare with $P_4(2, 3)$:

### 1. Vector to $P_5(1, 4)$:
- $\Delta x = 1 - 2 = -1, \quad \Delta y = 4 - 3 = +1$.
- $g = \gcd(1, 1) = 1$.
- Normalize sign ($dx < 0 \implies$ negate both):
  $$
  dx = -(-1) = 1, \quad dy = -(1) = -1
  $$
- Key: $(1, -1)$.
- Increment: $\text{slopes}[(1, -1)] = 1$.

---

### 2. Vector to $P_1(3, 2)$:
- $\Delta x = 3 - 2 = +1, \quad \Delta y = 2 - 3 = -1$.
- $g = \gcd(1, 1) = 1$.
- Denominator $dx = 1 > 0$ already.
- Key: $(1, -1)$.
- Increment: $\text{slopes}[(1, -1)] = 1 + 1 = 2$.

---

### 3. Vector to $P_3(4, 1)$:
- $\Delta x = 4 - 2 = +2, \quad \Delta y = 1 - 3 = -2$.
- $g = \gcd(2, 2) = 2$.
- Reduce by $g$:
  $$
  dx = \frac{2}{2} = 1, \quad dy = \frac{-2}{2} = -1
  $$
- Key: $(1, -1)$.
- Increment: $\text{slopes}[(1, -1)] = 2 + 1 = 3$.

---

### 4. Vector to $P_0(1, 1)$:
- $\Delta x = 1 - 2 = -1, \quad \Delta y = 1 - 3 = -2$.
- Normalize: $dx = 1, dy = 2$. Key: $(1, 2)$.
- Increment: $\text{slopes}[(1, 2)] = 1$.

---

### 5. Vector to $P_2(5, 3)$:
- $\Delta x = 5 - 2 = +3, \quad \Delta y = 3 - 3 = 0$ (Horizontal).
- Canonical key: $(1, 0)$.
- Increment: $\text{slopes}[(1, 0)] = 1$.

---

### Anchor Summary for $P_4(2, 3)$:
- Hash Map: `{(1, -1): 3, (1, 2): 1, (1, 0): 1}`.
- Max collinear points sharing slope $(1, -1)$:
  $$
  \text{Count} = 1 (\text{anchor } P_4) + 3 (\text{neighbors } P_5, P_1, P_3) = \mathbf{4}
  $$
- Update: $\text{max\_pts} = \max(2, 4) = \mathbf{4}$.

Global maximum collinear points: $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
Points: P0(1,1), P1(3,2), P2(5,3), P3(4,1), P4(2,3), P5(1,4)

Anchor P4(2,3):
  -> P5(1,4): dx=-1, dy= 1 -> reduced: (1, -1)   count: 1
  -> P1(3,2): dx= 1, dy=-1 -> reduced: (1, -1)   count: 2
  -> P3(4,1): dx= 2, dy=-2 -> reduced: (1, -1)   count: 3
  -> P0(1,1): dx=-1, dy=-2 -> reduced: (1,  2)   count: 1
  -> P2(5,3): dx= 3, dy= 0 -> reduced: (1,  0)   count: 1

Max for P4: 1 (anchor) + 3 = 4 points collinear on line y = -x + 5
```

| Anchor Point $P_i$ | Target Point $P_j$ | $\Delta x, \Delta y$ | $\gcd$ | Reduced Key $(dx, dy)$ | Slope Count in Map | Total Collinear ($1 + \text{count}$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $P_4(2, 3)$ | $P_5(1, 4)$ | $(-1, 1)$ | 1 | $(1, -1)$ | 1 | 2 |
| $P_4(2, 3)$ | $P_1(3, 2)$ | $(1, -1)$ | 1 | $(1, -1)$ | 2 | 3 |
| **$P_4(2, 3)$** | **$P_3(4, 1)$** | **$(2, -2)$** | **2** | **$(1, -1)$** | **3** | **4 (Global Max)** |
| $P_4(2, 3)$ | $P_0(1, 1)$ | $(-1, -2)$ | 1 | $(1, 2)$ | 1 | 2 |
| $P_4(2, 3)$ | $P_2(5, 3)$ | $(3, 0)$ | 3 | $(1, 0)$ | 1 | 2 |

Sweeping every anchor settles maximality rather than assuming it. Any line carrying $5$ points would have to surface as a largest class of size $4$ under the lowest-indexed point on that line, so it is enough to list each anchor's tally:

| Anchor $P_i$ | Slope keys tallied as key and count | Largest class | Local maximum $1 + \text{count}$ | Global $\text{max\_pts}$ afterwards |
|:---:|:---|:---:|:---:|:---:|
| $P_0(1, 1)$ | $(2, 1)$ twice, $(1, 0)$ once, $(1, 2)$ once, $(0, 1)$ once | $(2, 1)$ with $2$ | $1 + 2 = 3$ | $3$ |
| $P_1(3, 2)$ | $(2, 1)$ once, $(1, -1)$ three times | $(1, -1)$ with $3$ | $1 + 3 = 4$ | $4$ |
| $P_2(5, 3)$ | $(1, 2)$ once, $(1, 0)$ once, $(4, -1)$ once | a three-way tie at $1$ | $1 + 1 = 2$ | $4$ |
| $P_3(4, 1)$ | $(1, -1)$ twice | $(1, -1)$ with $2$ | $1 + 2 = 3$ | $4$ |
| $P_4(2, 3)$ | $(1, -1)$ once, from $P_5$ alone, because $P_0$ through $P_3$ all have lower indices and are no longer candidates | $(1, -1)$ with $1$ | $1 + 1 = 2$ | $4$ |
| $P_5(1, 4)$ | no candidate satisfies $j > 5$, so nothing enters the map | empty map | $1$, the anchor alone | $4$ |

Three facts fall out of the sweep. The protocol of Section 2, which only pairs an anchor with later points, meets the line $x + y = 5$ at $P_1$, its lowest-indexed member, where the slope to $P_3$, $P_4$, and $P_5$ all reduce to $(1, -1)$ and the class reaches $3$. The Section 3 walkthrough reached the same four points from $P_4$ because it compared $P_4$ against *every* other point instead of only later ones; that variant is equally sound, since the completeness argument only requires the maximal line to be found at *some* anchor, and both variants agree on the value $4$. No anchor reaches $5$, so no line carries five points. And the final anchor has no partner at all, which is why an implementation must tolerate an empty tally instead of taking a maximum over it.

---

## 5. Algorithmic Correctness

**Soundness.** Three points $A, B, C$ are collinear if and only if the slope between $A$ and $B$ equals the slope between $A$ and $C$. By reducing fraction $(dx, dy)$ by $\gcd(|dx|, |dy|)$ and enforcing $dx > 0$, every geometric line through anchor $A$ maps to a unique hash key. No distinct lines can produce identical keys.

**Completeness.** Every pair of points $(i, j)$ with $i < j$ is evaluated. For any maximal set of collinear points $S$, choosing the point in $S$ with the smallest index as anchor will group all other $|S|-1$ points under the exact same slope key.

---

## 6. Traps This Instance Exposes

- **Floating-Point Imprecision:** Using `float(dy) / dx` causes distinct lines with slightly different slopes to collide, or identical slopes to map to different hash buckets due to rounding (e.g. `1/3` vs `2/6`). Using coprime tuples `(dx, dy)` guarantees exact integer equality.
- **Negative Denominator Alignment:** Slope $-1/2$ and $1/(-2)$ represent the same line. Without normalizing $dx > 0$, they would generate keys $(2, -1)$ and $(-2, 1)$, failing to group together!
- **Small Inputs ($N \le 2$):** Any 1 or 2 points trivially lie on a straight line. Returning $N$ directly avoids empty hash map exceptions.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the number of points. There are $N$ choices for anchor point $P_i$. For each anchor, we examine $N - 1 - i$ other points. Computing $\gcd(dx, dy)$ takes logarithmic time in coordinate magnitude ($O(\log(\max |X|, |Y|))$), which is $O(1)$ for 32-bit integers. Total runtime is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store at most $N$ slope keys in the hash map per anchor.
