# Guided Example: First Missing Positive

We trace the step-by-step execution of in-place cyclic sort placement on a representative unsorted array instance:

- **Input:** $\text{nums} = [3, 4, -1, 1]$
- **Required output:** $2$

This instance demonstrates Pigeonhole Principle bounds ($1 \le \text{ans} \le N + 1$), cyclic home-index swapping ($x \mapsto \text{nums}[x - 1]$), handling negative and out-of-range elements, and identifying the first missing positive integer in $O(N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an unsorted integer array $\text{nums}$ of length $N = 4$:
$$
[3, 4, -1, 1]
$$

We must find the smallest positive integer missing from the array. The algorithm must run in $O(N)$ time and use strictly $O(1)$ auxiliary space.

A naive hash set stores all positive integers in $O(N)$ extra memory. Comparison sorting takes $O(N \log N)$ time.
By the **Pigeonhole Principle**, an array of length $N$ can contain at most $N$ distinct positive integers. Therefore, the smallest missing positive integer must lie in the discrete range:
$$
\text{Missing Positive} \in [1, N + 1]
$$
This allows us to use the array itself as a zero-allocation hash table, placing each valid integer $x \in [1, N]$ at its corresponding target index $x - 1$.

---

## 2. Conceptual Foundation & Invariants

### Home Index Mapping
For any element $x = \text{nums}[i]$:
- If $1 \le x \le N$, its "home" position is index $\text{home} = x - 1$.
- If $x \le 0$ or $x > N$, the element cannot help fill the range $[1, N]$ and is ignored.

### Cyclic Sort Algorithm
We iterate index $i$ from $0$ to $N - 1$:
While $\text{nums}[i] \in [1, N]$ and $\text{nums}[\text{nums}[i] - 1] \ne \text{nums}[i]$:
- Let $\text{target\_idx} = \text{nums}[i] - 1$.
- Swap $\text{nums}[i]$ and $\text{nums}[\text{target\_idx}]$.
- *(Each swap places at least one previously misplaced positive number into its correct home).*

### Verification Pass
After cyclic sort, scan indices $i \in [0, N - 1]$:
- The first index where $\text{nums}[i] \ne i + 1$ indicates that the integer $i + 1$ is missing. Return $i + 1$.
- If every index $i$ satisfies $\text{nums}[i] == i + 1$, all integers $1 \dots N$ are present. Return $N + 1$.

> **Invariant.** At each swap, the count of elements residing at their correct home indices strictly increases. Each element is placed at its home index at most once, bounding total swaps to $N$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [3, 4, -1, 1]$ ($N = 4$):

### Pass 1: Cyclic Sort Placement

- **Index $i = 0$:**
  - Value: $\text{nums}[0] = 3$.
  - In range $[1, 4]$: Yes. Target home index is $3 - 1 = 2$.
  - Target occupant: $\text{nums}[2] = -1 \ne 3$.
  - Action: Swap $\text{nums}[0]$ with $\text{nums}[2]$.
  - Array state: $[\mathbf{-1}, 4, \mathbf{3}, 1]$.
  - Inspect current occupant at $i = 0$: $\text{nums}[0] = -1$.
  - In range $[1, 4]$: No (negative). While-loop halts for $i = 0$. Advance $i \to 1$.

- **Index $i = 1$:**
  - Value: $\text{nums}[1] = 4$.
  - In range $[1, 4]$: Yes. Target home index is $4 - 1 = 3$.
  - Target occupant: $\text{nums}[3] = 1 \ne 4$.
  - Action: Swap $\text{nums}[1]$ with $\text{nums}[3]$.
  - Array state: $[-1, \mathbf{1}, 3, \mathbf{4}]$.
  - Inspect current occupant at $i = 1$: $\text{nums}[1] = 1$.
  - In range $[1, 4]$: Yes. Target home index is $1 - 1 = 0$.
  - Target occupant: $\text{nums}[0] = -1 \ne 1$.
  - Action: Swap $\text{nums}[1]$ with $\text{nums}[0]$.
  - Array state: $[\mathbf{1}, \mathbf{-1}, 3, 4]$.
  - Inspect current occupant at $i = 1$: $\text{nums}[1] = -1$.
  - In range $[1, 4]$: No. While-loop halts for $i = 1$. Advance $i \to 2$.

- **Index $i = 2$:**
  - Value: $\text{nums}[2] = 3$. Target home is $3 - 1 = 2$.
  - Already at home ($\text{nums}[2] == 3$). While-loop halts. Advance $i \to 3$.

- **Index $i = 3$:**
  - Value: $\text{nums}[3] = 4$. Target home is $4 - 1 = 3$.
  - Already at home ($\text{nums}[3] == 4$). While-loop halts.

Cyclic sort completes with array: $[1, -1, 3, 4]$.

---

### Pass 2: Identification of Smallest Missing Positive

- **Index $0$:** Expected $0 + 1 = 1$. Observed $\text{nums}[0] = 1$. Match.
- **Index $1$:** Expected $1 + 1 = 2$. Observed $\text{nums}[1] = -1 \ne 2$. **Mismatch!**
- The smallest positive integer missing is $1 + 1 = 2$.
- Return $2$.

---

## 4. Complete Execution Trace

| Step | Current Index $i$ | Value $\text{nums}[i]$ | Target Index $\text{nums}[i] - 1$ | Target Value $\text{nums}[\text{target}]$ | Swap Action | Array State After Step |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 | - | - | - | - | Initial state | $[3, 4, -1, 1]$ |
| 1 | 0 | 3 | 2 | -1 | Swap $\text{nums}[0] \leftrightarrow \text{nums}[2]$ | $[-1, 4, 3, 1]$ |
| 2 | 0 | -1 | - | - | Out of range; advance to $i = 1$ | $[-1, 4, 3, 1]$ |
| 3 | 1 | 4 | 3 | 1 | Swap $\text{nums}[1] \leftrightarrow \text{nums}[3]$ | $[-1, 1, 3, 4]$ |
| 4 | 1 | 1 | 0 | -1 | Swap $\text{nums}[1] \leftrightarrow \text{nums}[0]$ | $[1, -1, 3, 4]$ |
| 5 | 1 | -1 | - | - | Out of range; advance to $i = 2$ | $[1, -1, 3, 4]$ |
| 6 | 2 | 3 | 2 | 3 | Already at home; advance to $i = 3$ | $[1, -1, 3, 4]$ |
| 7 | 3 | 4 | 3 | 4 | Already at home; scan finishes | $[1, -1, 3, 4]$ |
| Scan | 1 | -1 | - | - | $\text{nums}[1] \ne 1 + 1$ | **Return 2** |

---

## 5. Algorithmic Correctness

**Soundness.** Swapping places in-range elements $x \in [1, N]$ into index $x - 1$. After the cyclic sort, an element $x \in [1, N]$ is present in the array if and only if $\text{nums}[x - 1] == x$. The second linear scan checks each positive integer from $1$ upward; the first index $i$ failing the equality $\text{nums}[i] == i + 1$ is provably the smallest absent positive integer.

**Completeness.** Each swap places at least one element into its permanent home index. Once an element is at its home, it is never swapped again. Since there are $N$ positions, at most $N$ swaps occur across the entire algorithm. The while loop is guaranteed to terminate in $O(N)$ total steps.

---

## 6. Traps This Instance Exposes

- **Infinite Loop on Duplicate Values:** If $\text{nums} = [1, 1]$, index 1 has value $1$ with target home $0$. If we check only $\text{nums}[i] \ne i + 1$, swapping $\text{nums}[1]$ with $\text{nums}[0]$ creates an infinite loop because both are $1$. The condition must check $\text{nums}[i] \ne \text{nums}[\text{nums}[i] - 1]$ to halt when the target position already contains the correct value.
- **Negative and Out-of-Bounds Numbers:** Values $\le 0$ or $> N$ must not be swapped. Attempting to index $\text{nums}[x - 1]$ when $x \le 0$ or $x > N$ causes invalid memory access or negative index aliasing.
- **Array Fully Populated:** For $\text{nums} = [1, 2, 3]$, all indices match ($1, 2, 3$). The scan finishes without finding a mismatch; the algorithm correctly returns $N + 1 = 4$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in $\text{nums}$. Although there is a nested while-loop, each swap permanently fixes at least one element into its correct position. No element is swapped into its home more than once, bounding total swaps to at most $N$. The subsequent verification pass takes $O(N)$ time. Total runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Swapping modifies the input array in place without extra memory allocations.
