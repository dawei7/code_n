# Guided Example: Linked List Cycle

We trace the step-by-step convergence of Floyd's Cycle-Finding Algorithm (Tortoise and Hare) on representative cyclic and acyclic linked list instances:

- **Input:** $\text{head} = [3, 2, 0, -4]$, with tail node $-4$ connected back to node $2$ at index $\text{pos} = 1$
- **Required output:** `true` (Cycle confirmed via pointer collision)
- **Acyclic Base Instance:** $\text{head} = [1, 2], \text{pos} = -1 \implies \text{false}$ (Fast reaches null terminal)

This instance demonstrates Floyd's two-pointer algorithm with differential velocities ($v_{\text{slow}} = 1, v_{\text{fast}} = 2$), proves relative distance reduction ($\Delta d = 1$ per tick modulo cycle length $C$), bounds worst-case convergence steps ($O(N)$), and operates with strictly $O(1)$ auxiliary space without hash sets or node modifications.

---

## 1. Instance & Teaching Goal

Given the head of a linked list with $4$ nodes:
$$
3 \longrightarrow \mathbf{2} \longrightarrow 0 \longrightarrow -4 \longrightarrow (\text{loops back to } \mathbf{2})
$$
Determine whether the list contains a cycle.

In this instance:
- Node $0$ has value $3$, pointing to Node $1$ (value $2$).
- The cycle comprises three nodes: $2 \to 0 \to -4 \to 2$.
- Advancing infinitely along `next` pointers never encounters `null`.
The algorithm must return `true`.

Storing visited nodes in a hash set achieves $O(N)$ time, but consumes $O(N)$ auxiliary memory.
Floyd's Cycle-Finding Algorithm uses two pointers moving at different speeds:
- A `slow` pointer advancing $1$ node per step.
- A `fast` pointer advancing $2$ nodes per step.
If a cycle exists, the faster pointer enters the cycle first and closes the gap on the slower pointer by exactly $1$ node per iteration, guaranteeing a collision without extra space.

---

## 2. Conceptual Foundation & Invariants

### The Floyd Collision Principle
Let the distance from `head` to the cycle entrance be $K$, and the perimeter of the cycle be $C$.

1. **Phase 1: Entering the Cycle:**
   The `slow` pointer enters the cycle after exactly $K$ steps. By this time, the `fast` pointer is already inside the cycle at some relative position.
2. **Phase 2: Catch-Up Dynamics:**
   Once both pointers are inside the cycle, let the distance from `slow` to `fast` measured along the direction of traversal be $d \in [0, C-1]$.
   In each successive iteration:
   $$
   \text{pos}_{\text{slow}}' = (\text{pos}_{\text{slow}} + 1) \bmod C
   $$
   $$
   \text{pos}_{\text{fast}}' = (\text{pos}_{\text{fast}} + 2) \bmod C
   $$
   The distance from `fast` behind `slow` decreases by:
   $$
   (2 - 1) = 1 \text{ step per iteration}
   $$
   Since the gap strictly decreases by $1$ in every step, `fast` is mathematically guaranteed to collide with `slow` within at most $C$ iterations.

### Two-Pointer Protocol
Initialize `slow = head`, `fast = head`.
While `fast is not None` and `fast.next is not None`:
1. `slow = slow.next`
2. `fast = fast.next.next`
3. `if slow == fast: return True`
If the loop terminates because `fast` or `fast.next` is `None`, return `False`.

> **Invariant.** If the list is acyclic, `fast` reaches `null` in $\lceil N/2 \rceil$ steps. If the list contains a cycle, `fast` never encounters `null` and catches `slow` in at most $K + C$ iterations.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{head} = [3, 2, 0, -4]$ where $-4 \to 2$:
Cycle length $C = 3$, non-cyclic prefix $K = 1$.

### Initial State (Step 0)
- `slow` points to Node 0 (value $3$).
- `fast` points to Node 0 (value $3$).

---

### Step 1
- Advance `slow` by 1: $\text{Node}(3) \to \mathbf{\text{Node}(2)}$.
- Advance `fast` by 2: $\text{Node}(3) \to \text{Node}(2) \to \mathbf{\text{Node}(0)}$.
- Pointers: `slow = Node(2)`, `fast = Node(0)`.
- `slow != fast` ($2 \ne 0$). Loop continues.

---

### Step 2
- Advance `slow` by 1: $\text{Node}(2) \to \mathbf{\text{Node}(0)}$.
- Advance `fast` by 2: $\text{Node}(0) \to \text{Node}(-4) \to \mathbf{\text{Node}(2)}$ (wraps around cycle!).
- Pointers: `slow = Node(0)`, `fast = Node(2)`.
- `slow != fast` ($0 \ne 2$). Loop continues.

---

### Step 3
- Advance `slow` by 1: $\text{Node}(0) \to \mathbf{\text{Node}(-4)}$.
- Advance `fast` by 2: $\text{Node}(2) \to \text{Node}(0) \to \mathbf{\text{Node}(-4)}$.
- **Pointer Collision Detected!**
  $$
  \text{slow} == \text{fast} == \mathbf{\text{Node}(-4)}
  $$
- Both pointers occupy the identical memory address at Node $-4$.
- Immediately return `true`!

---

## 4. Complete Execution Trace

```text
Step 0:   [3] -> [2] -> [0] -> [-4]
         S, F     ^              |
                  \--------------/

Step 1:   [3] -> [2] -> [0] -> [-4]
                  S      F

Step 2:   [3] -> [2] -> [0] -> [-4]
                  F      S

Step 3:   [3] -> [2] -> [0] -> [-4]
                               S, F  ==> COLLISION DETECTED!
```

