# Guided Example: Merge Two Sorted Lists

We trace the step-by-step execution of the optimal two-pointer linked list merge on a representative instance:

- **Input:** $\text{list1} = [1, 2, 4]$, $\text{list2} = [1, 3, 4]$
- **Required output:** $[1, 1, 2, 3, 4, 4]$

This instance demonstrates sentinel head initialization, iterative minimum selection between two sorted heads, pointer splicing in place without allocating new list nodes, and suffix attachment when one list is exhausted.

---

## 1. Instance & Teaching Goal

Given the heads of two sorted linked lists $\text{list1}$ and $\text{list2}$, we must merge them into a single sorted list by splicing together the existing nodes:

```text
list1:  [1] -> [2] -> [4] -> None
list2:  [1] -> [3] -> [4] -> None
```

The merged output must preserve non-decreasing order:
$$
[1] \to [1] \to [2] \to [3] \to [4] \to [4] \to \text{None}
$$

A naive approach extracts all values into an array, sorts the array, and constructs entirely new list nodes, consuming $O(N_1 + N_2)$ auxiliary space. The optimal algorithm splices existing nodes in place using a sentinel $\text{dummy}$ node and a tail pointer, achieving $O(N_1 + N_2)$ time with strictly $O(1)$ auxiliary space.

The three ways to combine the lists differ mainly in what they allocate, and on the traced instance every one of them costs $N_1 + N_2 = 6$ node placements:

| Strategy | How the Result Is Built | Time | Auxiliary Space | Tradeoff |
|:---|:---|:---|:---|:---|
| Copy the values, sort, build new nodes | Collects all six values into an array, orders them, then allocates six fresh nodes | $O((N_1 + N_2)\log(N_1 + N_2))$ | $O(N_1 + N_2)$ for the array, plus six new nodes | Throws away the ordering that both inputs already guarantee and duplicates the entire list |
| Recursive merge | Chooses the smaller head, recurses on what remains, and links the result behind it | $O(N_1 + N_2)$ | $O(N_1 + N_2)$ frames when the inputs interleave | Elegant, but the frame depth grows with the merged length instead of staying constant |
| Sentinel plus tail pointer, splicing in place | Reuses the existing nodes, rewires their links, and attaches the leftover suffix with a single assignment | $O(N_1 + N_2)$ | $O(1)$: the sentinel and one tail reference | Chosen: no node is allocated and neither input list is copied |

---

## 2. Conceptual Foundation & Invariants

### Sentinel Node & Tail Pointer
We initialize a sentinel node $\text{dummy}$ and maintain a moving pointer $\text{tail}$ initially pointing to $\text{dummy}$:
$$
\text{tail} = \text{dummy}
$$
At each step, while both $\text{list1} \ne \text{None}$ and $\text{list2} \ne \text{None}$:
1. Compare $\text{list1.val}$ and $\text{list2.val}$.
2. If $\text{list1.val} \le \text{list2.val}$:
   - Attach $\text{tail.next} \leftarrow \text{list1}$.
   - Advance $\text{list1} \leftarrow \text{list1.next}$.
3. Else:
   - Attach $\text{tail.next} \leftarrow \text{list2}$.
   - Advance $\text{list2} \leftarrow \text{list2.next}$.
4. Advance $\text{tail} \leftarrow \text{tail.next}$.

### Suffix Attachment
When either list becomes $\text{None}$, the remaining nodes of the other list are already sorted and strictly greater than or equal to $\text{tail.val}$. We splice the remaining list directly in $O(1)$ time:
$$
\text{tail.next} \leftarrow (\text{list1} \text{ if } \text{list1} \ne \text{None} \text{ else } \text{list2})
$$

> **Invariant.** At every step, the chain from $\text{dummy}$ to $\text{tail}$ contains the smallest processed nodes from $\text{list1}$ and $\text{list2}$ in sorted order. All remaining nodes in both lists are $\ge \text{tail.val}$.

---

## 3. Step-by-Step Worked Execution

We merge $\text{list1} = [1, 2, 4]$ and $\text{list2} = [1, 3, 4]$:

### Step 0: Initialization
- Create $\text{dummy}$ node.
- $\text{tail} = \text{dummy}$.
- Active heads: $\text{list1} = \text{Node}(1)$, $\text{list2} = \text{Node}(1)$.

---

