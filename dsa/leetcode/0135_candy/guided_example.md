# Guided Example: Candy

We trace the step-by-step bidirectional slope constraint propagation and peak height harmonization on representative child rating arrays:

- **Input:** $\text{ratings} = [1, 0, 2]$
- **Required output:** $5$ (Optimal distribution: $[2, 1, 2]$, total $2 + 1 + 2 = 5$)
- **Asymmetric Peak & Plateau Instance:** $\text{ratings} = [1, 2, 87, 87, 87, 2, 1] \implies 13$ ($[1, 2, 3, 1, 3, 2, 1]$)

This instance demonstrates decomposing bidirectional neighbor constraints into independent left-to-right and right-to-left monotonic passes, resolving peak conflicts via $\max(\text{left}[i], \text{right}[i])$, handling equal-rating plateaus (which do not require strict inequality), and executing in $O(N)$ time with a single allocation pass.

---

## 1. Instance & Teaching Goal

There are $n$ children standing in a line with rating values $\text{ratings} = [1, 0, 2]$.
You must distribute candies according to two rules:
1. Every child must receive at least $1$ candy.
2. Any child with a higher rating than an immediate neighbor must receive strictly more candies than that neighbor.
Find the **minimum total candies** required.

Evaluating constraints for $\text{ratings} = [1, 0, 2]$:
- Child 0 has rating $1$, higher than Child 1 ($0$). Child 0 must have more candies than Child 1: $C_0 > C_1$.
- Child 1 has rating $0$, lower than both neighbors. Child 1 receives the baseline minimum: $C_1 = 1$.
- Child 2 has rating $2$, higher than Child 1 ($0$). Child 2 must have more candies than Child 1: $C_2 > C_1 \implies C_2 \ge 2$.
Combining requirements yields distribution $[2, 1, 2]$, totaling $2 + 1 + 2 = 5$ candies.

A single greedy pass cannot satisfy both neighbors simultaneously because a long descent to the right can force an earlier peak to climb higher than the left pass predicted.
Separating the requirements into two passes—a forward pass ensuring left-neighbor correctness and a backward pass ensuring right-neighbor correctness—harmonizes both constraints via $C[i] = \max(\text{left}[i], \text{right}[i])$ in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### Two-Pass Bidirectional Propagation Protocol
Initialize an array `candies` of length $N$ with all $1$s:
$$
C = [1, 1, \dots, 1]
$$

#### Pass 1: Forward Sweep (Left-Neighbor Condition)
Ensure $R[i] > R[i - 1] \implies C[i] > C[i - 1]$:
For $i$ from $1$ to $N - 1$:
$$
\text{if } \text{ratings}[i] > \text{ratings}[i - 1]: \quad C[i] \leftarrow C[i - 1] + 1
$$
*(If $\text{ratings}[i] \le \text{ratings}[i - 1]$, $C[i]$ remains at $1$, since no obligation to exceed the left neighbor exists)*.

#### Pass 2: Backward Sweep (Right-Neighbor Condition)
Ensure $R[i] > R[i + 1] \implies C[i] > C[i + 1]$:
For $i$ from $N - 2$ down to $0$:
$$
\text{if } \text{ratings}[i] > \text{ratings}[i + 1]: \quad C[i] \leftarrow \max(C[i], \, C[i + 1] + 1)
$$
*(Using $\max(C[i], C[i+1] + 1)$ guarantees that satisfying the right neighbor does not violate the previously established left-neighbor constraint)*.

Total candies needed:
$$
\text{Total} = \sum_{i=0}^{N-1} C[i]
$$

> **Invariant.** After Pass 1, $C[i]$ satisfies all left-neighbor relations. After Pass 2, $C[i]$ satisfies both left- and right-neighbor constraints simultaneously while remaining strictly minimal.

---

## 3. Step-by-Step Worked Execution

We trace the two passes on $\text{ratings} = [1, 0, 2]$ ($N = 3$):

### Initialization
- Start with baseline candy allocation:
  $$
  C = [1, \, 1, \, 1]
  $$

---

### Pass 1: Forward Sweep ($i = 1 \dots 2$)

- **Index $i = 1$ ($R[1] = 0$ vs $R[0] = 1$):**
  - $0 \not> 1$.
  - No left-neighbor constraint. $C[1]$ stays $1$.
  - $C = [1, 1, 1]$.

- **Index $i = 2$ ($R[2] = 2$ vs $R[1] = 0$):**
  - $2 > 0$ (Strictly greater!).
  - Update: $C[2] \leftarrow C[1] + 1 = 1 + 1 = 2$.
  - $C = [1, 1, 2]$.

