# Guided Example: Design Linked List

We trace the step-by-step dummy sentinel head initialization, predecessor node traversal ($index$ steps from $dummy$), head and tail insertion delegation ($addAtIndex(0, val)$ / $addAtIndex(cnt, val)$), arbitrary-index node insertion ($pre.next = \text{Node}(val, pre.next)$), middle-node deletion ($pre.next \leftarrow pre.next.next$), and 0-indexed element retrieval on representative linked list mutations:

- **Input:**
  - Operations sequence:
    ```text
    MyLinkedList()
    addAtHead(1)
    addAtTail(3)
    addAtIndex(1, 2)
    get(1)
    deleteAtIndex(1)
    get(1)
    ```
- **Required output:** `[2, 3]`
  - Linked List operations:
    - `addAtHead(val)`: Prepend a new node with $val$ before the current head.
    - `addAtTail(val)`: Append a new node with $val$ after the current tail.
    - `addAtIndex(index, val)`: Insert a node with $val$ immediately before the $index$-th node. If $index = cnt$, append to the tail. If $index > cnt$, ignore.
    - `deleteAtIndex(index)`: Delete the $index$-th node if valid ($0 \le index < cnt$).
    - `get(index)`: Retrieve the value of the $index$-th node. If invalid index, return $-1$.
    - Lifecycle trace:
      - Initially empty.
      - `addAtHead(1)`: List is $[1]$.
      - `addAtTail(3)`: List is $[1, 3]$.
      - `addAtIndex(1, 2)`: Insert $2$ at index 1 $\implies$ list is $[1, 2, 3]$.
      - `get(1)`: Index 1 contains value **`2`**.
      - `deleteAtIndex(1)`: Remove node at index 1 $\implies$ list is $[1, 3]$.
      - `get(1)`: Index 1 now contains value **`3`**.
      - Results: `[2, 3]`.
- **The Dummy Sentinel Node & Predecessor Traversal Invariant:**
  - **The Dummy Head Invariant:**
    - Maintain a fixed dummy node $dummy$ whose $.next$ pointer always references the true head of the linked list:
      $$
      dummy \to \text{Head} \to \text{Node}_1 \to \dots \to \text{null}
      $$
    - Why use a dummy head?
      - Inserting or deleting at index 0 (the head) modifies the exact same pointer as inserting or deleting at index $k > 0$.
      - Zero special-casing for empty lists or head changes!
  - **The Predecessor Traversal Rule:**
    - To insert or delete at index $k$, begin at $pre = dummy$ and advance $k$ steps:
      $$
      pre \leftarrow pre.next \quad (k \text{ times})
      $$
    - Because the traversal begins at $dummy$ (which is 1 position before index 0), advancing $k$ times places $pre$ **strictly at the predecessor** of target index $k$.
  - **Pointer Mutations:**
    - **Insertion:**
      $$
      \text{newNode}.next \leftarrow pre.next
      $$
      $$
      pre.next \leftarrow \text{newNode}
      $$
      $$
      cnt \leftarrow cnt + 1
      $$
    - **Deletion:**
      $$
      pre.next \leftarrow pre.next.next
      $$
      $$
      cnt \leftarrow cnt - 1
      $$
