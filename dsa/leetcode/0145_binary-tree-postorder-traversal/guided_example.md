# Guided Example: Binary Tree Postorder Traversal

We trace the step-by-step Left-Right-Root postorder tree traversal using both iterative stack reversal duality and single-stack state tracking on representative binary tree instances:

- **Input:** $\text{root} = [1, \text{null}, 2, 3]$
- **Required output:** $[3, 2, 1]$
- **Full Hierarchy Instance:** $\text{root} = [1, 2, 3, 4, 5] \implies [4, 5, 2, 3, 1]$

This instance demonstrates the Left $\to$ Right $\to$ Root visiting invariant, establishes the mathematical duality between Modified Preorder (Root $\to$ Right $\to$ Left) and Postorder via sequence inversion, compares two-stack and single-stack `prev`-pointer tracking, and guarantees linear $O(N)$ runtime.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
1 \\
\quad \searrow \\
\qquad 2 \\
\qquad \swarrow \\
\quad 3
\end{gathered}
$$
Return the **postorder traversal** of its nodes' values.

In a postorder traversal, every subtree is visited in the strict recursive order:
$$
\mathbf{\text{Left Subtree}} \longrightarrow \mathbf{\text{Right Subtree}} \longrightarrow \mathbf{\text{Root}}
$$
For $\text{root} = [1, \text{null}, 2, 3]$:
1. Left child of 1 is null.
2. Evaluate right subtree rooted at 2:
   - Left child of 2 is 3 (leaf $\implies$ visits $3$).
   - Right child of 2 is null.
   - Visit root $2$.
   - Right subtree yields $[3, 2]$.
3. Finally visit root $1$.
Emitted order: $[3, 2, 1]$.

Iterative postorder is notoriously tricky because a parent node must be retained on the stack until *both* of its child subtrees have finished executing.
The **Preorder-Postorder Duality**:
- Standard Preorder: $\text{Root} \to \text{Left} \to \text{Right}$.
- Modified Preorder: $\text{Root} \to \text{Right} \to \text{Left}$.
- Reversing the Modified Preorder sequence yields:
  $$
  \text{Reverse}(\text{Root} \to \text{Right} \to \text{Left}) = \mathbf{\text{Left} \to \text{Right} \to \text{Root}}
  $$
This algebraic equivalence allows an iterative preorder engine to produce postorder simply by pushing children in $(\text{Left}, \text{Right})$ order and reversing the final result array.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Iterative Duality (Modified Preorder + Reverse)
Initialize `stack = [root]` and `traversal = []`.
If `root` is null: return `[]`.

While `stack` is non-empty:
1. Pop node $\text{curr} = \text{stack.pop()}$.
2. Append to sequence: $\text{traversal.append}(\text{curr.val})$.
3. **Push Left Child First:**
   If $\text{curr.left}$ exists:
   $$
   \text{stack.append}(\text{curr.left})
   $$
4. **Push Right Child Second:**
   If $\text{curr.right}$ exists:
   $$
   \text{stack.append}(\text{curr.right})
   $$
   *(Right child sits on top of the stack and pops first, generating $\text{Root} \to \text{Right} \to \text{Left}$)*.

**Final Step:**
Return the inverted sequence:
$$
\text{result} = \text{traversal}[::-1]
$$

### Method 2: Single Stack with `last_visited` Pointer
Traverse down the left spine, pushing nodes to `stack`.
When `curr` is null:
- Look at `peek = stack[-1]`.
- If `peek.right` exists and `peek.right != last_visited`:
  - Move to right child: `curr = peek.right`.
- Else:
  - Both subtrees are finished! Pop `peek`, visit `peek.val`, set `last_visited = peek`.

> **Invariant.** Under the duality method, each parent is placed before its children in `traversal`, and the right child precedes the left child. Reversing this sequence places the parent after both children, with left before right.

---

## 3. Step-by-Step Worked Execution

We trace the duality stack method on $\text{root} = [1, \text{null}, 2, 3]$:

### Step 0: Initialization
- `stack = [Node(1)]`
- `traversal = []`