After Pass 1: $C = [1, 1, 2]$. Left constraints satisfied.

---

### Pass 2: Backward Sweep ($i = 1 \dots 0$)

- **Index $i = 1$ ($R[1] = 0$ vs $R[2] = 2$):**
  - $0 \not> 2$.
  - No right-neighbor constraint. $C[1]$ stays $1$.
  - $C = [1, 1, 2]$.

- **Index $i = 0$ ($R[0] = 1$ vs $R[1] = 0$):**
  - $1 > 0$ (Strictly greater!).
  - Right requirement: $C[1] + 1 = 1 + 1 = 2$.
  - Take maximum: $C[0] \leftarrow \max(C[0], 2) = \max(1, 2) = \mathbf{2}$.
  - $C = [2, 1, 2]$.

---

### Summation
$$
\text{Total} = C[0] + C[1] + C[2] = 2 + 1 + 2 = \mathbf{5}
$$
Final answer: $\mathbf{5}$.

---

## 4. Complete Execution Trace

### State Evolution Table for $[1, 0, 2]$

```text
Ratings:          1       0       2
Initial:         [1]     [1]     [1]
Pass 1 (Left->): [1]     [1]     [2]   (2 > 0 -> 1+1=2)
Pass 2 (<-Right):[2]     [1]     [2]   (1 > 0 -> max(1, 1+1)=2)
Total:            2   +   1   +   2   = 5
```

