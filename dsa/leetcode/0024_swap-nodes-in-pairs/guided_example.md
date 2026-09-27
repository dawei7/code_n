# Guided Example: Swap Nodes in Pairs

We trace the step-by-step in-place pointer rewiring for pairwise linked list node swapping on a representative instance:

- **Input:** $\text{head} = [1, 2, 3, 4]$
- **Required output:** $[2, 1, 4, 3]$

This instance demonstrates sentinel node anchoring, isolating adjacent two-node pairs, executing a 3-link pointer permutation without allocating new nodes or altering node values, and advancing the anchor across consecutive pairs.

---

## 1. Instance & Teaching Goal

Given the head of a linked list with $N = 4$ nodes:
$$
[1] \to [2] \to [3] \to [4] \to \text{None}
$$

We must swap every two adjacent nodes in place without modifying the integer values inside the nodes (only node references may be altered):
$$
[2] \to [1] \to [4] \to [3] \to \text{None}
$$

A naive approach overwrites `node.val`, which violates interview and production constraints where node objects carry external identity or state. The optimal approach uses a sentinel $\text{dummy}$ node and rewires exactly three pointer references per pair in $O(N)$ time and $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### The 3-Link Rewiring Permutation
To swap adjacent nodes $A$ and $B$ that follow an anchor node $\text{prev}$:
```text
Initial state:
prev -> [A] -> [B] -> [next_pair]
```

We must transform the connections into:
```text
Final state:
prev -> [B] -> [A] -> [next_pair]
```

This requires three sequential pointer reassignments:
1. $\text{prev.next} \leftarrow B$ (link anchor to $B$)
2. $B.\text{next} \leftarrow A$ (invert direction between $B$ and $A$)
3. $A.\text{next} \leftarrow \text{next\_pair}$ (connect $A$ to the unswapped remainder)

After rewiring, $A$ occupies the second position of the pair. We advance $\text{prev} \leftarrow A$ to anchor the subsequent pair.

> **Invariant.** Before processing each pair, all preceding pairs have been inverted into their final sorted positions, and $\text{prev}$ points to the tail of the last completed pair. If fewer than two nodes remain after $\text{prev}$, the algorithm terminates.

---

## 3. Step-by-Step Worked Execution

We process list $[1, 2, 3, 4]$:

### Initialization
- Prepend sentinel: $\text{dummy.next} \leftarrow \text{Node}(1)$.
- Anchor pointer: $\text{prev} = \text{dummy}$.
- State: $\text{dummy} \to 1 \to 2 \to 3 \to 4 \to \text{None}$.

---

### Pair 1: Nodes $1$ and $2$
- Identify pair nodes:
  - $A = \text{prev.next} = \text{Node}(1)$
  - $B = A.\text{next} = \text{Node}(2)$
  - Suffix node $\text{nxt} = B.\text{next} = \text{Node}(3)$
- Execute 3-link rewiring:
  1. $\text{prev.next} \leftarrow B$: $\text{dummy} \to \text{Node}(2)$
  2. $B.\text{next} \leftarrow A$: $\text{Node}(2) \to \text{Node}(1)$
  3. $A.\text{next} \leftarrow \text{nxt}$: $\text{Node}(1) \to \text{Node}(3)$
- Resulting chain: $\text{dummy} \to 2 \to 1 \to 3 \to 4$.
- Advance anchor: $\text{prev} \leftarrow A$ ($\text{Node}(1)$).

---

### Pair 2: Nodes $3$ and $4$
- Identify pair nodes:
  - $A = \text{prev.next} = \text{Node}(3)$
  - $B = A.\text{next} = \text{Node}(4)$
  - Suffix node $\text{nxt} = B.\text{next} = \text{None}$
- Execute 3-link rewiring:
  1. $\text{prev.next} \leftarrow B$: $\text{Node}(1) \to \text{Node}(4)$
  2. $B.\text{next} \leftarrow A$: $\text{Node}(4) \to \text{Node}(3)$
  3. $A.\text{next} \leftarrow \text{nxt}$: $\text{Node}(3) \to \text{None}$
- Resulting chain: $\text{dummy} \to 2 \to 1 \to 4 \to 3 \to \text{None}$.
- Advance anchor: $\text{prev} \leftarrow A$ ($\text{Node}(3)$).

---

### Termination
- Check remaining nodes: $\text{prev.next} = \text{None}$ (fewer than 2 nodes remain).
- The while loop `while prev.next and prev.next.next:` halts.
- Return $\text{dummy.next} = \text{Node}(2)$.

---

## 4. Complete Execution Trace

| Step | Anchor $\text{prev}$ Node | First Node $A$ | Second Node $B$ | Remainder $\text{nxt}$ | Swapped Subsegment | Full Chain State After Rewiring |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 (Init) | $\text{dummy}$ | - | - | - | - | $\text{dummy} \to 1 \to 2 \to 3 \to 4 \to \text{None}$ |
| 1 | $\text{dummy}$ | $\text{Node}(1)$ | $\text{Node}(2)$ | $\text{Node}(3)$ | $[2 \to 1]$ | $\text{dummy} \to 2 \to 1 \to 3 \to 4 \to \text{None}$ |
| 2 | $\text{Node}(1)$ | $\text{Node}(3)$ | $\text{Node}(4)$ | $\text{None}$ | $[4 \to 3]$ | $\text{dummy} \to 2 \to 1 \to 4 \to 3 \to \text{None}$ |
| Final | $\text{Node}(3)$ | $\text{None}$ | - | - | - | Emitted Head: $\text{dummy.next} = \text{Node}(2)$ |

---

## 5. Algorithmic Correctness

**Soundness.** Swapping modifies only the forward `.next` pointers among existing node instances. Since the link $A.\text{next} \leftarrow \text{nxt}$ connects the swapped pair to the remainder of the list before advancing $\text{prev}$, no nodes are orphaned or lost from the chain.

**Completeness.** Each iteration consumes exactly two nodes from the input list. The loop condition `while prev.next and prev.next.next:` runs as long as an intact pair exists. If the list length is odd, the trailing singleton node remains unswapped as required by the problem specification.

---

## 6. Traps This Instance Exposes

- **Modifying Node Values:** Swapping `node.val` rather than pointer references violates problem rules requiring structural node manipulation.
- **Lost References During Rewire:** If $B.\text{next}$ is updated to $A$ before storing $B.\text{next}$ into $\text{nxt}$, the remaining list $[3 \to 4]$ becomes unreferenced and permanently lost.
- **Odd Length List Handling:** For a 3-node list $[1, 2, 3]$, after swapping $1$ and $2$, $\text{prev}$ is at $1$. Then $\text{prev.next} = \text{Node}(3)$, but $\text{prev.next.next} = \text{None}$. The condition fails cleanly, leaving node $3$ untouched and producing $[2, 1, 3]$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. The pointer moves through the list in steps of $2$, visiting each node once.
- **Auxiliary Space Complexity:** $O(1)$. Swapping modifies existing pointers strictly in place, requiring only fixed scalar pointer handles ($\text{dummy}$, $\text{prev}$, $A$, $B$).