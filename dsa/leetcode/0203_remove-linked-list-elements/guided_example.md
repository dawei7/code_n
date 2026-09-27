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

The candidate strategies differ only in how they absorb the boundary cases, and that difference is what decides the auxiliary space and the number of distinct removal rules a reader must keep straight:

| Approach | How a removal is performed | Auxiliary space | Cost or failure mode |
|:---|:---|:---:|:---|
| Rebuild into a fresh list | Copy each retained value into a newly allocated node | $O(N)$ | Correct output, but the entire list is duplicated and the original nodes are leaked unless freed separately |
| Strip the head, then walk | A leading loop advances `head` past every matching prefix node; a second walk handles the interior | $O(1)$ | Two removal rules instead of one; a mistake in either silently corrupts the chain |
| Recursive removal | Recurse to the tail, then re-link each returned node on the way back, dropping matches | $O(N)$ call stack | Correct, but the stack depth equals the list length, which overflows on a long list |
| Sentinel dummy node (used here) | One guard links `dummy.next = head`, after which every removal is the same single rewire | $O(1)$ | Only one extra node; retention and deletion share one uniform code path |

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

A concrete run on `[1, 6, 6, 2]` with $\text{val} = 6$ shows exactly why the hold is required. The cursor stays on Node 1 for two consecutive iterations and evaluates the newly exposed successor each time:

| Iteration | `curr` | `curr.next.val` | Match? | Action | Chain reachable from `dummy` after the step |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | `dummy` | 1 | No | Advance to Node 1 | `dummy -> 1 -> 6 -> 6 -> 2` |
| 2 | Node 1 | 6 | Yes | Rewire `1.next` to the second 6; hold | `dummy -> 1 -> 6 -> 2` (first 6 detached) |
| 3 | Node 1 | 6 | Yes | Rewire `1.next` to Node 2; hold | `dummy -> 1 -> 2` (second 6 detached) |
| 4 | Node 1 | 2 | No | Advance to Node 2 | `dummy -> 1 -> 2` |
| 5 | Node 2 | `null` | — | Loop guard `curr.next != null` fails | `[1, 2]` returned |

Had the cursor advanced inside iteration 2, `curr` would have landed on the second 6, so iteration 3 would have compared Node 2 against $\text{val}$ and never tested the second 6 itself; the answer would wrongly be `[1, 6, 2]`.
- **Deleting the Head Node Without Sentinel:** When `head.val == val` (e.g. `[6, 6, 1]`), updating `head` without a dummy node requires an outer `while head and head.val == val: head = head.next` loop. The dummy sentinel node unifies all cases seamlessly.
- **Empty List:** When `head is None`, `dummy.next` is `None`, and the `while curr.next` loop immediately terminates, safely returning `None`.

Because the sentinel removes the special case entirely, the same three-line rule covers every boundary shape. The rows below are the boundary inputs a reviewer should try, and the sentinel behaviour each one depends on:

| Scenario | Input `head` | `val` | What the sentinel makes possible | Result |
|:---|:---|:---:|:---|:---|
| Matches in the interior | `[1, 2, 6, 3, 4, 5, 6]` | 6 | two independent rewires at unrelated positions | `[1, 2, 3, 4, 5]` |
| Target only at the head | `[6, 1, 2]` | 6 | `dummy.next` is moved before the cursor has advanced once | `[1, 2]` |
| Matches at head, interior, and tail | `[2, 1, 2, 3, 2]` | 2 | the first rewire moves `dummy.next`; the last sets `curr.next` to `null` | `[1, 3]` |
| Every node matches | `[7, 7, 7, 7]` | 7 | `dummy.next` is rewired four times while `curr` never leaves the sentinel | `[]` |
| Empty list | `[]` | 1 | the loop guard on `curr.next` fails on the first test | `[]` |

The all-matching row is the strongest evidence for the sentinel: a solution without it would have to advance `head` four times and could end holding `null`, whereas here `curr` is still the dummy when the loop exits and `dummy.next` is already `null`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The loop executes at most $N$ iterations because each iteration either advances `curr` or removes a node from the remaining chain.
- **Auxiliary Space Complexity:** $O(1)$ constant extra space, creating only a single sentinel `ListNode` object.
