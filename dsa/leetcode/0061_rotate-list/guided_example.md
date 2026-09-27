# Guided Example: Rotate List

We trace the step-by-step circular-ring closure and split pointer manipulation on a representative linked list instance:

- **Input:** $\text{head} = [1, 2, 3, 4, 5], k = 2$
- **Required output:** $[4, 5, 1, 2, 3]$

This instance demonstrates counting linked list length $L$, taking effective modulo rotation ($k \pmod L$), closing the list into a circular ring, locating the split node at step $L - (k \pmod L)$, and severing the ring in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given the head of a linked list of $L = 5$ nodes:
$$
1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5 \longrightarrow \emptyset
$$
rotate the list to the right by $k = 2$ places.

Rotating right by 1 shifts the last node to the front: $[5, 1, 2, 3, 4]$.
Rotating right by 2 shifts the last two nodes to the front: $[4, 5, 1, 2, 3]$.

Notice that rotating by $L$ places returns the list to its exact original state. Hence, rotating by $k$ is identical to rotating by $k \pmod L$. The optimal algorithm links the tail to the head to form a circular ring, traverses to the new tail at position $L - (k \pmod L)$, and breaks the ring.

---

## 2. Conceptual Foundation & Invariants

### 4-Step Circular Ring Algorithm
1. **Edge Cases:** If $\text{head} == \emptyset$ or $\text{head.next} == \emptyset$ or $k == 0$, return $\text{head}$.
2. **Length Measurement & Ring Formation:**
   Traverse from $\text{head}$ to locate the tail node and compute length $L$.
   Connect the tail to the head:
   $$
   \text{tail.next} \leftarrow \text{head}
   $$
   *(The list is now a closed cycle).*
3. **Effective Offset:**
   Compute effective rotation:
   $$
   k' = k \pmod L
   $$
   If $k' == 0$, break $\text{tail.next} = \emptyset$ and return $\text{head}$.
4. **Locate Split Node:**
   The new head will be the $(L - k')$-th node (1-based), and the new tail will be the $(L - k')$-th node from the start.
   Advance a pointer $\text{steps} = L - k' - 1$ times from $\text{head}$:
   $$
   \text{new\_tail} = \text{node after } (L - k' - 1) \text{ steps}
   $$
   $$
   \text{new\_head} = \text{new\_tail.next}
   $$
   $$
   \text{new\_tail.next} = \emptyset
   $$

> **Invariant.** Closing the list into a cycle guarantees that advancing $L - k'$ steps from the original head always reaches the correct new head without wrapping logic.

---

## 3. Step-by-Step Worked Execution

We trace $\text{head} = [1, 2, 3, 4, 5]$ with $k = 2$:

### Step 1: Traverse to Tail and Measure Length
- Start at node $1$ ($L = 1$).
- Advance: $1 \to 2$ ($L = 2$).
- Advance: $2 \to 3$ ($L = 3$).
- Advance: $3 \to 4$ ($L = 4$).
- Advance: $4 \to 5$ ($L = 5$, $\text{node.next} == \emptyset$).
- Length is $L = 5$, and $\text{tail}$ is node $5$.

---

### Step 2: Form Circular Ring
- Connect tail to head:
  $$
  \text{node}(5).\text{next} \leftarrow \text{node}(1)
  $$
- Structure is now a 5-node cycle:
  $$
  1 \to 2 \to 3 \to 4 \to 5 \to 1 \to \dots
  $$

---

### Step 3: Compute Effective Shift
- $k' = k \pmod L = 2 \pmod 5 = 2$.
- The new tail is located at step:
  $$
  \text{steps} = L - k' - 1 = 5 - 2 - 1 = 2
  $$

---

### Step 4: Advance to New Tail and Sever Ring
- Start at original head (node 1).
- Step 1: Advance to node 2.
- Step 2: Advance to node 3.
- Stop! New tail is **node 3**.
- Identify new head:
  $$
  \text{new\_head} = \text{node}(3).\text{next} = \textbf{node 4}
  $$
- Sever link:
  $$
  \text{node}(3).\text{next} \leftarrow \emptyset
  $$

Resulting list:
$$
4 \longrightarrow 5 \longrightarrow 1 \longrightarrow 2 \longrightarrow 3 \longrightarrow \emptyset
$$

### Position Mapping Verification

A right rotation by $k' = 2$ sends every element from its old index $i$ to the index $(i + k') \bmod L$. The severed ring must reproduce exactly that permutation:

