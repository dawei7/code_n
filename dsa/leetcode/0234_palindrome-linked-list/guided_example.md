# Guided Example: Palindrome Linked List

We trace the step-by-step fast/slow midpoint bisection, in-place second-half pointer reversal, and dual-head symmetry verification on representative singly linked lists:

- **Input:** $\text{head} = [1, 2, 2, 1]$
- **Required output:** `true` (Symmetric across center: values read identical forward and backward)
- **Odd Length Instance:** $\text{head} = [1, 2, 3, 2, 1] \implies \text{true}$ (Center element $3$ is self-symmetric)
- **Asymmetric Instance:** $\text{head} = [1, 2] \implies \text{false}$ ($1 \ne 2$)
- **Single Node Instance:** $\text{head} = [1] \implies \text{true}$

This instance demonstrates the classical three-phase linked list pipeline (Tortoise-and-Hare midpoint search, three-pointer in-place list reversal, and paired comparison), proves why the algorithm achieves $O(N)$ time with strictly $O(1)$ auxiliary memory without copying values to an external array, and handles both even and odd length parity.

---

## 1. Instance & Teaching Goal

Given a singly linked list $\text{head} = 1 \to 2 \to 2 \to 1 \to \text{None}$:
Determine whether the node values form a palindrome.

In an array, palindrome checking uses two inward pointers (`left = 0, right = N - 1`) moving in $O(1)$ space.
In a singly linked list, nodes only have forward `next` pointers; backward traversal is impossible without copying values to an array (taking $O(N)$ auxiliary space) or using recursion (taking $O(N)$ call stack space).
To satisfy the follow-up of **$O(1)$ auxiliary space**, we execute a 3-phase structural transformation:
1. **Find the Midpoint:** Use Floyd's Tortoise and Hare pointers (`slow` and `fast`) to reach the center of the list in one pass.
2. **Reverse the Second Half:** Invert the forward `next` pointers of the second half in place.
3. **Compare Halves:** Advance two pointers from the list head and the reversed second-half head, checking value equality until the end.

---

## 2. Conceptual Foundation & Invariants

### Phase 1: Tortoise-and-Hare Midpoint Search
Initialize `slow = head`, `fast = head`.
While `fast and fast.next`:
$$
\text{slow} \leftarrow \text{slow.next}, \quad \text{fast} \leftarrow \text{fast.next.next}
$$
- If length is even ($2k$): `slow` lands at index $k$ (the exact start of the second half).
- If length is odd ($2k + 1$): `slow` lands at index $k$ (the center element).

### Phase 2: In-Place Reversal of Second Half
Reverse the sublist starting from `slow`:
Initialize `prev = None`, `curr = slow`.
While `curr`:
$$
\text{nxt} = \text{curr.next}, \quad \text{curr.next} = \text{prev}, \quad \text{prev} = \text{curr}, \quad \text{curr} = \text{nxt}
$$
`prev` becomes the head of the reversed second half.

### Phase 3: Paired Equality Comparison
Set $p_1 = \text{head}$ and $p_2 = \text{prev}$.
While $p_2$ is not None:
- If $p_1\text{.val} \ne p_2\text{.val}$: return `false`.
- $p_1 \leftarrow p_1\text{.next}, \quad p_2 \leftarrow p_2\text{.next}$.
Return `true`.

> **Invariant.** At each comparison step, $p_1$ traverses the first half from left to right, while $p_2$ traverses the second half from right to left (toward the center).

---

## 3. Step-by-Step Worked Execution

We trace the 3 phases on $\text{head} = [1, 2, 2, 1]$:
Nodes: $N_0(1) \to N_1(2) \to N_2(2) \to N_3(1) \to \text{None}$.

### Phase 1: Fast/Slow Pointers to Find Midpoint
- **Start:** $\text{slow} = N_0(1), \quad \text{fast} = N_0(1)$.
- **Iteration 1:**
  - $\text{slow} \to N_1(2)$.
  - $\text{fast} \to N_2(2)$.
- **Iteration 2:**
  - $\text{slow} \to N_2(2)$.
  - $\text{fast} \to \text{None}$ (since $N_2\text{.next.next} = N_3\text{.next} = \text{None}$).
- Loop ends. `slow` points to $N_2(2)$, the start of the second half.

---

### Phase 2: Reverse Second Half Starting at $N_2$
Sublist to reverse: $N_2(2) \to N_3(1) \to \text{None}$.
- **Init:** $\text{prev} = \text{None}, \quad \text{curr} = N_2(2)$.
- **Step 1 ($N_2$):**
  - $\text{nxt} = N_3(1)$.
  - $N_2\text{.next} = \text{None}$.
  - $\text{prev} = N_2(2), \quad \text{curr} = N_3(1)$.
- **Step 2 ($N_3$):**
  - $\text{nxt} = \text{None}$.
  - $N_3\text{.next} = N_2(2)$.
  - $\text{prev} = N_3(1), \quad \text{curr} = \text{None}$.
- Reversal complete! Head of reversed second half is $p_2 = \text{prev} = N_3(1)$.
- Graph structure:
  - First half: $N_0(1) \to N_1(2) \to \dots$
  - Second half reversed: $N_3(1) \to N_2(2) \to \text{None}$.

