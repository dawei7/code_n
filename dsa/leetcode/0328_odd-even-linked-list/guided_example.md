# Guided Example: Odd Even Linked List

We trace the step-by-step two-pointer linked list partitioning, alternating leapfrog pointer splicing (`a.next = b.next`, `b.next = a.next`), even head anchor preservation (`c = head.next`), and tail-to-head splice reconnection on representative singly-linked list instances:

- **Input:** Singly linked list $\text{head} = [1, 2, 3, 4, 5]$
- **Required output:** $[1, 3, 5, 2, 4]$
  - Odd nodes (by 1-based index): Node $1$, Node $3$, Node $5 \implies 1 \to 3 \to 5$
  - Even nodes (by 1-based index): Node $2$, Node $4 \implies 2 \to 4$
  - Splicing odd tail ($5$) to even head ($2$): $1 \to 3 \to 5 \to 2 \to 4 \to \text{null}$
- **Even Length List Instance:** $\text{head} = [1, 2, 3, 4] \implies [1, 3, 2, 4]$
- **Complex Interleaved Instance:** $\text{head} = [2, 1, 3, 5, 6, 4, 7] \implies [2, 3, 6, 7, 1, 5, 4]$
- **Empty / Single / Two Nodes Base Cases:**
  - $\text{head} = \text{null} \implies \text{null}$
  - $\text{head} = [1] \implies [1]$
  - $\text{head} = [1, 2] \implies [1, 2]$

This instance demonstrates in-place structural pointer manipulation, explains why saving the even head reference $c$ prevents losing half the list, mathematically proves why `while b and b.next` handles both odd and even length lists without null dereferences, and achieves $O(N)$ linear time and strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a singly linked list:
$$
1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5 \longrightarrow \text{null}
$$
Group all nodes with **odd 1-based indices** together, followed by all nodes with **even 1-based indices**:
- The relative ordering of elements within the odd group and within the even group must be preserved.
- The solution must execute **in-place** with $O(1)$ extra space and $O(N)$ time (no creating new nodes).

```text
Original indices:
Index: 1      2      3      4      5
Node: [1] -> [2] -> [3] -> [4] -> [5] -> null
Type: Odd   Even   Odd   Even   Odd

Desired Reordering:
Odd Nodes:  [1] -> [3] -> [5]
Even Nodes: [2] -> [4]
Combined:   [1] -> [3] -> [5] -> [2] -> [4] -> null
```

---

## 2. Conceptual Foundation & Invariants

### Pointers & Invariants:
1. `a`: Current tail of the odd chain (initialized to `head`).
2. `b`: Current tail of the even chain (initialized to `head.next`).
3. `c`: Permanent anchor holding the start of the even chain (`head.next`).

### The Alternating Leapfrog Step:
While `b` and `b.next` are non-null:
1. **Advance Odd Pointer:**
   Node `b.next` is the next odd node.
   - `a.next = b.next` (Odd tail skips even node `b` to point to `b.next`).
   - `a = a.next` (Advance odd pointer to the newly added odd node).
2. **Advance Even Pointer:**
   Node `a.next` is now the next even node (or null).
   - `b.next = a.next` (Even tail skips newly added odd node to point to `a.next`).
   - `b = b.next` (Advance even pointer).

### Final Reconnection:
Attach the head of the even chain `c` to the tail of the odd chain `a`:
$$
a.\text{next} = c
$$
Return `head`.

> **Invariant.** At the start of each while iteration, `a` is the tail of a valid odd-indexed sublist, `b` is the tail of a valid even-indexed sublist, and `b.next` points to the next unprocessed odd node.

---

## 3. Step-by-Step Worked Execution

We trace the pointer movements on $\text{head} = [1, 2, 3, 4, 5]$:
- Initial state:
  - $a = \text{Node}(1)$
  - $b = \text{Node}(2)$
  - $c = \text{Node}(2)$ (even head anchor)

---

### Step 1: Iteration 1 ($b = 2$, $b.\text{next} = 3$)
- Condition check: $b$ is non-null ($2$) and $b.\text{next}$ is non-null ($3$) $\implies$ Proceed.
- **Rewire Odd:**
  - $a.\text{next} = b.\text{next} \implies \text{Node}(1).\text{next} = \text{Node}(3)$.
  - $a = a.\text{next} \implies a = \text{Node}(3)$.
  - Odd chain is now: $1 \to 3$.
- **Rewire Even:**
  - $b.\text{next} = a.\text{next} \implies \text{Node}(2).\text{next} = \text{Node}(4)$.
  - $b = b.\text{next} \implies b = \text{Node}(4)$.
  - Even chain is now: $2 \to 4$.