| Child Index $i$ | Rating $R[i]$ | Initial $C[i]$ | Pass 1 Condition ($R[i] > R[i-1]$) | Pass 1 Value | Pass 2 Condition ($R[i] > R[i+1]$) | Pass 2 Final $C[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | Boundary (no left) | 1 | **Yes ($1 > 0$)** $\implies \max(1, 1+1)$ | **2** |
| 1 | 0 | 1 | No ($0 \le 1$) | 1 | No ($0 \le 2$) | **1** |
| 2 | 2 | 1 | **Yes ($2 > 0$)** $\implies 1 + 1$ | 2 | Boundary (no right) | **2** |
| **Sum** | - | - | - | - | - | **5 (Result)** |

### Complex Case: Peak Harmonization on $[1, 2, 87, 87, 87, 2, 1]$
- Pass 1 (Left $\to$ Right): $[1, 2, 3, 1, 1, 1, 1]$ (Plateau resets $87 \to 87$ to $1$).
- Pass 2 (Right $\to$ Left): $[1, 2, 3, 1, 3, 2, 1]$ (Right slope $87 > 2 > 1$ elevates 4th index to $3$).
- Sum $= 1 + 2 + 3 + 1 + 3 + 2 + 1 = \mathbf{13}$.

The two prose arrays above hide where each value comes from, so the same instance is expanded row by row. The binding column is the pass that actually sets the final value, and the last row shows why neither pass may be used alone:

| Child $i$ | $R[i]$ | Forward rule applied | $\text{left}[i]$ | Backward rule applied | $\text{right}[i]$ | $C[i] = \max(\text{left}[i], \text{right}[i])$ | Binding pass |
|:---:|:---:|:---|:---:|:---|:---:|:---:|:---|
| 0 | 1 | left boundary, no comparison | 1 | $R[0] = 1 \le R[1] = 2$, nothing forced | 1 | 1 | neither |
| 1 | 2 | $R[1] = 2 > R[0] = 1 \implies 1 + 1$ | 2 | $2 \le 87$ | 1 | 2 | forward |
| 2 | 87 | $87 > 2 \implies 2 + 1$ | 3 | $87 \le 87$, a plateau forces nothing | 1 | 3 | forward |
| 3 | 87 | $87 \le 87$, plateau restarts at the baseline | 1 | $87 \le 87$ | 1 | 1 | neither |
| 4 | 87 | $87 \le 87$ | 1 | $87 > 2 \implies 2 + 1$ | 3 | 3 | backward |
| 5 | 2 | $2 \le 87$ | 1 | $2 > 1 \implies 1 + 1$ | 2 | 2 | backward |
| 6 | 1 | $1 \le 2$ | 1 | right boundary, no comparison | 1 | 1 | neither |
| **Sum** | - | - | **10** | - | **10** | **13** | - |

Neither column sums to the answer: $\sum \text{left}[i] = 10$ and $\sum \text{right}[i] = 10$, while the coordinate-wise maximum costs $13$. The two partial arrays are not merely smaller, they are invalid — the forward array gives child 4 only $1$ candy although its right neighbor has rating $2$, and the backward array gives child 1 only $1$ candy although its left neighbor has rating $1$ and child 1 is rated higher.

---

## 5. Algorithmic Correctness

**Soundness.** A distribution is valid if and only if for every $i$:
1. $C[i] \ge 1$
2. $R[i] > R[i-1] \implies C[i] \ge C[i-1] + 1$
3. $R[i] > R[i+1] \implies C[i] \ge C[i+1] + 1$
Because Pass 1 enforces condition 2, and Pass 2 enforces condition 3 via $\max(C[i], C[i+1]+1)$ without ever decreasing $C[i]$, both conditions are simultaneously satisfied upon completion.

**Completeness.** Since $C[i]$ only increases when forced by a strictly larger neighbor, no child receives more candies than strictly necessary, proving that the sum $\sum C[i]$ is minimal.

---

## 6. Traps This Instance Exposes

- **Equal Ratings (Plateaus Do Not Require Inequality):** If two adjacent children have identical ratings ($R[i] == R[i-1]$), neither is required to have more candies than the other! Setting $C[i] = C[i-1]$ would waste candies; the rules permit a child on an equal plateau to receive $1$ candy if its other neighbor allows.
- **Overwriting Instead of Max in Pass 2:** Setting $C[i] = C[i+1] + 1$ directly during Pass 2 can destroy a larger value established during Pass 1! Using $\max(C[i], C[i+1] + 1)$ is essential to preserve the taller slope.
- **Single Child:** If $N = 1$, neither loop runs, returning $1$.

The authored cases of this package exercise each of those traps, and the intermediate arrays below are what the two sweeps must produce before the maximum is taken:

| Authored case | $\text{ratings}$ | $\text{left}[i]$ | $\text{right}[i]$ | $C[i]$ | Total | Boundary exercised |
|:---|:---|:---|:---|:---|:---:|:---|
| `sample-1` | $[1, 0, 2]$ | $[1, 1, 2]$ | $[2, 1, 1]$ | $[2, 1, 2]$ | 5 | A valley at index 1 keeps the baseline while both neighbors are raised |
| `sample-2` | $[1, 2, 2]$ | $[1, 2, 1]$ | $[1, 1, 1]$ | $[1, 2, 1]$ | 4 | An equal-rating plateau at indices 1 and 2 forces no inequality, so the trailing child stays at 1 |
| `trial-single-child` | $[9]$ | $[1]$ | $[1]$ | $[1]$ | 1 | Both sweeps are empty; the baseline already satisfies every constraint |
| `trial-long-slope` | $[1, 3, 4, 5, 2]$ | $[1, 2, 3, 4, 1]$ | $[1, 1, 1, 2, 1]$ | $[1, 2, 3, 4, 1]$ | 11 | A four-step ascent is preserved intact, and the drop at index 4 is absorbed without raising the peak |

The `trial-long-slope` row is the one that punishes a direct overwrite in the backward sweep: at index 3 the backward requirement is only $2$, and assigning that value outright would erase the $4$ established by the ascending run.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of children. The algorithm performs two linear scans across the array, each step taking $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ to store the single candy allocation array $C$ of length $N$.

The linear bound does not depend on the direction of the sweeps, only on never re-examining an index more than a constant number of times:

| Strategy | How a violation is repaired | Time | Auxiliary space | Behavior on `[1, 2, 87, 87, 87, 2, 1]` |
|:---|:---|:---:|:---:|:---|
| Two sweeps into two arrays, then coordinate-wise maximum | Each index is raised once from the left and once from the right | $O(N)$ | $O(N)$ | Produces $[1, 2, 3, 1, 3, 2, 1]$ for a total of 13 |
| Two sweeps over one array | The backward sweep applies $\max(C[i], C[i+1] + 1)$ in place | $O(N)$ | $O(N)$ | Same distribution; the maximum is what protects the peak at index 2 |
| Single forward sweep with retroactive repairs | On a descent, walk back and raise every earlier child until the slope is satisfied again | $O(N^2)$ | $O(N)$ | The plateau of three 87s is visited repeatedly, and the long descent in `trial-long-slope` re-raises four indices on every fix |
| Relax all violated pairs repeatedly until stable | Sweep the whole array and repeat while any pair is violated | $O(N^2)$ | $O(N)$ | Converges to the same 13, but only after the right-hand slope has propagated leftwards across the plateau |

The first two rows are the same algorithm with one fewer array. The last two are correct but quadratic, because a single monotone run of length $k$ can force up to $k$ repairs per element instead of one.

---
