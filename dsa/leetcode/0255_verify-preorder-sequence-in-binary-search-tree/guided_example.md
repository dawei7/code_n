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

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `preorder`. Each element is pushed onto the stack exactly once and popped from the stack at most once. The total number of stack operations across the entire loop is at most $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ for the explicit stack (or strictly $O(1)$ auxiliary space using in-place two-pointer simulation over `preorder`).
