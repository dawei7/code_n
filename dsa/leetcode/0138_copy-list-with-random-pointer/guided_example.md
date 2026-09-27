# Guided Example: Copy List with Random Pointer

We trace the step-by-step three-pass in-place node interweaving and random pointer synchronization on a representative linked list with arbitrary random references:

- **Input:** $\text{head} = [[7, \text{null}], [13, 0], [11, 4], [10, 2], [1, 0]]$
- **Required output:** Deep cloned list with identical values, next links, and random target links
- **Null Base Case:** $\text{head} = \text{null} \implies \text{null}$

This instance demonstrates in-place node cloning without auxiliary hash maps, interweaving copied nodes ($A \to A' \to B \to B'$), synchronizing random pointers in $O(1)$ extra space via $\text{curr.next.random} = \text{curr.random.next}$, and cleanly decoupling the interwoven chains back into two independent lists.

---

## 1. Instance & Teaching Goal

A linked list of length $n = 5$ has nodes where each node contains an integer `val`, a `next` pointer, and an additional `random` pointer that can point to any node in the list or `null`:
- Node 0: $\text{val} = 7, \quad \text{random} = \text{null}$
- Node 1: $\text{val} = 13, \quad \text{random} = \text{Node}(0)$
- Node 2: $\text{val} = 11, \quad \text{random} = \text{Node}(4)$
- Node 3: $\text{val} = 10, \quad \text{random} = \text{Node}(2)$
- Node 4: $\text{val} = 1, \quad \text{random} = \text{Node}(0)$

Construct a complete deep copy of the list. None of the pointers in the new list should point to nodes in the original list.

