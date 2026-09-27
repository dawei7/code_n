# Guided Example: Sort Colors

We trace the step-by-step three-way partitioning of Dijkstra's Dutch National Flag algorithm on a representative array:

- **Input:** $\text{nums} = [2, 0, 2, 1, 1, 0]$
- **Required output:** $[0, 0, 1, 1, 2, 2]$

This instance demonstrates in-place three-pointer invariant maintenance ($L$, $cur$, $R$), asymmetric pointer advancement (advancing $cur$ on $0$ vs withholding $cur$ on $2$), single-pass classification in $O(N)$ time, and strictly $O(1)$ auxiliary memory.

---

## 1. Instance & Teaching Goal

Given an array $\text{nums}$ with $N = 6$ objects colored red ($0$), white ($1$), or blue ($2$), sort them **in-place** so that objects of the same color are adjacent, with the colors in the order $0$, then $1$, then $2$.

For $[2, 0, 2, 1, 1, 0]$:
- There are two $0$s, two $1$s, and two $2$s.
- The sorted result must be $[0, 0, 1, 1, 2, 2]$.

A two-pass counting sort (counting occurrences of 0, 1, 2 and overwriting) takes $O(N)$ time, but Dijkstra's Dutch National Flag algorithm performs the sort in a single linear pass using three pointers.

---

## 2. Conceptual Foundation & Invariants

### The 4-Region Invariant
We partition the array into four contiguous logical intervals using three pointers:
- $L = 0$ (Next slot for a $0$)
- $R = N - 1$ (Next slot for a $2$)
- $cur = 0$ (Current element being inspected)

```text
[ 0 0 ... 0 | 1 1 ... 1 | ? ? ... ? | 2 2 ... 2 ]
 0         L-1  L      cur-1  cur   R  R+1       N-1
```

1. Region $[0, L - 1]$: All confirmed $0$s.
2. Region $[L, cur - 1]$: All confirmed $1$s.
3. Region $[cur, R]$: Unclassified elements.
4. Region $[R + 1, N - 1]$: All confirmed $2$s.

### Transition Rules (While $cur \le R$)
- **Case 1 ($\text{nums}[cur] == 0$):**
  Swap $\text{nums}[cur]$ with $\text{nums}[L]$.
  Increment $L \leftarrow L + 1$.
  Increment $cur \leftarrow cur + 1$.
  *(We can safely advance $cur$ because the element swapped into $cur$ from $L$ was already examined and is known to be $1$, or $cur == L$)*.
- **Case 2 ($\text{nums}[cur] == 1$):**
  The element belongs in the middle region.
  Increment $cur \leftarrow cur + 1$.
- **Case 3 ($\text{nums}[cur] == 2$):**
  Swap $\text{nums}[cur]$ with $\text{nums}[R]$.
  Decrement $R \leftarrow R - 1$.
  *(Crucial: do **not** advance $cur$; the incoming element from $R$ is unexamined and must be inspected on the next iteration)*.

> **Invariant.** The unclassified region $[cur, R]$ shrinks by at least one element in every iteration.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [2, 0, 2, 1, 1, 0]$ with initial pointers $L = 0, cur = 0, R = 5$:

### Iteration 1 ($cur = 0, R = 5$)
- Current element: $\text{nums}[0] = 2$.
- Action: Swap $\text{nums}[cur]$ with $\text{nums}[R]$ ($\text{nums}[0] \leftrightarrow \text{nums}[5]$).
- Array state: $[\mathbf{0}, 0, 2, 1, 1, \mathbf{2}]$.
- Pointers: $R \leftarrow 5 - 1 = 4$. $cur$ remains $0$.

---

### Iteration 2 ($cur = 0, R = 4$)
- Current element: $\text{nums}[0] = 0$.
- Action: Swap $\text{nums}[cur]$ with $\text{nums}[L]$ ($\text{nums}[0] \leftrightarrow \text{nums}[0]$).
- Array state: $[0, 0, 2, 1, 1, 2]$.
- Pointers: $L \leftarrow 0 + 1 = 1$, $cur \leftarrow 0 + 1 = 1$.

---

### Iteration 3 ($cur = 1, R = 4$)
- Current element: $\text{nums}[1] = 0$.
- Action: Swap $\text{nums}[cur]$ with $\text{nums}[L]$ ($\text{nums}[1] \leftrightarrow \text{nums}[1]$).
- Array state: $[0, 0, 2, 1, 1, 2]$.
- Pointers: $L \leftarrow 1 + 1 = 2$, $cur \leftarrow 1 + 1 = 2$.

