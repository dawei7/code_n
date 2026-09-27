# Guided Example: Reorder List

We trace the step-by-step three-phase in-place list restructuring (midpoint bisection, suffix reversal, and alternating node interweaving) on representative linked list instances:

- **Input:** $\text{head} = [1, 2, 3, 4, 5]$
- **Required output:** $[1, 5, 2, 4, 3]$ (Interwoven sequence $L_0 \to L_4 \to L_1 \to L_3 \to L_2$)
- **Even-Length Instance:** $\text{head} = [1, 2, 3, 4] \implies [1, 4, 2, 3]$

This instance demonstrates finding the list midpoint using slow/fast pointers, severing the list into two disjoint halves, reversing the second half in-place via three-pointer iterative reversal, and alternatingly splicing nodes without modifying node values in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given a singly linked list $L_0 \to L_1 \to \dots \to L_{n-1} \to L_n$:
$$
1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5
$$
Reorder the nodes into alternating front-and-back order:
$$
L_0 \longrightarrow L_n \longrightarrow L_1 \longrightarrow L_{n-1} \longrightarrow L_2 \longrightarrow \dots
$$
For $\text{head} = [1, 2, 3, 4, 5]$, the resulting order is:
$$
1 \longrightarrow 5 \longrightarrow 2 \longrightarrow 4 \longrightarrow 3
$$
Node values cannot be modified; only pointer links may be updated.

Copying all nodes into an array allows trivial two-pointer indexing, but consumes $O(N)$ auxiliary memory.
The optimal in-place algorithm decomposes into three linear phases:
1. **Phase 1 (Find Midpoint & Bisect):** Use slow/fast pointers to find the median node and sever `slow.next = None`.
2. **Phase 2 (Reverse Second Half):** Reverse the second half in-place ($4 \to 5 \implies 5 \to 4$).
3. **Phase 3 (Merge & Interweave):** Zip the two halves together by alternating next pointers.

---

## 2. Conceptual Foundation & Invariants

### The 3-Phase In-Place Pipeline

#### Phase 1: Median Split
Initialize `slow = head`, `fast = head`.
Advance `slow` by 1 and `fast` by 2 until `fast.next` or `fast.next.next` is null:
- Split the list at `slow`:
  $$
  \text{second} = \text{slow.next}
  $$
  $$
  \text{slow.next} = \text{null}
  $$
- First half: $L_0 \to \dots \to L_{\lceil n/2 \rceil}$.
- Second half: $L_{\lceil n/2 \rceil + 1} \to \dots \to L_n$.

#### Phase 2: In-Place Reversal of Second Half
Reverse `second` using standard three-pointer sliding:
$$
\text{prev} = \text{null}, \quad \text{curr} = \text{second}
$$
While `curr`:
- $\text{nxt} = \text{curr.next}$
- $\text{curr.next} = \text{prev}$
- $\text{prev} = \text{curr}$
- $\text{curr} = \text{nxt}$
The head of the reversed second half is `prev`.

#### Phase 3: Alternating Zipper Merge
Let `first = head` and `second = prev`.
While `second`:
- Save forward links: $t_1 = \text{first.next}, \, t_2 = \text{second.next}$.
- Splice: $\text{first.next} = \text{second}, \, \text{second.next} = t_1$.
- Advance: $\text{first} = t_1, \, \text{second} = t_2$.

> **Invariant.** At each zipper step, the prefix of length $2k$ strictly alternates between elements from the original front and original reversed back, with no dangling circular references.

---

## 3. Step-by-Step Worked Execution

We trace the 5-node list $\text{head} = [1, 2, 3, 4, 5]$:

### Phase 1: Find Midpoint & Bisect
- Start: `slow = Node(1)`, `fast = Node(1)`.
- Step 1: `slow = Node(2)`, `fast = Node(3)`.
- Step 2: `slow = Node(3)`, `fast = Node(5)` (`fast.next == None`).
- Median node is `Node(3)`.
- Sever list:
  - $\text{second} = \text{Node}(4)$.
  - $\text{slow.next} = \text{null}$ ($\text{Node}(3).\text{next} = \text{null}$).
