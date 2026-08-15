# Guided Example: Reverse Linked List II

We will reverse a specific interior subsegment $[2, 4]$ of a singly linked list in a single pass:

- **Input:** `head = [1, 2, 3, 4, 5]`, `left = 2`, `right = 4`
- **Required output:** `[1, 4, 3, 2, 5]`

This representative instance is ideal because the reversed subsegment lies in the interior of the list ($1 < \text{left} < \text{right} < n$), requiring the algorithm to preserve the prefix (`1`), reverse the target window (`2 -> 3 -> 4` to `4 -> 3 -> 2`), and reconnect the suffix (`5`) without extra memory or multiple passes.

---

## 1. Instance & Teaching Goal

In-place linked list reversal requires reorienting `next` pointers without creating new `ListNode` instances.

When reversing a subsegment between 1-based indices $\text{left}$ and $\text{right}$:
1. We position a pointer $\text{prev}$ immediately before the subsegment (at position $\text{left} - 1$).
2. The node at position $\text{left}$ becomes the subsegment's tail ($\text{curr}$).
3. In each iteration, we take the node immediately following $\text{curr}$ ($\text{then} = \text{curr.next}$) and splice it to the front of the reversed subsegment (immediately after $\text{prev}$).

A dummy sentinel node positioned before `head` ensures uniform handling even when $\text{left} = 1$.

---

## 2. Conceptual Foundation & Invariants

We establish a sentinel $\text{dummy}$ pointing to $\text{head}$.

- Initial structure: $\text{dummy}(0) \to 1 \to 2 \to 3 \to 4 \to 5$
- Target positions: $\text{left} = 2$, $\text{right} = 4$.
- Number of splice operations required: $\text{right} - \text{left} = 4 - 2 = 2$.

| Pointer | Node Value | Role in Invariant |
|---|---|---|
| $\text{prev}$ | $1$ | Fixed anchor immediately preceding the reversal window |
| $\text{curr}$ | $2$ | The original first node of the window, gradually pushed to become its tail |
| $\text{then}$ | $\text{curr.next}$ | The next node to be moved to the head of the reversed window |

> **Invariant.** After $k$ splice operations ($k < \text{right} - \text{left}$), the subsegment of length $k+1$ starting from $\text{prev.next}$ is completely reversed, $\text{curr}$ points to the tail of this reversed subsegment, and $\text{curr.next}$ points to the next unprocessed node.

---

## 3. Step-by-Step Worked Execution

### Initialization: Position $\text{prev}$ and $\text{curr}$

Advance $\text{prev}$ by $\text{left} - 1 = 1$ step from $\text{dummy}$.
Set $\text{curr} = \text{prev.next}$.

| Pointer | Targeted Node |
|---|---|
| $\text{prev}$ | Node $1$ |
| $\text{curr}$ | Node $2$ |
| $\text{curr.next}$ | Node $3$ |

Current list structure: `dummy -> 1 (prev) -> 2 (curr) -> 3 -> 4 -> 5`

---

### Step 1: Splice Node 3 to Window Front ($k = 1$)

Identify $\text{then} = \text{curr.next} = \text{Node } 3$.

Execute the 3 pointer reassignments:
1. `curr.next = then.next` $\implies$ Node $2$ now points to Node $4$.
2. `then.next = prev.next` $\implies$ Node $3$ now points to Node $2$.
3. `prev.next = then` $\implies$ Node $1$ now points to Node $3$.

| Step Parameter | State After Reassignment |
|---|---|
| Fixed Anchor $\text{prev}$ | Node $1$ |
| Window Head $\text{prev.next}$ | Node $3$ |
| Subsegment Reversed | $3 \to 2$ |
| Window Tail $\text{curr}$ | Node $2$ |
| Unprocessed Frontier $\text{curr.next}$ | Node $4$ |

Resulting list chain: `dummy -> 1 -> 3 -> 2 -> 4 -> 5`

---

### Step 2: Splice Node 4 to Window Front ($k = 2$)

Identify $\text{then} = \text{curr.next} = \text{Node } 4$.

Execute the 3 pointer reassignments:
1. `curr.next = then.next` $\implies$ Node $2$ now points to Node $5$.
2. `then.next = prev.next` $\implies$ Node $4$ now points to Node $3$.
3. `prev.next = then` $\implies$ Node $1$ now points to Node $4$.

| Step Parameter | State After Reassignment |
|---|---|
| Fixed Anchor $\text{prev}$ | Node $1$ |
| Window Head $\text{prev.next}$ | Node $4$ |
| Subsegment Reversed | $4 \to 3 \to 2$ |
| Window Tail $\text{curr}$ | Node $2$ |
| Suffix Connected $\text{curr.next}$ | Node $5$ |

Resulting list chain: `dummy -> 1 -> 4 -> 3 -> 2 -> 5`

Reversal limit $\text{right} - \text{left} = 2$ is reached. Iteration concludes.

---

## 4. Complete Execution Trace

| Phase | $k$ | $\text{prev}$ Val | $\text{curr}$ Val | $\text{then}$ Val | Pointer Rewirings | List State Representation |
|---|---|---|---|---|---|---|
| Setup | 0 | 1 | 2 | 3 | Position anchors | `1 -> 2 -> 3 -> 4 -> 5` |
| Splice 1 | 1 | 1 | 2 | 3 | $2\to 4,\; 3\to 2,\; 1\to 3$ | `1 -> [3 -> 2] -> 4 -> 5` |
| Splice 2 | 2 | 1 | 2 | 4 | $2\to 5,\; 4\to 3,\; 1\to 4$ | `1 -> [4 -> 3 -> 2] -> 5` |
| Result | - | 1 | 2 | $\varnothing$ | Return $\text{dummy.next}$ | `[1, 4, 3, 2, 5]` |

---

## 5. Algorithmic Correctness

**Soundness.** Each splice operation strictly preserves list continuity: no node is orphaned because `then.next` is saved before disconnecting $\text{then}$, and `curr.next` maintains the link to the remaining suffix. The sublist $[left, right]$ is inverted in place without altering any values outside $[left, right]$.

**Completeness.** By performing exactly $\text{right} - \text{left}$ splices, all nodes originally occupying positions $\text{left} + 1 \dots \text{right}$ are sequentially moved to the front in reverse order, guaranteeing full and exact segment inversion.

---

## 6. Traps This Instance Exposes

- **Reversing From Index 1 ($\text{left} = 1$):** If the head itself is part of the reversal, $\text{prev}$ must be a dummy node (`dummy.next = head`); otherwise, $\text{prev}$ is undefined.
- **Orphaning the Suffix:** Forgetting `curr.next = then.next` drops the remaining nodes ($5 \dots n$), causing a memory leak or truncated list.
- **Cycle Creation:** Setting `then.next = prev` instead of `then.next = prev.next` creates an immediate pointer cycle between `prev` and `then`.
- **Identity Swapping vs. Pointer Rewiring:** Swapping node values instead of mutating `next` references violates strict pointer-manipulation interview contracts.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ single pass. Advancing $\text{prev}$ takes $\text{left} - 1$ steps, and the reversal takes $\text{right} - \text{left}$ splices. Total node visits $\le \text{right} \le N$.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant extra space. Only 3 reference pointers ($\text{prev}, \text{curr}, \text{then}$) are maintained.
