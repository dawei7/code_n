# Guided Example: Sliding Window Maximum

We trace the step-by-step monotonic decreasing deque invariant, dominated-element eviction, and window boundary expiration on representative integer arrays:

- **Input:** $\text{nums} = [1, 3, -1, -3, 5, 3, 6, 7], \quad k = 3$
- **Required output:** $[3, 3, 5, 5, 6, 7]$
- **Single Element Window:** $\text{nums} = [1], \quad k = 1 \implies [1]$
- **Strictly Decreasing Instance:** $\text{nums} = [9, 8, 7, 6], \quad k = 2 \implies [9, 8, 7]$
- **Strictly Increasing Instance:** $\text{nums} = [1, 2, 3, 4], \quad k = 2 \implies [2, 3, 4]$

This instance demonstrates the optimal Monotonic Decreasing Deque data structure for sliding window extremum queries, proves why elements smaller than the incoming element can never serve as future window maxima (the domination property), contrasts $O(N)$ amortized deque operations with $O(N \log N)$ lazy heap deletion, and enforces $O(k)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 3, -1, -3, 5, 3, 6, 7]$ and window size $k = 3$:
Slide a window of size $3$ across the array from left to right, recording the maximum value at each position:
```text
Window Position                Max
-------------------------     -----
[1  3 -1] -3  5  3  6  7   ->   3
 1 [3 -1 -3] 5  3  6  7   ->   3
 1  3 [-1 -3  5] 3  6  7   ->   5
 1  3 -1 [-3  5  3] 6  7   ->   5
 1  3 -1 -3 [5  3  6] 7   ->   6
 1  3 -1 -3  5 [3  6  7]  ->   7
Output: [3, 3, 5, 5, 6, 7]
```

- A naive rescan of each size-$k$ window takes $O(k)$ per step, totaling $O(N \cdot k)$ time (up to $10^{10}$ operations for $N = 10^5, k = 10^5$).
- A Max-Heap with lazy deletion takes $O(N \log N)$ time.
- A **Monotonic Decreasing Deque** tracks candidate maximum indices in strictly descending value order. Every element enters and exits the deque at most once, yielding optimal **strictly $O(N)$ linear time**.

---

## 2. Conceptual Foundation & Invariants

### The Domination Principle
Why can smaller, older elements be discarded permanently?
Suppose at index $i$, we encounter $\text{nums}[i]$.
Consider any previous candidate index $j < i$ currently in the deque:
If $\text{nums}[j] \le \text{nums}[i]$:
1. $\text{nums}[i]$ is larger than $\text{nums}[j]$.
2. $\text{nums}[i]$ will remain in the sliding window **longer** than $\text{nums}[j]$ (since $i > j$, index $j$ expires before $i$).
Therefore, $\text{nums}[j]$ **can never be the maximum of the current window or any future window**!
Index $j$ is permanently dominated and can be discarded immediately.

Every eviction in the worked trace can be checked against that criterion. With window length $k$, an index $j$ popped for a later index $i$ satisfies $\text{nums}[j] \le \text{nums}[i]$, and the gap $i - j < k$ guarantees that each window which can still occur and contains $j$ must also contain $i$; since $\text{nums}[i]$ is at least as large, $j$ cannot be the maximum of any of them.