| Iteration Step | `slow` Node (Value) | `fast` Traversal Path | `fast` Node (Value) | `slow == fast`? | Action Taken |
|:---:|:---:|:---|:---:|:---:|:---|
| 0 (Start) | $N_0$ ($3$) | Base head | $N_0$ ($3$) | True (Initial) | Enter loop |
| 1 | $N_1$ ($2$) | $N_0 \to N_1 \to N_2$ | $N_2$ ($0$) | False | Continue |
| 2 | $N_2$ ($0$) | $N_2 \to N_3 \to N_1$ | $N_1$ ($2$) | False | Continue |
| **3** | **$N_3$ ($-4$)** | **$N_1 \to N_2 \to N_3$** | **$N_3$ ($-4$)** | **True** | **Collision! Return `true`** |

### Relative Gap Dynamics Inside the Cycle

Numbering the cycle nodes in traversal order as $N_1 = 0$, $N_2 = 1$, and
$N_3 = 2$ gives the cycle coordinate of each pointer. The trailing distance
$(\text{pos}_{\text{slow}} - \text{pos}_{\text{fast}}) \bmod 3$ is the quantity
the invariant claims decreases by exactly $1$ per tick.

| Iteration | `slow` cycle coordinate | `fast` cycle coordinate | Trailing distance $(\text{pos}_{\text{slow}} - \text{pos}_{\text{fast}}) \bmod 3$ | `slow == fast`? | Why this state is consistent with the invariant |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | outside the cycle at $N_0$ | outside the cycle at $N_0$ | undefined — neither pointer has entered the cycle yet | True, but never tested | Both pointers begin at the head, so their coincidence at step $0$ carries no evidence; only equality observed *after* a double advance proves a cycle. |
| 1 | $0$ ($N_1$, value $2$) | $1$ ($N_2$, value $0$) | $(0 - 1) \bmod 3 = 2$ | False | `slow` has just entered the cycle at its entrance $N_1$, and `fast` sits one node ahead, so `fast` still has $2$ nodes to travel to reach `slow`. |
| 2 | $1$ ($N_2$, value $0$) | $0$ ($N_1$, value $2$) | $(1 - 0) \bmod 3 = 1$ | False | `fast` gained exactly one node on `slow`; the trailing distance fell from $2$ to $1$, the $\Delta d = 1$ decrement the invariant predicts. |
| **3** | **$2$ ($N_3$, value $-4$)** | **$2$ ($N_3$, value $-4$)** | **$(2 - 2) \bmod 3 = 0$** | **True — collision** | The trailing distance reached $0$ on the third iteration, satisfying the bound of at most $C = 3$ iterations once `slow` is inside the cycle. |

---

## 5. Algorithmic Correctness

**Soundness.** A list without a cycle contains a finite number of nodes ending in a `null` reference. Because `fast` advances strictly two nodes per iteration, it will encounter `null` in at most $\lceil N/2 \rceil$ steps and terminate with `false`. A pointer collision can occur if and only if both pointers are trapped in an infinite loop (a cycle).

**Completeness.** Once `slow` reaches the cycle, `fast` is already in the cycle. The distance from `fast` to `slow` along the cycle decreases by $1$ modulo $C$ on every step. A strictly decreasing positive integer sequence modulo $C$ must reach $0$, proving that a collision is mathematically unavoidable.

---

## 6. Traps This Instance Exposes

- **Null Pointer Dereference on Fast Runner:** Checking `while fast and fast.next:` is mandatory. On odd-length lists, `fast.next` will be `null`, so attempting `fast.next.next` without the guard throws a null reference exception.
- **Empty List and Single Node Without Loop:** If `head is None` or `head.next is None`, the while loop never executes and immediately returns `false`.
- **Identity Check vs Value Check:** The check must compare node references (`slow == fast`), never node values (`slow.val == fast.val`), because multiple distinct nodes in the list can have identical values.

### Boundary Inputs and Their Iteration Counts

| Boundary input | Node structure | Result | Loop iterations | Why the guard or the collision produces it |
|:---|:---|:---:|:---:|:---|
| `[]`, $\text{pos} = -1$ (empty list) | `head` is the null reference | `false` | 0 | The guard demands that both `fast` and `fast.next` exist; with `fast` already null the body never executes, and the method returns `false` without a single comparison. |
| `[7]`, $\text{pos} = 0$ (self-loop) | $N_0$ points to itself, so $K = 0$ and $C = 1$ | `true` | 1 | The guard passes because $N_0$ has a successor. One tick sends `slow` from $N_0$ to $N_0$ and `fast` from $N_0$ through $N_0$ back to $N_0$, so the two pointers coincide on the very first check. |
| `[1, 2]`, $\text{pos} = 0$ (tail links to head) | $N_0(1) \to N_1(2) \to N_0(1)$, so $K = 0$ and $C = 2$ | `true` | 2 | The entrance is the head, so `slow` is inside the cycle immediately. The trailing distance $(\text{pos}_{\text{slow}} - \text{pos}_{\text{fast}}) \bmod 2$ is $1$ after the first tick and $0$ after the second, where the pointers meet at $N_0$. |
| `[1]`, $\text{pos} = -1$ (one node, no loop) | $N_0(1) \to \text{null}$ | `false` | 0 | Here $N_0$ exists, but `fast.next` is null, so the guard rejects the first iteration and the method correctly reports the absence of a cycle. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of nodes. If no cycle exists, `fast` reaches the end in $N/2$ iterations. If a cycle exists, `slow` enters the cycle in $K$ steps, and `fast` catches `slow` in at most $C$ steps. Total iterations $\le K + C = N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only two pointer references (`slow` and `fast`).