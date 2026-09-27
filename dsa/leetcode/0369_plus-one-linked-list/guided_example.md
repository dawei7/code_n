# Guided Example: Plus One Linked List

We trace the step-by-step dummy sentinel anchoring (`dummy = ListNode(0, head)`), rightmost non-9 digit location tracking (`target`), single-pass in-place incrementation (`target.val += 1`), and cascading zero propagation (`target.next ... val = 0`) on representative singly linked lists:

- **Input:** `head = [1, 2, 3]`
- **Required output:** `[1, 2, 4]`
  - Sentinel attachment: `dummy(0) -> 1 -> 2 -> 3 -> None`
  - Linear scan for last non-9 digit:
    - Node 1: `val = 1 != 9 \implies target = 1`
    - Node 2: `val = 2 != 9 \implies target = 2`
    - Node 3: `val = 3 != 9 \implies target = 3`
  - Rightmost non-9 node is Node 3:
    - Increment: `target.val += 1 \implies 3 + 1 = 4`
    - Trailing 9s to zero: None
  - Sentinel value remains 0 $\implies$ return `dummy.next`: `[1, 2, 4]`
- **Trailing 9s Rollover:** `head = [1, 2, 9] \implies [1, 3, 0]`
  - Last non-9 is 2 $\implies$ increments to 3; trailing 9 resets to 0
- **All 9s Full Cascading Carry:** `head = [9, 9, 9] \implies [1, 0, 0, 0]`
  - No node in the original list is $< 9$
  - `target` remains anchored at `dummy(0)`
  - Sentinel increments from 0 to 1; all three 9s reset to 0
  - Output expands length by 1 digit: `[1, 0, 0, 0]`

This instance demonstrates in-place linked list arithmetic without reversal, mathematically proves why tracking the rightmost digit strictly less than 9 isolates the entire ripple carry in a single forward pass, and guarantees $O(N)$ linear time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a non-negative integer represented as a singly linked list of digits:
$$
\text{head} = 1 \to 2 \to 3 \quad (\text{representing the integer } 123)
$$
Add one to the integer and return the head of the updated linked list.
The most significant digit is at the head of the list.

```text
Initial List:     1 -> 2 -> 3
Increment (+1):             + 1
Resulting List:   1 -> 2 -> 4

All-Nines Cascade Example:
Initial List:     dummy(0) -> 9 -> 9 -> 9
Increment (+1):     +1       (all trailing 9s flip to 0)
Resulting List:     1    -> 0 -> 0 -> 0 (Returns dummy!)
```

### Eliminating List Reversal and Recursion
- Traditional big-integer addition works from right to left (least significant digit first). Doing this on singly linked lists typically requires either:
  1. Reversing the list, adding one, and reversing it back ($3$ traversals).
  2. Recursive DFS to reach the tail and propagate the carry backward ($O(N)$ stack memory).
- **The Ripple Carry Invariant:**
  When adding $1$ to an integer, carry propagation cascades through trailing $9$s and **stops immediately at the rightmost digit that is strictly less than $9$**!
  - Every digit strictly to the right of this position is a $9$ and must flip to $0$.
  - The rightmost non-9 digit itself increases by $1$ (yielding $\le 9$, generating no further carry).
  - Digits to the left of this position remain completely untouched!
- By tracking this rightmost non-9 node in a single forward pass, we can update the list in-place in $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### 1. Sentinel Dummy Anchor
Prepend `dummy = ListNode(0, head)`.
If every digit in the original list is $9$ (e.g. $999 \to 1000$), the rightmost non-9 digit is the sentinel itself (`dummy.val = 0`).

### 2. Pointer Walk Protocol:
1. Initialize `target = dummy`.
2. Traverse `head` until `None`:
   $$
   \text{if } head.val \ne 9: \quad target \leftarrow head
   $$
   Advance `head = head.next`.
3. Increment anchor:
   $$
   target.val \leftarrow target.val + 1
   $$
4. Reset trailing segment:
   Advance `target = target.next`.
   While `target` is not `None`:
   $$
   target.val \leftarrow 0
   $$
   $$
   target \leftarrow target.next
   $$
5. Return result:
   - If `dummy.val == 1`: return `dummy` (Digit count increased).
   - Else: return `dummy.next` (Original head).

> **Invariant.** `target` always references the rightmost node whose value is strictly less than 9. All nodes following `target` contain value 9.

---

## 3. Step-by-Step Worked Execution

We trace `head = [1, 2, 3]`:
Initial list: `dummy(0) -> 1 -> 2 -> 3 -> None`.
`target = dummy`.

---

### Step 1: Forward Scan to Locate Rightmost Non-9 Node
- **Visit Node 1 ($val = 1$):**
  - $1 \ne 9 \implies target \leftarrow \text{Node 1}$.
  - Advance to Node 2.
- **Visit Node 2 ($val = 2$):**
  - $2 \ne 9 \implies target \leftarrow \text{Node 2}$.
  - Advance to Node 3.