- List 1: $1 \to 2 \to 3 \to \text{null}$.
- List 2: $4 \to 5 \to \text{null}$.

---

### Phase 2: Reverse Second Half ($4 \to 5$)
- Initial: `prev = null`, `curr = Node(4)`.
- **Iteration 1 ($curr = 4$):**
  - $\text{nxt} = \text{Node}(5)$.
  - $\text{Node}(4).\text{next} = \text{null}$.
  - $\text{prev} = \text{Node}(4)$, $\text{curr} = \text{Node}(5)$.
- **Iteration 2 ($curr = 5$):**
  - $\text{nxt} = \text{null}$.
  - $\text{Node}(5).\text{next} = \text{Node}(4)$.
  - $\text{prev} = \text{Node}(5)$, $\text{curr} = \text{null}$.
- Second half reversed: $5 \to 4 \to \text{null}$. Head is `prev = Node(5)`.

---

### Phase 3: Zipper Merge
`first = Node(1)`, `second = Node(5)`.

- **Merge Step 1:**
  - Cache: $t_1 = \text{Node}(2), \, t_2 = \text{Node}(4)$.
  - Wire: $\text{Node}(1).\text{next} = \text{Node}(5)$.
  - Wire: $\text{Node}(5).\text{next} = \text{Node}(2)$.
  - Interwoven: $1 \to 5 \to 2 \dots$
  - Advance: `first = Node(2)`, `second = Node(4)`.

- **Merge Step 2:**
  - Cache: $t_1 = \text{Node}(3), \, t_2 = \text{null}$.
  - Wire: $\text{Node}(2).\text{next} = \text{Node}(4)$.
  - Wire: $\text{Node}(4).\text{next} = \text{Node}(3)$.
  - Interwoven: $1 \to 5 \to 2 \to 4 \to 3 \dots$
  - Advance: `first = Node(3)`, `second = null`.

- `second` is null. Merge terminates!

Final list: $1 \to 5 \to 2 \to 4 \to 3 \to \text{null}$.

---

## 4. Complete Execution Trace

```text
Initial:        1 -> 2 -> 3 -> 4 -> 5
Phase 1 Split:  L1: 1 -> 2 -> 3 -> null
                L2: 4 -> 5 -> null

Phase 2 Rev:    L2_rev: 5 -> 4 -> null

Phase 3 Merge:  1 -> 5 -> 2 -> 4 -> 3 -> null
```

| Phase | Operation | Active Nodes | Action Taken | Resulting Structure |
|:---:|:---:|:---:|:---|:---|
| 1 | Midpoint Search | `slow=3`, `fast=5` | Split at `slow` | $L_1 = [1, 2, 3], \, L_2 = [4, 5]$ |
| 2 | Reverse $L_2$ | $4 \to 5$ | In-place link reversal | $L_2^{\text{rev}} = 5 \to 4 \to \text{null}$ |
| 3.1 | Interweave | $L_1(1), L_2(5)$ | Connect $1 \to 5 \to 2$ | $1 \to 5 \to 2 \dots$ |
| 3.2 | Interweave | $L_1(2), L_2(4)$ | Connect $2 \to 4 \to 3$ | $1 \to 5 \to 2 \to 4 \to 3 \to \text{null}$ |
| **Final** | Termination | `second=null` | List complete | **$[1, 5, 2, 4, 3]$** |

### Phase 2 Reversal Ledger

The second half of this instance is only two nodes long, so the three-pointer
reversal is easy to misread as a single swap. Tracking `prev`, `curr`, and the
cached `nxt` separately shows that each node is relinked exactly once.

