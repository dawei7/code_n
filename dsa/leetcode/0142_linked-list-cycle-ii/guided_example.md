# Guided Example: Linked List Cycle II

We trace the step-by-step mathematical derivation and two-phase pointer reset of Floyd's Cycle Detection Algorithm to locate the exact cycle entrance on representative linked list instances:

- **Input:** $\text{head} = [3, 2, 0, -4]$ with tail node $-4$ pointing back to node $2$ ($\text{pos} = 1$)
- **Required output:** Reference to $\text{Node}(2)$ (the cycle entry node)
- **Acyclic Base Instance:** $\text{head} = [1, 2], \text{pos} = -1 \implies \text{null}$

This instance demonstrates the algebraic proof relating non-cyclic prefix length $L$ to modular cycle circumference $C$ ($L = k \cdot C - d$), explains why resetting one pointer to `head` while keeping the other at the collision point guarantees intersection at the entry node, and achieves linear $O(N)$ runtime with strictly $O(1)$ auxiliary memory without modifying the list.

---

## 1. Instance & Teaching Goal

Given the head of a linked list:
$$
3 \overset{L=1}{\longrightarrow} \mathbf{2} \overset{d=1}{\longrightarrow} 0 \overset{d=2}{\longrightarrow} -4 \overset{}{\longrightarrow} (\text{loops back to } \mathbf{2})
$$
where node $-4$ links back to node $2$. Find the **exact node where the cycle begins**. If there is no cycle, return `null`. Do not modify the linked list.

In this instance:
- Prefix before cycle: node $3$ (length $L = 1$).
- Cycle entrance: node $2$.
- Cycle circumference: $C = 3$ nodes ($2 \to 0 \to -4 \to 2$).
The algorithm must return the node object with value $2$.

A hash set storing visited node addresses can identify the first repeated node, but requires $O(N)$ extra memory.
Floyd's two-phase pointer algorithm:
1. **Phase 1:** Detects whether a cycle exists using `slow` (speed 1) and `fast` (speed 2).
2. **Phase 2:** Once they collide at node $-4$, resets one pointer to `head` and advances both pointers at speed 1. They collide at the cycle entry node in $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Mathematical Proof of Cycle Entry Alignment
Let:
- $L$: distance from `head` to the cycle entrance.
- $C$: circumference (length) of the cycle.
- $d$: distance from the cycle entrance to the meeting point inside the cycle.

At the moment `slow` and `fast` collide:
1. Total distance traveled by `slow`:
   $$
   D_{\text{slow}} = L + d
   $$
2. Total distance traveled by `fast`:
   $$
   D_{\text{fast}} = L + d + k \cdot C \quad (\text{for some integer } k \ge 1)
   $$
3. Because `fast` moves twice as fast as `slow`:
   $$
   D_{\text{fast}} = 2 \cdot D_{\text{slow}}
   $$
   $$
   L + d + k \cdot C = 2(L + d)
   $$
4. Rearranging terms:
   $$
   L + d = k \cdot C \implies L = k \cdot C - d = (k - 1) \cdot C + (C - d)
   $$

### The Phase 2 Discovery Principle
Look at the derived identity $L = (k - 1) \cdot C + (C - d)$:
- $L$ is the distance from `head` to the cycle entrance.
- $(C - d)$ is the remaining distance from the collision point forward to the cycle entrance.
- $(k - 1) \cdot C$ represents full integer revolutions around the cycle.

Therefore, if we place pointer $P_1$ at `head` and pointer $P_2$ at the collision point, and advance **both** at the identical velocity of $1$ node per step:
When $P_1$ walks $L$ steps, it arrives at the cycle entrance.
Simultaneously, $P_2$ walks $(k - 1) \cdot C + (C - d)$ steps, completing full laps and landing **at the exact same cycle entrance node**!

> **Invariant.** The first point of intersection between $P_1$ (advancing from `head`) and $P_2$ (advancing from the Phase 1 collision point) is mathematically guaranteed to be the cycle entry node.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{head} = [3, 2, 0, -4]$ where $-4 \to 2$:
$L = 1$, $C = 3$, entrance node is Node(2).

### Phase 1: Detect Collision
- Initial: `slow = Node(3)`, `fast = Node(3)`.

- **Step 1:**
  - `slow`: $\text{Node}(3) \to \text{Node}(2)$.
  - `fast`: $\text{Node}(3) \to \text{Node}(2) \to \text{Node}(0)$.
  - `slow != fast` ($2 \ne 0$).