- **Visit Node 3 ($val = 3$):**
  - $3 \ne 9 \implies target \leftarrow \text{Node 3}$.
  - Advance to `None`.
- Scan terminates. Rightmost non-9 node is **Node 3**.

---

### Step 2: Increment the Target Node
- `target` points to Node 3.
- Increment value:
  $$
  target.val \leftarrow 3 + 1 = \mathbf{4}
  $$

---

### Step 3: Zero Out Trailing Nodes
- Advance: `target = target.next` $\implies \text{None}$.
- No trailing nodes exist. While loop terminates immediately.

---

### Step 4: Return List Entry Point
- Check sentinel: `dummy.val = 0`.
- No new leading digit was generated.
- Return `dummy.next`:
  $$
  \mathbf{1 \to 2 \to 4}
  $$

---

### Walkthrough: Cascading 9s Example (`head = [1, 2, 9]`)
1. `dummy(0) -> 1 -> 2 -> 9 -> None`.
2. Scan:
   - At Node 1: $1 \ne 9 \implies target = \text{Node 1}$.
   - At Node 2: $2 \ne 9 \implies target = \text{Node 2}$.
   - At Node 9: $9 == 9 \implies target$ remains at **Node 2**!
3. Increment: `target.val = 2 + 1 = 3`.
4. Zero out trailing nodes:
   - `target = target.next` (Node 9).
   - Set `target.val = 0`.
5. Return `dummy.next`: $\mathbf{1 \to 3 \to 0}$.

---

### Walkthrough: All 9s Cascade Example (`head = [9, 9, 9]`)
1. `dummy(0) -> 9 -> 9 -> 9 -> None`.
2. Scan:
   - Every node in `head` has value 9.
   - `target` never advances from `dummy`!
3. Increment: `dummy.val = 0 + 1 = 1`.
4. Zero out trailing nodes:
   - All three 9s become 0: `1 -> 0 -> 0 -> 0`.
5. Since `dummy.val == 1`, return `dummy`: $\mathbf{1 \to 0 \to 0 \to 0}$.

---

## 4. Complete Execution Trace

```text
head = [1, 2, 3]
Sentinel attached: dummy(0) -> 1 -> 2 -> 3

Scan:
  visit 1: val != 9 -> target = Node(1)
  visit 2: val != 9 -> target = Node(2)
  visit 3: val != 9 -> target = Node(3)

Increment: target(Node 3).val += 1 -> 4
Zeroing: target.next is None -> no trailing 9s

Result: dummy.next -> [1, 2, 4]
```

| Traversal Step | Node Visited | Node Value | Value $\ne 9$? | Updated `target` Reference | List State After Step |
|:---:|:---:|:---:|:---:|:---:|:---|
| Init | `dummy` | 0 | - | `dummy(0)` | `0 -> 1 -> 2 -> 3` |
| 1 | Node 1 | 1 | Yes ($1 \ne 9$) | Node 1 | `0 -> 1 -> 2 -> 3` |
| 2 | Node 2 | 2 | Yes ($2 \ne 9$) | Node 2 | `0 -> 1 -> 2 -> 3` |
| **3** | **Node 3** | **3** | **Yes ($3 \ne 9$)** | **Node 3** | `0 -> 1 -> 2 -> 3` |
| **Increment** | Target | 3 | - | - | **`0 -> 1 -> 2 -> 4`** |
| **Output** | Return `dummy.next` | - | - | - | **`[1, 2, 4]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Adding 1 to an integer affects only the suffix of consecutive 9s and the single digit directly preceding that suffix. Let the number be $P \cdot 10^k + (10^k - 1)$, where the suffix consists of $k$ nines and the last digit of $P$ is $d < 9$. Adding 1 yields $(P + 1) \cdot 10^k$, which increments digit $d$ by 1 and sets all $k$ following digits to 0. Since $d < 9$, $d + 1 \le 9$, generating zero further carry. The pointer manipulation precisely reflects this mathematical transformation.

**Completeness.** Every node is visited once during the forward scan. The `dummy` node prepended to the head ensures that even if all digits are 9, a valid non-9 node (`dummy` with value 0) exists to absorb the carry.

---

## 6. Traps This Instance Exposes

- **All-Nines Overflow:** When $head = [9]$, the output requires two nodes: $[1, 0]$. Without a sentinel dummy node, creating a new head requires awkward special-case branch logic.
- **Multiple Non-Adjacent Nines:** In $head = [1, 9, 2]$, the digit 9 is followed by a 2. Adding 1 gives $193$, NOT $200$. Only trailing 9s after the **last** non-9 node roll over to 0. Updating `target` on **every** non-9 node guarantees only genuine trailing 9s are cleared.
- **Node Mutation vs Allocation:** This algorithm operates entirely in-place by mutating `val`, requiring zero new node allocations (except the dummy node).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The algorithm makes one forward pass to find `target` ($N$ steps) and one partial forward pass from `target` to the end ($\le N$ steps), for total time strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, creating only a single sentinel node and two local pointer variables.