- Unprocessed remainder begins at $a.\text{next} = \text{Node}(5)$.

---

### Step 2: Iteration 2 ($b = 4$, $b.\text{next} = 5$)
- Condition check: $b$ is non-null ($4$) and $b.\text{next}$ is non-null ($5$) $\implies$ Proceed.
- **Rewire Odd:**
  - $a.\text{next} = b.\text{next} \implies \text{Node}(3).\text{next} = \text{Node}(5)$.
  - $a = a.\text{next} \implies a = \text{Node}(5)$.
  - Odd chain is now: $1 \to 3 \to 5$.
- **Rewire Even:**
  - $b.\text{next} = a.\text{next} \implies \text{Node}(4).\text{next} = \text{null}$.
  - $b = b.\text{next} \implies b = \text{null}$.
  - Even chain is now: $2 \to 4 \to \text{null}$.

---

### Step 3: Loop Termination & Splice
- Condition check: $b$ is `null` $\implies$ Loop exits!
- Connect odd tail $a$ ($\text{Node}(5)$) to even head $c$ ($\text{Node}(2)$):
  $$
  a.\text{next} = c \implies \text{Node}(5).\text{next} = \text{Node}(2)
  $$
- Completed linked list:
  $$
  1 \longrightarrow 3 \longrightarrow 5 \longrightarrow 2 \longrightarrow 4 \longrightarrow \text{null}
  $$
- Return `head` (which remains at Node $1$).

---

## 4. Complete Execution Trace

```text
Original: 1 -> 2 -> 3 -> 4 -> 5 -> null
a = 1, b = 2, c = 2

Iteration 1:
  a.next = b.next (1 -> 3)
  a = 3
  b.next = a.next (2 -> 4)
  b = 4
  State: (1 -> 3), (2 -> 4 -> 5)

Iteration 2:
  a.next = b.next (3 -> 5)
  a = 5
  b.next = a.next (4 -> null)
  b = null
  State: (1 -> 3 -> 5), (2 -> 4 -> null)

Loop ends (b is null)
Splicing: a.next = c (5 -> 2)

Result: 1 -> 3 -> 5 -> 2 -> 4 -> null
```

| Loop Iteration | Current $a$ | Current $b$ | Action $a.\text{next} = b.\text{next}$ | New $a$ | Action $b.\text{next} = a.\text{next}$ | New $b$ | Active Odd Chain | Active Even Chain |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| Init | 1 | 2 | - | 1 | - | 2 | `1` | `2` |
| 1 | 1 | 2 | $1 \to 3$ | 3 | $2 \to 4$ | 4 | `1 -> 3` | `2 -> 4` |
| 2 | 3 | 4 | $3 \to 5$ | 5 | $4 \to \text{null}$ | null | `1 -> 3 -> 5` | `2 -> 4 -> null` |
| **Splice** | **5** | **null** | **$5 \to 2$ ($a.\text{next} = c$)** | - | - | - | **`1 -> 3 -> 5 -> 2 -> 4 -> null`** | - |

---

## 5. Algorithmic Correctness

**Soundness.** At each iteration, $a$ and $b$ leapfrog one node ahead. Node $b.\text{next}$ is guaranteed to be odd because $b$ is an even node; node $a.\text{next}$ is guaranteed to be even because $a$ is an odd node. Because pointers are updated strictly along original link directions, relative ordering inside both the odd and even partitions is invariant. Terminating when $b$ or $b.\text{next}$ is null ensures that the even chain is properly null-terminated.

**Completeness.** Every node from index $1$ to $N$ is visited and incorporated into either the odd or even chain. Reconnecting $a.\text{next} = c$ links the two chains seamlessly into a single valid linked list of length $N$.

---

## 6. Traps This Instance Exposes

- **Losing the Even Head:** If `head.next` is not cached in variable $c$ before the loop, the reference to the first even node is lost once $a.\text{next}$ is overwritten, making it impossible to splice the even sublist back.
- **Dangling Cycles / Non-Null Termination:** On even-length lists, forgetting to update $b.\text{next}$ could leave the last even node pointing back to an earlier odd node, creating an infinite cycle. Setting $b.\text{next} = a.\text{next}$ guarantees clean null-termination.
- **Loop Condition Robustness:** Using `while b and b.next` cleanly covers both odd-length lists (where $b$ becomes null) and even-length lists (where $b.\text{next}$ becomes null) without `NoneType has no attribute 'next'` errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The loop traverses the list in steps of 2, visiting each node exactly once.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory using three node pointers ($a, b, c$) with zero heap memory allocations.
