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

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of children. The algorithm performs two linear scans across the array, each step taking $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ to store the single candy allocation array $C$ of length $N$.
