# Guided Example: Remove Duplicates from Sorted List II

We trace the step-by-step complete duplicate cluster excision on a representative sorted linked list:

- **Input:** $\text{head} = [1, 2, 3, 3, 4, 4, 5]$
- **Required output:** $[1, 2, 5]$
- **Head Duplicate Deletion:** $\text{head} = [1, 1, 1, 2, 3] \implies [2, 3]$

This instance demonstrates using a sentinel dummy node to handle deletions at the head of the list, detecting contiguous duplicate clusters ($\text{cur.val} == \text{cur.next.val}$), skipping all instances of duplicate values, and rewiring the predecessor anchor in strictly $O(N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given the head of a sorted linked list of $7$ nodes:
$$
1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 3 \longrightarrow 4 \longrightarrow 4 \longrightarrow 5 \longrightarrow \emptyset
$$
delete **all** nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Notice the difference from LeetCode 83 (which leaves one instance of each duplicate):
- Here, values $3$ and $4$ appear multiple times, so **every** node containing $3$ or $4$ must be eliminated completely.
- The resulting list must contain only $1 \to 2 \to 5$.

A naive approach using a hash map counter takes $O(N)$ extra memory and two passes.
By exploiting the sorted property, duplicate values appear strictly contiguously. A sentinel dummy node and a two-pointer rewiring loop eliminate whole duplicate clusters in a single forward pass without extra memory allocations.

---

## 2. Conceptual Foundation & Invariants

### Predecessor Anchor Protocol
Because the head node itself might be part of a duplicate cluster (e.g. $[1, 1, 2]$), we prepend a sentinel node:
$$
\text{dummy} \longrightarrow \text{head}
$$
We maintain:
- `prev`: The last confirmed distinct node (initially `prev = dummy`).
- `cur`: The candidate node currently being inspected (initially `cur = head`).

### Excision Loop (While `cur` is not null)
1. **Duplicate Detection:**
   Check if `cur.next` exists and $\text{cur.val} == \text{cur.next.val}$:
   - If **True**, a duplicate cluster is present:
     - Store duplicate value: $\text{dup\_val} = \text{cur.val}$.
     - Advance `cur` while $\text{cur} \ne \emptyset$ and $\text{cur.val} == \text{dup\_val}$:
       $$
       \text{cur} \leftarrow \text{cur.next}
       $$
     - Excision link:
       $$
       \text{prev.next} \leftarrow \text{cur}
       $$
     - *(Crucial: do **not** advance `prev`, because the new node at `cur` might itself be the start of another duplicate cluster!)*.
   - If **False**, `cur` is a unique node:
     - Advance anchor: $\text{prev} \leftarrow \text{cur}$.
     - Advance candidate: $\text{cur} \leftarrow \text{cur.next}$.

> **Invariant.** The sublist from `dummy` to `prev` contains only confirmed, strictly distinct elements that will never be modified again.

---

## 3. Step-by-Step Worked Execution

We trace $\text{head} = [1, 2, 3, 3, 4, 4, 5]$:

### Initialization
- Prepend sentinel: $\text{dummy}.\text{next} \to \text{Node}(1)$.
- Pointers: $\text{prev} = \text{dummy}$, $\text{cur} = \text{Node}(1)$.

---

### Step 1: Examine Node 1
- `cur.val = 1`, `cur.next.val = 2`.
- Distinct! ($1 \ne 2$).
- Advance: $\text{prev} \leftarrow \text{Node}(1)$, $\text{cur} \leftarrow \text{Node}(2)$.
- Confirmed list: $\text{dummy} \to 1$.

---

### Step 2: Examine Node 2
- `cur.val = 2`, `cur.next.val = 3`.
- Distinct! ($2 \ne 3$).
- Advance: $\text{prev} \leftarrow \text{Node}(2)$, $\text{cur} \leftarrow \text{Node}(3)$.
- Confirmed list: $\text{dummy} \to 1 \to 2$.

---

### Step 3: Examine Node 3 (Duplicate Cluster Detected)
- `cur.val = 3`, `cur.next.val = 3` ($3 == 3$).
- Duplicate value: $\text{dup\_val} = 3$.
- Advance `cur` past all nodes with value 3:
  - Skip first 3 $\to$ at second 3.
  - Skip second 3 $\to$ at $\text{Node}(4)$.
  - Node 4 has value $4 \ne 3$. Advance halts with $\text{cur} = \text{Node}(4)$.
- Excision: Rewire $\text{prev.next} \leftarrow \text{cur}$ ($\text{Node}(2).\text{next} \to \text{Node}(4)$).
- State: $\text{prev}$ remains at $\text{Node}(2)$, `cur` is $\text{Node}(4)$.

---

### Step 4: Examine Node 4 (Consecutive Duplicate Cluster Detected)
- `cur.val = 4`, `cur.next.val = 4` ($4 == 4$).
- Duplicate value: $\text{dup\_val} = 4$.
- Advance `cur` past all nodes with value 4:
  - Skip first 4 $\to$ at second 4.
  - Skip second 4 $\to$ at $\text{Node}(5)$.
  - Advance halts with $\text{cur} = \text{Node}(5)$.
- Excision: Rewire $\text{prev.next} \leftarrow \text{cur}$ ($\text{Node}(2).\text{next} \to \text{Node}(5)$).
- State: $\text{prev}$ remains at $\text{Node}(2)$, `cur` is $\text{Node}(5)$.

---

### Step 5: Examine Node 5
- `cur.val = 5`, `cur.next == None`.
- Distinct!
- Advance: $\text{prev} \leftarrow \text{Node}(5)$, $\text{cur} \leftarrow \text{None}$.
- Confirmed list: $\text{dummy} \to 1 \to 2 \to 5$.

`cur` is null; loop terminates.
Return $\text{dummy.next} \implies 1 \longrightarrow 2 \longrightarrow 5 \longrightarrow \emptyset$.

---

## 4. Complete Execution Trace

| Step | Current Candidate $\text{cur}$ | Value Comparison ($\text{cur.val}$ vs $\text{cur.next.val}$) | Duplicate Flag? | Cluster Nodes Skipped | Link Rewired ($\text{prev.next}$) | Retained Chain |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 1 | $\text{Node}(1)$ | $1 \ne 2$ | No | None | Advance `prev` to $\text{Node}(1)$ | $\text{dummy} \to 1$ |
| 2 | $\text{Node}(2)$ | $2 \ne 3$ | No | None | Advance `prev` to $\text{Node}(2)$ | $\text{dummy} \to 1 \to 2$ |
| 3 | $\text{Node}(3)$ | $3 == 3$ | **Yes** | $\text{Node}(3), \text{Node}(3)$ | $\text{Node}(2).\text{next} \to \text{Node}(4)$ | $\text{dummy} \to 1 \to 2$ |
| 4 | $\text{Node}(4)$ | $4 == 4$ | **Yes** | $\text{Node}(4), \text{Node}(4)$ | $\text{Node}(2).\text{next} \to \text{Node}(5)$ | $\text{dummy} \to 1 \to 2$ |
| 5 | $\text{Node}(5)$ | $\text{cur.next} == \emptyset$ | No | None | Advance `prev` to $\text{Node}(5)$ | $\text{dummy} \to 1 \to 2 \to 5$ |
| Exit | $\emptyset$ | - | - | - | - | **Final: $[1, 2, 5]$** |

---

## 5. Algorithmic Correctness

**Soundness.** A node is retained if and only if it differs from both its predecessor and successor. Because the list is sorted, all occurrences of any value are adjacent. Skipping the inner while-loop when $\text{cur.val} == \text{cur.next.val}$ guarantees that every node sharing $\text{dup\_val}$ is bypassed by the pointer assignment $\text{prev.next} = \text{cur}$.

**Completeness.** Pointer `cur` advances strictly forward along the list without looping or backtracking, examining every node in the original linked list.

---

## 6. Traps This Instance Exposes

- **Advancing `prev` Too Early:** Advancing `prev = prev.next` immediately after bypassing a duplicate cluster breaks if consecutive different duplicate clusters follow each other (e.g. $3, 3$ followed immediately by $4, 4$). Keeping `prev` anchored until a node is proven unique handles back-to-back clusters correctly.
- **Head Node Duplicates ($[1, 1, 2]$):** Without a dummy sentinel node, deleting the head requires separate special-case code to update the head pointer. The dummy node makes head deletions identical to interior node deletions.
- **Null-Check on `.next`:** In the while-loop skipping duplicates, testing `cur and cur.val == dup_val` prevents `NullPointerException` / `AttributeError` when a duplicate cluster extends to the very end of the list (e.g. $[1, 2, 2]$).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. Every node is visited at most twice (once by `cur` and once by the inner cluster skip loop).
- **Auxiliary Space Complexity:** $O(1)$. Pointers are rewired strictly in place without allocating new node structures.