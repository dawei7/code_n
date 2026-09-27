# Guided Example: Count Univalue Subtrees

We trace the step-by-step bottom-up post-order DFS propagation, univalue subtree validation, and short-circuit avoidance on representative binary trees:

- **Input:** $\text{root} = [5, 1, 5, 5, 5, \text{null}, 5]$
- **Required output:** $4$ (Four univalue subtrees: three leaf nodes with value $5$, and the right subtree rooted at $5$)
- **Uniform Tree Instance:** $\text{root} = [5, 5, 5, 5, 5, \text{null}, 5] \implies 6$ (Every single node roots a univalue subtree)
- **Single Node Instance:** $\text{root} = [1] \implies 1$ (A single leaf node is always univalue)
- **Empty Tree Instance:** $\text{root} = [] \implies 0$

This instance demonstrates post-order divide-and-conquer on binary trees, explains why bottom-up traversal ensures child subtrees are evaluated before their parent, formalizes the four necessary and sufficient conditions for univalue qualification, warns against short-circuit boolean evaluation traps, and runs in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given a binary tree:
```text
          5 (node 1)
         / \
   (node 2) 1   5 (node 3)
           / \   \
          5   5   5 (node 6)
   (node 4) (node 5)
```
Count the total number of **uni-value subtrees** (subtrees where every node in the subtree has the exact same value).

Let us inspect each subtree:
1. Subtree at leaf node 4 (value $5$): Only one node $\implies$ **Univalue!** (Count $= 1$)
2. Subtree at leaf node 5 (value $5$): Only one node $\implies$ **Univalue!** (Count $= 2$)
3. Subtree at leaf node 6 (value $5$): Only one node $\implies$ **Univalue!** (Count $= 3$)
4. Subtree at node 2 (value $1$, children $5, 5$): Contains values $\{1, 5\} \implies$ Not univalue.
5. Subtree at node 3 (value $5$, right child $5$): All nodes have value $5 \implies$ **Univalue!** (Count $= 4$)
6. Root node 1 (value $5$, left child $1$): Left child is not univalue $\implies$ Root is not univalue.

Total univalue subtrees: $\mathbf{4}$.

---

## 2. Conceptual Foundation & Invariants

### Univalue Subtree Theorem
A subtree rooted at `node` is a uni-value subtree **if and only if** all four conditions are satisfied:
1. Its left child subtree is uni-value (or `node.left` is `None`).
2. Its right child subtree is uni-value (or `node.right` is `None`).
3. If `node.left` exists, $\text{node.val} == \text{node.left.val}$.
4. If `node.right` exists, $\text{node.val} == \text{node.right.val}$.

### Post-Order Bottom-Up Traversal Contract `dfs(node)`
`dfs(node)` returns a boolean indicating whether the subtree rooted at `node` is uni-value:
1. **Base Case:**
   If $\text{node is None}$: return `True` (an empty subtree trivially satisfies uniformity and does not invalidate a parent).
2. **Recursive Child Evaluation (MANDATORY NON-SHORT-CIRCUIT):**
   Evaluate both subtrees completely:
   $$
   \text{is\_left} = \text{dfs}(\text{node.left})
   $$
   $$
   \text{is\_right} = \text{dfs}(\text{node.right})
   $$
   *(Warning: Never write `dfs(node.left) and dfs(node.right)` inline! If the left call returns `False`, short-circuit evaluation skips the right child, failing to count univalue subtrees in the right branch!)*
3. **Combine Conditions:**
   If $\text{is\_left}$ and $\text{is\_right}$:
   - Check value agreement:
     If $(\text{node.left is None or node.val == node.left.val})$ and $(\text{node.right is None or node.val == node.right.val})$:
     $$
     \text{count} \mathrel{+}= 1
     $$
     $$
     \text{return True}
     $$
4. Return `False`.

> **Invariant.** When `dfs(node)` completes, all univalue subtrees contained within the subtree rooted at `node` have been counted, and the boolean return value accurately reflects whether the entire subtree is univalue.

---

## 3. Step-by-Step Worked Execution

We trace the post-order traversal on $\text{root} = [5, 1, 5, 5, 5, \text{null}, 5]$:
Initial state: $\text{count} = 0$.

### Step 1: Leaf Node 4 ($\text{val} = 5$)
- Left child: `None` $\implies \text{is\_left} = \text{True}$.
- Right child: `None` $\implies \text{is\_right} = \text{True}$.
- Values: No children to mismatch.
- $\text{count} \leftarrow 0 + 1 = \mathbf{1}$.
- **Returns `True`.**

---

### Step 2: Leaf Node 5 ($\text{val} = 5$)
- Left child: `None` $\implies \text{is\_left} = \text{True}$.
- Right child: `None` $\implies \text{is\_right} = \text{True}$.
- Values: No children to mismatch.
- $\text{count} \leftarrow 1 + 1 = \mathbf{2}$.
- **Returns `True`.**

