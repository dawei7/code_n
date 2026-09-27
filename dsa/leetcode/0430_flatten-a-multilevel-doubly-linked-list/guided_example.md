# Guided Example: Flatten a Multilevel Doubly Linked List

We trace the step-by-step preorder recursive traversal, child list splicing, bidirectional pointer rewiring (`prev` and `next`), child pointer nullification, and subsegment tail reconnection on representative multilevel doubly linked lists:

- **Input:** Multilevel doubly linked list:
  ```text
  1 --- 2 --- 3 --- 4 --- 5 --- 6
              |
              7 --- 8 --- 9 --- 10
                    |
                    11 --- 12
  ```
- **Required output:** Flat doubly linked list:
  $$
  1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 7 \rightleftharpoons 8 \rightleftharpoons 11 \rightleftharpoons 12 \rightleftharpoons 9 \rightleftharpoons 10 \rightleftharpoons 4 \rightleftharpoons 5 \rightleftharpoons 6
  $$
- **Execution trace:**
  - Traverse Level 1:
    - Node $1 \rightleftharpoons 2 \rightleftharpoons 3$.
  - At Node $3$:
    - Child exists: Node $7$.
    - Save original successor: $next\_node = 4$.
    - Recurse on child sublist starting at $7$:
      - Node $7 \rightleftharpoons 8$.
      - At Node $8$:
        - Child exists: Node $11$.
        - Save original successor: $8.next = 9$.
        - Recurse on child sublist starting at $11$:
          - Nodes $11 \rightleftharpoons 12$. Node $12$ is tail.
          - Wire $8 \rightleftharpoons 11$, clear $8.child = \text{None}$.
          - Wire tail $12 \rightleftharpoons 9$.
          - Return tail of level 2 sublist: Node $10$.
      - Level 2 finishes with tail Node $10$.
    - Wire Node $3 \rightleftharpoons 7$. Clear $3.child = \text{None}$.
    - Wire tail $10 \rightleftharpoons 4$.
  - Continue traversing: $4 \rightleftharpoons 5 \rightleftharpoons 6$.
  - Resulting list is completely linear with all `child` pointers set to `None`.
- **Empty List Instance:** $head = \text{None} \implies \text{None}$
- **Single Node Without Child:** $head = [1] \implies [1]$

This instance demonstrates recursive structural tree flattening into a linear doubly linked list, mathematically proves why returning the subsegment tail enables $O(1)$ splicing without rescanning, and achieves $O(N)$ runtime and $O(D)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the head of a doubly linked list where each node has a `next`, `prev`, and an optional `child` pointer that may point to a separate doubly linked list:
Flatten the list so that all nodes appear in a single-level doubly linked list.
Nodes from the child list must appear **immediately following** the parent node and **before** the parent's original `next` node (preorder tree traversal order). All `child` pointers must be set to `None`.

```text
Multilevel Structure:
  1 <===> 2 <===> 3 <===> 4 <===> 5 <===> 6
                  |
                  7 <===> 8 <===> 9 <===> 10
                          |
                          11 <===> 12

Flattened Preorder Sequence:
  1 <=> 2 <=> 3 <=> 7 <=> 8 <=> 11 <=> 12 <=> 9 <=> 10 <=> 4 <=> 5 <=> 6
```

### The Splicing and Tail Problem
When node $u$ has a child list $C$:
1. $u.next$ must be redirected to $C$.
2. The child's `prev` pointer must point back to $u$: $C.prev = u$.
3. $u.child$ must be set to `None`.
4. The **tail node** of the flattened child branch must be connected to $u$'s original successor: $tail.next = original\_next$ and $original\_next.prev = tail$.
If we had to scan the child list to find its tail on every splice, repeated deep nestings could cause $O(N^2)$ time.
By designing the recursion to **return the tail node** of the flattened sublist, each splice is wired in $O(1)$ operations, achieving strict $O(N)$ linear time.

---

## 2. Conceptual Foundation & Invariants

### 1. Preorder Splicing Function:
Define a function `flatten_tail(curr)` that flattens the list starting at `curr` and **returns the last node (tail)** of the flattened segment:
1. Walk through the list with `curr`:
   - If `curr.child` is present:
     - Save original successor: $nxt = curr.next$.
     - Recursively flatten the child: $child\_tail = \text{flatten\_tail}(curr.child)$.
     - Wire parent to child:
       $$
       curr.next \leftarrow curr.child, \quad curr.child.prev \leftarrow curr
       $$
       $$
       curr.child \leftarrow \text{None}
       $$
     - Wire child tail to original successor (if $nxt$ exists):
       $$
       child\_tail.next \leftarrow nxt, \quad nxt.prev \leftarrow child\_tail
       $$
     - Move cursor to $child\_tail$ (or $nxt$).
   - Advance cursor: $tail \leftarrow curr, \; curr \leftarrow curr.next$.
2. Return $tail$.

> **Invariant.** After `flatten_tail(node)` returns, the sublist starting at `node` forms an unbroken, strictly 1-level doubly linked list where every `child` pointer is `None`, and the returned node is the unique terminal element.

---

## 3. Step-by-Step Worked Execution

We trace the representative list:

---