| Evicted index $j$ | $\text{nums}[j]$ | Evicting index $i$ | $\text{nums}[i]$ | Gap $i - j$ | Why every still-reachable window containing $j$ also contains $i$ | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| $0$ | $1$ | $1$ | $3$ | $1$ | The only window containing index $0$ is $[0, 2]$, and it includes index $1$ | $1$ can never be a window maximum again |
| $3$ | $-3$ | $4$ | $5$ | $1$ | Windows containing index $3$ start at $1$, $2$, or $3$; the ones that can still occur start at $2$ or $3$, and both include index $4$ | $-3$ is dominated by the newer, larger $5$ |
| $2$ | $-1$ | $4$ | $5$ | $2$ | Windows containing index $2$ start at $0$, $1$, or $2$; only start $2$ can still occur, giving $[2, 4]$ | $-1$ cannot outlive $5$ |
| $5$ | $3$ | $6$ | $6$ | $1$ | Windows containing index $5$ start at $3$, $4$, or $5$; the reachable ones start at $4$ or $5$ and both include index $6$ | $3$ is dominated by the later $6$ |
| $4$ | $5$ | $6$ | $6$ | $2$ | Windows containing index $4$ start at $2$, $3$, or $4$; only start $4$ can still occur, giving $[4, 6]$ | $5$ is dominated |
| $6$ | $6$ | $7$ | $7$ | $1$ | Windows containing index $6$ start at $4$, $5$, or $6$; start $6$ would run past the array, so only $[5, 7]$ remains | $6$ is dominated |
| $1$ | $4$ | $3$ | $4$ | $2$ | On the duplicate case $[4, 4, 2, 4, 1]$, windows containing index $1$ start at $0$, $1$, or $2$; the reachable ones are $[1, 3]$ and $[2, 4]$, and both include index $3$ | Equal values still dominate, because the newer index leaves every future window later |

### Deque Maintenance Protocol
Store **indices** in a double-ended queue $Q$:
For each index $i$ from $0$ to $N - 1$:
1. **Evict Expired Window Head:**
   The active window ending at $i$ spans $[i - k + 1, i]$.
   If the index at the front of $Q$ has expired ($Q[0] < i - k + 1$):
   $$
   Q.\text{popleft}()
   $$
2. **Evict Dominated Candidates from the Back:**
   While $Q$ is not empty and $\text{nums}[Q[-1]] \le \text{nums}[i]$:
   $$
   Q.\text{pop}()
   $$
3. **Enqueue Current Index:**
   $$
   Q.\text{append}(i)
   $$
4. **Collect Window Maximum:**
   Once the first window has matured ($i \ge k - 1$):
   The maximum element of the active window is always at the front:
   $$
   \text{result}.\text{append}(\text{nums}[Q[0]])
   $$

> **Invariant.** At every step, $Q$ contains indices from the active window whose corresponding values are in **strictly decreasing order**: $\text{nums}[Q[0]] > \text{nums}[Q[1]] > \dots > \text{nums}[Q[-1]]$. Thus, $Q[0]$ is always the maximum.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [1, 3, -1, -3, 5, 3, 6, 7]$ with $k = 3$:

### Step 1: Index $i = 0$ ($x = 1$)
- Evict expired: None.
- Domination: $Q$ is empty.
- Add $0$: $Q = [0]$ (values: $[1]$).
- $i = 0 < k - 1$ (Window building).

---

### Step 2: Index $i = 1$ ($x = 3$)
- Evict expired: None.
- Domination: $\text{nums}[Q[-1]] = 1 \le 3 \implies$ Pop index $0$!
- Add $1$: $Q = [1]$ (values: $[3]$).
- $i = 1 < k - 1$ (Window building).

---

### Step 3: Index $i = 2$ ($x = -1$) — First Full Window $[0 \dots 2]$
- Evict expired: $Q[0] = 1 \ge 2 - 3 + 1 = 0$ (Valid).
- Domination: $\text{nums}[Q[-1]] = 3 \not\le -1$. No pop.
- Add $2$: $Q = [1, 2]$ (values: $[3, -1]$).
- Window mature ($i \ge 2$): Maximum is $\text{nums}[Q[0]] = \text{nums}[1] = \mathbf{3}$.
- Result: `[3]`.

---

### Step 4: Index $i = 3$ ($x = -3$) — Window $[1 \dots 3]$
- Evict expired: $Q[0] = 1 \ge 3 - 3 + 1 = 1$ (Valid).
- Domination: $-3 < -1$. No pop.
- Add $3$: $Q = [1, 2, 3]$ (values: $[3, -1, -3]$).
- Window mature: Maximum is $\text{nums}[Q[0]] = \text{nums}[1] = \mathbf{3}$.
- Result: `[3, 3]`.

---

### Step 5: Index $i = 4$ ($x = 5$) — Window $[2 \dots 4]$
- Evict expired: $Q[0] = 1 < 4 - 3 + 1 = 2 \implies$ **Popleft index $1$!**
  - Remaining $Q = [2, 3]$ (values: $[-1, -3]$).