- **Step-by-Step Worked Execution Trace on the Sample Sequence:**
  - Initialization: $dummy \to \text{null}, \; cnt = 0$.
  - **Operation 1: `addAtHead(1)`:**
    - Delegates to `addAtIndex(0, 1)`.
    - Start at $pre = dummy$. Advance 0 steps $\implies pre = dummy$.
    - Splice new node with value 1:
      $$
      \text{newNode}(1).next \leftarrow dummy.next \; (\text{null})
      $$
      $$
      dummy.next \leftarrow \text{newNode}(1)
      $$
      $$
      cnt \leftarrow 1
      $$
    - List: $dummy \to [1] \to \text{null}$.
  - **Operation 2: `addAtTail(3)`:**
    - Delegates to `addAtIndex(1, 3)`.
    - Start at $pre = dummy$. Advance 1 step $\implies pre = \text{Node}(1)$.
    - Splice new node with value 3:
      $$
      \text{newNode}(3).next \leftarrow pre.next \; (\text{null})
      $$
      $$
      pre.next \leftarrow \text{newNode}(3)
      $$
      $$
      cnt \leftarrow 2
      $$
    - List: $dummy \to [1] \to [3] \to \text{null}$.
  - **Operation 3: `addAtIndex(1, 2)`:**
    - Target index: 1, Value: 2.
    - Start at $pre = dummy$. Advance 1 step:
      $$
      pre = pre.next = \text{Node}(1)
      $$
    - Splice new node:
      $$
      \text{newNode}(2).next \leftarrow pre.next \; (\text{Node } 3)
      $$
      $$
      pre.next \leftarrow \text{newNode}(2)
      $$
      $$
      cnt \leftarrow 3
      $$
    - List: $dummy \to [1] \to [2] \to [3] \to \text{null}$.
  - **Operation 4: `get(1)`:**
    - Target index: 1.
    - Valid check: $0 \le 1 < 3$ (Valid).
    - Start at $cur = dummy.next = \text{Node}(1)$.
    - Advance 1 step: $cur = cur.next = \text{Node}(2)$.
    - Value at $cur$: $2$.
    - Emit output:
      $$
      ans \leftarrow \mathbf{2}
      $$
  - **Operation 5: `deleteAtIndex(1)`:**
    - Target index: 1.
    - Valid check: $1 < 3$ (Valid).
    - Start at $pre = dummy$. Advance 1 step:
      $$
      pre = pre.next = \text{Node}(1)
      $$
    - Bypass target node (Node 2):
      $$
      target = pre.next \; (\text{Node } 2)
      $$
      $$
      pre.next \leftarrow target.next \; (\text{Node } 3)
      $$
      $$
      cnt \leftarrow cnt - 1 = 2
      $$
    - List: $dummy \to [1] \to [3] \to \text{null}$.
  - **Operation 6: `get(1)`:**
    - Target index: 1.
    - Valid check: $0 \le 1 < 2$ (Valid).
    - Start at $cur = dummy.next = \text{Node}(1)$.
    - Advance 1 step: $cur = cur.next = \text{Node}(3)$.
    - Value at $cur$: $3$.
    - Emit output:
      $$
      ans \leftarrow \mathbf{3}
      $$
  - **Consolidated Outputs:**
    $$
    [\mathbf{2}, \; \mathbf{3}]
    $$
- **Out of Bounds Index Rejection:**
  - `get(5)` when $cnt = 2$: $5 \ge cnt \implies$ returns $-1$.
  - `addAtIndex(5, 10)` when $cnt = 2$: $5 > cnt \implies$ ignores insertion.
  - `deleteAtIndex(5)` when $cnt = 2$: $5 \ge cnt \implies$ ignores deletion.

This instance demonstrates fundamental singly-linked list pointer manipulation and sentinel head invariants, mathematically proves why dummy nodes unify boundary and interior pointer mutations, and derives $O(1)$ head/tail operations, $O(K)$ arbitrary index operations, and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement a **Singly Linked List** supporting:
`addAtHead`, `addAtTail`, `addAtIndex`, `deleteAtIndex`, and `get`.

```text
Operations:
  addAtHead(1)     -> [ 1 ]
  addAtTail(3)     -> [ 1, 3 ]
  addAtIndex(1, 2) -> [ 1, 2, 3 ]
  get(1)           -> node at index 1 is 2 -> returns 2
  deleteAtIndex(1) -> removes node 2 -> [ 1, 3 ]
  get(1)           -> node at index 1 is 3 -> returns 3

Result: [ 2, 3 ]
```

### The Invariant of the Dummy Sentinel Head
- Maintaining a `dummy` node whose `.next` points to the head guarantees that every valid node (including index 0) has a preceding node.
- Advancing $k$ steps from $dummy$ lands on index $k-1$ (the predecessor), allowing unified insertion and deletion logic across all positions.

---

## 2. Conceptual Foundation & Invariants