### Step 1: Traverse Nodes 1 and 2
- Node 1: no child $\implies$ advance to 2.
- Node 2: no child $\implies$ advance to 3.

---

### Step 2: Encounter Node 3 with Child 7
- Save successor: $nxt_3 = 4$.
- Recurse on child sublist starting at Node 7:
  - Node 7: no child $\implies$ advance to 8.
  - Node 8 has child: Node 11.
    - Save successor: $nxt_8 = 9$.
    - Recurse on child sublist starting at Node 11:
      - Node 11: no child $\implies$ advance to 12.
      - Node 12: no child, end of list.
      - Returns tail: Node 12.
    - Wire Node 8 to Node 11:
      $$
      8.next \leftarrow 11, \quad 11.prev \leftarrow 8, \quad 8.child \leftarrow \text{None}
      $$
    - Wire child tail 12 to saved successor 9:
      $$
      12.next \leftarrow 9, \quad 9.prev \leftarrow 12
      $$
    - Sublist from 8 is now: $8 \rightleftharpoons 11 \rightleftharpoons 12 \rightleftharpoons 9$.
  - Continue traversing: advance to Node 9, then Node 10.
  - Node 10: end of list.
  - Returns tail of Level 2: Node 10.

---

### Step 3: Splice Level 2 into Level 1 at Node 3
- Wire Node 3 to Node 7:
  $$
  3.next \leftarrow 7, \quad 7.prev \leftarrow 3, \quad 3.child \leftarrow \text{None}
  $$
- Wire child tail 10 to saved successor 4:
  $$
  10.next \leftarrow 4, \quad 4.prev \leftarrow 10
  $$
- Complete list so far:
  $$
  1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 7 \rightleftharpoons 8 \rightleftharpoons 11 \rightleftharpoons 12 \rightleftharpoons 9 \rightleftharpoons 10 \rightleftharpoons 4
  $$

---

### Step 4: Continue Traversing Remaining Level 1 Nodes
- From Node 4, advance to Node 5, then Node 6.
- Node 6: end of list.
- Entire list is now linear! Return `head = 1`.

---

## 4. Complete Execution Trace

| Step | Current Node | Child Pointer | Spliced Sublist | Saved `nxt` | Child Tail Returned | Link Adjustments Applied |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| **1** | Node $1$ | `None` | — | Node $2$ | — | None |
| **2** | Node $2$ | `None` | — | Node $3$ | — | None |
| **3** | Node $3$ | Node $7$ | Calls sublist $7\dots 10$ | Node $4$ | Node $10$ | $3 \rightleftharpoons 7, \; 10 \rightleftharpoons 4, \; 3.child = \text{None}$ |
| $\to$ Sub | Node $7$ | `None` | — | Node $8$ | — | None |
| $\to$ Sub | Node $8$ | Node $11$ | Calls sublist $11\dots 12$ | Node $9$ | Node $12$ | $8 \rightleftharpoons 11, \; 12 \rightleftharpoons 9, \; 8.child = \text{None}$ |
| $\to\to$ Sub | Node $11$ | `None` | — | Node $12$ | — | None |
| $\to\to$ Sub | Node $12$ | `None` | Tail of level 3 | `None` | **Node $12$** | End of sublist |
| $\to$ Sub | Node $9$ | `None` | — | Node $10$ | — | None |
| $\to$ Sub | Node $10$ | `None` | Tail of level 2 | `None` | **Node $10$** | End of sublist |
| **4** | Node $4$ | `None` | — | Node $5$ | — | Resumed from $10 \rightleftharpoons 4$ |
| **5** | Node $5$ | `None` | — | Node $6$ | — | None |
| **6** | Node $6$ | `None` | End of list | `None` | **Node $6$** | Flattening complete |

---

## 5. Boundary Cases & Failure Modes

- **Empty List ($head = \text{None}$):** Returns `None` immediately without null pointer exceptions.
- **Child at Last Node of Level ($5 \to 6$ with $6.child = 7$):** Saved successor $nxt$ is `None`. The child tail becomes the new global tail, and no `tail.next` assignment to null is attempted.
- **Single Node with Child ($1$ with $1.child = 2$):** $nxt = \text{None}$. Wires $1 \rightleftharpoons 2$, returns $1$.
- **No Children Anywhere:** Traverses the original list without modifications, clearing 0 children, returning original head.

---

## 6. Traps & Common Anti-Patterns

- **Leaving `child` Pointers Dangling:** Forgetting to set `curr.child = None` leaves child references in the returned list, violating the problem contract.
- **Unidirectional Splicing:** Wiring `curr.next = child` and `child_tail.next = nxt` without updating `child.prev = curr` and `nxt.prev = child_tail` breaks the doubly linked list invariants.
- **Quadratic Rescanning:** Failing to return the tail from recursive calls forces a linear scan to find the end of each child list, degrading runtime from $O(N)$ to $O(N^2)$ on left-skewed multilevel chains.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each node is visited exactly twice: once when advancing forward and once when spliced.
  - Every pointer update is performed in $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(D)$ where $D$ is the maximum multilevel nesting depth, representing the recursion stack.
  - In the worst case of completely nested lists, $D \le N$.
  - In-place transformation allocates zero new nodes.