- Domination:
  - $\text{nums}[3] = -3 \le 5 \implies$ Pop index $3$.
  - $\text{nums}[2] = -1 \le 5 \implies$ Pop index $2$.
- Add $4$: $Q = [4]$ (values: $[5]$).
- Window mature: Maximum is $\text{nums}[Q[0]] = \text{nums}[4] = \mathbf{5}$.
- Result: `[3, 3, 5]`.

---

### Step 6: Index $i = 5$ ($x = 3$) — Window $[3 \dots 5]$
- Evict expired: $Q[0] = 4 \ge 5 - 3 + 1 = 3$ (Valid).
- Domination: $5 > 3$. No pop.
- Add $5$: $Q = [4, 5]$ (values: $[5, 3]$).
- Window mature: Maximum is $\text{nums}[Q[0]] = \text{nums}[4] = \mathbf{5}$.
- Result: `[3, 3, 5, 5]`.

---

### Step 7: Index $i = 6$ ($x = 6$) — Window $[4 \dots 6]$
- Evict expired: $Q[0] = 4 \ge 6 - 3 + 1 = 4$ (Valid).
- Domination:
  - $\text{nums}[5] = 3 \le 6 \implies$ Pop index $5$.
  - $\text{nums}[4] = 5 \le 6 \implies$ Pop index $4$.
- Add $6$: $Q = [6]$ (values: $[6]$).
- Window mature: Maximum is $\text{nums}[Q[0]] = \text{nums}[6] = \mathbf{6}$.
- Result: `[3, 3, 5, 5, 6]`.

---

### Step 8: Index $i = 7$ ($x = 7$) — Window $[5 \dots 7]$
- Evict expired: $Q[0] = 6 \ge 7 - 3 + 1 = 5$ (Valid).
- Domination: $\text{nums}[6] = 6 \le 7 \implies$ Pop index $6$.
- Add $7$: $Q = [7]$ (values: $[7]$).
- Window mature: Maximum is $\text{nums}[Q[0]] = \text{nums}[7] = \mathbf{7}$.
- Result: `[3, 3, 5, 5, 6, 7]`.

---

## 4. Complete Execution Trace

```text
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

i = 0 (1):  Q = [0(1)]
i = 1 (3):  1 <= 3 -> pop 0. Q = [1(3)]
i = 2 (-1): Q = [1(3), 2(-1)]                 -> Max = 3
i = 3 (-3): Q = [1(3), 2(-1), 3(-3)]           -> Max = 3
i = 4 (5):  exp 1 -> popleft. -3, -1 <= 5 -> pop 3, 2. Q = [4(5)] -> Max = 5
i = 5 (3):  Q = [4(5), 5(3)]                   -> Max = 5
i = 6 (6):  3, 5 <= 6 -> pop 5, 4. Q = [6(6)]  -> Max = 6
i = 7 (7):  6 <= 7 -> pop 6. Q = [7(7)]        -> Max = 7

Final Output: [3, 3, 5, 5, 6, 7]
```

| Index $i$ | Value $x$ | Front Eviction ($Q[0] < i - k + 1$) | Back Eviction ($\le x$) | Resulting Deque $Q$ (Indices) | Window Max ($\text{nums}[Q[0]]$) |
|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | 1 | None | None | `[0]` | - |
| 1 | 3 | None | Pop 0 ($1 \le 3$) | `[1]` | - |
| **2** | **-1** | None | None | `[1, 2]` | **3** |
| **3** | **-3** | None | None | `[1, 2, 3]` | **3** |
| **4** | **5** | **Popleft 1** ($1 < 2$) | Pop 3 ($-3 \le 5$), Pop 2 ($-1 \le 5$) | `[4]` | **5** |
| **5** | **3** | None | None | `[4, 5]` | **5** |
| **6** | **6** | None | Pop 5 ($3 \le 6$), Pop 4 ($5 \le 6$) | `[6]` | **6** |
| **7** | **7** | None | Pop 6 ($6 \le 7$) | `[7]` | **7** |

