# Guided Example: Remove Duplicates from Sorted List

We trace the step-by-step single-pointer duplicate bypass on a representative sorted linked list:

- **Input:** $\text{head} = [1, 1, 2, 3, 3]$
- **Required output:** $[1, 2, 3]$

This instance demonstrates in-place successor link rewiring (`cur.next = cur.next.next`), maintaining the active node when a duplicate is bypassed, advancing only when adjacent values differ, and contrasting retaining one duplicate copy versus complete deletion.

---

## 1. Instance & Teaching Goal

Given the head of a sorted linked list:
$$
1 \longrightarrow 1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 3 \longrightarrow \emptyset
$$
delete all duplicates such that each element appears **only once**, returning the linked list sorted as well.

In this instance:
- The value $1$ appears twice $\implies$ delete one node, keeping one $1$.
- The value $2$ appears once $\implies$ keep it.
- The value $3$ appears twice $\implies$ delete one node, keeping one $3$.
The result is $1 \longrightarrow 2 \longrightarrow 3 \longrightarrow \emptyset$.

In contrast to LeetCode 82 (which completely eliminates all numbers that have duplicates), LeetCode 83 retains the first occurrence of every number and unlinks subsequent duplicates. This requires only a single pointer `cur` without dummy sentinel nodes or predecessor tracking.

The two semantics diverge sharply on the same input, which is the fastest way to keep them apart:

| Input list | This problem's result (keep one copy) | Complete-excision result (drop every repeated value) | Decisive difference |
|:---|:---|:---|:---|
| $[1, 1, 2, 3, 3]$ | $[1, 2, 3]$ | $[2]$ | $1$ and $3$ are each represented once rather than erased. |
| $[1, 1, 2]$ | $[1, 2]$ | $[2]$ | The surviving copy of $1$ is the retained head node. |
| $[1, 2, 3]$ | $[1, 2, 3]$ | $[1, 2, 3]$ | With no duplicates at all the two problems agree. |
| $[1, 1]$ | $[1]$ | $[\ ]$ | Surplus copies are unlinked; the first occurrence is never at risk. |

---

## 2. Conceptual Foundation & Invariants

### Single-Pointer Successor Bypass
We initialize `cur = head`.
While `cur` is not null and `cur.next` is not null:
1. **Duplicate Check:**
   Compare $\text{cur.val}$ with $\text{cur.next.val}$:
   - **If $\text{cur.val} == \text{cur.next.val}$:**
     The node at `cur.next` is a duplicate of `cur`.
     Bypass it by rewiring:
     $$
     \text{cur.next} \leftarrow \text{cur.next.next}
     $$
     *(Do **not** advance `cur`, because the new successor might also share the same value, e.g. in a run of three identical nodes like $[1, 1, 1]$)*.
   - **If $\text{cur.val} \ne \text{cur.next.val}$:**
     The successor has a distinct new value.
     Safely advance pointer:
     $$
     \text{cur} \leftarrow \text{cur.next}
     $$

> **Invariant.** The sublist from `head` up to `cur` contains strictly unique, sorted values with zero duplicates.

---

## 3. Step-by-Step Worked Execution

We trace $\text{head} = [1, 1, 2, 3, 3]$:

### Initialization
- Pointer `cur` placed at `Node(1)` (the first node).
- Active list: $1 \to 1 \to 2 \to 3 \to 3$.

---

### Step 1: Compare First and Second Nodes
- `cur.val = 1`, `cur.next.val = 1`.
- Condition: Values match ($1 == 1$).
- Bypass: Set $\text{Node}(1).\text{next} \leftarrow \text{Node}(2)$.
- The second node with value $1$ is unlinked.
- Pointer: `cur` remains at the first `Node(1)`.
- List state: $1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 3 \longrightarrow \emptyset$.

---

### Step 2: Compare First and Second Nodes (After Bypass)
- `cur.val = 1`, `cur.next.val = 2`.
- Condition: Values differ ($1 \ne 2$).
- Action: Advance `cur` to `Node(2)`.
- List state: $1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 3$.

---

### Step 3: Compare Node 2 and Node 3
- `cur.val = 2`, `cur.next.val = 3`.
- Condition: Values differ ($2 \ne 3$).
- Action: Advance `cur` to first `Node(3)`.
- List state: $1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 3$.

---

### Step 4: Compare Node 3 and its Successor
- `cur.val = 3`, `cur.next.val = 3`.
- Condition: Values match ($3 == 3$).
- Bypass: Set $\text{Node}(3).\text{next} \leftarrow \emptyset$.
- The second node with value $3$ is unlinked.
- Pointer: `cur` remains at first `Node(3)`.
- List state: $1 \longrightarrow 2 \longrightarrow 3 \longrightarrow \emptyset$.

---

### Step 5: Termination
- `cur.next == None`.
- Loop halts. Return `head` ($1 \longrightarrow 2 \longrightarrow 3$).

---

### Instance 2: Every Node Equal ($[7, 7, 7, 7, 7]$)

This is the case that punishes advancing `cur` inside the bypass branch. Nodes are named
$\text{N}_0$ through $\text{N}_4$ by their original position, and `cur` never leaves
$\text{N}_0$: each iteration removes exactly one successor from the live chain.