The three-pointer loop is easy to run in the head and easy to get wrong on paper, so the table records every link write of this reversal. `nxt` is always read *before* `curr.next` is overwritten; forgetting that order loses the rest of the suffix and turns the reversal into a truncation.

| Reversal step | `curr` entering the step | `nxt` saved first | Link rewritten | `prev` after the step | Suffix not yet reversed |
|:---:|:---:|:---:|:---|:---:|:---|
| Init | $N_2(2)$ | not yet read | none | `None` | $N_2(2) \to N_3(1)$ |
| 1 | $N_2(2)$ | $N_3(1)$ | $N_2\text{.next} \leftarrow \text{None}$ | $N_2(2)$ | $N_3(1)$ |
| 2 | $N_3(1)$ | `None` | $N_3\text{.next} \leftarrow N_2(2)$ | $N_3(1)$ | empty |
| Exit | `None` | not read | none | $N_3(1)$ is the new head | empty |

---

### Phase 3: Compare First Half with Reversed Second Half
- **Init:** $p_1 = N_0(1), \quad p_2 = N_3(1)$.
- **Comparison 1:**
  - $p_1\text{.val} = 1, \quad p_2\text{.val} = 1$.
  - Values match ($1 == 1$)!
  - Advance: $p_1 \to N_1(2), \quad p_2 \to N_2(2)$.
- **Comparison 2:**
  - $p_1\text{.val} = 2, \quad p_2\text{.val} = 2$.
  - Values match ($2 == 2$)!
  - Advance: $p_1 \to N_2(2), \quad p_2 \to \text{None}$.
- $p_2$ reached `None`. All pairs matched!
- **Return `true`.**

---

## 4. Complete Execution Trace

```text
Original List:
1 (N0) -> 2 (N1) -> 2 (N2) -> 1 (N3) -> None

Phase 1 (Tortoise & Hare):
  slow stops at N2(2)

Phase 2 (Reverse from slow):
  N3(1) -> N2(2) -> None

Phase 3 (Two Pointers):
  p1 at N0(1), p2 at N3(1): 1 == 1 (Match)
  p1 at N1(2), p2 at N2(2): 2 == 2 (Match)
  p2 is None -> True!
```

| Phase | Active Pointer 1 | Active Pointer 2 | Operation / Action | Comparison State | Result |
|:---:|:---:|:---:|:---|:---:|:---:|
| **1: Midpoint** | $\text{slow} = N_0(1)$ | $\text{fast} = N_0(1)$ | Initial position | - | - |
| **1: Midpoint** | $\text{slow} = N_1(2)$ | $\text{fast} = N_2(2)$ | Fast moves $2\times$ | - | - |
| **1: Midpoint** | $\text{slow} = N_2(2)$ | $\text{fast} = \text{None}$ | `fast` reaches end | Midpoint $= N_2$ | - |
| **2: Reversal** | $\text{curr} = N_2(2)$ | $\text{prev} = \text{None}$ | $N_2\text{.next} \leftarrow \text{None}$ | Invert link | - |
| **2: Reversal** | $\text{curr} = N_3(1)$ | $\text{prev} = N_2(2)$ | $N_3\text{.next} \leftarrow N_2$ | Invert link | Reversed Head $= N_3$ |
| **3: Compare** | $p_1 = N_0(1)$ | $p_2 = N_3(1)$ | Compare values | $1 == 1$ | Match |
| **3: Compare** | $p_1 = N_1(2)$ | $p_2 = N_2(2)$ | Compare values | $2 == 2$ | Match |
| **Finish** | $p_1 = N_2(2)$ | $p_2 = \text{None}$ | Loop terminates | All pairs match | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** Reversing the second half allows us to traverse the latter half of the list in reverse order. Comparing $p_1$ (nodes $0, 1, \dots$) and $p_2$ (nodes $N-1, N-2, \dots$) pairwise verifies the mathematical definition of a palindrome: $\text{val}[i] == \text{val}[N - 1 - i]$ for all $i < \lfloor N / 2 \rfloor$.

**Completeness.** Every pair of mirror elements is examined. If any pair differs, the algorithm immediately terminates and returns `false`. If all pairs match, `true` is returned.

---

## 6. Traps This Instance Exposes

- **Odd Length Center Element:** When $N$ is odd (e.g. $[1, 2, 3, 2, 1]$), `slow` lands on the exact center node ($3$). Reversing from `slow` includes $3$ in the reversed list. Because the loop condition is `while p2:`, comparing $p_1$ and $p_2$ tests $1 == 1, 2 == 2, 3 == 3$, which succeeds correctly without special handling for the middle node.
- **Copying to List vs In-Place Reversal:** Appending node values to a Python list `vals = []` and checking `vals == vals[::-1]` takes $O(N)$ auxiliary memory. The pointer reversal technique is required to achieve $O(1)$ space.
- **Restoring List (Good Practice):** Mutating input structures during a query can have side effects in concurrent systems. In production, re-reversing the second half before returning restores the original list geometry.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list.
  - Finding midpoint: $N/2$ steps.
  - Reversing second half: $N/2$ steps.
  - Comparing halves: $N/2$ steps.
  - Total operations: $3N/2 = O(N)$ time.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. No new nodes or collections are created; pointer references are rewired in place.