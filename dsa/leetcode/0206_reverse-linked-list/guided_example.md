# Guided Example: Reverse Linked List

We trace the step-by-step three-pointer in-place link reversal and recursive unwinding mechanics on representative singly linked list chains:

- **Input:** $\text{head} = [1, 2, 3, 4, 5]$
- **Required output:** $[5, 4, 3, 2, 1]$ (All directed edges reversed in-place)
- **Two-Node Instance:** $\text{head} = [1, 2] \implies [2, 1]$
- **Single-Node Instance:** $\text{head} = [1] \implies [1]$
- **Empty List Instance:** $\text{head} = [] \implies []$

This instance demonstrates in-place directed graph edge inversion ($\text{curr.next} \leftarrow \text{prev}$), proves why caching the forward reference ($\text{nxt} = \text{curr.next}$) is mandatory to prevent orphan node loss, analyzes both iterative $O(1)$-space and recursive call-stack approaches, and runs in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the head of a singly linked list:
$$
\text{head} \to 1 \to 2 \to 3 \to 4 \to 5 \to \text{null}
$$
Reverse the direction of every single pointer such that the tail becomes the new head:
$$
\text{new\_head} \to 5 \to 4 \to 3 \to 2 \to 1 \to \text{null}
$$

In a singly linked list, each node contains only a single forward reference (`next`) without a backward pointer.
Reversing the link $\text{curr} \to \text{prev}$ by setting $\text{curr.next} = \text{prev}$ immediately severs access to the remainder of the list!
To prevent losing the rest of the chain, the algorithm must maintain **three simultaneous pointers**:
- `prev`: tracks the head of the already-reversed prefix.
- `curr`: tracks the node currently being inverted.
- `nxt`: temporarily preserves the unvisited suffix before the forward link is overwritten.

---

## 2. Conceptual Foundation & Invariants

### Iterative Three-Pointer Reversal Protocol
Initialize:
$$
\text{prev} = \text{null}, \quad \text{curr} = \text{head}
$$

While $\text{curr} \ne \text{null}$:
1. **Cache Forward Pointer:**
   $$
   \text{nxt} \leftarrow \text{curr.next}
   $$
2. **Reverse Directed Link:**
   Rewire the active node to point to its predecessor:
   $$
   \text{curr.next} \leftarrow \text{prev}
   $$
3. **Advance Inverted Boundary:**
   $$
   \text{prev} \leftarrow \text{curr}
   $$
4. **Advance Exploration Cursor:**
   $$
   \text{curr} \leftarrow \text{nxt}
   $$

When `curr` reaches `null`, all nodes have been reversed. Return `prev` as the new head.

### Recursive Reversal Alternative:
```python
def reverseList(head):
    if not head or not head.next:
        return head
    new_head = reverseList(head.next)
    head.next.next = head   # Reverse successor's pointer to point back to current node
    head.next = None        # Sever original forward edge
    return new_head
```

> **Invariant.** At the beginning of each loop iteration, `prev` is the head of a completely reversed list containing all nodes processed so far, while `curr` points to the head of the remaining unreversed list.

---

## 3. Step-by-Step Worked Execution

We trace the iterative algorithm on $\text{head} = [1, 2, 3, 4, 5]$:

### Step 0: Initial Setup
- $\text{prev} = \text{null}$.
- $\text{curr} = \text{Node 1}$.
- Active chain: $1 \to 2 \to 3 \to 4 \to 5 \to \text{null}$.

---

### Step 1: Invert Node 1
1. Cache next: $\text{nxt} = \text{curr.next} = \text{Node 2}$.
2. Invert link: $\text{curr.next} = \text{prev} = \text{null}$.
   *(Node 1 now terminates the reversed list)*.
3. Advance `prev`: $\text{prev} = \text{Node 1}$.
4. Advance `curr`: $\text{curr} = \text{Node 2}$.
- State: $\text{null} \leftarrow 1 \quad \mathbf{\text{and}} \quad 2 \to 3 \to 4 \to 5$.

---

### Step 2: Invert Node 2
1. Cache next: $\text{nxt} = \text{curr.next} = \text{Node 3}$.
2. Invert link: $\text{curr.next} = \text{prev} = \text{Node 1}$.
3. Advance `prev`: $\text{prev} = \text{Node 2}$.
4. Advance `curr`: $\text{curr} = \text{Node 3}$.
- State: $\text{null} \leftarrow 1 \leftarrow 2 \quad \mathbf{\text{and}} \quad 3 \to 4 \to 5$.

---