- **Step 2:**
  - `slow`: $\text{Node}(2) \to \text{Node}(0)$.
  - `fast`: $\text{Node}(0) \to \text{Node}(-4) \to \text{Node}(2)$.
  - `slow != fast` ($0 \ne 2$).

- **Step 3:**
  - `slow`: $\text{Node}(0) \to \text{Node}(-4)$.
  - `fast`: $\text{Node}(2) \to \text{Node}(0) \to \text{Node}(-4)$.
  - **Phase 1 Collision Detected at $\text{Node}(-4)$!**

Distance inside cycle from entrance: $d = \text{dist}(\text{Node}(2) \to \text{Node}(-4)) = 2$.

---

### Phase 2: Locate Cycle Entrance
- Keep `ptr2 = Node(-4)` (collision point).
- Reset `ptr1 = head = Node(3)`.
- Advance both pointers at speed $1$:

- **Step 1:**
  - `ptr1`: $\text{Node}(3) \to \mathbf{\text{Node}(2)}$ ($1$ step from `head`).
  - `ptr2`: $\text{Node}(-4) \to \mathbf{\text{Node}(2)}$ ($C - d = 3 - 2 = 1$ step from collision).
  - **Collision Detected!**
    $$
    \text{ptr1} == \text{ptr2} == \mathbf{\text{Node}(2)}
    $$

Return reference to $\mathbf{\text{Node}(2)}$.

---

## 4. Complete Execution Trace

```text
Phase 1:
Step 0:   [3] -> [2] -> [0] -> [-4]
         S, F     ^              |
                  \--------------/
Step 3:   Collision at [-4] (S == F == -4)

Phase 2:
Reset:    ptr1 = [3],  ptr2 = [-4]
Step 1:   ptr1 -> [2], ptr2 -> [2]
          ptr1 == ptr2 == [2] (CYCLE ENTRANCE FOUND!)
```

| Phase | Step | `ptr1` / `slow` Location | `ptr2` / `fast` Location | Match? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | $\text{Node}(3)$ | $\text{Node}(3)$ | Yes (Start) | Advance $\text{slow}\times 1, \text{fast}\times 2$ |
| 1 | 1 | $\text{Node}(2)$ | $\text{Node}(0)$ | No | Advance |
| 1 | 2 | $\text{Node}(0)$ | $\text{Node}(2)$ | No | Advance |
| **1** | **3** | **$\text{Node}(-4)$** | **$\text{Node}(-4)$** | **Yes** | **Collision! Begin Phase 2** |
| 2 | Reset | $\text{Node}(3)$ (from head) | $\text{Node}(-4)$ (from collision) | No | Advance both $\times 1$ |
| **2** | **1** | **$\text{Node}(2)$** | **$\text{Node}(2)$** | **Yes** | **Cycle Entrance! Return $\text{Node}(2)$** |

---

## 5. Algorithmic Correctness

**Soundness.** From the algebraic equation $L = (k-1)C + (C-d)$, moving $L$ steps from `head` lands on the entrance node, while moving $L$ steps from the meeting point traverses the remaining $C-d$ distance to the entrance followed by $(k-1)$ full loops. Thus, both pointers arrive at the cycle entry node at the exact same step.

**Completeness.** If the list has no cycle, `fast` encounters `null` in Phase 1, correctly returning `null`. If a cycle exists, Phase 1 terminates in at most $L + C$ steps, and Phase 2 terminates in exactly $L$ steps.

---

## 6. Traps This Instance Exposes

- **Acyclic List Check in Phase 1:** If the while loop terminates without collision (`not fast or not fast.next`), immediately return `null`.
- **Modifying Node Values:** Altering node values or injecting sentinel markers (like `node.val = 100001`) modifies user data and is strictly forbidden by the problem statement.
- **Head is the Cycle Entrance ($L = 0$):** If the tail links directly back to `head` (e.g. $[1, 2]$ with $2 \to 1$), Phase 1 collision occurs, and Phase 2 immediately detects `ptr1 == ptr2 == head` at Step 0, correctly returning `head`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of nodes. Phase 1 takes at most $L + C \le N$ iterations. Phase 2 takes exactly $L \le N$ iterations. Total runtime is linear $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, maintaining only pointer references (`slow`, `fast`, `ptr1`, `ptr2`).