Across the authored cases the deque's total work never approaches the $2N$ bound: each index is appended exactly once, and the two eviction sites together can remove at most one entry per index. The strictly decreasing case never evicts from the back — its entries leave only through expiry — while the duplicate case is the one that exercises the non-strict comparison.

| Instance | $N$ | $k$ | Appends | Back (domination) pops | Front (expiry) pops | Peak deque length | Output |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $[1, 3, -1, -3, 5, 3, 6, 7]$ | $8$ | $3$ | $8$ | $6$ | $1$ | $3$ | $[3, 3, 5, 5, 6, 7]$ |
| $[1]$ | $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $[1]$ |
| $[9, 8, 7, 6]$ | $4$ | $2$ | $4$ | $0$ | $2$ | $2$ | $[9, 8, 7]$ |
| $[4, 4, 2, 4, 1]$ | $5$ | $3$ | $5$ | $3$ | $0$ | $2$ | $[4, 4, 4]$ |

---

## 5. Algorithmic Correctness

**Soundness.** Because indices entering $Q$ are appended after popping all smaller values, the values in $Q$ are strictly monotonic decreasing. The front of $Q$ always holds the index of the maximum value among all valid candidates. Because expired indices are popped from the front, $Q[0]$ is guaranteed to lie within the active window $[i - k + 1, i]$.

**Completeness.** Any element discarded during back eviction was smaller than or equal to an element that arrived later, meaning it could never be the maximum of any window containing both. Discarded elements are provably suboptimal, so the true maximum is never lost.

---

## 6. Traps This Instance Exposes

- **Storing Values Instead of Indices in Deque:** Storing raw values makes it impossible to determine when an element has expired from the window! Storing **indices** allows testing $Q[0] < i - k + 1$ in $O(1)$ time.
- **Strict vs Non-Strict Inequality in Domination:** Using $\le$ rather than $<$ when popping from the back discards duplicate values. Since the newer duplicate has a larger index and will survive longer, discarding the older duplicate is completely safe and keeps the deque as small as possible.
- **Heap Inefficiency:** While a max-heap with lazy deletion achieves $O(N \log N)$, it consumes $O(N)$ space in the worst case, which occurs when the values are strictly increasing: the newest element is then always the heap maximum, no expired entry ever reaches the root, and stale entries accumulate. The monotonic deque strictly bounds auxiliary memory to $O(k)$.

Each alternative below reaches a correct answer, and each pays in either time or working memory compared with the deque.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| Rescan every window | Read all $k$ values of each window and take their maximum | $O(N \cdot k)$ | $O(1)$ beyond the output | For $N = k = 10^{5}$ this is on the order of $10^{10}$ comparisons, far outside a practical budget |
| Max-heap with lazy deletion | Push every index with its negated value and pop expired roots | $O(N \log N)$ | $O(N)$ in the worst case | On strictly increasing input the newest maximum sits at the root, so expired entries are never popped and the heap grows with $N$ |
| Monotonic deque of indices (this lesson) | Keep candidate indices in decreasing value order; evict expired fronts and dominated backs | $O(N)$ amortized | $O(k)$ | Requires a deque with operations at both ends; evicting on the wrong side breaks the invariant immediately |
| Sparse table of range maxima | Precompute maxima for all power-of-two ranges, then answer each window with two lookups | $O(N \log N)$ to build, $O(1)$ per window | $O(N \log N)$ | Pays a large constant to answer a query pattern that only ever slides forward by one |
| Block prefix and suffix maxima | Precompute maxima inside blocks of length $k$ and combine two block fragments per window | $O(N)$ | $O(N)$ for the two precomputed arrays | Same asymptotic time as the deque but keeps two full arrays instead of $k$ candidate slots |
| Two-stack queue with running maxima | Maintain a pair of stacks whose maxima are tracked on push | $O(1)$ amortized per operation | $O(k)$ | Meets the same bound with more moving parts, because each element transfers between the stacks once |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Although there is a nested `while` loop, each index from $0$ to $N - 1$ is pushed onto the deque exactly once and popped from the deque at most once. The total number of deque operations across the entire algorithm is bounded by $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(k)$ auxiliary space for the deque, which never contains more than $k$ indices simultaneously.
