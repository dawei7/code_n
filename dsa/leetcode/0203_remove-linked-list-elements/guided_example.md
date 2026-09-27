# Guided Example: Remove Linked List Elements

We trace the step-by-step in-place pointer rewiring, sentinel dummy node anchoring, and consecutive target deletion on representative linked list sequences:

- **Input:** $\text{head} = [1, 2, 6, 3, 4, 5, 6], \quad \text{val} = 6$
- **Required output:** $[1, 2, 3, 4, 5]$ (Both occurrences of $6$ excised)
- **All-Target Instance:** $\text{head} = [7, 7, 7, 7], \quad \text{val} = 7 \implies []$ (Sentinel dummy node prevents null head crashes)
- **Target At Head Instance:** $\text{head} = [6, 1, 2], \quad \text{val} = 6 \implies [1, 2]$
- **Empty List Instance:** $\text{head} = [], \quad \text{val} = 1 \implies []$

This instance demonstrates sentinel dummy node stabilization (`dummy.next = head`), proves why the tracking pointer must **not advance** when an element is removed (`curr.next = curr.next.next`), handles consecutive duplicates without orphan memory leaks, and runs in $O(N)$ time with strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given the head of a singly linked list and an integer $\text{val} = 6$:
$$
\text{head} \to 1 \to 2 \to \mathbf{6} \to 3 \to 4 \to 5 \to \mathbf{6} \to \text{null}
$$
Remove all nodes where $\text{Node.val} == \text{val}$, returning the modified linked list:
$$
\text{new\_head} \to 1 \to 2 \to 3 \to 4 \to 5 \to \text{null}
$$

The primary challenge in linked list removal is handling boundary edge cases:
- Deleting an interior node is easy: if `curr` precedes the target, set `curr.next = curr.next.next`.
- However, if the target is the **head node** (or multiple consecutive nodes at the head), there is no preceding node!
Allocating a new list copies nodes and wastes memory.
The standard pattern introduces a **sentinel dummy node** before `head`:
- `dummy = ListNode(0, head)` ensures that *every* node in the original list has a valid predecessor.
- The new head is always accessed as `dummy.next`.

---

## 2. Conceptual Foundation & Invariants

### Sentinel Pointer Protocol
1. **Initialize Sentinel:**
   Create a dummy node pointing to `head`:
   $$
   \text{dummy} \to \text{head}, \quad \text{curr} = \text{dummy}
   $$
2. **Examine Forward Node (`curr.next`):**
   While $\text{curr.next} \ne \text{null}$:
   - **Case A: Target Value Detected ($\text{curr.next.val} == \text{val}$):**
     Bypass the forward node by linking directly to its successor:
     $$
     \text{curr.next} \leftarrow \text{curr.next.next}
     $$
     *(Do NOT advance $\text{curr}$! The new $\text{curr.next}$ must be inspected on the next iteration in case it is also equal to $\text{val}$)*.
   - **Case B: Retain Node ($\text{curr.next.val} \ne \text{val}$):**
     The node $\text{curr.next}$ is valid. Advance the cursor:
     $$
     \text{curr} \leftarrow \text{curr.next}
     $$
3. **Return:**
   $$
   \text{return } \text{dummy.next}
   $$

> **Invariant.** At every step, all nodes from $\text{dummy}$ up to and including $\text{curr}$ have values strictly not equal to $\text{val}$.

---

## 3. Step-by-Step Worked Execution

We trace the traversal on $\text{head} = [1, 2, 6, 3, 4, 5, 6]$ with $\text{val} = 6$:

### Step 0: Sentinel Setup
- $\text{dummy} \to 1 \to 2 \to 6 \to 3 \to 4 \to 5 \to 6 \to \text{null}$.
- $\text{curr} = \text{dummy}$.

---

### Step 1: Examine $\text{curr.next}$ (Node 1)
- $\text{curr.next.val} = 1 \ne 6$.
- Retain node. Advance cursor:
  $$
  \text{curr} \leftarrow \text{Node 1}
  $$

---

### Step 2: Examine $\text{curr.next}$ (Node 2)
- $\text{curr.next.val} = 2 \ne 6$.
- Retain node. Advance cursor:
  $$
  \text{curr} \leftarrow \text{Node 2}
  $$

---

### Step 3: Examine $\text{curr.next}$ (Node 6) — Target Found!
- $\text{curr.next.val} = 6 == 6$.
- Target node detected! Bypass Node 6:
  $$
  \text{curr.next} \leftarrow \text{curr.next.next} \quad (\text{Node 2 points to Node 3})
  $$