| Original index $i$ | Value | Destination index $(i + 2) \bmod 5$ | Position in the result | Value now at that position |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | 3rd from the left | 1 |
| 1 | 2 | 3 | 4th from the left | 2 |
| 2 | 3 | 4 | 5th from the left | 3 |
| 3 | 4 | 0 | 1st from the left | 4 |
| 4 | 5 | 1 | 2nd from the left | 5 |

Each destination index $0, 1, \dots, 4$ is claimed exactly once, so the mapping is a bijection: severing the ring neither duplicates nor drops a node, and the relative order inside each of the two blocks is preserved.

---

## 4. Complete Execution Trace

| Phase | Pointer Action | Node Visited / Affected | Pointer Next Target | List Structural State |
|:---:|:---|:---:|:---:|:---|
| Scan | Length counting | Nodes $1 \to 2 \to 3 \to 4 \to 5$ | - | $L = 5$, $\text{tail} = \text{Node}(5)$ |
| Cycle | Ring closure | $\text{Node}(5)$ | $\text{Node}(1)$ | $1 \to 2 \to 3 \to 4 \to 5 \to 1$ (Ring) |
| Offset | Compute step count | Formula $5 - 2 - 1 = 2$ | - | Need 2 steps from head |
| Step 1 | Forward advance | $\text{Node}(1) \to \text{Node}(2)$ | - | 1 step remaining |
| Step 2 | Forward advance | $\text{Node}(2) \to \text{Node}(3)$ | - | **New Tail = Node(3)** |
| Split | Extract new head | $\text{Node}(3).\text{next}$ | $\text{Node}(4)$ | **New Head = Node(4)** |
| Break | Terminate tail | $\text{Node}(3).\text{next}$ | $\emptyset$ | **Final: $[4, 5, 1, 2, 3]$** |

---

## 5. Algorithmic Correctness

**Soundness.** Rotating right by $k$ places means the last $k'$ elements move to the front of the list, and the remaining $L - k'$ elements follow them. Connecting tail to head preserves all relative orderings. Severing after the $(L - k')$-th element places the $(L - k' + 1)$-th element at the head, strictly satisfying the rotation definition.

**Completeness.** Finding length $L$ takes $L$ steps. Traversing to the new tail takes $L - k'$ steps. Total node traversals are at most $2L$, visiting every relevant node with no cycles left unsevered.

---

## 6. Traps This Instance Exposes

- **$k \ge L$ Overflow:** $k$ can be up to $2 \times 10^9$, much larger than list length $L \le 500$. Taking $k \pmod L$ handles arbitrary large rotations in $O(1)$.
- **$k \pmod L == 0$ No-Op:** If $k$ is an exact multiple of $L$, rotating leaves the list unchanged. Detecting $k' == 0$ avoids severing and reconnecting the list.
- **Off-by-One in Tail Selection:** The loop must advance $L - k' - 1$ times, not $L - k'$ times, because starting at `head` already accounts for step 1.

The same four phases absorb every degenerate input in the package's case set without a special-purpose branch beyond the two guards:

| Instance | Input | $L$ | $k' = k \bmod L$ | Expected output | Why the method is still correct |
|:---|:---|:---:|:---:|:---|:---|
| Main trace | `head = [1,2,3,4,5]`, `k = 2` | 5 | 2 | `[4,5,1,2,3]` | New tail is node 3; severing after it yields the two-block rotation. |
| Rotation exceeds length | `head = [0,1,2]`, `k = 4` | 3 | 1 | `[2,0,1]` | Four right rotations equal one, so the ring is walked one step past the old tail. |
| Whole multiples of $L$ | `head = [1,2,3]`, `k = 6` | 3 | 0 | `[1,2,3]` | $k' = 0$ exits before any pointer moves, so the list is untouched. |
| Single node | `head = [9]`, `k = 100` | 1 | 0 | `[9]` | $\text{head.next} == \emptyset$ returns immediately; a one-node ring is already closed. |
| Empty list | `head = []`, `k = 7` | 0 | undefined | `[]` | The empty guard fires before the length loop, so the modulo by $L$ is never evaluated. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. One pass of $N$ steps determines length, and a second partial pass of $N - k'$ steps finds the new tail ($N + N - k' \le 2N = O(N)$).
- **Auxiliary Space Complexity:** $O(1)$. Pointer manipulation reorders references in place without allocating new list nodes.