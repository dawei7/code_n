# Guided Example: Delete Node in a Linked List

We trace the step-by-step value copying, successor pointer bypass, and in-place node transformation without access to the list head or predecessor:

- **Input:** Linked list $4 \to 5 \to 1 \to 9$, given target node pointer $\text{node}$ referencing value $5$
- **Required output:** $4 \to 1 \to 9$ (Node $5$ eliminated; list reduced from 4 nodes to 3 nodes)
- **Penultimate Node Deletion:** $4 \to 5 \to 1 \to 9$, delete node $1 \implies 4 \to 5 \to 9$
- **Guaranteed Constraint:** Target $\text{node}$ is never the tail node ($\text{node.next}$ is guaranteed non-null)

This instance demonstrates the "Copy-and-Bypass" paradigm for unidirectional linked list deletion without predecessor pointers, proves why overwriting $\text{node.val}$ with its successor value and bypassing $\text{node.next.next}$ satisfies all external list invariants, and runs in strictly $O(1)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a singly linked list $4 \to 5 \to 1 \to 9$, delete the node with value $5$:
```text
4 -> [5] -> 1 -> 9 -> None
```
**Constraint:** We are **only given a direct reference to the target node (`node`)**. We have **no access to `head`**, and nodes in a singly linked list have no backward pointers (`prev`).

### The Predecessor Paradox
In standard linked list deletion:
To remove node $B$ from $A \to B \to C$, we set $A\text{.next} = C$.
However, without a pointer to node $A$, we cannot modify $A$'s `next` pointer!
How can node $B$ be deleted when no reference to $A$ exists?
Instead of physically removing node $B$:
1. **Copy the Successor:** Overwrite $B$'s payload with $C$'s payload ($B\text{.val} \leftarrow C\text{.val}$). Node $B$ now disguises itself as node $C$!
2. **Bypass the Duplicate Successor:** Rewire $B\text{.next} \leftarrow C\text{.next}$, disconnecting node $C$ from the list.
To any external observer, node $B$ has disappeared and the list structure is preserved!

---

## 2. Conceptual Foundation & Invariants

### The Copy-and-Bypass Protocol
Given node reference `node`:
1. **Payload Transfer:**
   Copy the value of the immediate successor:
   $$
   \text{node.val} \leftarrow \text{node.next.val}
   $$
2. **Pointer Bypass:**
   Skip over the immediate successor:
   $$
   \text{node.next} \leftarrow \text{node.next.next}
   $$

### Why This is Valid:
- The problem contract specifies: "By deleting the node, we do not mean removing it from memory. We mean the value should not exist, count decreases by 1, and order is preserved."
- Because $\text{node}$ is guaranteed **not to be the tail**, $\text{node.next}$ is always a valid node with a real value and a valid `next` reference.

> **Invariant.** After the two operations, the list contains precisely the elements in their original relative order with the target node's original value omitted, and the length is decreased by 1.

---

## 3. Step-by-Step Worked Execution

We trace the operation on $\text{head} = 4 \to 5 \to 1 \to 9$, given pointer $\text{node}$ referencing $5$:
Let nodes be $N_0(4) \to N_1(5) \to N_2(1) \to N_3(9) \to \text{None}$.
Target: $\text{node} = N_1$.

### Step 1: Examine State Before Deletion
- Predecessor $N_0(4)$ points to $N_1(5)$.
- Target $N_1(5)$ points to $N_2(1)$.
- Successor $N_2(1)$ points to $N_3(9)$.
- List: $4 \to 5 \to 1 \to 9$.

---

### Step 2: Copy Successor Value to Target Node
- Read successor value: $\text{node.next.val} = N_2\text{.val} = 1$.
- Overwrite target payload:
  $$
  N_1\text{.val} \leftarrow 1
  $$
- Intermediate list state:
  $$
  4 \to \mathbf{1} \to 1 \to 9 \to \text{None}
  $$
- Notice: The original value $5$ is completely erased! $N_1$ now carries value $1$.

---

### Step 3: Bypass Duplicate Successor Node
- Rewire pointer:
  $$
  N_1\text{.next} \leftarrow N_2\text{.next} = N_3(9)
  $$
- Successor $N_2$ is disconnected from the list.
- Resulting list structure:
  $$
  N_0(4) \longrightarrow N_1(1) \longrightarrow N_3(9) \longrightarrow \text{None}
  $$
- List values: $[4, 1, 9]$.
- Number of nodes: decreased from 4 to 3.
- Values before $5$ ($[4]$): order preserved.
- Values after $5$ ($[1, 9]$): order preserved.

Deletion complete in 2 operations!

Only two of the four references in play are allowed to move. The predecessor is never touched — that is the whole point of the technique — and the successor's own `next` link is left exactly as it was, which is why the nodes after the target stay attached in order.

| Reference | Before | After | Written by this algorithm? | Consequence |
|:---|:---|:---|:---:|:---|
| $N_0\text{.next}$ (predecessor) | $N_1(5)$ | $N_1(1)$ | no | The predecessor still points at the same object, so the list head never needs to know |
| $N_1\text{.val}$ (target payload) | $5$ | $1$ | yes, first assignment | The old value $5$ no longer exists anywhere in the chain |
| $N_1\text{.next}$ (target link) | $N_2(1)$ | $N_3(9)$ | yes, second assignment | $N_2$ falls out of the chain and the remaining order is untouched |
| $N_2\text{.next}$ (successor link) | $N_3(9)$ | $N_3(9)$ | no | The orphaned successor still points into the live list, so freeing it must not free $N_3$ |