- **Cursor $\text{curr}$ stays at Node 2!**
- List state: $\text{dummy} \to 1 \to 2 \to 3 \to 4 \to 5 \to 6 \to \text{null}$.

---

### Step 4: Examine $\text{curr.next}$ (Node 3)
- $\text{curr.next.val} = 3 \ne 6$.
- Retain node. Advance cursor:
  $$
  \text{curr} \leftarrow \text{Node 3}
  $$

---

### Step 5: Examine $\text{curr.next}$ (Node 4)
- $\text{curr.next.val} = 4 \ne 6$.
- Retain node. Advance cursor:
  $$
  \text{curr} \leftarrow \text{Node 4}
  $$

---

### Step 6: Examine $\text{curr.next}$ (Node 5)
- $\text{curr.next.val} = 5 \ne 6$.
- Retain node. Advance cursor:
  $$
  \text{curr} \leftarrow \text{Node 5}
  $$

---

### Step 7: Examine $\text{curr.next}$ (Node 6) — Target Found!
- $\text{curr.next.val} = 6 == 6$.
- Target node detected! Bypass Node 6:
  $$
  \text{curr.next} \leftarrow \text{curr.next.next} \quad (\text{Node 5 points to null})
  $$
- Cursor $\text{curr}$ stays at Node 5.
- Next check: $\text{curr.next} == \text{null}$. Loop terminates!

Final list: $\text{dummy.next} \to 1 \to 2 \to 3 \to 4 \to 5 \to \text{null}$.

---

## 4. Complete Execution Trace

```text
Dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> null,  val = 6

curr = Dummy: curr.next is 1 (!=6) -> curr moves to 1
curr = 1:     curr.next is 2 (!=6) -> curr moves to 2
curr = 2:     curr.next is 6 (==6) -> REWIRE: 2.next = 3 (curr stays at 2)
curr = 2:     curr.next is 3 (!=6) -> curr moves to 3
curr = 3:     curr.next is 4 (!=6) -> curr moves to 4
curr = 4:     curr.next is 5 (!=6) -> curr moves to 5
curr = 5:     curr.next is 6 (==6) -> REWIRE: 5.next = null (curr stays at 5)
curr = 5:     curr.next is null    -> FINISHED

Result: [1, 2, 3, 4, 5]
```

| Step | `curr` Position | Forward Node `curr.next` | `curr.next.val` | Action Taken | Next `curr` Position | Active Spliced Sequence |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `dummy` | Node 1 | 1 | Advance cursor | Node 1 | `dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6` |
| 1 | Node 1 | Node 2 | 2 | Advance cursor | Node 2 | `dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6` |
| **2** | **Node 2** | **Node 6** | **6** | **Rewire (`2.next = 3`)** | **Node 2 (hold)** | **`dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6`** |
| 3 | Node 2 | Node 3 | 3 | Advance cursor | Node 3 | `dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` |
| 4 | Node 3 | Node 4 | 4 | Advance cursor | Node 4 | `dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` |
| 5 | Node 4 | Node 5 | 5 | Advance cursor | Node 5 | `dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` |
| **6** | **Node 5** | **Node 6** | **6** | **Rewire (`5.next = null`)** | **Node 5 (hold)** | **`dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null`** |
| 7 | Node 5 | `null` | - | Terminate loop | - | **`[1, 2, 3, 4, 5]` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** A node is excised if and only if its value matches `val`. Setting `curr.next = curr.next.next` drops the reference to the matching node. Because `curr` is not advanced when a deletion occurs, any subsequent consecutive nodes with value `val` are correctly evaluated against `curr.next` on the next iteration.

**Completeness.** Every node in the original list is examined in sequence through `curr.next`. All nodes with `val == val` are removed, and the list terminates with `curr.next == null`.

---

## 6. Traps This Instance Exposes

- **Advancing Cursor on Deletion:** Advancing `curr = curr.next` inside the deletion branch fails on consecutive duplicates (e.g. `[1, 6, 6, 2]` would skip inspecting the second `6` and leave it in the list). Only advance `curr` when `curr.next.val != val`.
- **Deleting the Head Node Without Sentinel:** When `head.val == val` (e.g. `[6, 6, 1]`), updating `head` without a dummy node requires an outer `while head and head.val == val: head = head.next` loop. The dummy sentinel node unifies all cases seamlessly.
- **Empty List:** When `head is None`, `dummy.next` is `None`, and the `while curr.next` loop immediately terminates, safely returning `None`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The loop executes at most $N$ iterations because each iteration either advances `curr` or removes a node from the remaining chain.
- **Auxiliary Space Complexity:** $O(1)$ constant extra space, creating only a single sentinel `ListNode` object.