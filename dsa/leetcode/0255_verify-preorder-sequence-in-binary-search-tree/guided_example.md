# Guided Example: Verify Preorder Sequence in Binary Search Tree

We trace the step-by-step monotonic decreasing stack simulation, left-to-right subtree descent transitions, and lower-bound enforcement on representative BST preorder sequences:

- **Input:** $\text{preorder} = [5, 2, 1, 3, 6]$
- **Required output:** `true` (Corresponds to a valid BST with root 5, left subtree $\{2, 1, 3\}$, and right subtree $\{6\}$)
- **Invalid Ancestor Breach:** $\text{preorder} = [5, 2, 6, 1, 3] \implies \text{false}$ (Value 1 appears after 6, violating the lower bound $x > 5$ established by root 5)
- **Strictly Decreasing Spine:** $\text{preorder} = [5, 4, 3, 2, 1] \implies \text{true}$ (A linear left-skewed chain)
- **Strictly Increasing Spine:** $\text{preorder} = [1, 2, 3, 4, 5] \implies \text{true}$ (A linear right-skewed chain)

This instance demonstrates monotonic stack modeling of tree traversals, explains why climbing up ancestors updates the global minimum lower bound when entering right subtrees, shows how the array itself can be reused as the stack for $O(1)$ auxiliary space, and guarantees strictly $O(N)$ linear time.

---

## 1. Instance & Teaching Goal

Given an array of unique integers:
$$
\text{preorder} = [5, 2, 1, 3, 6]
$$
Determine whether this sequence represents the preorder traversal ($\text{Root} \to \text{Left} \to \text{Right}$) of a valid Binary Search Tree (BST).

```text
Constructed BST:
         5
        / \
       2   6
      / \
     1   3
Preorder sequence: [5, 2, 1, 3, 6] (Valid!)
```

### Preorder BST Invariants
1. When values **decrease** ($5 \to 2 \to 1$), we are continuing down left child branches: $\text{child} < \text{parent}$.
2. When a value **increases** (e.g. $1 \to 3$), we have reached the end of a left subtree and transitioned into a right subtree!
   - To find which ancestor's right subtree we are entering, we pop all ancestors smaller than $3$.
   - The last popped ancestor was $2$. This means $3$ is in the right subtree of $2$!
   - Because $3$ is in the right subtree of $2$, **every single subsequent node in the entire remaining traversal MUST be strictly greater than $2$**!
   - We record a new lower bound: $\text{lower\_bound} = 2$.
3. If any future value drops below the established $\text{lower\_bound}$, the sequence is mathematically impossible for a BST and must be rejected.

---

## 2. Conceptual Foundation & Invariants

### Monotonic Decreasing Stack Protocol
Initialize $\text{stack} = []$ and $\text{lower\_bound} = -\infty$:
For each value $x \in \text{preorder}$:
1. **Lower Bound Violation Check:**
   If $x < \text{lower\_bound}$:
   $$
   \text{return false}
   $$
2. **Right Subtree Transition (Unwinding the Left Spine):**
   While $\text{stack}$ is not empty and $\text{stack}[-1] < x$:
   $$
   \text{lower\_bound} \leftarrow \text{stack}.\text{pop}()
   $$
   *(The last popped node is the deepest ancestor whose right subtree now contains $x$. All future nodes must be greater than this ancestor)*.
3. **Push Current Node:**
   $$
   \text{stack}.\text{append}(x)
   $$
Return `true`.

### $O(1)$ Space In-Place Stack Optimization
Instead of allocating an external stack list, we can repurpose the `preorder` array itself. A write pointer $k = -1$ tracks the top of the stack within `preorder`:
- Popping corresponds to $k \leftarrow k - 1$.
- Pushing corresponds to $k \leftarrow k + 1; \, \text{preorder}[k] = x$.

> **Invariant.** At any step, $\text{stack}$ holds active left-descending ancestors in strictly decreasing order, and $\text{lower\_bound}$ strictly enforces the BST condition that no future node can belong to a closed left subtree.

---

## 3. Step-by-Step Worked Execution

We trace the execution on $\text{preorder} = [5, 2, 1, 3, 6]$:
Initial state: $\text{stack} = [], \quad \text{lower\_bound} = -\infty$.