---

### Step 3: Node 2 ($\text{val} = 1$)
- Left child (Node 4): $\text{is\_left} = \text{True}$, value $= 5$.
- Right child (Node 5): $\text{is\_right} = \text{True}$, value $= 5$.
- Check parent-child values:
  $$
  \text{node.val} = 1 \ne \text{node.left.val} = 5
  $$
- Value mismatch! Subtree is **not univalue**.
- $\text{count}$ remains $2$.
- **Returns `False`.**

---

### Step 4: Leaf Node 6 ($\text{val} = 5$)
- Left child: `None` $\implies \text{is\_left} = \text{True}$.
- Right child: `None` $\implies \text{is\_right} = \text{True}$.
- $\text{count} \leftarrow 2 + 1 = \mathbf{3}$.
- **Returns `True`.**

---

### Step 5: Node 3 ($\text{val} = 5$)
- Left child: `None` $\implies \text{is\_left} = \text{True}$.
- Right child (Node 6): $\text{is\_right} = \text{True}$, value $= 5$.
- Value check: $\text{node.val} = 5 == \text{node.right.val} = 5$.
- All conditions satisfied!
- $\text{count} \leftarrow 3 + 1 = \mathbf{4}$.
- **Returns `True`.**

---

### Step 6: Root Node 1 ($\text{val} = 5$)
- Left child (Node 2): $\text{is\_left} = \mathbf{\text{False}}$.
- Right child (Node 3): $\text{is\_right} = \text{True}$.
- Because $\text{is\_left}$ is False, the root cannot be univalue.
- $\text{count}$ remains $4$.
- **Returns `False`.**

Traversal completes. Global count is $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
Post-order visit:
Node 4 (val 5): Leaf -> Univalue -> count = 1, return True
Node 5 (val 5): Leaf -> Univalue -> count = 2, return True
Node 2 (val 1): Left=5, Right=5, val=1 != 5 -> NOT Univalue -> count = 2, return False
Node 6 (val 5): Leaf -> Univalue -> count = 3, return True
Node 3 (val 5): Left=None, Right=5 (val 5 == 5) -> Univalue -> count = 4, return True
Node 1 (val 5): Left child returned False -> NOT Univalue -> count = 4, return False

Total Count: 4
```

| Traversal Order | Node Index | Node Value | Left Child Status | Right Child Status | Parent-Child Match? | Univalue Subtree? | Running Count |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 4 | 5 | `None` (`True`) | `None` (`True`) | Leaf | **Yes** | **1** |
| 2 | 5 | 5 | `None` (`True`) | `None` (`True`) | Leaf | **Yes** | **2** |
| 3 | 2 | 1 | Node 4 (`True`) | Node 5 (`True`) | $1 \ne 5$ (Mismatch) | **No** | 2 |
| 4 | 6 | 5 | `None` (`True`) | `None` (`True`) | Leaf | **Yes** | **3** |
| 5 | 3 | 5 | `None` (`True`) | Node 6 (`True`) | $5 == 5$ (Match) | **Yes** | **4** |
| 6 | 1 (Root) | 5 | Node 2 (`False`) | Node 3 (`True`) | Left is not univalue | **No** | **4 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** A tree of size 1 is univalue. For any tree of size $> 1$, all its nodes have value $V$ if and only if its left subtree consists entirely of $V$s, its right subtree consists entirely of $V$s, and the root value is $V$. The four conjunction checks verify this inductive definition.

**Completeness.** Post-order DFS visits every node in the binary tree exactly once. Because both recursive calls are guaranteed to execute before evaluating the parent, every candidate subtree in the tree is checked and counted.

---

## 6. Traps This Instance Exposes

- **Short-Circuit Evaluation Bug:** Writing `return dfs(node.left) and dfs(node.right) and ...` halts traversal of `node.right` if `node.left` returns `False`. Any univalue subtrees inside the right branch would be skipped and uncounted! Evaluating `is_left` and `is_right` on separate lines ensures complete traversal.
- **Top-Down $O(N^2)$ Recomputation:** Running a `is_univalue(node)` function from every node from the top down checks the same descendants repeatedly, degrading performance to $O(N^2)$. Bottom-up post-order DFS aggregates status in a single pass of $O(N)$ time.
- **Null Child Handling:** A null child must return `True` so it acts as a neutral element in the boolean conjunction without falsely failing leaf nodes.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited exactly once during the post-order depth-first search. At each node, constant-time operations ($O(1)$) perform equality checks and state aggregation.
- **Auxiliary Space Complexity:** $O(H)$ auxiliary call-stack memory, where $H$ is the height of the tree ($O(\log N)$ for balanced trees, $O(N)$ for skewed trees).