---

### Step 1: Pop Node 1
- Pop `curr = Node(1)`.
- Append value: `traversal = [1]`.
- Push children:
  - Left child is `None`.
  - Right child is `Node(2)` $\implies$ Push `Node(2)`.
- Stack: `[Node(2)]`.

---

### Step 2: Pop Node 2
- Pop `curr = Node(2)`.
- Append value: `traversal = [1, 2]`.
- Push children:
  - Left child is `Node(3)` $\implies$ Push `Node(3)`.
  - Right child is `None`.
- Stack: `[Node(3)]`.

---

### Step 3: Pop Node 3
- Pop `curr = Node(3)`.
- Append value: `traversal = [1, 2, 3]`.
- Push children:
  - Leaf node (no children).
- Stack: `[]` (empty).

---

### Step 4: Sequence Inversion
- Forward traversal (Root $\to$ Right $\to$ Left):
  $$
  \text{traversal} = [1, 2, 3]
  $$
- Invert sequence:
  $$
  \text{result} = \text{traversal}[::-1] = \mathbf{[3, 2, 1]}
  $$

Final Postorder output: $[3, 2, 1]$.

---

## 4. Complete Execution Trace

```text
Tree:        [1]
               \
               [2]
               /
             [3]

Modified Preorder (Root -> Right -> Left):
Pop 1 -> Append 1, Push 2
Pop 2 -> Append 2, Push 3
Pop 3 -> Append 3
Forward:   [1, 2, 3]

Reversed (Left -> Right -> Root):
Result:    [3, 2, 1]
```

| Iteration | Stack Before Pop | Popped Node `curr` | Forward Append | Children Pushed (Left, then Right) | Stack After Push |
|:---:|:---|:---:|:---:|:---|:---|
| 0 (Init) | - | - | - | - | `[Node(1)]` |
| 1 | `[Node(1)]` | $\text{Node}(1)$ | 1 | Left: $\emptyset$, Right: $\text{Node}(2)$ | `[Node(2)]` |
| 2 | `[Node(2)]` | $\text{Node}(2)$ | 2 | Left: $\text{Node}(3)$, Right: $\emptyset$ | `[Node(3)]` |
| 3 | `[Node(3)]` | $\text{Node}(3)$ | 3 | Left: $\emptyset$, Right: $\emptyset$ | `[]` |
| **Invert** | `[]` | - | - | **Reverse $[1, 2, 3]$** | **`[3, 2, 1]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $T$ be a binary tree with root $R$, left subtree $L$, and right subtree $R_T$.
The modified preorder produces sequence $R \circ \text{MPre}(R_T) \circ \text{MPre}(L)$.
Taking the reverse of this sequence:
$$
\left( R \circ \text{MPre}(R_T) \circ \text{MPre}(L) \right)^R = \text{MPre}(L)^R \circ \text{MPre}(R_T)^R \circ R
$$
By mathematical induction, $\text{MPre}(L)^R = \text{Post}(L)$ and $\text{MPre}(R_T)^R = \text{Post}(R_T)$.
Therefore, the inverted sequence is $\text{Post}(L) \circ \text{Post}(R_T) \circ R$, which is precisely the definition of postorder traversal.

**Completeness.** Every node in the tree is pushed and popped exactly once, ensuring all node values appear in the final inverted array.

---

## 6. Traps This Instance Exposes

- **Infinite Loops with Single Stack:** In a single-stack implementation, returning from the right child to the parent can accidentally re-enter the right child if the algorithm does not track `last_visited`. The condition `if peek.right and peek.right != last_visited:` prevents re-visitation.
- **Empty Tree:** An empty tree $\text{root} == \emptyset$ returns `[]` immediately.
- **Pushing Order in Duality:** To produce Root $\to$ Right $\to$ Left, the left child must be pushed *before* the right child so that the right child is on top of the stack and popped first.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes. The stack processes each node once in $O(1)$ time, and reversing the array of length $N$ takes $O(N)$ operations.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the tree ($O(\log N)$ balanced, $O(N)$ skewed), to store nodes on the stack.