# Guided Example: Wiggle Sort

We trace the step-by-step single-pass greedy adjacent swap protocol, alternating parity inequality verification, and inductive preservation proof on representative integer arrays:

- **Input:** $\text{nums} = [3, 5, 2, 1, 6, 4]$
- **Required output:** $[3, 5, 1, 6, 2, 4]$ (Satisfies $3 \le 5 \ge 1 \le 6 \ge 2 \le 4$)
- **Already Wiggled Array:** $\text{nums} = [1, 5, 2, 6] \implies [1, 5, 2, 6]$ (Zero swaps executed)
- **Identical Elements Instance:** $\text{nums} = [6, 6, 6, 6] \implies [6, 6, 6, 6]$ (Non-strict $\le$ and $\ge$ trivially satisfied)
- **Two Elements Minimal Pair:** $\text{nums} = [5, 2] \implies [2, 5]$ (Swapped to satisfy $\text{nums}[0] \le \text{nums}[1]$)

This instance demonstrates linear-time in-place greedy rearrangement, mathematically proves why swapping adjacent elements at index $i$ preserves the previously satisfied inequality at $i - 1$, avoids unnecessary $O(N \log N)$ sorting, and operates in strictly $O(N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [3, 5, 2, 1, 6, 4]$, reorder it in-place such that:
$$
\text{nums}[0] \le \text{nums}[1] \ge \text{nums}[2] \le \text{nums}[3] \ge \text{nums}[4] \le \dots
$$
Alternating peaks (high points at odd indices) and valleys (low points at even indices).

```text
Wiggle condition:
Index:     0    1    2    3    4    5
Relation:  nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] <= nums[5]
Values:       3    <=    5    >=    1    <=    6    >=    2    <=    4
```

### The In-Place Greedy Principle
Sorting the array takes $O(N \log N)$ time and sorting followed by pairing odd/even indices works, but is suboptimal.
We can satisfy the condition in a single $O(N)$ linear pass:
At each index $i$, if the required relationship between $\text{nums}[i]$ and $\text{nums}[i + 1]$ is violated, simply **swap them**.
Crucially, swapping $\text{nums}[i]$ and $\text{nums}[i + 1]$ **never invalidates** the previous relation between $\text{nums}[i - 1]$ and $\text{nums}[i]$!

---

## 2. Conceptual Foundation & Invariants

### Alternating Parity Rules
For index $i \in [0, N - 2]$:
1. **If $i$ is even ($0, 2, 4, \dots$):**
   Requirement: $\text{nums}[i] \le \text{nums}[i + 1]$.
   If $\text{nums}[i] > \text{nums}[i + 1]$:
   Swap $\text{nums}[i]$ and $\text{nums}[i + 1]$.
2. **If $i$ is odd ($1, 3, 5, \dots$):**
   Requirement: $\text{nums}[i] \ge \text{nums}[i + 1]$.
   If $\text{nums}[i] < \text{nums}[i + 1]$:
   Swap $\text{nums}[i]$ and $\text{nums}[i + 1]$.

### Proof of Inductive Preservation
Suppose we are at an odd index $i$, and we already know $\text{nums}[i - 1] \le \text{nums}[i]$ from the previous step.
Now, suppose a violation occurs at index $i$:
$$
\text{nums}[i] < \text{nums}[i + 1]
$$
We swap $\text{nums}[i]$ and $\text{nums}[i + 1]$.
- After the swap, the new value at index $i$ is $\text{nums}_{\text{new}}[i] = \text{nums}_{\text{old}}[i + 1]$.
- Since $\text{nums}_{\text{old}}[i + 1] > \text{nums}_{\text{old}}[i] \ge \text{nums}[i - 1]$, we have:
  $$
  \text{nums}_{\text{new}}[i] > \text{nums}[i - 1]
  $$
The previous inequality $\text{nums}[i - 1] \le \text{nums}[i]$ **remains strictly preserved**!
Symmetrically, if $i$ is even, swapping preserves the preceding inequality. Thus, no backtracking is ever needed.

> **Invariant.** After processing index $i$, the entire prefix $\text{nums}[0 \dots i + 1]$ forms a valid wiggle sequence.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [3, 5, 2, 1, 6, 4]$ ($N = 6$):

---

### Step 1 ($i = 0$, Even Index $\implies$ Requires $\le$)
- Pair evaluated: $\text{nums}[0] = 3, \quad \text{nums}[1] = 5$.
- Condition: $3 \le 5$ (**True**).
- Action: No swap needed.
- Array state: `[3, 5, 2, 1, 6, 4]`.

---

### Step 2 ($i = 1$, Odd Index $\implies$ Requires $\ge$)
- Pair evaluated: $\text{nums}[1] = 5, \quad \text{nums}[2] = 2$.
- Condition: $5 \ge 2$ (**True**).
- Action: No swap needed.
- Array state: `[3, 5, 2, 1, 6, 4]`.

---

### Step 3 ($i = 2$, Even Index $\implies$ Requires $\le$)
- Pair evaluated: $\text{nums}[2] = 2, \quad \text{nums}[3] = 1$.
- Condition: $2 \le 1$ (**False; Violation!** $2 > 1$).
- Action: **Swap $\text{nums}[2]$ and $\text{nums}[3]$**.
- Array state: `[3, 5, 1, 2, 6, 4]`.
- Check preservation: $5 \ge 1$ still holds at index $1$!

---

### Step 4 ($i = 3$, Odd Index $\implies$ Requires $\ge$)
- Pair evaluated: $\text{nums}[3] = 2, \quad \text{nums}[4] = 6$.
- Condition: $2 \ge 6$ (**False; Violation!** $2 < 6$).
- Action: **Swap $\text{nums}[3]$ and $\text{nums}[4]$**.
- Array state: `[3, 5, 1, 6, 2, 4]`.
- Check preservation: $1 \le 6$ still holds at index $2$!

---

### Step 5 ($i = 4$, Even Index $\implies$ Requires $\le$)
- Pair evaluated: $\text{nums}[4] = 2, \quad \text{nums}[5] = 4$.
- Condition: $2 \le 4$ (**True**).
- Action: No swap needed.
- Array state: `[3, 5, 1, 6, 2, 4]`.

---

### Final Validation
All pairs satisfy:
$$
3 \le 5 \ge 1 \le 6 \ge 2 \le 4
$$
Final array:
$$
\mathbf{[3, 5, 1, 6, 2, 4]}
$$

---

### Contrast Trace: A Fully Descending Array

The traced instance repairs two different parities once each, which can hide the
fact that a violation at index $i$ always leaves the *previous* pair repaired. A
strictly descending array makes that preservation visible, because every repair
lands on an even index and each new value is placed below the peak that was
already settled.

| Step $i$ | Parity | Elements Compared | Status | Action | Array After Step | Relation at $i - 1$ After the Step |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 | Even | $6 \le 5$ | Violated | Swap | `[5, 6, 4, 3, 2, 1]` | No earlier pair exists |
| 1 | Odd | $6 \ge 4$ | Satisfied | None | `[5, 6, 4, 3, 2, 1]` | $5 \le 6$ still holds |
| 2 | Even | $4 \le 3$ | Violated | Swap | `[5, 6, 3, 4, 2, 1]` | $6 \ge 3$ still holds: the smaller value $3$ lands at index 2 while index 1 keeps $6$ |
| 3 | Odd | $4 \ge 2$ | Satisfied | None | `[5, 6, 3, 4, 2, 1]` | $3 \le 4$ still holds |
| 4 | Even | $2 \le 1$ | Violated | Swap | `[5, 6, 3, 4, 1, 2]` | $4 \ge 1$ still holds |
| End | — | — | — | — | `[5, 6, 3, 4, 1, 2]` | Full sequence $5 \le 6 \ge 3 \le 4 \ge 1 \le 2$ |

Every repair moved the *smaller* of the two values into the even index, which is
exactly the shape a valley must have, and the value it displaced into the odd
index was necessarily at least as large as the settled peak to its left. That is
the inductive preservation argument in concrete numbers: three swaps, no
backtracking, and each completed prefix stays valid forever.

---

## 4. Complete Execution Trace

```text
nums = [3, 5, 2, 1, 6, 4]

i = 0 (even): 3 <= 5 -> OK
i = 1 (odd):  5 >= 2 -> OK
i = 2 (even): 2 <= 1 -> Violation! Swap(2, 1) -> [3, 5, 1, 2, 6, 4]
i = 3 (odd):  2 >= 6 -> Violation! Swap(2, 6) -> [3, 5, 1, 6, 2, 4]
i = 4 (even): 2 <= 4 -> OK

Result: [3, 5, 1, 6, 2, 4]
```

| Step $i$ | Parity | Required Relation | Elements Compared | Status | Action Taken | Array State After Step |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | Even | $\text{nums}[0] \le \text{nums}[1]$ | $3 \le 5$ | Satisfied | None | `[3, 5, 2, 1, 6, 4]` |
| 1 | Odd | $\text{nums}[1] \ge \text{nums}[2]$ | $5 \ge 2$ | Satisfied | None | `[3, 5, 2, 1, 6, 4]` |
| **2** | **Even** | $\text{nums}[2] \le \text{nums}[3]$ | **$2 \le 1$** | **Violated** | **Swap(2, 1)** | `[3, 5, 1, 2, 6, 4]` |
| **3** | **Odd** | $\text{nums}[3] \ge \text{nums}[4]$ | **$2 \ge 6$** | **Violated** | **Swap(2, 6)** | `[3, 5, 1, 6, 2, 4]` |
| 4 | Even | $\text{nums}[4] \le \text{nums}[5]$ | $2 \le 4$ | Satisfied | None | `[3, 5, 1, 6, 2, 4]` |
| **End** | - | - | - | - | - | **`[3, 5, 1, 6, 2, 4]` (Wiggled)** |

### Boundary Census Across Input Shapes

The single pass is uniform, but the number and parity of its repairs depend on
the input's shape. Sorted indices below follow the same convention as the trace
table: a position $i$ means the pair $(\text{nums}[i], \text{nums}[i + 1])$.

| Input | Length | Indices repaired | Swaps | Result | What this shape proves |
|:---|:---:|:---:|:---:|:---|:---|
| `[7]` | 1 | none | 0 | `[7]` | With no pair to inspect the loop body never runs; the array is trivially wiggled |
| `[10000, 0]` | 2 | $0$ | 1 | `[0, 10000]` | The shortest real repair: an even index holding the larger value must be swapped |
| `[7, 7, 7, 7, 7]` | 5 | none | 0 | `[7, 7, 7, 7, 7]` | Equal neighbors satisfy both $\le$ and $\ge$, so duplicates alone never force a swap |
| `[1, 5, 2, 6]` | 4 | none | 0 | `[1, 5, 2, 6]` | An input that is already wiggled costs one comparison per pair and zero writes |
| `[3, 5, 2, 1, 6, 4]` | 6 | $2, 3$ | 2 | `[3, 5, 1, 6, 2, 4]` | Repairs at both parities, which is why preservation must be argued for each of them |
| `[6, 5, 4, 3, 2, 1]` | 6 | $0, 2, 4$ | 3 | `[5, 6, 3, 4, 1, 2]` | Every even index violates, so the pass performs one repair per pair |
| `[1, 2, 3, 4, 5, 6]` | 6 | $1, 3$ | 2 | `[1, 3, 2, 5, 4, 6]` | The mirror image: only the odd indices violate, and the first pair is already correct |
| `[2, 1, 1, 2, 2, 1]` | 6 | $0, 4$ | 2 | `[1, 2, 1, 2, 1, 2]` | Index 3 is left alone because $2 \ge 2$ holds with equality, so non-strict comparison saves a swap |
| `[10000, 0, 10000, 0, 10000, 0, 10000]` | 7 | $0, 2, 4$ | 3 | `[0, 10000, 0, 10000, 0, 10000, 10000]` | Odd length: the last pair is settled by the odd-index rule, and the final two equal values need no repair |

Notice that the swap count follows the *order* of the input rather than its
length: the descending and alternating arrays need one repair per pair, while an
already wiggled array needs none. The pass never revisits an index, which is
precisely why the total work stays linear even in the worst shapes above.

---

## 5. Algorithmic Correctness

**Soundness.** Every adjacent pair $(i, i + 1)$ is explicitly inspected. If the required parity relation is violated, the two elements are swapped, placing the appropriate relative magnitudes at both indices.

**Completeness.** By the inductive preservation proof, swapping $\text{nums}[i]$ and $\text{nums}[i + 1]$ cannot violate the previously settled inequality between $\text{nums}[i - 1]$ and $\text{nums}[i]$. Therefore, once the loop advances past index $i$, all earlier inequalities remain valid, guaranteeing the whole array is properly wiggled upon completion.

---

## 6. Traps This Instance Exposes

- **Sorting Overhead ($O(N \log N)$):** Sorting the entire array and then interweaving elements takes $O(N \log N)$ time. The single-pass greedy swap method runs in strictly $O(N)$ time.
- **Strict Inequalities vs Non-Strict:** Wiggle Sort I uses $\le$ and $\ge$, which makes the greedy local swap algorithm complete and universally applicable. In contrast, Wiggle Sort II (LeetCode 324) requires strict inequalities ($<$ and $>$) and permits duplicates, necessitating virtual index mapping around the median.
- **Off-by-One Loop Boundary:** The loop must iterate up to index $N - 2$ (so the comparison `nums[i + 1]` stays within bounds).

### Strategy Comparison on `[3, 5, 2, 1, 6, 4]`

All four rows below produce a legal wiggle ordering except the third, which is the
tempting simplification that fails. Comparing them on one instance keeps the
tradeoff concrete rather than asymptotic.

| Strategy | Mechanism | Result on this instance | Time | Auxiliary space | Outcome |
|:---|:---|:---|:---:|:---:|:---|
| Parity-aware adjacent swap (this lesson) | Inspect each adjacent pair once and swap only when that pair's required parity relation is violated | `[3, 5, 1, 6, 2, 4]` | $O(N)$ | $O(1)$ | Correct in a single pass with no extra storage |
| Sort, then exchange each odd-even pair | Sort ascending, then swap positions $1 \leftrightarrow 2$, $3 \leftrightarrow 4$, and so on | `[1, 3, 2, 5, 4, 6]` | $O(N \log N)$ | $O(N)$ | Correct but pays a full sort for an ordering that needs no global order |
| Swap whenever an adjacent descent appears | Ignore parity and swap any pair with $\text{nums}[i] > \text{nums}[i + 1]$ | `[3, 2, 1, 5, 4, 6]` | $O(N)$ | $O(1)$ | Wrong: the first swap puts $2$ before $3$ and breaks the already-settled pair $3 \le 5$, and the pass never returns to fix it |
| Counting-sort buckets by value | Exploit $0 \le \text{nums}[i] \le 10^{4}$: tally each value, then re-emit valleys and peaks from the tally | valid ordering | $O(N + V)$ with $V = 10^{4} + 1$ | $O(V)$ | Correct and linear, but $O(V)$ memory is worse than $O(1)$ when $N$ is small, so it only pays off for very large arrays |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. A single loop from $0$ to $N - 2$ performs at most one comparison and one swap per index ($O(1)$ operations per step).
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. Reordering is performed entirely in-place.