---

## 4. Complete Execution Trace

```text
Initial List:
Node(4) -> Node(5) [node] -> Node(1) -> Node(9) -> None

Step 1: node.val = node.next.val
Node(4) -> Node(1) [node] -> Node(1) -> Node(9) -> None

Step 2: node.next = node.next.next
Node(4) -> Node(1) [node] -------------> Node(9) -> None

Final Traversal: 4 -> 1 -> 9 -> None
```

| Execution Step | Instruction Executed | Target Node Memory State | Node Payload Before / After | Resulting Linked List Chain |
|:---:|:---|:---:|:---:|:---|
| **0** | Initial State | $N_1$ (`next` $\to N_2$) | $N_1\text{.val} = 5$ | $4 \to 5 \to 1 \to 9$ |
| **1** | `node.val = node.next.val` | $N_1$ (`next` $\to N_2$) | $N_1\text{.val} = 1$ | $4 \to 1 \to 1 \to 9$ |
| **2** | `node.next = node.next.next` | $N_1$ (`next` $\to N_3$) | $N_1\text{.val} = 1$ | **$4 \to 1 \to 9$ (Complete)** |

---

## 5. Algorithmic Correctness

**Soundness.** Overwriting `node.val` with `node.next.val` and skipping `node.next` produces a linked list where:
1. The original `node.val` ($5$) is nowhere in the chain.
2. The successor value ($1$) appears exactly once at the position previously occupied by $5$.
3. All subsequent links ($N_3, \dots$) remain attached in their exact original order.
4. The list length is reduced by exactly one node.

**Completeness.** Because the problem guarantees `node` is not the tail, `node.next` is always a valid object, guaranteeing that `node.next.val` and `node.next.next` never raise null-pointer exceptions.

---

## 6. Traps This Instance Exposes

- **Attempting to Delete the Tail Node:** If `node` were the tail node, `node.next` would be `None`. There would be no successor to copy from, and this technique cannot work without a pointer to the predecessor! The problem explicitly guarantees that `node` is not the last node.
- **Dangling References in Memory:** In garbage-collected languages (like Python and Java), disconnected node $N_2$ is automatically collected. In C/C++, `ListNode* temp = node->next; ... delete temp;` must be called to prevent memory leaks.
- **Reference Equality:** If other external pointers held references to $N_2$, those references are now detached from the main list. Since the problem only evaluates list traversal from `head`, the solution is completely valid.

The same two assignments must cover every position the contract allows, and the rows below trace them on the authored cases. Read the fourth column as the *only* place the algorithm ever looks past the target, and the fifth column as what an observer traversing from the target node sees afterwards.

| Scenario | Sublist seen from `node` | Payload copied into the target | `node.next` after the bypass | Sequence read from `node` afterwards | What the invariant guarantees |
|:---|:---|:---:|:---|:---|:---|
| Interior node, short suffix | $[5, 1, 9]$ | $1$ | Node $(9)$ | $[1, 9]$ | The erased value $5$ is absent and the tail order is preserved |
| Node immediately before the tail | $[1, 9]$ | $9$ | `None` | $[9]$ | The target object becomes the new tail, so the bypass writes the null terminator; this is the only case where the successor's own link is `None` |
| Interior node, longer suffix | $[3, 4, 5, 6]$ | $4$ | Node $(5)$ | $[4, 5, 6]$ | Only one node disappears; every later node keeps its payload and its relative order |
| Successor payload equals the target payload | $[2, 2, 3, 2]$ | $2$ (no visible change) | Node $(3)$ | $[2, 3, 2]$ | A length check, not the value sequence, is what proves the deletion happened |
| Target is the tail (excluded by the contract) | $[9]$ | nothing to copy | undefined | not produced | No successor exists, so this technique has no legal move and a predecessor reference would be required |

Because no head or predecessor pointer is available, every design that deletes by relinking is off the table, and the remaining alternatives each pay somewhere else.

| Approach | Mechanism | Time | Auxiliary space | Why it is unavailable or worse here |
|:---|:---|:---:|:---:|:---|
| Predecessor walk from the head | Traverse to the node before the target, then point it past the target | $O(N)$ | $O(1)$ | Correct but unusable: the contract hands over only the target node, never `head` |
| Copy-and-bypass (this lesson) | Move the successor's payload into the target and unlink the successor | $O(1)$ | $O(1)$ | Depends on a non-null successor, so the tail node cannot be deleted this way |
| Store a predecessor link in every node | Deleting means pointing the predecessor and the successor at each other | $O(1)$ | $O(N)$ for the extra link per node | Changes the given data structure and its memory footprint before any deletion can be attempted |
| Rebuild the chain skipping the target | Walk from the head and relink only the kept nodes | $O(N)$ | $O(1)$ extra, or $O(N)$ for copied nodes | Needs a traversal from the head and re-creates most links to remove one value |
| Mark the node as deleted for external readers | Keep the node in the chain and set a flag that consumers honor | $O(1)$ to mark | $O(1)$ per node for the flag | Raw list length and payload sequence stay unchanged, so any consumer that ignores the flag sees a stale list |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. Exactly two pointer/value assignments are executed.
- **Auxiliary Space Complexity:** $O(1)$ constant memory. Zero new nodes or data structures are allocated.