# Guided Example: Remove Nth Node From End of List

We trace the step-by-step execution of the one-pass, two-pointer gap technique on a representative linked list instance:

- **Input:** $\text{head} = [1, 2, 3, 4, 5]$, $n = 2$
- **Required output:** $[1, 2, 3, 5]$

This instance demonstrates sentinel node anchoring, establishing a fixed $n$-step pointer offset between `fast` and `slow` cursors, synchronous single-pass traversal, and safe in-place node deletion.

---

## 1. Instance & Teaching Goal

Given the head of a linked list with $L = 5$ nodes and an offset $n = 2$, we must remove the $2^{\text{nd}}$ node from the end (node with value $4$) and return the updated head.

A naive two-pass approach traverses the list once to measure the total length $L$, then executes a second pass to index $(L - n)$ to perform deletion. 

The optimal one-pass algorithm uses two pointers separated by an exact gap of $n$ nodes. When the lead pointer (`fast`) reaches the end of the list, the trailing pointer (`slow`) arrives precisely at the predecessor of the target node, allowing deletion in a single pass with $O(1)$ auxiliary space.

The competing strategies differ in how much they must remember, which is the only reason the two-pass approach is not simply shorter:

| Strategy | Structural Passes | Pointer Advances on the Traced List ($L = 5$, $n = 2$) | Auxiliary Space | Tradeoff |
|:---|:---|:---|:---|:---|
| Count $L$, then walk to index $L - n$ | Two: one to measure, one to reach the predecessor | $5$ advances to count, then $3$ advances to reach index $3$ | $O(1)$ | Simple, but the deletion index is unknown until the entire list has been counted |
| Unwind recursively from the tail | One traversal, with the work deferred to the returns | $5$ calls before the innermost return, then $5$ unwinds | $O(L) = 5$ frames, growing with the list | A list of length $L = 30$ needs $30$ frames, so the auxiliary space scales with the input |
| Store node references in an array | One traversal | $5$ advances to fill the container | $O(L) = 5$ references | Gives direct indexing, but allocates a second container as large as the list |
| One-pass fixed-gap scan with a sentinel | One traversal | `fast` advances $L + 1 = 6$ times; `slow` advances $L - n = 3$ times | $O(1)$ | Chosen: the fixed gap encodes the offset directly, so neither the length nor a container is needed |

---

## 2. Conceptual Foundation & Invariants

### Sentinel Node
To eliminate special cases when deleting the first node of the list (e.g. when $n = L$), we prepend a sentinel node $\text{dummy}$ pointing to $\text{head}$:
$$
\text{dummy} \to 1 \to 2 \to 3 \to 4 \to 5 \to \text{None}
$$

### The Fixed-Gap Invariant
1. **Gap Creation:** Start both $\text{fast}$ and $\text{slow}$ at $\text{dummy}$. Advance $\text{fast}$ forward by $n + 1$ steps (or advance $\text{fast}$ by $n$ steps starting from $\text{head}$).
2. **Lockstep Traversal:** Advance both $\text{fast}$ and $\text{slow}$ by one node simultaneously until $\text{fast}$ reaches $\text{None}$.
3. **Distance Relationship:** Because $\text{fast}$ is always $n + 1$ nodes ahead of $\text{slow}$, when $\text{fast}$ moves past the tail (reaching $\text{None}$ at index $L + 1$), $\text{slow}$ is positioned at index:
   $$
   (L + 1) - (n + 1) = L - n
   $$
   Node $L - n$ is the node *immediately before* the $n$-th node from the end.
4. **Bypass Link:** Set $\text{slow.next} \leftarrow \text{slow.next.next}$.

> **Invariant.** Throughout synchronous traversal, $\text{distance}(\text{slow}, \text{fast}) = n + 1$. When $\text{fast}$ reaches $\text{None}$, $\text{slow.next}$ is guaranteed to be the exact target node.

---

## 3. Step-by-Step Worked Execution

We trace list $[1, 2, 3, 4, 5]$ with $n = 2$:

### Phase 1: Initialize Sentinel and Create Gap
- Attach sentinel: $\text{dummy.next} \to 1$.
- Initialize pointers: $\text{slow} = \text{dummy}$, $\text{fast} = \text{dummy}$.
- Advance $\text{fast}$ by $n + 1 = 3$ steps:
  - Step 1: $\text{fast} \to \text{Node}(1)$
  - Step 2: $\text{fast} \to \text{Node}(2)$
  - Step 3: $\text{fast} \to \text{Node}(3)$
- Gap established: $\text{slow}$ is at $\text{dummy}$, $\text{fast}$ is at $\text{Node}(3)$ (distance = 3).

---

### Phase 2: Synchronous Lockstep Traversal
Both pointers advance one step at a time until $\text{fast} = \text{None}$:

- **Iteration 1:**
  - $\text{slow}$ moves to $\text{Node}(1)$
  - $\text{fast}$ moves to $\text{Node}(4)$
- **Iteration 2:**
  - $\text{slow}$ moves to $\text{Node}(2)$
  - $\text{fast}$ moves to $\text{Node}(5)$
- **Iteration 3:**
  - $\text{slow}$ moves to $\text{Node}(3)$
  - $\text{fast}$ moves to $\text{None}$ (past tail $\text{Node}(5)$)
- Traversal halts because $\text{fast}$ is $\text{None}$.

---

