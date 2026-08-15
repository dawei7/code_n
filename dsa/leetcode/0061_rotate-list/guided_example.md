# Guided Example: Rotate List

We execute the single-pass Linked List, Two Pointers pointer manipulation on a representative linked list instance.

- **Input:** `{"head": [1, 2, 3, 4, 5], "k": 2}`
- **Required output:** `[4, 5, 1, 2, 3]`

This instance demonstrates boundary positioning, sentinel pointer preservation, and in-place reference mutations without extra allocations.

---

## 1. Instance & Teaching Goal

The objective for **Rotate List** is to transform the linked structure by strictly updating `next` references in place.
A naive approach allocating new list nodes incurs unnecessary $O(N)$ auxiliary memory.
Using sentinel anchors and precise pointer reassignments guarantees $O(1)$ extra space while avoiding null reference dereferences.

---

## 2. Conceptual Foundation & Invariants

We introduce a dummy sentinel node pointing to the head to normalize edge conditions at the first node.

| Pointer Identifier | Targeted Node Role | Invariant State |
|---|---|---|
| $\text{dummy}$ | Sentinel node before head | Preserves immutable list entry point |
| $\text{prev}$ | Preceding subsegment anchor | Points to confirmed sorted/processed boundary |
| $\text{curr}$ | Active processing node | Advances linearly through input sequence |

> **Invariant.** At each step, all nodes before $\text{curr}$ maintain valid list structural integrity, and no reference to remaining unprocessed nodes is lost.

---

## 3. Step-by-Step Worked Execution

### Step 1: Sentinel Initialization & Anchor Positioning

- Attach $\text{dummy} \to \text{head}$.
- Position $\text{prev}$ at the target boundary and identify the initial active node $\text{curr}$.

| State Parameter | Configuration |
|---|---|
| Sentinel State | $\text{dummy.next} = \text{head}$ |
| Active Pointer | $\text{curr} = \text{prev.next}$ |
| Frontier Link | Reference to subsequent elements preserved |

---

### Step 2: In-Place Pointer Reconnection

- Cache the next candidate node $\text{next} = \text{curr.next}$.
- Splice and rewire links to incorporate $\text{next}$ into the desired target position.

| State Parameter | Configuration |
|---|---|
| Rewired Segment | References updated without node duplication |
| Active Cursor | Cursor advanced to next valid link |
| Suffix Link | Unprocessed remainder remains reachable |

---

### Step 3: Traversal Completion & Output Extraction

- Once all target nodes have been visited, the pointer chain is fully re-established.
- Return $\text{dummy.next}$ as the new head.

| State Parameter | Final State |
|---|---|
| Termination Condition | All target nodes processed |
| Head Extraction | $\text{dummy.next}$ |
| Integrity Check | Complete chain connected |

---

## 4. Complete Execution Trace

| Step | Active Node | Reference Action | Invariant State Maintained | Sublist Structure |
|---|---|---|---|---|
| 0 (Init) | Sentinel | Attach $\text{dummy} \to \text{head}$ | Anchor established | `dummy -> [initial list]` |
| 1 (Rewire) | Intermediate nodes | Splice `next` pointers | Monotonic sublist validity | In-place reordered subsegment |
| 2 (Finish) | Tail node | Connect final suffix | Complete chain preserved | Emitted result $\text{dummy.next}$ |

---

## 5. Algorithmic Correctness

**Soundness.** Because `next` references are cached prior to disconnection, no node becomes orphaned. Every pointer mutation preserves a valid path from $\text{dummy}$ to the terminal `None`.

**Completeness.** Traversal visits every targeted node exactly once, guaranteeing that all required operations are executed in full.

---

## 6. Traps This Instance Exposes

- **Head Boundary Mutation:** Operating directly on `head` without a sentinel causes null exceptions or lost references when the first node is modified.
- **Orphaned Sublists:** Overwriting `curr.next` before preserving `curr.next.next` disconnects and permanently loses the remaining list suffix.
- **Accidental Cycles:** Reconnecting backwards without clearing forward references creates infinite circular chains.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ single pass where $N$ is the number of nodes visited.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant extra memory; only a fixed set of pointer handles is maintained.