---

### Step 1: Element $x = 5$
- Check bound: $5 < -\infty$ (False).
- Pop condition: $\text{stack}$ is empty.
- Push $5$: $\text{stack} = [5]$.
- State: $\text{stack} = [5], \quad \text{lower\_bound} = -\infty$.

---

### Step 2: Element $x = 2$
- Check bound: $2 < -\infty$ (False).
- Pop condition: $\text{stack}[-1] = 5 \not< 2$. No pop.
- Push $2$: $\text{stack} = [5, 2]$.
- State: $\text{stack} = [5, 2], \quad \text{lower\_bound} = -\infty$.

---

### Step 3: Element $x = 1$
- Check bound: $1 < -\infty$ (False).
- Pop condition: $\text{stack}[-1] = 2 \not< 1$. No pop.
- Push $1$: $\text{stack} = [5, 2, 1]$.
- State: $\text{stack} = [5, 2, 1], \quad \text{lower\_bound} = -\infty$.

---

### Step 4: Element $x = 3$
- Check bound: $3 < -\infty$ (False).
- Pop condition ($\text{stack}[-1] < 3$):
  - Pop $1$: $\text{lower\_bound} \leftarrow 1$. $\text{stack} = [5, 2]$.
  - Pop $2$: $\text{lower\_bound} \leftarrow 2$. $\text{stack} = [5]$.
  - $\text{stack}[-1] = 5 \not< 3$. Stop popping.
- Push $3$: $\text{stack} = [5, 3]$.
- State: $\text{stack} = [5, 3], \quad \text{lower\_bound} = \mathbf{2}$.

---

### Step 5: Element $x = 6$
- Check bound: $6 < \text{lower\_bound} = 2$ (False).
- Pop condition ($\text{stack}[-1] < 6$):
  - Pop $3$: $\text{lower\_bound} \leftarrow 3$. $\text{stack} = [5]$.
  - Pop $5$: $\text{lower\_bound} \leftarrow 5$. $\text{stack} = []$.
  - $\text{stack}$ empty. Stop popping.
- Push $6$: $\text{stack} = [6]$.
- State: $\text{stack} = [6], \quad \text{lower\_bound} = \mathbf{5}$.

---

### Step 6: Completion
All elements processed without violating bounds.
**Return `true`!**

---

## 4. Complete Execution Trace

```text
preorder = [5, 2, 1, 3, 6]

x = 5: stack = [5],              lower_bound = -inf
x = 2: stack = [5, 2],           lower_bound = -inf
x = 1: stack = [5, 2, 1],        lower_bound = -inf
x = 3: pop 1 (lb=1), pop 2 (lb=2) -> stack = [5, 3], lower_bound = 2
x = 6: pop 3 (lb=3), pop 5 (lb=5) -> stack = [6],    lower_bound = 5

Traversal valid -> Return True
```

| Step | Value $x$ | Bound Check ($x < \text{lower\_bound}$) | Popped Ancestors | Updated $\text{lower\_bound}$ | Stack State After Push | Action Interpretation |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| **1** | 5 | $5 < -\infty$ (OK) | None | $-\infty$ | `[5]` | Root placed |
| **2** | 2 | $2 < -\infty$ (OK) | None | $-\infty$ | `[5, 2]` | Left child of 5 |
| **3** | 1 | $1 < -\infty$ (OK) | None | $-\infty$ | `[5, 2, 1]` | Left child of 2 |
| **4** | 3 | $3 < -\infty$ (OK) | Pop 1, Pop 2 | **2** | `[5, 3]` | Right child of 2; bound raised to 2 |
| **5** | 6 | $6 < 2$ (OK) | Pop 3, Pop 5 | **5** | `[6]` | Right child of 5; bound raised to 5 |
| **End** | - | - | - | - | - | **`true`** |

### A Nine-Element Valid Sequence With Repeated Multi-Pops ($\text{preorder} = [10, 5, 1, 7, 6, 8, 40, 30, 50]$)

The primary instance pops more than one ancestor only once, at $x = 6$. This longer instance pops twice at three different steps and shows the bound rising monotonically while the stack keeps changing shape.

