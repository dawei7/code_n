# Guided Example: Maximum Twin Sum of a Linked List

We trace the step-by-step execution of the optimal two-pointer midpoint detection, in-place suffix reversal, and synchronized twin accumulation approach on a representative problem instance:

- **Input Linked List (`head`):** `5 -> 4 -> 2 -> 1`
- **Expected Output:** `6`

This instance illustrates the symmetry of twin indices in an even-length singly linked list, showcasing how fast and slow pointers locate the exact midpoint without counting the list length, how in-place reversal aligns twin pairs for simultaneous forward traversal, and how memory usage is kept to strictly $\mathcal{O}(1)$ auxiliary space.

---

## 1. Problem Overview & Representative Instance

In a singly linked list of even length $n$, the $i$-th node (0-indexed) is defined as the twin of the $(n - 1 - i)$-th node for all $0 \le i \le \frac{n}{2} - 1$.
The twin sum is the arithmetic sum of the values of a node and its twin:

$$\text{TwinSum}(i) = \text{val}_i + \text{val}_{n - 1 - i}$$

Our goal is to return the maximum twin sum over all pairs $i \in \{0, \dots, \frac{n}{2} - 1\}$.

Consider our representative instance: `5 -> 4 -> 2 -> 1` with $n = 4$:
- Node $0$ (value $5$) pairs with Node $3$ (value $1$): Twin Sum $= 5 + 1 = 6$.
- Node $1$ (value $4$) pairs with Node $2$ (value $2$): Twin Sum $= 4 + 2 = 6$.
The maximum twin sum across all pairs is $\max(6, 6) = 6$.

In a singly linked list, we cannot traverse backward from the tail. Copying node values into an auxiliary array would require $\mathcal{O}(n)$ extra space. Instead, by locating the midpoint and reversing the second half in place, we can traverse both halves simultaneously in $\mathcal{O}(1)$ space.

---

## 2. Mathematical & Algorithmic Principles

### Symmetric Pairing Involution
The twin mapping $\tau(i) = n - 1 - i$ is a symmetric involution on $\{0, \dots, n-1\}$:

$$\tau(\tau(i)) = n - 1 - (n - 1 - i) = i$$

For even $n = 2k$, the list partitions into:
- The first half: indices $0, 1, \dots, k - 1$.
- The second half: indices $k, k + 1, \dots, 2k - 1$.
The twins of the first half appear in strictly reversed order within the second half: the twin of $0$ is $2k - 1$, the twin of $1$ is $2k - 2$, down to the twin of $k - 1$ which is $k$.

### Three-Phase Constant-Space Pipeline
1. **Tortoise and Hare Midpoint Detection:** A slow pointer advances by $1$ step while a fast pointer advances by $2$ steps. When the fast pointer reaches the end of the list, the slow pointer rests precisely at index $k = n / 2$, the head of the second half.
2. **In-Place Suffix Reversal:** We invert the `next` pointers of the sublist starting at the slow pointer. The tail of the original list becomes the head of the reversed second half.
3. **Dual-Cursor Synchronized Scan:** We initialize pointer $p_1$ at the list head (node $0$) and pointer $p_2$ at the reversed suffix head (node $n-1$). Advancing both pointers in lockstep simultaneously yields $(\text{node}_i, \text{node}_{n-1-i})$ at each step $i$.

| Phase | Action | Pointers Utilized | State Invariant |
|---|---|---|---|
| Phase 1: Bisect | Fast & Slow march | `slow` (+1), `fast` (+2) | `slow` reaches index $n/2$ when `fast` reaches end |
| Phase 2: Invert | In-place link reversal | `prev`, `curr`, `next` | Second half links reoriented toward tail |
| Phase 3: Compare | Lockstep traversal | $p_1$ (head), $p_2$ (suffix head) | At step $i$, $p_1 = \text{node}_i$ and $p_2 = \text{node}_{n-1-i}$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Initial list: `5 -> 4 -> 2 -> 1` ($n = 4$).

### Phase 1: Locating Midpoint
- **Step 0:** `slow` at Node $0$ (val $5$), `fast` at Node $0$ (val $5$).
- **Step 1:** `slow` advances to Node $1$ (val $4$); `fast` advances $2$ steps to Node $2$ (val $2$).
- **Step 2:** `slow` advances to Node $2$ (val $2$); `fast` advances $2$ steps to `None` (past Node $3$).
- `fast` reached the end! `slow` is now positioned at Node $2$ (val $2$), which is the start of the second half ($k = 4/2 = 2$).

### Phase 2: In-Place Reversal of Second Half
Sublist to reverse: `2 -> 1 -> None`.
- Initialize `prev = None`, `curr = Node 2`.
- **Iteration 1:**
  - Cache next node: `nxt = curr.next` (Node $1$).
  - Rewire: `curr.next = prev` (`Node 2.next = None`).
  - Advance: `prev = Node 2`, `curr = Node 1`.