### Step 3: Invert Node 3
1. Cache next: $\text{nxt} = \text{curr.next} = \text{Node 4}$.
2. Invert link: $\text{curr.next} = \text{prev} = \text{Node 2}$.
3. Advance `prev`: $\text{prev} = \text{Node 3}$.
4. Advance `curr`: $\text{curr} = \text{Node 4}$.
- State: $\text{null} \leftarrow 1 \leftarrow 2 \leftarrow 3 \quad \mathbf{\text{and}} \quad 4 \to 5$.

---

### Step 4: Invert Node 4
1. Cache next: $\text{nxt} = \text{curr.next} = \text{Node 5}$.
2. Invert link: $\text{curr.next} = \text{prev} = \text{Node 3}$.
3. Advance `prev`: $\text{prev} = \text{Node 4}$.
4. Advance `curr`: $\text{curr} = \text{Node 5}$.
- State: $\text{null} \leftarrow 1 \leftarrow 2 \leftarrow 3 \leftarrow 4 \quad \mathbf{\text{and}} \quad 5$.

---

### Step 5: Invert Node 5
1. Cache next: $\text{nxt} = \text{curr.next} = \text{null}$.
2. Invert link: $\text{curr.next} = \text{prev} = \text{Node 4}$.
3. Advance `prev`: $\text{prev} = \text{Node 5}$.
4. Advance `curr`: $\text{curr} = \text{null}$.
- State: $\text{null} \leftarrow 1 \leftarrow 2 \leftarrow 3 \leftarrow 4 \leftarrow 5$.

---

### Step 6: Loop Termination
- $\text{curr} == \text{null}$. Loop terminates.
- New head of reversed list is $\text{prev} = \mathbf{\text{Node 5}}$.
- Sequence: $5 \to 4 \to 3 \to 2 \to 1 \to \text{null}$.

---

## 4. Complete Execution Trace

```text
Start: prev = null, curr = 1 -> 2 -> 3 -> 4 -> 5

Iter 1: 1.next = null  -> prev = 1, curr = 2
Iter 2: 2.next = 1     -> prev = 2, curr = 3
Iter 3: 3.next = 2     -> prev = 3, curr = 4
Iter 4: 4.next = 3     -> prev = 4, curr = 5
Iter 5: 5.next = 4     -> prev = 5, curr = null

End: curr is null -> return prev (5)
List: 5 -> 4 -> 3 -> 2 -> 1 -> null
```

| Iteration | Active Node `curr` | Cached `nxt` | Inverted Assignment `curr.next` | New `prev` Anchor | Unprocessed Suffix |
|:---:|:---:|:---:|:---:|:---:|:---|
| Init | Node 1 | - | - | `null` | `1 -> 2 -> 3 -> 4 -> 5` |
| 1 | Node 1 | Node 2 | `null` | Node 1 | `2 -> 3 -> 4 -> 5` |
| 2 | Node 2 | Node 3 | Node 1 | Node 2 | `3 -> 4 -> 5` |
| 3 | Node 3 | Node 4 | Node 2 | Node 3 | `4 -> 5` |
| 4 | Node 4 | Node 5 | Node 3 | Node 4 | `5` |
| **5** | **Node 5** | **`null`** | **Node 4** | **Node 5** | **`null` (Finished)** |

---

## 5. Algorithmic Correctness

**Soundness.** At each step, the directed edge from `curr` to `nxt` is redirected to `prev`. Because `nxt` was cached prior to link modification, no pointers are lost and memory leaks or detached cycles cannot occur. At termination, all $N$ directed edges point backwards, and the former tail node (`Node 5`) becomes the accessible entry point.

**Completeness.** The loop visits each node exactly once in sequential order. When `curr` becomes `null`, every node in the original list has been processed.

---

## 6. Traps This Instance Exposes

- **Overwriting Pointer Before Caching:** Setting `curr.next = prev` before assigning `nxt = curr.next` destroys the reference to the rest of the list, permanently losing all nodes after `curr`.
- **Cyclic Reference at the Tail:** Forgetting to initialize $\text{prev} = \text{null}$ causes the original head's `next` pointer to point to garbage instead of `null`, producing an infinite cycle when traversed.
- **Empty List or Single Node:** If `head is None`, the loop never runs and returns `None`. If `head.next is None`, the loop runs once, sets `1.next = None`, and returns `Node 1`, naturally handling boundary sizes without special-case branches.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The loop executes exactly $N$ times, with $O(1)$ pointer assignments per iteration.
- **Auxiliary Space Complexity:**
  - Iterative Approach: $O(1)$ constant memory, mutating pointers strictly in-place.
  - Recursive Approach: $O(N)$ call-stack memory due to $N$ stack frames.