### 1. Unified Splicing Operations:
To insert at index $k$:
$$
pre = dummy \xrightarrow{\text{step } k \text{ times}} \text{Node}_{k-1}
$$
$$
pre.next \leftarrow \text{ListNode}(val, \; pre.next)
$$
To delete at index $k$:
$$
pre = dummy \xrightarrow{\text{step } k \text{ times}} \text{Node}_{k-1}
$$
$$
pre.next \leftarrow pre.next.next
$$

### 2. Size Conservation:
$$
cnt_{new} = \begin{cases} cnt + 1 & \text{on successful add} \\ cnt - 1 & \text{on successful delete} \end{cases}
$$

> **Sentinel-Uniform Predecessor Invariant.** In any singly linked list augmented with a left sentinel $S$, the $k$-th element is strictly the target of the successor pointer of the $k$-th step in the traversal sequence initialized at $S$, establishing a universal bijection between indices $k \in [0, n]$ and reachable pointer slots.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `addAtHead(1)`
- Splice after $dummy \implies dummy \to [1] \to \text{null}$.

---

### Step 2: `addAtTail(3)`
- Advance 1 step to $[1]$. Splice $[3] \implies dummy \to [1] \to [3] \to \text{null}$.

---

### Step 3: `addAtIndex(1, 2)`
- Advance 1 step to $[1]$. Splice $[2] \implies dummy \to [1] \to [2] \to [3] \to \text{null}$.

---

### Step 4: `get(1)`
- Node at index 1 is **`2`**.

---

### Step 5: `deleteAtIndex(1)`
- Advance 1 step to $[1]$. Set $[1].next \leftarrow [3] \implies dummy \to [1] \to [3] \to \text{null}$.

---

### Step 6: `get(1)`
- Node at index 1 is now **`3`**.

---

## 4. Complete Execution Trace

| Step | Operation Invoked | Target Index | Predecessor Reached | Pointer Update | Linked List Topology | Returned Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `addAtHead(1)` | $0$ | $dummy$ | $dummy.next \to [1]$ | `[1]` | — |
| $2$ | `addAtTail(3)` | $1$ | Node $1$ | $1.next \to [3]$ | `[1, 3]` | — |
| $3$ | `addAtIndex(1, 2)`| $1$ | Node $1$ | $1.next \to [2] \to [3]$ | `[1, 2, 3]` | — |
| **$4$**| **`get(1)`** | **$1$** | — | Read Node $2$ | `[1, 2, 3]` | **`2`** |
| $5$ | `deleteAtIndex(1)`| $1$ | Node $1$ | $1.next \to [3]$ | `[1, 3]` | — |
| **$6$**| **`get(1)`** | **$1$** | — | Read Node $3$ | `[1, 3]` | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Insert at Head ($index = 0$):** Predecessor is $dummy$, correctly replaces head.
- **Insert at Tail ($index = cnt$):** Predecessor is current tail, appends seamlessly.
- **Index Out of Bounds ($index > cnt$ on add, $index \ge cnt$ on delete/get):** Handled safely with early return / $-1$.
- **Empty List Operations:** `get(0)` on empty list returns $-1$.

---

## 6. Traps & Common Anti-Patterns

- **Null Pointer Dereference without Dummy Head:** Trying to insert at index 0 without a dummy head requires special branch cases for `self.head is None`, frequently leading to bugs.
- **Off-By-One Steps on Predecessor:** Stepping $k + 1$ times from $dummy$ lands on the node itself instead of the predecessor, preventing pointer reassignment.
- **Forgetting to Update Count ($cnt$):** Failing to increment/decrement `self.cnt` breaks subsequent bounds checking.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `addAtHead(val)`: $\mathcal{O}(1)$ time.
  - `addAtTail(val)`: $\mathcal{O}(N)$ time (or $\mathcal{O}(1)$ if tail pointer maintained).
  - `addAtIndex(index, val)`: $\mathcal{O}(index) \le \mathcal{O}(N)$ time.
  - `deleteAtIndex(index)`: $\mathcal{O}(index) \le \mathcal{O}(N)$ time.
  - `get(index)`: $\mathcal{O}(index) \le \mathcal{O}(N)$ time.
  - Completes $2000$ operations in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for node structures, and $\mathcal{O}(1)$ auxiliary space per operation.
