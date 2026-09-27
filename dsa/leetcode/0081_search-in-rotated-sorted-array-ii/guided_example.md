# Guided Example: Search in Rotated Sorted Array II

We trace the step-by-step rotated binary search with duplicate boundary trimming on representative instances:

- **Input:** $\text{nums} = [2, 5, 6, 0, 0, 1, 2]$, $\text{target} = 0$
- **Required output:** $\text{True}$
- **Degenerate Duplicate Ambiguity:** $\text{nums} = [1, 0, 1, 1, 1]$, $\text{target} = 0 \implies \text{True}$

This instance demonstrates identifying sorted halves in rotated arrays containing duplicate elements, detecting the ambiguous case ($\text{nums}[L] == \text{nums}[M] == \text{nums}[R]$), shrinking boundary pointers ($L{++}, R{--}$), and analyzing worst-case $O(N)$ vs average-case $O(\log N)$ complexity.

---

## 1. Instance & Teaching Goal

An integer array $\text{nums}$ sorted in non-decreasing order is rotated at an unknown pivot index. Given $\text{nums} = [2, 5, 6, 0, 0, 1, 2]$ and a target $0$, return `True` if target exists in $\text{nums}$, or `False` otherwise.

In contrast to LeetCode 33 (where all elements are distinct), the presence of duplicates introduces ambiguity:
For $[1, 0, 1, 1, 1]$, $L = 0, M = 2, R = 4$, so $\text{nums}[L] = \text{nums}[M] = \text{nums}[R] = 1$.
Here, the target $0$ lies in the left half.
However, for $[1, 1, 1, 0, 1]$, the target $0$ lies in the right half despite identical values at $L$, $M$, and $R$.

Because a single comparison cannot determine which half is sorted when $\text{nums}[L] == \text{nums}[M] == \text{nums}[R]$, the algorithm safely contracts both boundaries ($L \leftarrow L + 1, R \leftarrow R - 1$), preserving binary search speed wherever possible.

---

## 2. Conceptual Foundation & Invariants

### 3-Way Half-Sorted Bisection with Duplicate Trimming
At each step, calculate $M = L + \lfloor (R - L) / 2 \rfloor$:
- If $\text{nums}[M] == \text{target}$: return $\text{True}$.

1. **Duplicate Ambiguity ($\text{nums}[L] == \text{nums}[M] == \text{nums}[R]$):**
   Neither the left nor right half is guaranteed monotonic.
   Contract boundaries:
   $$
   L \leftarrow L + 1, \quad R \leftarrow R - 1
   $$
2. **Left Half is Sorted ($\text{nums}[L] \le \text{nums}[M]$):**
   - If $\text{nums}[L] \le \text{target} < \text{nums}[M]$:
     Target must lie within the sorted left half:
     $$
     R \leftarrow M - 1
     $$
   - Else: Target must lie in the right half:
     $$
     L \leftarrow M + 1
     $$
3. **Right Half is Sorted ($\text{nums}[M] \le \text{nums}[R]$):**
   - If $\text{nums}[M] < \text{target} \le \text{nums}[R]$:
     Target must lie within the sorted right half:
     $$
     L \leftarrow M + 1
     $$
   - Else: Target must lie in the left half:
     $$
     R \leftarrow M - 1
     $$

> **Invariant.** If `target` is present in $\text{nums}$, it is guaranteed to lie within $[\text{nums}[L], \dots, \text{nums}[R]]$.

---

## 3. Step-by-Step Worked Execution

### Instance 1: Standard Rotated Search ($[2, 5, 6, 0, 0, 1, 2]$, $\text{target} = 0$)
- **Step 1 ($L = 0, R = 6$):**
  - Midpoint: $M = 0 + \lfloor (6 - 0) / 2 \rfloor = 3$.
  - Probe: $\text{nums}[3] = 0$.
  - Compare: $\text{nums}[3] == \text{target}$ ($0 == 0$).
  - **Immediate Match!** Return $\text{True}$.