- **Iteration 2:**
  - Cache next node: `nxt = curr.next` (`None`).
  - Rewire: `curr.next = prev` (`Node 1.next = Node 2`).
  - Advance: `prev = Node 1`, `curr = None`.
- Reversal complete! The reversed second half starts at `prev = Node 1`, with structure `1 -> 2 -> None`.

### Phase 3: Twin Sum Comparison
We initialize:
- $p_1$ at the beginning of the first half: Node $0$ (val $5$).
- $p_2$ at the head of the reversed second half: Node $3$ (val $1$).
- Running maximum twin sum: $\mu = 0$.

#### Pair $i = 0$:
- Values observed: $p_1.\text{val} = 5$, $p_2.\text{val} = 1$.
- Current twin sum: $5 + 1 = 6$.
- Update running max: $\mu = \max(0, 6) = 6$.
- Advance pointers: $p_1 \leftarrow \text{Node 1}$ (val $4$), $p_2 \leftarrow \text{Node 2}$ (val $2$).

#### Pair $i = 1$:
- Values observed: $p_1.\text{val} = 4$, $p_2.\text{val} = 2$.
- Current twin sum: $4 + 2 = 6$.
- Update running max: $\mu = \max(6, 6) = 6$.
- Advance pointers: $p_1 \leftarrow \text{Node 2}$, $p_2 \leftarrow \text{None}$.

Both pointers finish their $k = 2$ step traversals. The final maximum twin sum is $6$.

---

## 4. Comprehensive State Trace

The table below traces the twin pair evaluations and pointer progression during the synchronized scan:

| Pair Step ($i$) | Pointer $p_1$ Target | $p_1$ Node Value | Pointer $p_2$ Target | $p_2$ Node Value | Pair Twin Sum | Running Maximum ($\mu$) |
|---|---|---|---|---|---|---|
| Initialization | Node 0 | $5$ | Node 3 (Tail) | $1$ | — | $0$ |
| Step 0 | Node 0 | $5$ | Node 3 | $1$ | $5 + 1 = 6$ | $6$ |
| Step 1 | Node 1 | $4$ | Node 2 | $2$ | $4 + 2 = 6$ | $6$ |
| Termination | Node 2 | — | `None` | — | Scan Complete | $6$ |

The computed maximum twin sum across all pairs is verified as $6$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** For an even-length list of length $2k$, the slow and fast pointer approach advances `slow` by exactly $k$ steps before `fast` becomes `None`. Reversing the links of the sublist starting at `slow` turns the original sequence $v_k \to v_{k+1} \to \dots \to v_{2k-1}$ into $v_{2k-1} \to v_{2k-2} \to \dots \to v_k$. When $p_1$ starts at $v_0$ and $p_2$ starts at $v_{2k-1}$, advancing both by one step at a time guarantees that after $j$ steps, $p_1$ points to $v_j$ and $p_2$ points to $v_{2k-1-j} = v_{n-1-j}$. This pairs every node with its exact mathematical twin.

**Completeness.** Exactly $k = n / 2$ pairs exist in a list of even length $n$. The loop runs until $p_2$ reaches `None`, which occurs after exactly $k$ iterations. Because every pair is visited and the running maximum tracks the supremum across all evaluated twin sums, the global maximum is guaranteed to be returned.

---

## 6. Edge Cases & Anti-Patterns

- **Minimal Even List ($n = 2$):** For `head = [1, 1000]`, `slow` lands on node 1 immediately. The reversed second half has one node. The loop evaluates the single pair $1 + 1000 = 1001$ and halts.
- **Identical Twin Values:** When all twin sums are equal, the supremum operator returns the common value without ambiguity.
- **Asymmetric Peak:** In a list like `[1, 100, 2, 5]`, Pair 0 has sum $1 + 5 = 6$ while Pair 1 has sum $100 + 2 = 102$, correctly yielding $\max(6, 102) = 102$.
- **Anti-Pattern — Auxiliary Array or Stack:** Copying node values into a dynamic array or pushing them onto a stack uses $\mathcal{O}(n)$ extra space. In-place reversal of the suffix achieves optimal $\mathcal{O}(1)$ auxiliary space without compromising linear runtime.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of nodes in the linked list. Locating the midpoint takes $n / 2$ iterations, reversing the second half takes $n / 2$ link updates, and computing twin sums takes $n / 2$ additions and comparisons. Total time is $\mathcal{O}(n)$ with small constant factors.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. The algorithm only manipulates pointer variables (`slow`, `fast`, `prev`, `curr`, `nxt`, $p_1$, $p_2$) and scalar numbers, requiring strictly zero heap memory allocations.