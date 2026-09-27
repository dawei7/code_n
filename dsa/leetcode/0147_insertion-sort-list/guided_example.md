# Guided Example: Insertion Sort List

We trace the step-by-step in-place insertion sort pointer splicing and sorted boundary maintenance on representative singly linked list instances:

- **Input:** $\text{head} = [4, 2, 1, 3]$
- **Required output:** $[1, 2, 3, 4]$
- **Negative & Zero Instance:** $\text{head} = [-1, 5, 3, 4, 0] \implies [-1, 0, 3, 4, 5]$

This instance demonstrates in-place linked list insertion sort using a dummy sentinel node, maintaining the boundary between the sorted prefix (`last_sorted`) and unsorted suffix (`curr`), skipping linear scans when elements are already in order ($O(N)$ best case), and executing pointer rewiring in $O(1)$ extra space.

---

## 1. Instance & Teaching Goal

Given the head of a singly linked list:
$$
4 \longrightarrow 2 \longrightarrow 1 \longrightarrow 3
$$
Sort the list using **insertion sort** and return the head of the sorted list.

Insertion sort consumes one element at a time from the unsorted suffix, finds its correct insertion location in the sorted prefix, and splices it in.
In an array, insertion requires shifting $O(N)$ elements rightward. In a linked list, elements are not contiguous in memory, so insertion requires no shifting—only rewriting three pointer references:
1. Unlink node from its current position: $\text{last\_sorted.next} = \text{curr.next}$.
2. Point node to target successor: $\text{curr.next} = \text{prev.next}$.
3. Point target predecessor to node: $\text{prev.next} = \text{curr}$.

By anchoring the list with a dummy sentinel node `dummy`, insertion at the very head of the list follows the exact same logic as an interior insertion.

---

## 2. Conceptual Foundation & Invariants

### In-Place Pointer Manipulation Protocol
1. **Sentinel Initialization:**
   $$
   \text{dummy} = \text{Node}(0, \, \text{head})
   $$
   $$
   \text{last\_sorted} = \text{head}, \quad \text{curr} = \text{head.next}
   $$
2. **Loop Condition (`while curr`):**
   - **Case 1: Already Sorted ($curr.val \ge last\_sorted.val$):**
     The current node is greater than or equal to the maximum element seen so far. No repositioning needed:
     $$
     \text{last\_sorted} \leftarrow \text{curr}
     $$
     $$
     \text{curr} \leftarrow \text{last\_sorted.next}
     $$
   - **Case 2: Out of Order ($curr.val < last\_sorted.val$):**
     Scan from `dummy` to locate the insertion predecessor:
     - Initialize $\text{prev} = \text{dummy}$.
     - Advance while $\text{prev.next.val} \le \text{curr.val}$:
       $$
       \text{prev} \leftarrow \text{prev.next}
       $$
     - **Splice Node into Sorted Prefix:**
       $$
       \text{last\_sorted.next} = \text{curr.next}
       $$
       $$
       \text{curr.next} = \text{prev.next}
       $$
       $$
       \text{prev.next} = \text{curr}
       $$
     - Advance to next unsorted candidate:
       $$
       \text{curr} \leftarrow \text{last\_sorted.next}
       $$

> **Invariant.** The chain from `dummy.next` up to `last_sorted` is monotonically non-decreasing at the start and end of every iteration.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{head} = [4, 2, 1, 3]$:
Initial: $\text{dummy} \to 4 \to 2 \to 1 \to 3$.
`last_sorted = Node(4)`, `curr = Node(2)`.

---

### Iteration 1: Process Node 2 ($2 < 4$)
- Condition $2 < 4 \implies$ Node 2 must be moved before 4.
- Locate insertion predecessor:
  - Start at `prev = dummy`.
  - Next value is $4 > 2 \implies$ stop scan! (`prev = dummy`).
- Splice Node 2:
  - $\text{Node}(4).\text{next} = \text{Node}(1)$.
  - $\text{Node}(2).\text{next} = \text{Node}(4)$.
  - $\text{dummy.next} = \text{Node}(2)$.
- Structure: $\text{dummy} \to \mathbf{2 \to 4} \to 1 \to 3$.
- Advance: `curr = last_sorted.next = Node(1)`.

---