---

### Instance 2: Duplicate Ambiguity Resolution ($[1, 0, 1, 1, 1]$, $\text{target} = 0$)
- **Step 1 ($L = 0, R = 4$):**
  - Midpoint: $M = 2$.
  - Values: $\text{nums}[0] = 1$, $\text{nums}[2] = 1$, $\text{nums}[4] = 1$.
  - Ambiguity detected: $\text{nums}[L] == \text{nums}[M] == \text{nums}[R] == 1$.
  - Action: Contract both ends:
    $$
    L \leftarrow 0 + 1 = 1, \quad R \leftarrow 4 - 1 = 3
    $$
  - Active subarray: indices $[1 \dots 3]$, elements $[0, 1, 1]$.
- **Step 2 ($L = 1, R = 3$):**
  - Midpoint: $M = 1 + \lfloor (3 - 1) / 2 \rfloor = 2$.
  - Probe: $\text{nums}[2] = 1 \ne 0$.
  - Boundaries: $\text{nums}[1] = 0$, $\text{nums}[3] = 1$.
  - Left half $[1, 2]$ has values $[0, 1]$. Since $\text{nums}[1] \le \text{nums}[2]$ ($0 \le 1$), left half is sorted.
  - Target containment: $\text{nums}[1] \le 0 < \text{nums}[2]$ ($0 \le 0 < 1$). True!
  - Search left: $R \leftarrow M - 1 = 1$.
- **Step 3 ($L = 1, R = 1$):**
  - Midpoint: $M = 1$.
  - Probe: $\text{nums}[1] = 0$.
  - $\text{nums}[1] == \text{target}$ ($0 == 0$).
  - **Match Found!** Return $\text{True}$.

---

### Instance 3: Degenerate All-Equal Array ($[1, 1, 1, 1, 1]$, $\text{target} = 0$)

When every element of the live window equals every other, the ambiguity test fires on
every iteration and the window shrinks by only two indices at a time. No comparison can
ever certify a sorted half, so the search degenerates to a linear scan that still
terminates correctly:

| Iteration | $L$ | $R$ | $M = L + \lfloor (R - L)/2 \rfloor$ | $(\text{nums}[L], \text{nums}[M], \text{nums}[R])$ | $\text{nums}[M] == 0$? | Classification | Action | Next $[L, R]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|:---:|
| 1 | 0 | 4 | 2 | $(1, 1, 1)$ | $1 \ne 0$ | Ambiguous triplet | $L \leftarrow 1,\ R \leftarrow 3$ | $[1, 3]$ |
| 2 | 1 | 3 | 2 | $(1, 1, 1)$ | $1 \ne 0$ | Ambiguous triplet | $L \leftarrow 2,\ R \leftarrow 2$ | $[2, 2]$ |
| 3 | 2 | 2 | 2 | $(1, 1, 1)$ | $1 \ne 0$ | Ambiguous triplet (single cell) | $L \leftarrow 3,\ R \leftarrow 1$ | $[3, 1]$ empty |

After three probes the window is empty, so the answer is $\text{False}$. A window of $n$
identical values costs $\lceil n/2 \rceil$ iterations, which is the concrete mechanism
behind the linear worst case discussed in Section 6.

---

## 4. Complete Execution Trace

### Ambiguous Duplicate Trace ($[1, 0, 1, 1, 1]$, $\text{target} = 0$)

| Step | Left $L$ | Right $R$ | Mid $M$ | Values $(\text{nums}[L], \text{nums}[M], \text{nums}[R])$ | Classification | Action Taken | Next Range |
|:---:|:---:|:---:|:---:|:---:|:---|:---|:---:|
| 1 | 0 | 4 | 2 | $(1, 1, 1)$ | Ambiguous Triplet | Trim: $L{++}, R{--}$ | $[1, 3]$ |
| 2 | 1 | 3 | 2 | $(0, 1, 1)$ | Left sorted ($0 \le 1$) | Target in left ($0 \le 0 < 1$) | $[1, 1]$ |
| 3 | 1 | 1 | 1 | $(0, 0, 0)$ | Single cell match | **Target == nums[1]** | **Return True** |