| Step | Value $x$ | Bound check $x < \text{lower\_bound}$ | Popped ancestors, each raising the bound | $\text{lower\_bound}$ after popping | Stack after pushing $x$ | Edge the value occupies |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| 1 | 10 | $10 < -\infty$ (OK) | none: the stack is empty | $-\infty$ | `[10]` | root of the tree |
| 2 | 5 | $5 < -\infty$ (OK) | none: $10 \not< 5$ | $-\infty$ | `[10, 5]` | left child of 10 |
| 3 | 1 | $1 < -\infty$ (OK) | none: $5 \not< 1$ | $-\infty$ | `[10, 5, 1]` | left child of 5 |
| 4 | 7 | $7 < -\infty$ (OK) | pop 1, then pop 5 | **5** | `[10, 7]` | right child of 5 |
| 5 | 6 | $6 < 5$ (OK) | none: $7 \not< 6$ | 5 | `[10, 7, 6]` | left child of 7 |
| 6 | 8 | $8 < 5$ (OK) | pop 6, then pop 7 | **7** | `[10, 8]` | right child of 7 |
| 7 | 40 | $40 < 7$ (OK) | pop 8, then pop 10 | **10** | `[40]` | right child of 10 |
| 8 | 30 | $30 < 10$ (OK) | none: $40 \not< 30$ | 10 | `[40, 30]` | left child of 40 |
| 9 | 50 | $50 < 10$ (OK) | pop 30, then pop 40 | **40** | `[50]` | right child of 40 |
| **End** | - | never violated across nine steps | - | $40$ | `[50]` | **`true`** |

The bound is monotone non-decreasing throughout: $-\infty \to 5 \to 7 \to 10 \to 40$, and it never has to be recomputed, only raised. Steps 5 and 8 are the mirror cases that keep the sequence valid: a value smaller than the stack top ($6 < 7$, and $30 < 40$) simply descends without popping and stays inside the current window, while a value larger than the top ($8 > 7$, and $50 > 40$) closes the subtrees it has outgrown and raises the bound to the last ancestor it closed. The reconstructed tree is root 10 with left child 5 (children 1 and 7, and 7 in turn has children 6 and 8) and right child 40 (children 30 and 50), whose preorder traversal is exactly the input.

### Contrast: Invalid Sequence Trace ($\text{preorder} = [5, 2, 6, 1, 3]$)
- $x = 5$: `stack = [5]`, `lb = -inf`
- $x = 2$: `stack = [5, 2]`, `lb = -inf`
- $x = 6$: pops 2 (`lb = 2`), pops 5 (`lb = 5`). `stack = [6]`, `lb = 5`.
- $x = 1$: Check bound:
  $$
  x < \text{lower\_bound} \iff 1 < 5 \quad (\mathbf{\text{Violation!}})
  $$
  Node 1 cannot appear in the right subtree of root 5!
- **Returns `false` immediately.**

---

## 5. Algorithmic Correctness

**Soundness.** Whenever a node is popped, the traversal has permanently completed that node's left subtree and transitioned to its right. In a BST, every descendant in a right subtree must be strictly greater than the root of that subtree. Any value smaller than `lower_bound` contradicts this property, proving the sequence cannot represent a valid BST.

**Completeness.** Preorder visits nodes in root-left-right order. When descending left, nodes enter the stack. When branching right, popping retrieves the exact parent node. If the sequence is a valid preorder traversal, every value satisfies the required ancestor bounds and will not trigger rejection.

---

## 6. Traps This Instance Exposes

- **Duplicate Values:** The problem guarantees unique integers. If duplicates were allowed, the strict inequality checks ($<$ vs $\le$) would require careful alignment depending on whether duplicates are placed in left or right subtrees.
- **Checking Only Immediate Parent:** Simply verifying that $x > \text{parent}$ when branching right is insufficient. For instance, in $[5, 2, 6, 1]$, $1 < 6$ is true, but $1 < 5$ violates the ancestor bound established by root 5. The stack correctly propagates the global ancestor constraint.
- **Constant Space Modification:** Using the input array `preorder` as the stack array achieves $O(1)$ space, but mutates the input. If input immutability is required, an explicit stack provides clean $O(N)$ auxiliary memory.