### Phase 3: Node Deletion & Extraction
- $\text{slow}$ is currently at $\text{Node}(3)$.
- Target node to delete: $\text{slow.next} = \text{Node}(4)$.
- Bypass target node:
  $$
  \text{slow.next} \leftarrow \text{slow.next.next} = \text{Node}(5)
  $$
- Chain becomes: $\text{dummy} \to 1 \to 2 \to 3 \to 5 \to \text{None}$.
- Return $\text{dummy.next} = \text{Node}(1)$.

---

## 4. Complete Execution Trace

### Pointer Movement Table

| Step | Phase | $\text{slow}$ Position | $\text{slow}$ Node Value | $\text{fast}$ Position | $\text{fast}$ Node Value | Offset Between Cursors |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 0 | Setup Sentinel | Index 0 | $\text{dummy}$ | Index 0 | $\text{dummy}$ | 0 |
| 1 | Advance $\text{fast}$ | Index 0 | $\text{dummy}$ | Index 1 | 1 | 1 |
| 2 | Advance $\text{fast}$ | Index 0 | $\text{dummy}$ | Index 2 | 2 | 2 |
| 3 | Advance $\text{fast}$ | Index 0 | $\text{dummy}$ | Index 3 | 3 | **3 ($n+1$)** |
| 4 | Lockstep Step 1 | Index 1 | 1 | Index 4 | 4 | 3 |
| 5 | Lockstep Step 2 | Index 2 | 2 | Index 5 | 5 | 3 |
| 6 | Lockstep Step 3 | Index 3 | **3** | Index 6 | $\text{None}$ | 3 (Terminal) |
| 7 | Rewire Link | Index 3 | 3 ($\text{next} \to 5$) | - | - | Node 4 bypassed |

### Memory Diagram

```text
Initial:  dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> None
                                  ^      |      ^
                                  |   (remove)  |
Final:    dummy -> [1] -> [2] -> [3] -----------> [5] -> None
```

---

## 5. Algorithmic Correctness

**Soundness.** Prepending $\text{dummy}$ guarantees that $\text{slow}$ always points to a valid list node whose `.next` reference exists. By advancing $\text{slow.next} = \text{slow.next.next}$, the target node is unlinked from the chain without modifying any other links or creating disconnected memory leaks.

**Completeness.** A list of length $L$ has indices $1$ to $L$. The $n$-th node from the end is located at 1-based index $L - n + 1$. Its preceding node is at index $L - n$. Because $\text{fast}$ traverses exactly $L + 1$ steps to reach $\text{None}$, keeping $\text{slow}$ exactly $n + 1$ steps behind places $\text{slow}$ at index $(L + 1) - (n + 1) = L - n$, which is precisely the target's predecessor.

---

## 6. Traps This Instance Exposes

- **Deleting the Head Node ($n = L$):** When $n = L$, the node to delete is the first node ($\text{head}$). Without a sentinel, $\text{slow}$ would need to point before `head`, which is invalid. The $\text{dummy}$ node handles this cleanly: $\text{slow}$ remains at $\text{dummy}$, and $\text{dummy.next}$ is set to $\text{head.next}$.
- **Single-Node List ($L = 1, n = 1$):** If the list has only one node, $\text{dummy.next} = \text{head}$. After the loop, $\text{slow}$ is at $\text{dummy}$, and $\text{dummy.next} \leftarrow \text{head.next} = \text{None}$. The function correctly returns an empty list ($\text{None}$).
- **Two-Pass vs One-Pass:** Counting length $L$ in a first pass requires traversing the list twice. The $n$-gap technique achieves true single-pass execution while visiting each node at most once.

The positions can be read off arithmetically, and doing so makes the two boundary shapes mechanical rather than special:

| Instance | $L$ | $n$ | Removed 1-Based Index $L - n + 1$ | Removed Value | Final $\text{slow}$ Index $L - n$ | $\text{slow}$ Node | Output |
|:---|:---:|:---:|:---:|:---:|:---:|:---|:---|
| `[1, 2, 3, 4, 5]` | 5 | 2 | 4 | 4 | 3 | $\text{Node}(3)$ | `[1, 2, 3, 5]` |
| `[1, 2]` | 2 | 1 | 2 | 2 | 1 | $\text{Node}(1)$ | `[1]` |
| `[1, 2]` | 2 | 2 | 1 | 1 | 0 | $\text{dummy}$ | `[2]` |
| `[1]` | 1 | 1 | 1 | 1 | 0 | $\text{dummy}$ | `[]` |
| `[4, 8, 15, 16, 23, 42]` | 6 | 3 | 4 | 16 | 3 | $\text{Node}(15)$ | `[4, 8, 15, 23, 42]` |
| `[0, 1, \dots, 29]` | 30 | 15 | 16 | 15 | 15 | $\text{Node}(14)$ | the same list with the value $15$ removed |

The two rows with $\text{slow}$ index $0$ are the ones that would break without the sentinel: the predecessor of the head is the sentinel itself, so the bypass $\text{slow.next} \leftarrow \text{slow.next.next}$ reduces to $\text{dummy.next} \leftarrow \text{head.next}$ with no separate branch.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$, where $L$ is the number of nodes in the linked list. The `fast` pointer advances through $L + 1$ nodes, visiting each node exactly once.
- **Auxiliary Space Complexity:** $O(1)$. Only two scalar pointer references (`slow` and `fast`) and one sentinel node are allocated, operating strictly in-place.