### Iteration 2: Process Node 1 ($1 < 4$)
- Condition $1 < 4 \implies$ Node 1 must be moved before 2.
- Locate insertion predecessor:
  - Start at `prev = dummy`.
  - Next value is $2 > 1 \implies$ stop scan! (`prev = dummy`).
- Splice Node 1:
  - $\text{Node}(4).\text{next} = \text{Node}(3)$.
  - $\text{Node}(1).\text{next} = \text{Node}(2)$.
  - $\text{dummy.next} = \text{Node}(1)$.
- Structure: $\text{dummy} \to \mathbf{1 \to 2 \to 4} \to 3$.
- Advance: `curr = last_sorted.next = Node(3)`.

---

### Iteration 3: Process Node 3 ($3 < 4$)
- Condition $3 < 4 \implies$ Node 3 must be moved between 2 and 4.
- Locate insertion predecessor:
  - Start at `prev = dummy`.
  - Check `prev.next` ($1 \le 3$): advance `prev = Node(1)`.
  - Check `prev.next` ($2 \le 3$): advance `prev = Node(2)`.
  - Check `prev.next` ($4 > 3$): stop scan! (`prev = Node(2)`).
- Splice Node 3:
  - $\text{Node}(4).\text{next} = \text{null}$.
  - $\text{Node}(3).\text{next} = \text{Node}(4)$.
  - $\text{Node}(2).\text{next} = \text{Node}(3)$.
- Structure: $\text{dummy} \to \mathbf{1 \to 2 \to 3 \to 4} \to \text{null}$.
- Advance: `curr = last_sorted.next = null`.

`curr` is null. Sorting terminates!
Return `dummy.next = Node(1)`: $[1, 2, 3, 4]$.

---

## 4. Complete Execution Trace

```text
Initial:        dummy -> [4] -> [2] -> [1] -> [3]
Iter 1 (2<4):   dummy -> [2] -> [4] -> [1] -> [3]
Iter 2 (1<4):   dummy -> [1] -> [2] -> [4] -> [3]
Iter 3 (3<4):   dummy -> [1] -> [2] -> [3] -> [4] -> null
```

| Iteration | Evaluated Node `curr` | `last_sorted.val` | Comparison | Predecessor `prev` Found | Splice Action | Sorted Prefix State |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 (Init) | - | 4 | - | - | Initial Setup | `dummy -> [4]` |
| 1 | $\text{Node}(2)$ | 4 | $2 < 4$ | $\text{dummy}$ | Insert before 4 | `dummy -> [2, 4]` |
| 2 | $\text{Node}(1)$ | 4 | $1 < 4$ | $\text{dummy}$ | Insert before 2 | `dummy -> [1, 2, 4]` |
| **3** | **$\text{Node}(3)$** | **4** | **$3 < 4$** | **$\text{Node}(2)$** | **Insert between 2 and 4** | **`dummy -> [1, 2, 3, 4]`** |
| Done | $\emptyset$ | 4 | - | - | Traversal complete | **$[1, 2, 3, 4]$** |

---

## 5. Algorithmic Correctness

**Soundness.** Insertion sort maintains a partition where the prefix before `curr` is sorted. When `curr` is inserted after `prev`, $\text{prev.val} \le \text{curr.val} < \text{prev.next.val}$, so the non-decreasing order of the prefix is strictly preserved.

**Completeness.** Every node in the list is processed exactly once by `curr`. Splicing reconnects `last_sorted.next` to `curr.next`, ensuring no nodes in the unsorted suffix are orphaned or lost.

---

## 6. Traps This Instance Exposes

- **Failing to Advance `last_sorted.next`:** If `last_sorted.next = curr.next` is omitted during splicing, `last_sorted` will still point to `curr`, creating an infinite cycle.
- **Scanning from Dummy on Already Sorted Nodes:** If an element is already larger than `last_sorted`, scanning from `dummy` would degrade already-sorted lists to $O(N^2)$. The `if curr.val >= last_sorted.val` check achieves $O(N)$ best-case time.
- **Empty or Single Node List:** If `not head or not head.next: return head`, handles base cases in $O(1)$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$ worst-case (reverse sorted list), where each node requires scanning the entire sorted prefix. $O(N)$ best-case (already sorted list) due to the boundary comparison guard.
- **Auxiliary Space Complexity:** $O(1)$ constant extra space, manipulating only pointer references in place.