### Boundary instances and where the bound comes from

Each row is a separate input, and the third column names the exact moment the verdict is decided so that the origin of the decisive bound is explicit.

| Instance | Decisive moment | Result | Boundary it fixes |
|:---|:---|:---:|:---|
| `[1]` | neither rule can fire: the stack is empty and $\text{lower\_bound} = -\infty$ | `true` | a single node is always a valid BST preorder |
| `[10000, 1]` | $1 < -\infty$ passes, and $10000 \not< 1$ so nothing is popped | `true` | the global maximum as root with the global minimum as its left child is still legal |
| `[1, 2, 3, 4]` | every new value pops the whole stack, raising the bound to $1$, then $2$, then $3$ | `true` | a right spine is accepted even though the stack is emptied on every step |
| `[4, 3, 2, 1]` | no value is ever greater than the stack top, so no pop occurs and the bound stays $-\infty$ | `true` | a left spine is accepted with stack depth $4$ and no bound pressure at all |
| `[8, 5, 1, 7, 10, 12, 9]` | at $x = 9$ the bound is $10$, raised when $12$ closed the subtree rooted at $10$ | `false` | the violation can arrive at the very last element, long after its bound was established |
| `[10, 5, 1, 7, 40, 50, 30]` | at $x = 30$ the bound is $40$, set by an inner node rather than the root | `false` | an inner ancestor's bound rejects a value that the root's own bound would have allowed |
| `[5, 5]` | $5 < -\infty$ passes and $5 \not< 5$, so the second copy is pushed as a left descendant | `true` | both comparisons are strict, so equal neighbours survive; the contract promises unique values, so this input lies outside it |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `preorder`. Each element is pushed onto the stack exactly once and popped from the stack at most once. The total number of stack operations across the entire loop is at most $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ for the explicit stack (or strictly $O(1)$ auxiliary space using in-place two-pointer simulation over `preorder`).

### Cost of the alternatives

Push, pop and comparison counts below are exact for the two five-element instances, so the trade-offs are visible instead of merely asymptotic.

| Strategy | Mechanism | Work on the valid instance `[5, 2, 1, 3, 6]` | Work on the invalid instance `[5, 2, 6, 1, 3]` | Cost or failure mode |
|:---|:---|:---|:---|:---|
| Monotonic stack with a running lower bound (the method used) | push ancestors while descending, pop and raise the bound when a larger value arrives | 5 pushes, 4 pops, 5 bound checks, answer `true` | 3 pushes, 2 pops, and the fourth bound check rejects $x = 1$ | $O(N)$ time and $O(N)$ stack slots; no tree is ever built |
| In-place stack carved out of the input array | keep a write index and store the pushed ancestors inside `preorder` itself | identical push and pop counts with zero extra stack cells | identical decision, still rejecting at $x = 1$ | $O(1)$ auxiliary memory, but the caller's array is destroyed |
| Recursive verification with an allowed $(\text{low}, \text{high})$ window | consume the array in preorder with one shared index, tightening the window at each node | 5 node visits with a window check at each, recursion depth $3$ | rejected at the node holding $1$, whose window is $(5, \infty)$ | $O(N)$ time but $O(H)$ call frames, which is $O(N)$ on a spine |
| Rebuild the tree from preorder plus the sorted values | sort the values to obtain the inorder order, rebuild recursively, and reject any inconsistency | sorted order $[1, 2, 3, 5, 6]$ rebuilds successfully | after the root $5$ the next value $6$ cannot belong to the left region, so rebuilding stops | $O(N \log N)$ time and $O(N)$ memory for the sorted copy and the value-to-position map, all to construct a tree nobody needs |
| Naive recursive split that rescans every segment | at each node, scan the segment for the window and for the first larger element | element-to-window scans total $5 + 3 + 1 + 1 + 1 = 11$ comparisons | the same scan order reaches the contradiction at $x = 1$ | $\Theta(N^2)$ on a spine: a four-element spine already costs $4 + 3 + 2 + 1 = 10$ window comparisons where the stack needs only $4$ bound checks |

Only the first two rows keep the whole check linear with a single pass over the values; the remaining rows either allocate an order statistic that is not needed, or rescan segments that the stack already summarises in its decreasing order.