A hash map approach maps $\text{original} \to \text{clone}$, but consumes $O(N)$ extra space to store $N$ pointer pairs.
The optimal in-place algorithm temporarily weaves cloned nodes directly into the original list next to their source counterparts ($u \to u'$). This geometric relationship allows any clone to find its corresponding random clone in $O(1)$ operations via $u'.\text{random} = u.\text{random}.\text{next}$, achieving strictly $O(1)$ auxiliary memory.

---

## 2. Conceptual Foundation & Invariants

### The 3-Pass In-Place Interweaving Architecture

#### Pass 1: Duplicate and Interweave
Traverse the original list. For each node $u$:
- Create a clone $u' = \text{Node}(u.\text{val})$.
- Splice $u'$ immediately after $u$:
  $$
  u'.\text{next} = u.\text{next}, \quad u.\text{next} = u'
  $$
- Resulting chain: $A \to A' \to B \to B' \to C \to C' \to \dots$

#### Pass 2: Connect Cloned Random Pointers
For each original node $u$ (stepping two nodes at a time via $u = u.\text{next}.\text{next}$):
- If $u.\text{random}$ is not null:
  The clone of $u$ is $u.\text{next}$. The clone of $u.\text{random}$ is $u.\text{random}.\text{next}$.
  $$
  u.\text{next}.\text{random} \leftarrow u.\text{random}.\text{next}
  $$

#### Pass 3: Decouple Interwoven Lists
Restore the original list's `next` pointers while extracting the cloned chain:
- Separate $A \to A' \to B \to B'$ into original $A \to B \to C$ and clone $A' \to B' \to C'$.

> **Invariant.** During Pass 2, for every original node $u$, $u.\text{next}$ is its exact duplicate $u'$, and for any targeted node $v = u.\text{random}$, $v.\text{next}$ is its duplicate $v'$.

---

## 3. Step-by-Step Worked Execution

We trace the 5-node list:
Original nodes: $N_0(7), N_1(13), N_2(11), N_3(10), N_4(1)$.

### Pass 1: Duplicate and Interweave
- Clone $N_0(7) \to C_0(7)$: $N_0.\text{next} = C_0, \, C_0.\text{next} = N_1$.
- Clone $N_1(13) \to C_1(13)$: $N_1.\text{next} = C_1, \, C_1.\text{next} = N_2$.
- Clone $N_2(11) \to C_2(11)$: $N_2.\text{next} = C_2, \, C_2.\text{next} = N_3$.
- Clone $N_3(10) \to C_3(10)$: $N_3.\text{next} = C_3, \, C_3.\text{next} = N_4$.
- Clone $N_4(1) \to C_4(1)$: $N_4.\text{next} = C_4, \, C_4.\text{next} = \text{null}$.

Interwoven List:
$$
N_0 \to C_0 \to N_1 \to C_1 \to N_2 \to C_2 \to N_3 \to C_3 \to N_4 \to C_4 \to \text{null}
$$

---

### Pass 2: Assign Cloned Random Pointers
Traverse original nodes $N_0 \dots N_4$:
- **Node $N_0$:** $N_0.\text{random} = \text{null} \implies C_0.\text{random} = \text{null}$.
- **Node $N_1$:** $N_1.\text{random} = N_0$.
  - Clone $C_1 = N_1.\text{next}$.
  - Target clone: $N_0.\text{next} = C_0$.
  - Assign: $C_1.\text{random} \leftarrow C_0$.
- **Node $N_2$:** $N_2.\text{random} = N_4$.
  - Assign: $C_2.\text{random} \leftarrow N_4.\text{next} = C_4$.
- **Node $N_3$:** $N_3.\text{random} = N_2$.
  - Assign: $C_3.\text{random} \leftarrow N_2.\text{next} = C_2$.
- **Node $N_4$:** $N_4.\text{random} = N_0$.
  - Assign: $C_4.\text{random} \leftarrow N_0.\text{next} = C_0$.

All cloned random pointers are correctly linked to cloned nodes!

---

### Pass 3: Decouple Interwoven Lists
Restore original links and extract clone head $C_0$:
- $N_0.\text{next} = N_1, \quad C_0.\text{next} = C_1$.
- $N_1.\text{next} = N_2, \quad C_1.\text{next} = C_2$.
- $N_2.\text{next} = N_3, \quad C_2.\text{next} = C_3$.
- $N_3.\text{next} = N_4, \quad C_3.\text{next} = C_4$.
- $N_4.\text{next} = \text{null}, \quad C_4.\text{next} = \text{null}$.

Outputs:
Original list restored to $N_0 \to N_1 \to N_2 \to N_3 \to N_4 \to \text{null}$.
Cloned list returned: $C_0 \to C_1 \to C_2 \to C_3 \to C_4 \to \text{null}$.

---

## 4. Complete Execution Trace

### Pointer State Transitions Across Passes

```text
Original:      N0(7) -----------> N1(13) ----------> N2(11) ...
Pass 1:        N0 -> [C0] ------> N1 -> [C1] ------> N2 -> [C2] ...
Pass 2:        C1.random = N1.random.next = N0.next = C0
Pass 3:        Restore N0 -> N1 -> N2;  Emit C0 -> C1 -> C2
```

| Node Index | Original Node $N_i$ | Cloned Node $C_i$ | Original Random Link | Formula Applied | Cloned Random Assignment |
|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | $N_0(7)$ | $C_0(7)$ | $\text{null}$ | $N_0.\text{random} == \text{null}$ | $\text{null}$ |
| 1 | $N_1(13)$ | $C_1(13)$ | $N_0(7)$ | $C_1.\text{random} = N_0.\text{next}$ | **$C_0(7)$** |
| 2 | $N_2(11)$ | $C_2(11)$ | $N_4(1)$ | $C_2.\text{random} = N_4.\text{next}$ | **$C_4(1)$** |
| 3 | $N_3(10)$ | $C_3(10)$ | $N_2(11)$ | $C_3.\text{random} = N_2.\text{next}$ | **$C_2(11)$** |
| 4 | $N_4(1)$ | $C_4(1)$ | $N_0(7)$ | $C_4.\text{random} = N_0.\text{next}$ | **$C_0(7)$** |

Pass 3 is where the interwoven chain is cut apart, and its two outputs have to agree on both halves. The table below records the `next` pointer of every original and cloned node on either side of that pass:

| Index $i$ | $\text{val}$ | $N_i.\text{next}$ while interwoven | $C_i.\text{next}$ while interwoven | $N_i.\text{next}$ after Pass 3 | $C_i.\text{next}$ after Pass 3 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 7 | $C_0$ | $N_1$ | $N_1$ | $C_1$ |
| 1 | 13 | $C_1$ | $N_2$ | $N_2$ | $C_2$ |
| 2 | 11 | $C_2$ | $N_3$ | $N_3$ | $C_3$ |
| 3 | 10 | $C_3$ | $N_4$ | $N_4$ | $C_4$ |
| 4 | 1 | $C_4$ | null | null | null |

Before Pass 3 every original node points at its own clone and every clone points at the next original node, which is exactly the interleaving $N_0 \to C_0 \to N_1 \to C_1 \to \dots$. After Pass 3 the two columns are independent chains: no original node references a clone and no clone references an original node. The clone's `random` pointers are untouched by this pass, so they still point only at cloned nodes.

---

## 5. Algorithmic Correctness

**Soundness.** In Pass 1, inserting $u'$ as $u.\text{next}$ establishes a deterministic mapping where $u.\text{next}$ uniquely denotes the clone of $u$. In Pass 2, for any random edge $(u, v)$, $v.\text{next}$ is the clone of $v$, ensuring that $u'.\text{random} = v'$. In Pass 3, separating the links restores the original list to its exact initial state while producing an independent clone list.

**Completeness.** Every node in the list is duplicated in Pass 1. Every random pointer is resolved in Pass 2. Every `next` pointer is unlinked and reconstructed in Pass 3. No nodes or edges are omitted.

---

## 6. Traps This Instance Exposes

- **Null Pointer Dereference on Random:** If $u.\text{random}$ is `null`, attempting to access $u.\text{random}.\text{next}$ triggers an AttributeError / NullPointerException! The check `if curr.random:` must precede the assignment.
- **Failing to Restore the Original List:** LeetCode's judge tests whether the original list was modified or corrupted after the copy. Failing to restore $u.\text{next} = u'.\text{next}$ in Pass 3 causes judge failure.
- **Null Input:** If $\text{head} == \text{null}$, return `null` immediately without entering any pass.

The authored cases target the guards directly, and the last two rows are where an index-based shortcut breaks:

| Authored case | `nodes` (value, random index) | Nodes | Random edges | What the passes must produce |
|:---|:---|:---:|:---:|:---|
| `sample-empty` | `[]` | 0 | 0 | A null reference is returned, `clones` is never consulted, and no pass runs |
| `trial-single` | `[[5, 0]]` | 1 | 1, pointing at itself | $C_0.\text{random} = N_0.\text{random}.\text{next} = N_0.\text{next} = C_0$, so the clone points at itself and not at the original |
| `sample-self` | `[[1, 1], [2, 1]]` | 2 | 2, one crossing and one self-referential | Node 0's random crosses to node 1 while node 1's random stays on itself; both must resolve to cloned nodes |
| `trial-cycle` | `[[1, 2], [2, 0], [3, 1]]` | 3 | 3, forming a cycle | Every assignment reads a different pair's `next` pointer, so the clone's random edges form the same cycle |
| `sample-five` | `[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]` | 5 | 4, plus one null | Four assignments plus one null guard, which is the worked instance of this lesson |

Every authored array above happens to carry distinct values ($7, 13, 11, 10, 1$; $1, 2$; $1, 2, 3$; $5$), so a shortcut that keys clones by value rather than by node identity would still survive the whole suite. The interwoven layout does not depend on that coincidence: it answers "which clone?" positionally, through $v.\text{next}$, so repeated values cannot make two different random targets collapse onto the same clone.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The algorithm makes three sequential passes over the list, each performing $O(1)$ pointer reassignments per node.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Nodes are allocated solely for the returned cloned list; no hash map, stack, or recursion buffer is used.

The price of that constant bound is one extra traversal of the list, which the comparison below makes explicit:

| Strategy | How a clone is located from an original node | Passes | Time | Auxiliary space | Failure mode |
|:---|:---|:---:|:---:|:---:|:---|
| Interweaving in place | The clone of $u$ is literally $u.\text{next}$ | 3 | $O(N)$ | $O(1)$ | Forgets to restore the original `next` links if Pass 3 is skipped or truncated |
| Hash map from original node to clone | Dictionary lookup keyed by the node object | 2 | $O(N)$ | $O(N)$ | None for correctness; the map itself is the extra space |
| Map keyed by node value | Dictionary lookup keyed by $\text{val}$ | 2 | $O(N)$ | $O(N)$ | Collapses distinct nodes that share a value, so their clones are confused |
| Index the clones by their position | Walk the clone list in parallel with the original | 2 | $O(N)$ | $O(N)$ for the parallel list | Random targets still need the original-to-index mapping, which is the same work as the map |
| Recursive copy | Recurse on `next`, then resolve `random` | 1, but with an unusable order | $O(N)$ | $O(N)$ call stack | A random target further down the list has not been copied yet, so the recursion needs the map anyway, and a 1000-node list can exhaust the recursion limit |

The first two rows are the standard answers; the remaining rows are either incorrect on repeated values or merely rename the auxiliary map.

---