### Step 1: Compare $1$ vs $1$
- Values: $\text{list1.val} = 1$, $\text{list2.val} = 1$.
- Condition: $\text{list1.val} \le \text{list2.val}$.
- Action: Attach $\text{tail.next} \leftarrow \text{list1}$ ($\text{Node}(1)$).
- Advance: $\text{list1} \to \text{Node}(2)$, $\text{tail} \to \text{Node}(1)$.
- Chain: $\text{dummy} \to 1$.

---

### Step 2: Compare $2$ vs $1$
- Values: $\text{list1.val} = 2$, $\text{list2.val} = 1$.
- Condition: $\text{list2.val} < \text{list1.val}$.
- Action: Attach $\text{tail.next} \leftarrow \text{list2}$ ($\text{Node}(1)$).
- Advance: $\text{list2} \to \text{Node}(3)$, $\text{tail} \to \text{Node}(1)$.
- Chain: $\text{dummy} \to 1 \to 1$.

---

### Step 3: Compare $2$ vs $3$
- Values: $\text{list1.val} = 2$, $\text{list2.val} = 3$.
- Condition: $\text{list1.val} < \text{list2.val}$.
- Action: Attach $\text{tail.next} \leftarrow \text{list1}$ ($\text{Node}(2)$).
- Advance: $\text{list1} \to \text{Node}(4)$, $\text{tail} \to \text{Node}(2)$.
- Chain: $\text{dummy} \to 1 \to 1 \to 2$.

---

### Step 4: Compare $4$ vs $3$
- Values: $\text{list1.val} = 4$, $\text{list2.val} = 3$.
- Condition: $\text{list2.val} < \text{list1.val}$.
- Action: Attach $\text{tail.next} \leftarrow \text{list2}$ ($\text{Node}(3)$).
- Advance: $\text{list2} \to \text{Node}(4)$, $\text{tail} \to \text{Node}(3)$.
- Chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3$.

---

### Step 5: Compare $4$ vs $4$
- Values: $\text{list1.val} = 4$, $\text{list2.val} = 4$.
- Condition: $\text{list1.val} \le \text{list2.val}$.
- Action: Attach $\text{tail.next} \leftarrow \text{list1}$ ($\text{Node}(4)$).
- Advance: $\text{list1} \to \text{None}$, $\text{tail} \to \text{Node}(4)$.
- Chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4$.

---

### Step 6: Attach Remaining Suffix
- $\text{list1}$ is now $\text{None}$.
- $\text{list2}$ points to remaining node $\text{Node}(4) \to \text{None}$.
- Splicing action: $\text{tail.next} \leftarrow \text{list2}$.
- Final chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4 \to 4 \to \text{None}$.
- Return $\text{dummy.next} = \text{Node}(1)$.

---

## 4. Complete Execution Trace

| Step | $\text{list1}$ Head Value | $\text{list2}$ Head Value | Minimum Chosen | Spliced Node | Updated Merged Chain | Remaining Unmerged |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 (Init) | 1 | 1 | - | - | $\text{dummy}$ | $\text{list1}: [1,2,4], \text{list2}: [1,3,4]$ |
| 1 | 1 | 1 | $\text{list1}$ ($1$) | $\text{Node}(1)$ from $\text{list1}$ | $\text{dummy} \to 1$ | $\text{list1}: [2,4], \text{list2}: [1,3,4]$ |
| 2 | 2 | 1 | $\text{list2}$ ($1$) | $\text{Node}(1)$ from $\text{list2}$ | $\text{dummy} \to 1 \to 1$ | $\text{list1}: [2,4], \text{list2}: [3,4]$ |
| 3 | 2 | 3 | $\text{list1}$ ($2$) | $\text{Node}(2)$ from $\text{list1}$ | $\text{dummy} \to 1 \to 1 \to 2$ | $\text{list1}: [4], \text{list2}: [3,4]$ |
| 4 | 4 | 3 | $\text{list2}$ ($3$) | $\text{Node}(3)$ from $\text{list2}$ | $\text{dummy} \to 1 \to 1 \to 2 \to 3$ | $\text{list1}: [4], \text{list2}: [4]$ |
| 5 | 4 | 4 | $\text{list1}$ ($4$) | $\text{Node}(4)$ from $\text{list1}$ | $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4$ | $\text{list1}: \text{None}, \text{list2}: [4]$ |
| 6 (Suffix) | $\text{None}$ | 4 | Suffix ($\text{list2}$) | $\text{Node}(4)$ from $\text{list2}$ | $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4 \to 4$ | Both lists empty |