---

### Iteration 4 ($cur = 2, R = 4$)
- Current element: $\text{nums}[2] = 2$.
- Action: Swap $\text{nums}[cur]$ with $\text{nums}[R]$ ($\text{nums}[2] \leftrightarrow \text{nums}[4]$).
- Array state: $[0, 0, \mathbf{1}, 1, \mathbf{2}, 2]$.
- Pointers: $R \leftarrow 4 - 1 = 3$. $cur$ remains $2$.

---

### Iteration 5 ($cur = 2, R = 3$)
- Current element: $\text{nums}[2] = 1$.
- Action: In place. Increment $cur \leftarrow 2 + 1 = 3$.
- Array state: $[0, 0, 1, 1, 2, 2]$.

---

### Iteration 6 ($cur = 3, R = 3$)
- Current element: $\text{nums}[3] = 1$.
- Action: In place. Increment $cur \leftarrow 3 + 1 = 4$.
- Array state: $[0, 0, 1, 1, 2, 2]$.

---

### Termination
- Condition check: $cur = 4 > R = 3$.
- The unclassified region is empty.
- Final sorted array: $[0, 0, 1, 1, 2, 2]$.

---

## 4. Complete Execution Trace

| Iteration | Active $cur$ | Value $\text{nums}[cur]$ | $L$ | $R$ | Swap Performed | Array State After Step | Next Pointer Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 2 | 0 | 5 | $\text{nums}[0] \leftrightarrow \text{nums}[5]$ | `[0, 0, 2, 1, 1, 2]` | $R \leftarrow 4$, $cur$ unchanged |
| 2 | 0 | 0 | 0 | 4 | $\text{nums}[0] \leftrightarrow \text{nums}[0]$ | `[0, 0, 2, 1, 1, 2]` | $L \leftarrow 1, cur \leftarrow 1$ |
| 3 | 1 | 0 | 1 | 4 | $\text{nums}[1] \leftrightarrow \text{nums}[1]$ | `[0, 0, 2, 1, 1, 2]` | $L \leftarrow 2, cur \leftarrow 2$ |
| 4 | 2 | 2 | 2 | 4 | $\text{nums}[2] \leftrightarrow \text{nums}[4]$ | `[0, 0, 1, 1, 2, 2]` | $R \leftarrow 3$, $cur$ unchanged |
| 5 | 2 | 1 | 2 | 3 | None ($1$ in middle) | `[0, 0, 1, 1, 2, 2]` | $cur \leftarrow 3$ |
| 6 | 3 | 1 | 2 | 3 | None ($1$ in middle) | `[0, 0, 1, 1, 2, 2]` | $cur \leftarrow 4$ |
| Exit | 4 | - | 2 | 3 | - | `[0, 0, 1, 1, 2, 2]` | **Halt ($cur > R$)** |

---

## 5. Algorithmic Correctness

**Soundness.** Swapping a $0$ to $L$ moves it into the prefix region $[0, L - 1]$, and swapping a $2$ to $R$ moves it into the suffix region $[R + 1, N - 1]$. Elements skipped by $cur$ when value is $1$ remain in $[L, cur - 1]$. The four partitions preserve relative ordering without corrupting classified elements.

**Completeness.** In every step, either $cur$ increments or $R$ decrements. Therefore, the distance $(R - cur)$ strictly decreases by at least 1 per iteration. When $cur > R$, all elements have been assigned to their sorted segment.

---

## 6. Traps This Instance Exposes

- **Advancing $cur$ After Swapping with $R$:** When swapping with $R$, the incoming element from index $R$ has never been inspected. If you increment $cur$, that element will be skipped unclassified (e.g. if a $0$ was at $R$, it would be left stuck in the $1$s region).
- **Using Built-In Sort:** The problem specifically forbids using library sorting routines (`nums.sort()`), requiring an in-place partition.
- **Handling Arrays with Zero $1$s:** If the array consists only of $0$s and $2$s (e.g. $[2, 0, 2, 0]$), the algorithm correctly collapses the middle region without empty-boundary exceptions.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements. The loop runs at most $N$ times since each iteration either increments $cur$ or decrements $R$.
- **Auxiliary Space Complexity:** $O(1)$. Swaps are executed strictly in place using three pointer registers.