### Absent Target Trace ($[2, 5, 6, 0, 0, 1, 2]$, $\text{target} = 3$)
- Step 1: $M = 3 \implies \text{nums}[3] = 0$. Right sorted ($0 \le 2$). Target $3$ not in $[0, 2] \implies R \leftarrow 2$.
- Step 2: $L = 0, R = 2 \implies M = 1, \text{nums}[1] = 5$. Left sorted ($2 \le 5$). Target $3 \in [2, 5) \implies R \leftarrow 0$.
- Step 3: $L = 0, R = 0 \implies M = 0, \text{nums}[0] = 2 \ne 3 \implies L \leftarrow 1$.
- Step 4: $L = 1 > R = 0 \implies$ Halt. Return $\text{False}$.

---

## 5. Algorithmic Correctness

**Soundness.** When $\text{nums}[L] == \text{nums}[M] == \text{nums}[R]$, neither $\text{nums}[L]$ nor $\text{nums}[R]$ can be the target (since $\text{target} \ne \text{nums}[M]$). Discarding $L$ and $R$ preserves all other candidate elements. When one half is proven monotonic, checking interval boundaries guarantees the target is pursued in the correct segment.

**Completeness.** Every iteration either halves the search space via binary search or shrinks it by 2 via duplicate trimming. When $L > R$, the entire array has been examined, and an absent target safely returns $\text{False}$.

---

## 6. Traps This Instance Exposes

- **Worst-Case Linear Degradation:** For arrays where all elements are identical (e.g. $[1, 1, 1, 1, 1]$ with $\text{target} = 0$), $L$ and $R$ increment/decrement one step at a time, degrading runtime to $O(N)$.
- **Strict Inequality on Half-Sorted Check:** Using strictly $<$ vs $\le$ in $\text{nums}[L] \le \text{nums}[M]$ must be coupled with the three-way equality check first, otherwise duplicate prefixes will be misidentified as monotonically increasing.

### Boundary Conditions Exercised by the Authored Instances

| `nums` | `target` | Condition exercised | Result | Why the deciding branch is sound |
|:---|:---:|:---|:---:|:---|
| $[2, 5, 6, 0, 0, 1, 2]$ | 0 | Midpoint lands directly on the target | True | The first probe is $\text{nums}[3] = 0$, so one comparison settles it; no rotation reasoning is needed. |
| $[2, 5, 6, 0, 0, 1, 2]$ | 3 | Range test is necessary but not sufficient | False | At $[L, R] = [0, 2]$ the left half is sorted and $2 \le 3 < 5$ correctly keeps the target inside, yet the final cell is $\text{nums}[0] = 2$, so the value simply does not occur. |
| $[1, 0, 1, 1, 1]$ | 0 | Ambiguous triplet with the target in the left half | True | Trimming to $[1, 3]$ removes only values equal to $\text{nums}[M] \ne \text{target}$; the surviving containment test $0 \le 0 < 1$ then isolates index 1. |
| $[1]$ | 2 | Single-element array | False | The window opens already degenerate at $L = R = M = 0$; the sole value $1$ is not the target, so the window empties and no element is skipped. |
| $[1, 1, 1, 1, 2, 1, 1]$ | 2 | Duplicate blocks hiding the pivot on both sides | True | Two trims advance the window to $[2, 4]$; the only non-duplicate value, $\text{nums}[4] = 2$, survives and becomes the final probe. |

---

## 7. Complexity Derivation

- **Time Complexity:** Average case $O(\log N)$ when duplicates are sparse. Worst case $O(N)$ when all elements are identical.
- **Auxiliary Space Complexity:** $O(1)$ constant memory using two pointer registers ($L$ and $R$).