| Reversal iteration | `curr` before the step | `nxt = curr.next` cached first | Link written | `prev` after | `curr` after | Reversed chain built so far |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| initial | $\text{Node}(4)$ | not yet read | none | `null` | $\text{Node}(4)$ | empty |
| 1 | $\text{Node}(4)$ | $\text{Node}(5)$ | $\text{Node}(4).\text{next} \leftarrow \text{null}$ | $\text{Node}(4)$ | $\text{Node}(5)$ | $4 \to \text{null}$ |
| 2 | $\text{Node}(5)$ | `null` | $\text{Node}(5).\text{next} \leftarrow \text{Node}(4)$ | $\text{Node}(5)$ | `null`, so the loop ends | $5 \to 4 \to \text{null}$ |

Caching `nxt` before overwriting the link is what makes the walk safe: after
iteration 1 the only surviving route from $\text{Node}(4)$ is backwards, so
without the saved $\text{Node}(5)$ the tail would be lost.

---

## 5. Algorithmic Correctness

**Soundness.** Phase 1 partitions the list into lengths $\lceil N/2 \rceil$ and $\lfloor N/2 \rfloor$. Phase 2 reverses the second half, so nodes are visited from tail inward ($L_n, L_{n-1}, \dots$). Phase 3 alternates links between the forward list and reversed backward list. Since the first half is always equal to or exactly 1 node longer than the second half, the zipper completes with the median node at the tail without cycles.

**Completeness.** Every node belongs to either the first half or the second half. No nodes are dropped or overwritten during the pointer rewiring.

---

## 6. Traps This Instance Exposes

- **Failing to Sever `slow.next = None`:** Omitting `slow.next = None` leaves the first half connected to the second half, producing a circular cycle ($3 \to 4$ and $4 \to 3$) during the merge!
- **Even vs Odd Length Parity:** On even-length lists like $[1, 2, 3, 4]$, `slow` stops at $2$. $L_1 = [1, 2]$ and $L_2 = [3, 4] \implies [4, 3]$. Merging gives $1 \to 4 \to 2 \to 3 \to \text{null}$, matching exact parity.
- **Short Lists ($N \le 2$):** If `not head or not head.next or not head.next.next: return`, the list is already reordered.

### Split Sizes and Outcomes Across Representative Instances

The split point depends on parity, and on very short lists the midpoint loop
never runs. Each row below is the full three-phase outcome for one input.

| Input | Where Phase 1 stops with `slow` | First half $L_1$ | Second half after reversal | Merged output |
|:---|:---|:---|:---|:---|
| $[1, 2, 3, 4, 5]$ | $\text{Node}(3)$, the exact median | $1 \to 2 \to 3$ | $5 \to 4$ | $[1, 5, 2, 4, 3]$ |
| $[1, 2, 3, 4]$ | $\text{Node}(2)$, the lower median | $1 \to 2$ | $4 \to 3$ | $[1, 4, 2, 3]$ |
| $[1, 1, 2, 2, 3, 3]$ | the node of value $2$ at index $2$ | $1 \to 1 \to 2$ | $3 \to 3 \to 2$ | $[1, 3, 1, 3, 2, 2]$, so equal values never merge into one node |
| $[8, 9]$ | $\text{Node}(8)$; the `fast.next.next` test fails at once | $8$ | $9$ | $[8, 9]$, unchanged |
| $[1]$ | $\text{Node}(1)$; the `fast.next` test fails at once | $1$ | empty — the reversal loop never starts | $[1]$, unchanged |

The first half is never shorter than the second: for odd $N$ it holds
$\lceil N/2 \rceil = 3$ of the five nodes, and for even $N$ the halves are equal.
That imbalance is exactly what leaves the median node as the final tail after
the zipper stops.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes. Phase 1 takes $N/2$ steps, Phase 2 takes $N/2$ steps, and Phase 3 takes $N/2$ steps. Total operations $= \frac{3}{2}N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, performing all mutations in place using pointer variables.