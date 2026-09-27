# Guided Example: Intersection of Two Linked Lists

We trace the step-by-step two-pointer path equalization ($a + c + b = b + c + a$) on representative intersecting and non-intersecting linked list instances:

- **Input:** List $A = [4, 1, 8, 4, 5]$, List $B = [5, 6, 1, 8, 4, 5]$, intersecting at node with value $8$
- **Required output:** Reference to shared node $\text{Node}(8)$
- **Disjoint Lists Instance:** List $A = [2, 6, 4]$, List $B = [1, 5] \implies \text{null}$ (Both pointers reach `null` simultaneously)

This instance demonstrates the path-length equalization technique, eliminating the need for node hashing ($O(N)$ space) or length pre-computation passes, proving algebraic convergence at the intersection node or `null`, and operating in $O(N + M)$ time with strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given two singly linked lists $A$ and $B$:
$$
\begin{aligned}
A: \quad & 4 \longrightarrow 1 \searrow \\
& \quad\quad\quad\quad 8 \longrightarrow 4 \longrightarrow 5 \\
B: \quad & 5 \longrightarrow 6 \longrightarrow 1 \nearrow
\end{aligned}
$$
Find the node at which the two lists intersect by reference identity.

Because list $A$ has 2 prefix nodes before the intersection while list $B$ has 3 prefix nodes:
- Running two pointers in lockstep will reach the intersection at different times ($p_A$ reaches node 8 when $p_B$ is still at node 1).
- Storing visited nodes in a hash set requires $O(N)$ auxiliary heap allocations.

By redirecting each pointer to the head of the *other* list upon reaching `null`, both pointers traverse identical total distances:
$$
\text{Dist}(p_A) = |A| + |B_{\text{prefix}}| = (a + c) + b = a + b + c
$$
$$
\text{Dist}(p_B) = |B| + |A_{\text{prefix}}| = (b + c) + a = a + b + c
$$
Because both paths sum to $a + b + c$, $p_A$ and $p_B$ align perfectly and collide at the intersection node in at most two passes!

---

## 2. Conceptual Foundation & Invariants

### The Path-Equalization Theorem
Let $a$ be the length of list $A$'s unique prefix.
Let $b$ be the length of list $B$'s unique prefix.
Let $c$ be the length of the common suffix (with $c \ge 1$ if they intersect, or $c = 0$ if disjoint).

Maintain pointers $p_A$ (initially `headA`) and $p_B$ (initially `headB`):
- Advance both pointers by one step:
  $$
  p_A \leftarrow p_A.\text{next} \quad (\text{or } \text{headB if } p_A == \text{null})
  $$
  $$
  p_B \leftarrow p_B.\text{next} \quad (\text{or } \text{headA if } p_B == \text{null})
  $$
- Terminate when:
  $$
  p_A == p_B
  $$

#### Two Exhaustive Outcomes
1. **Intersection Exists ($c \ge 1$):**
   After exactly $a + b + c$ steps, $p_A$ and $p_B$ point to the same memory reference: the first shared node $\text{Node}(8)$.
2. **Disjoint Lists ($c = 0$):**
   After exactly $a + b$ steps, both pointers exhaust their respective second passes and become `null` simultaneously ($p_A == p_B == \text{null}$).

> **Invariant.** At any step $t$, the remaining distance from $p_A$ and $p_B$ to the intersection (or the terminal `null`) modulo $(a + b + c)$ decreases by 1 per step.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on:
- List $A$: $4 \to 1 \to 8 \to 4 \to 5 \to \emptyset$ ($a = 2, c = 3$, length $= 5$).
- List $B$: $5 \to 6 \to 1 \to 8 \to 4 \to 5 \to \emptyset$ ($b = 3, c = 3$, length $= 6$).

---

### Step 0 (Start)
- $p_A = \text{Node}(4)$
- $p_B = \text{Node}(5)$

---

### Step 1
- $p_A \to \text{Node}(1)$
- $p_B \to \text{Node}(6)$

---

### Step 2
- $p_A \to \text{Node}(8)$ *(Intersection node reached by $p_A$ first!)*
- $p_B \to \text{Node}(1)$