| Step | Comparison at `cur` | `cur.next` after the step | Position of `cur` | Live chain |
|:---:|:---|:---|:---|:---|
| 1 | $7 == 7$ ($\text{N}_0$ vs $\text{N}_1$) | $\text{N}_2$ | $\text{N}_0$, unchanged | $\text{N}_0 \to \text{N}_2 \to \text{N}_3 \to \text{N}_4$ |
| 2 | $7 == 7$ ($\text{N}_0$ vs $\text{N}_2$) | $\text{N}_3$ | $\text{N}_0$, unchanged | $\text{N}_0 \to \text{N}_3 \to \text{N}_4$ |
| 3 | $7 == 7$ ($\text{N}_0$ vs $\text{N}_3$) | $\text{N}_4$ | $\text{N}_0$, unchanged | $\text{N}_0 \to \text{N}_4$ |
| 4 | $7 == 7$ ($\text{N}_0$ vs $\text{N}_4$) | $\emptyset$ | $\text{N}_0$, unchanged | $\text{N}_0$ |
| Exit | Guard `cur.next` is $\emptyset$ | — | — | **Final: $[7]$** |

A stationary pointer does not mean stationary work: five equal nodes still cost four
unlinks, and the answer is the original head node $\text{N}_0$ itself. Advancing `cur`
after the first bypass would have stopped with $[7, 7]$ still linked, which is exactly the
trap described in Section 6.

---

## 4. Complete Execution Trace

| Step | Active Pointer $\text{cur}$ | Next Node $\text{cur.next}$ | Comparison ($\text{cur.val}$ vs $\text{cur.next.val}$) | Action Taken | List State After Step |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | $\text{Node}(1)$ | $\text{Node}(1)$ | $1 == 1$ (Match) | Bypass next: $\text{cur.next} = \text{cur.next.next}$ | $1 \to 2 \to 3 \to 3$ |
| 2 | $\text{Node}(1)$ | $\text{Node}(2)$ | $1 \ne 2$ (Distinct) | Advance `cur` to $\text{Node}(2)$ | $1 \to 2 \to 3 \to 3$ |
| 3 | $\text{Node}(2)$ | $\text{Node}(3)$ | $2 \ne 3$ (Distinct) | Advance `cur` to $\text{Node}(3)$ | $1 \to 2 \to 3 \to 3$ |
| 4 | $\text{Node}(3)$ | $\text{Node}(3)$ | $3 == 3$ (Match) | Bypass next: $\text{cur.next} = \emptyset$ | $1 \to 2 \to 3 \to \emptyset$ |
| Exit | $\text{Node}(3)$ | $\emptyset$ | Loop terminates | - | **Final: $[1, 2, 3]$** |

---

## 5. Algorithmic Correctness

**Soundness.** Because the input list is sorted, any duplicates of $\text{cur.val}$ must occur immediately adjacent to `cur`. When $\text{cur.val} == \text{cur.next.val}$, unlinking `cur.next` removes one duplicate while preserving `cur`. Keeping `cur` fixed ensures that multiple consecutive duplicates (e.g. $[1, 1, 1, 1]$) are pruned one by one until a distinct value or null is reached.

**Completeness.** When $\text{cur.val} \ne \text{cur.next.val}$, the value at `cur` has no further duplicates in the list. Advancing `cur` monotonically processes every node in the chain without skipping valid elements.

---

## 6. Traps This Instance Exposes

- **Advancing `cur` on Bypass:** If you write `cur = cur.next` inside the bypass branch, a run of three identical nodes like $[1, 1, 1]$ will only remove the second node and leave $[1, 1]$ unpruned. Pointer advancement must only occur when values are strictly different.
- **Empty or Single-Node List:** If $\text{head} == \emptyset$ or $\text{head.next} == \emptyset$, the loop condition `cur and cur.next` evaluates to false immediately, safely returning `head` without null pointer errors.

### Boundary Instances and Their Verdicts

| Instance | Input list | Expected output | Boundary exercised | Why the single-pointer protocol is correct here |
|:---|:---|:---|:---|:---|
| One duplicate run | $[1, 1, 2]$ | $[1, 2]$ | Duplicate at the very front | The first node is never unlinked, so the returned head needs no repair. |
| Duplicate prefix and suffix | $[1, 1, 2, 3, 3]$ | $[1, 2, 3]$ | Two separate runs | Each run is pruned when `cur` reaches its first node; $2$ is untouched because both neighbours differ from it. |
| Empty list | $[\ ]$ | $[\ ]$ | No nodes | The guard `cur and cur.next` fails on the first test and `head` is returned unchanged. |
| Already unique list | $[-2, 0, 4]$ | $[-2, 0, 4]$ | Identity case, negative values | Every comparison finds distinct values, so `cur` simply walks to the last node and no link is ever rewritten. |
| Every node equal | $[7, 7, 7, 7, 7]$ | $[7]$ | One maximal run | Each bypass shortens the chain by one node while `cur` stays at the head, leaving a single copy. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. Each node is inspected once.
- **Auxiliary Space Complexity:** $O(1)$. Modifies list pointers strictly in place.