---

## 5. Algorithmic Correctness

**Soundness.** At every step, the algorithm chooses $\min(\text{list1.val}, \text{list2.val})$. Because both input lists are sorted in non-decreasing order, this chosen value is $\le$ all remaining elements in both lists. Thus, every appended node satisfies $\text{tail.val} \le \text{node.val}$, ensuring the merged list is strictly sorted.

**Completeness.** Each iteration consumes exactly one node from either $\text{list1}$ or $\text{list2}$. When one list is exhausted, the non-empty suffix is attached in $O(1)$ time without examining individual nodes, because its internal links are already sorted. All $N_1 + N_2$ nodes are preserved.

---

## 6. Traps This Instance Exposes

- **Empty Input Lists:** If either $\text{list1}$ or $\text{list2}$ is empty at the start, the loop condition $\text{list1} \land \text{list2}$ is false immediately. Suffix attachment sets $\text{tail.next}$ to the non-empty list (or $\text{None}$ if both are empty), correctly returning the non-empty list without special-case branches.
- **Equal Values Handling:** When $\text{list1.val} == \text{list2.val}$, choosing $\text{list1}$ arbitrarily maintains stability and avoids unnecessary pointer juggling.
- **Loop Termination on Exhaustion:** Advancing in a while loop checking `while list1 and list2:` avoids null pointer dereferences. Once one list becomes $\text{None}$, attaching the remaining list with a single assignment avoids traversing the remaining suffix.

The empty-input and exhaustion shapes are where an incorrectly branched merge breaks, so each is tabulated with the iteration count that produces it:

| Instance | Combined Length $N_1 + N_2$ | Loop Iterations | Suffix Attached | Output | Why the Single Suffix Assignment Is Enough |
|:---|:---:|:---:|:---|:---|:---|
| $\text{list1} = []$, $\text{list2} = []$ | 0 | 0 | $\text{None}$ | `[]` | Both heads are $\text{None}$, so the loop condition fails on entry and the suffix assignment writes $\text{None}$ |
| $\text{list1} = []$, $\text{list2} = [0]$ | 1 | 0 | the whole of $\text{list2}$ | `[0]` | An empty first list leaves the entire other list as the leftover suffix |
| $\text{list1} = [-1, 0]$, $\text{list2} = []$ | 2 | 0 | the whole of $\text{list1}$ | `[-1, 0]` | The mirror image of the previous row; no comparison ever runs |
| $\text{list1} = [-3, -1, 0]$, $\text{list2} = [2, 5]$ | 5 | 3 | `[2, 5]` | `[-3, -1, 0, 2, 5]` | Every first-list value precedes every second-list value, so all three nodes of $\text{list1}$ are taken first and the untouched remainder is attached in one link change |
| $\text{list1} = [4, 8]$, $\text{list2} = [-5, -2, 0]$ | 5 | 3 | `[4, 8]` | `[-5, -2, 0, 4, 8]` | The roles reverse: all three comparisons select $\text{list2}$, exhausting it while $\text{list1}$ stays intact |
| $\text{list1} = [1, 3, 5, 7]$, $\text{list2} = [2, 4, 6, 8]$ | 8 | 7 | `[8]` | `[1, 2, 3, 4, 5, 6, 7, 8]` | Perfect alternation consumes seven nodes and stops the moment $\text{list1}$ empties, leaving exactly one node unattached |
| $\text{list1} = [-100, 0, 100]$, $\text{list2} = [-100, 0, 100]$ | 6 | 5 | `[100]` | `[-100, -100, 0, 0, 100, 100]` | Ties are resolved toward $\text{list1}$, so the second list keeps its last node and hands it over as the suffix |
| $\text{list1} = [0, 2, \dots, 48]$, $\text{list2} = [1, 3, \dots, 49]$ | 50 | 49 | `[49]` | `[0, 1, \dots, 49]` | Strict alternation ends when the even-valued list empties, and the single surviving odd value is linked rather than examined |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N_1 + N_2)$, where $N_1$ and $N_2$ are the lengths of $\text{list1}$ and $\text{list2}$. Each loop iteration performs $O(1)$ comparisons and pointer rewires, running at most $N_1 + N_2$ times. Suffix attachment takes $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Splicing modifies existing node pointers in place. Only two pointer references ($\text{dummy}$ and $\text{tail}$) are allocated.