---

### Step 3
- $p_A \to \text{Node}(4)$
- $p_B \to \text{Node}(8)$ *(Intersection node reached by $p_B$)*

---

### Step 4
- $p_A \to \text{Node}(5)$
- $p_B \to \text{Node}(4)$

---

### Step 5
- $p_A \to \emptyset \implies$ **Switch to `headB`:** $p_A \leftarrow \text{Node}(5)$
- $p_B \to \text{Node}(5)$

---

### Step 6
- $p_A \to \text{Node}(6)$
- $p_B \to \emptyset \implies$ **Switch to `headA`:** $p_B \leftarrow \text{Node}(4)$

---

### Step 7
- $p_A \to \text{Node}(1)$
- $p_B \to \text{Node}(1)$

---

### Step 8: Collision!
- $p_A \to \mathbf{\text{Node}(8)}$
- $p_B \to \mathbf{\text{Node}(8)}$
- $p_A == p_B == \text{Node}(8)$.

Both pointers point to the exact same node object!
Return $\text{Node}(8)$.

---

## 4. Complete Execution Trace

```text
Path of pA: 4 -> 1 -> 8 -> 4 -> 5 -> [switch to B] -> 5 -> 6 -> 1 -> (8)
Path of pB: 5 -> 6 -> 1 -> 8 -> 4 -> 5 -> [switch to A] -> 4 -> 1 -> (8)
Collision at Step 8: Node(8) == Node(8)
```

| Step $t$ | Pointer $p_A$ Location | Pointer $p_B$ Location | List Switch Event | Equal? ($p_A == p_B$) |
|:---:|:---:|:---:|:---:|:---:|
| 0 | $\text{Node}(4)_A$ | $\text{Node}(5)_B$ | - | No |
| 1 | $\text{Node}(1)_A$ | $\text{Node}(6)_B$ | - | No |
| 2 | $\text{Node}(8)$ | $\text{Node}(1)_B$ | - | No |
| 3 | $\text{Node}(4)$ | $\text{Node}(8)$ | - | No |
| 4 | $\text{Node}(5)$ | $\text{Node}(4)$ | - | No |
| 5 | $\text{Node}(5)_B$ | $\text{Node}(5)$ | $p_A$ reaches null $\to$ `headB` | No |
| 6 | $\text{Node}(6)_B$ | $\text{Node}(4)_A$ | $p_B$ reaches null $\to$ `headA` | No |
| 7 | $\text{Node}(1)_B$ | $\text{Node}(1)_A$ | - | No |
| **8** | **$\text{Node}(8)$** | **$\text{Node}(8)$** | **Both land on shared node** | **Yes (Return Node(8))** |

---

## 5. Algorithmic Correctness

**Soundness.** Equality $p_A == p_B$ checks pointer identity (memory address), not integer value equality. Two nodes are identical if and only if they are the exact same list node in memory.

**Completeness.** Since $a + c + b = b + c + a$, both pointers take exactly $a + b + c$ steps to reach the intersection. If no intersection exists ($c = 0$), both take $a + b$ steps to reach `null` simultaneously, terminating the loop and returning `null`.

---

## 6. Traps This Instance Exposes

- **Switching on `p.next` vs `p`:** If you switch when `p.next is None` instead of `p is None`, non-intersecting lists will enter an infinite loop because neither pointer will ever land on `null` simultaneously! Pointers must be allowed to step onto `null` before redirecting.
- **Comparing Node Values Instead of References:** Two distinct nodes can happen to store the same integer value (e.g. both lists having a node with value `1` before the intersection). Testing `pA.val == pB.val` produces false intersections! Always test `pA is pB`.
- **Modifying the List:** Algorithms that attempt to introduce cycles or modify `next` pointers violate the immutability constraint of the input lists.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + M)$, where $N = |A|$ and $M = |B|$. Each pointer traverses at most $N + M$ nodes before either colliding at the intersection node or both reaching `null`.
- **Auxiliary Space Complexity:** $O(1)$ constant space, requiring only two local pointer variables ($p_A$ and $p_B$).