# Guided Example: Move Zeroes

We trace the step-by-step two-pointer stable compaction, three-region boundary maintenance ($[0 \dots k-1]$ non-zero, $[k \dots i-1]$ zero, $[i \dots N-1]$ unvisited), and in-place adjacent zero bubble swapping on representative integer arrays:

- **Input:** $\text{nums} = [0, 1, 0, 3, 12]$
- **Required output:** $[1, 3, 12, 0, 0]$ (Relative order of non-zero elements $1, 3, 12$ is strictly preserved; all zeros are moved to the end)
- **Single Zero Base Case:** $\text{nums} = [0] \implies [0]$
- **No Zeros Instance:** $\text{nums} = [1, 2, 3] \implies [1, 2, 3]$ ($k == i$ at every step; self-swaps leave array unchanged)
- **All Zeros Instance:** $\text{nums} = [0, 0, 0] \implies [0, 0, 0]$ (Zero writes performed; pointer $k$ remains $0$)
- **Alternating Pattern:** $\text{nums} = [0, 1, 0, 2] \implies [1, 2, 0, 0]$

This instance demonstrates in-place two-pointer array compaction without auxiliary array allocation, explains why swapping `nums[k]` with `nums[i]` automatically bubbles zeros rightward while advancing non-zero elements leftward in original relative order, and guarantees strictly $O(N)$ single-pass time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [0, 1, 0, 3, 12]$:
Move all $0$s to the end of the array while maintaining the relative order of the non-zero elements **in-place without copying the array**.

```text
Initial array:    [0, 1, 0, 3, 12]
Non-zero elements: 1, 3, 12 (must stay in this exact order)
Zeros to move:    two zeros
Target array:     [1, 3, 12, 0, 0]
```

### The In-Place Stability Challenge
- Creating a new array and filtering non-zeros takes $O(N)$ extra space, violating the strict in-place constraint.
- Standard two-pointer partitioning (like Quicksort's partition) moves zeros to the end but reverses or scrambles the order of non-zero elements (unstable).
- We use a **two-pointer forward compaction scheme**:
  - `i`: Read pointer scanning forward across every element ($0 \dots N - 1$).
  - `k`: Write pointer marking the destination for the next non-zero element.

---

## 2. Conceptual Foundation & Invariants

### The Three-Region Array Invariant
At any step during the iteration over read index $i$, the array is partitioned into three distinct contiguous segments:

```text
[ Non-Zero Elements |   All Zeros   |    Unprocessed Elements    ]
 0 ............... k-1   k ....... i-1  i ..................... N-1
```

1. **Prefix $[0 \dots k - 1]$:** Contains only non-zero elements in their exact original relative order.
2. **Middle Region $[k \dots i - 1]$:** Contains only zeros that have been bubbled forward.
3. **Suffix $[i \dots N - 1]$:** Contains unvisited elements yet to be processed.

### Action Protocol for Element $\text{nums}[i]$:
- **If $\text{nums}[i] == 0$:**
  Do nothing. The read pointer $i$ advances, naturally expanding the middle zero region by one element.
- **If $\text{nums}[i] \ne 0$:**
  Swap $\text{nums}[k]$ and $\text{nums}[i]$:
  - If $k == i$: The element is already in its correct compacted position (self-swap / no-op).
  - If $k < i$: $\text{nums}[k]$ is guaranteed to be $0$ (by region 2). Swapping moves the non-zero element to index $k$ and pushes the $0$ to index $i$.
  Advance write pointer: $k \leftarrow k + 1$.

> **Invariant.** After processing index $i$, every non-zero element in prefix $\text{nums}[0 \dots i]$ has been moved to $\text{nums}[0 \dots k - 1]$ in original order, and all positions in $[k \dots i]$ are filled with zeros.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [0, 1, 0, 3, 12]$ ($N = 5$):
Initialize write pointer $k = 0$.

---

### Step 1 ($i = 0$): Inspect $\text{nums}[0] = 0$
- Element is $0$.
- Zero detected $\implies$ No swap. Write pointer $k$ remains $0$.
- Middle zero region: $[k \dots i] = [0 \dots 0]$ contains $\{0\}$.
- Array state: `[0, 1, 0, 3, 12]`.

---

### Step 2 ($i = 1$): Inspect $\text{nums}[1] = 1$
- Element is non-zero ($1 \ne 0$).
- Swap $\text{nums}[k=0]$ with $\text{nums}[i=1]$:
  $$
  \text{swap}(\text{nums}[0], \text{nums}[1]) \implies [1, 0, 0, 3, 12]
  $$
- Advance write pointer: $k \leftarrow 0 + 1 = \mathbf{1}$.
- Middle zero region: $[1 \dots 1]$ contains $\{0\}$.
- Array state: `[1, 0, 0, 3, 12]`.

---

### Step 3 ($i = 2$): Inspect $\text{nums}[2] = 0$
- Element is $0$.
- Zero detected $\implies$ No swap. Write pointer $k$ remains $1$.
- Middle zero region: $[1 \dots 2]$ contains $\{0, 0\}$.
- Array state: `[1, 0, 0, 3, 12]`.

---

### Step 4 ($i = 3$): Inspect $\text{nums}[3] = 3$
- Element is non-zero ($3 \ne 0$).
- Swap $\text{nums}[k=1]$ with $\text{nums}[i=3]$:
  $$
  \text{swap}(\text{nums}[1], \text{nums}[3]) \implies [1, 3, 0, 0, 12]
  $$
- Advance write pointer: $k \leftarrow 1 + 1 = \mathbf{2}$.
- Middle zero region: $[2 \dots 3]$ contains $\{0, 0\}$.
- Array state: `[1, 3, 0, 0, 12]`.

---

### Step 5 ($i = 4$): Inspect $\text{nums}[4] = 12$
- Element is non-zero ($12 \ne 0$).
- Swap $\text{nums}[k=2]$ with $\text{nums}[i=4]$:
  $$
  \text{swap}(\text{nums}[2], \text{nums}[4]) \implies [1, 3, 12, 0, 0]
  $$
- Advance write pointer: $k \leftarrow 2 + 1 = \mathbf{3}$.
- Final middle zero region: $[3 \dots 4]$ contains $\{0, 0\}$.
- Array state: `[1, 3, 12, 0, 0]`.

---

### Loop Termination
All $N = 5$ elements processed.
Final compacted array:
$$
\mathbf{[1, 3, 12, 0, 0]}
$$

---

## 4. Complete Execution Trace

```text
Initial: [0, 1, 0, 3, 12], k = 0

i = 0: nums[0] = 0  -> skip -> k = 0, array: [0, 1, 0, 3, 12]
i = 1: nums[1] = 1  -> swap(0, 1) -> k = 1, array: [1, 0, 0, 3, 12]
i = 2: nums[2] = 0  -> skip -> k = 1, array: [1, 0, 0, 3, 12]
i = 3: nums[3] = 3  -> swap(1, 3) -> k = 2, array: [1, 3, 0, 0, 12]
i = 4: nums[4] = 12 -> swap(2, 4) -> k = 3, array: [1, 3, 12, 0, 0]

Result: [1, 3, 12, 0, 0]
```

| Step $i$ | $\text{nums}[i]$ | Condition $\text{nums}[i] \ne 0$? | Write Pointer $k$ | Swap Action Performed | Array State After Step |
|:---:|:---:|:---:|:---:|:---|:---|
| Initial | - | - | 0 | None | `[0, 1, 0, 3, 12]` |
| 0 | 0 | No | 0 | None (Zero skipped) | `[0, 1, 0, 3, 12]` |
| **1** | **1** | **Yes** | 0 | $\text{swap}(\text{nums}[0], \text{nums}[1])$ | `[1, 0, 0, 3, 12]` |
| 2 | 0 | No | 1 | None (Zero skipped) | `[1, 0, 0, 3, 12]` |
| **3** | **3** | **Yes** | 1 | $\text{swap}(\text{nums}[1], \text{nums}[3])$ | `[1, 3, 0, 0, 12]` |
| **4** | **12** | **Yes** | 2 | $\text{swap}(\text{nums}[2], \text{nums}[4])$ | `[1, 3, 12, 0, 0]` |
| **End** | - | - | 3 | - | **`[1, 3, 12, 0, 0]`** |

### Region Ledger

The trace above records whole array states; the ledger below records the same steps as the three region boundaries of the invariant, which is what makes the sizes of those regions checkable at a glance. Entries are listed *after* the step for index $i$ has finished, so the zero window has already absorbed position $i$:

| State after step | Write pointer $k$ | Non-zero prefix $[0 \dots k-1]$ | Zero window $[k \dots i]$ | Unvisited suffix $[i+1 \dots N-1]$ |
|:---:|:---:|:---|:---|:---|
| Before $i = 0$ | 0 | empty | empty | $[0, 1, 0, 3, 12]$ |
| $i = 0$ | 0 | empty | $[0]$ | $[1, 0, 3, 12]$ |
| $i = 1$ | 1 | $[1]$ | $[0]$ | $[0, 3, 12]$ |
| $i = 2$ | 1 | $[1]$ | $[0, 0]$ | $[3, 12]$ |
| $i = 3$ | 2 | $[1, 3]$ | $[0, 0]$ | $[12]$ |
| $i = 4$ | 3 | $[1, 3, 12]$ | $[0, 0]$ | empty |

Every row satisfies two counting facts that follow from the region definitions: the three regions together cover exactly the indices $0 \dots N - 1$, and $k$ equals the number of non-zero elements seen so far. The second fact is why the single index $k$ is enough state — the algorithm never needs to know *which* non-zero elements were placed, only how many.

---

## 5. Algorithmic Correctness

**Soundness.** Every swap exchanges a non-zero element at $i$ with a $0$ at index $k$ (when $k < i$). The non-zero element is placed at position $k$, which is the earliest available non-zero slot. Because non-zero elements are encountered in their natural sequence from left to right, their relative order is strictly preserved.

**Completeness.** Every element of the array is visited once. Any element that is non-zero is swapped into the prefix $[0 \dots k - 1]$. The remaining elements in $[k \dots N - 1]$ are left as zeros. Total counts of zeros and non-zero elements remain invariant.

---

## 6. Traps This Instance Exposes

- **Overwriting Zeros without Swapping:** A two-pass approach copies non-zeros forward (`nums[k] = nums[i]`) and then runs a second loop filling zeros (`nums[k:] = 0`). While correct, it always performs $N$ writes even when few zeros exist. Swapping achieves in-place compaction in a single pass.
- **Unstable Partitioning:** Using opposite-end pointers ($L$ and $R$ moving inward) destroys the relative order of non-zero elements (e.g. $[0, 1, 2]$ would become $[2, 1, 0]$). The forward-moving two-pointer approach guarantees stability.
- **Self-Swap Optimization:** When the array starts with non-zeros (e.g. $[1, 2, 0]$), $k == i$ for the initial elements. The code executes a trivial self-swap `nums[i], nums[i] = nums[i], nums[i]`, maintaining correctness without conditional branching overhead.

### Boundary Instances and the Rule That Carries Each One

The traps above are easiest to separate when each boundary instance isolates one condition. The outcomes below are the required outcomes for those inputs:

| Instance | Distinguishing condition | Required outcome | Which part of the method carries it |
|:---|:---|:---|:---|
| $[0]$ | $N = 1$ and the only element is a zero | $[0]$ | No non-zero is ever encountered, so $k$ stays $0$ and no swap is attempted; the untouched array is already correct. |
| $[1, 2, 3]$ | No zeros at all | $[1, 2, 3]$ | $k$ and $i$ advance in lockstep, so every swap is a self-swap and each element is confirmed rather than relocated. |
| $[0, 0, 0]$ | Every element is a zero | $[0, 0, 0]$ | $k$ remains $0$ while the zero window grows to cover the entire array, which is exactly the required arrangement. |
| $[0, 0, 1]$ | Two leading zeros before the first non-zero | $[1, 0, 0]$ | The first non-zero appears at $i = 2$ and is swapped with $\text{nums}[0]$; the two zeros rotate one slot rightward into the window. |
| $[0, 1, 0, 2]$ | Alternating zero and non-zero | $[1, 2, 0, 0]$ | Each non-zero is swapped into the next free prefix slot, so $1$ and $2$ keep their encounter order while both zeros collect in the window. |

### Approach Comparison

| Approach | Mechanism | Time | Auxiliary space | Preserves non-zero order? | Tradeoff and verdict |
|:---|:---|:---:|:---:|:---:|:---|
| Auxiliary filter array | Copy every non-zero into a fresh list, append one zero per skipped element, then write the result back over the input. | $O(N)$ | $O(N)$ | yes | Simple and fast, but the extra buffer grows with the input and violates the in-place requirement. |
| Opposite-end partition | Walk one pointer from the left and one from the right, swapping a zero on the left with a non-zero on the right until they cross. | $O(N)$ | $O(1)$ | no | In-place and linear, but the exchanges reverse the non-zeros, so $[0, 1, 2]$ would become $[2, 1, 0]$. |
| Two-pass copy then fill | Copy non-zeros forward into their final prefix, then overwrite the remaining tail with zeros in a second sweep. | $O(N)$ | $O(1)$ | yes | Correct and stable, but it always performs $N$ writes even when the array contains no zeros to move. |
| Forward swap compaction | Swap $\text{nums}[k]$ with $\text{nums}[i]$ whenever $\text{nums}[i] \ne 0$, then advance $k$. | $O(N)$ | $O(1)$ | yes | Chosen here: one pass, in place and stable, and the swap degenerates to a self-swap whenever $k == i$, so already-correct elements cost only the comparison. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. A single loop from $0$ to $N - 1$ visits each element once, performing at most one constant-time swap and pointer increment per element.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. The operation modifies the input list strictly in-place using only scalar pointer variables.
