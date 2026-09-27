# Guided Example: Closest Binary Search Tree Value

We trace the step-by-step binary search tree (BST) descent, absolute difference minimization, tie-breaking policy, and branch elimination on representative BST instances:

- **Input:** $\text{root} = [4, 2, 5, 1, 3], \quad \text{target} = 3.714286$
- **Required output:** $4$ (Node values evaluated along the descent path: $4$ with distance $\approx 0.2857$, and $3$ with distance $\approx 0.7143$; $4$ is closest)
- **Single Node Instance:** $\text{root} = [1], \quad \text{target} = 4.428571 \implies 1$
- **Tie-Breaking Distance:** $\text{root} = [2, 1, 3], \quad \text{target} = 1.5$: $|1 - 1.5| = 0.5$ and $|2 - 1.5| = 0.5$; tie-breaker selects smaller value $1$
- **Exact Match:** $\text{root} = [4, 2, 5], \quad \text{target} = 5.0 \implies 5$ (Zero distance terminates early)

This instance demonstrates binary search tree navigation, proves why the opposite subtree cannot contain a closer element once the descent direction is chosen, shows how to handle floating-point distance comparisons with strict tie-breaking, and runs in optimal $O(H)$ time and $O(1)$ auxiliary space without in-order recursion.

---

## 1. Instance & Teaching Goal

Given the root of a binary search tree and a floating-point target:
$$
\text{root} = [4, 2, 5, 1, 3], \quad \text{target} = 3.714286
$$
```text
Tree topology:
        4
       / \
      2   5
     / \
    1   3
```
Find the node value closest to $\text{target}$. If two values are equidistant, return the **smaller** value.

### BST Subtree Pruning Principle
In a BST, every left descendant is $< \text{node.val}$, and every right descendant is $> \text{node.val}$.
At any node:
- If $\text{target} < \text{node.val}$:
  Every value in the right subtree is $> \text{node.val} > \text{target}$.
  The distance to any right descendant is:
  $$
  \text{val}_{\text{right}} - \text{target} > \text{node.val} - \text{target}
  $$
  Thus, no node in the right subtree can ever be closer to `target` than `node.val` itself!
  We safely **prune the entire right subtree** and descend into the left child.
- Conversely, if $\text{target} > \text{node.val}$, the left subtree is completely pruned, and we descend into the right child.
This single-path descent takes $O(H)$ time where $H \le N$ is the tree height.

---

## 2. Conceptual Foundation & Invariants

### Iterative Descent Protocol
Maintain `closest = root.val` and pointer `curr = root`:
1. **Distance Comparison & Tie-Breaking:**
   Compute absolute differences:
   $$
   d_{\text{curr}} = |\text{curr.val} - \text{target}|, \quad d_{\text{min}} = |\text{closest} - \text{target}|
   $$
   - If $d_{\text{curr}} < d_{\text{min}}$:
     $$
     \text{closest} \leftarrow \text{curr.val}
     $$
   - Else if $d_{\text{curr}} == d_{\text{min}}$:
     $$
     \text{closest} \leftarrow \min(\text{closest}, \; \text{curr.val})
     $$
2. **Branch Navigation:**
   - If $\text{target} < \text{curr.val}$:
     $$
     \text{curr} \leftarrow \text{curr.left}
     $$
   - Else if $\text{target} > \text{curr.val}$:
     $$
     \text{curr} \leftarrow \text{curr.right}
     $$
   - Else ($\text{target} == \text{curr.val}$):
     $$
     \text{return curr.val } \quad (\text{Exact match; distance 0})
     $$

> **Invariant.** The global closest value in the BST belongs either to the set of visited ancestors on the descent path or to the active subtree rooted at `curr`. Pruned subtrees cannot contain a strictly closer value.

---

## 3. Step-by-Step Worked Execution

We trace the descent on $\text{root} = [4, 2, 5, 1, 3]$ with $\text{target} = 3.714286$:
Initial state: $\text{closest} = 4, \quad \text{curr} = \text{Node}(4)$.

---

### Step 1: Visit Node 4 (Root)
- Current node: $\text{val} = 4$.
- Distance:
  $$
  |4 - 3.714286| = \mathbf{0.285714}
  $$
- Best distance so far: $0.285714 \implies \text{closest} = 4$.
- Direction decision:
  $$
  \text{target} < 4 \implies 3.714286 < 4 \quad (\mathbf{\text{Descend Left}})
  $$
  *(Right subtree containing $\{5\}$ is pruned; $5 - 3.714286 = 1.2857 > 0.2857$)*.
- Advance: $\text{curr} \leftarrow \text{curr.left} = \text{Node}(2)$.

---

### Step 2: Visit Node 2
- Current node: $\text{val} = 2$.
- Distance:
  $$
  |2 - 3.714286| = \mathbf{1.714286}
  $$
- Compare: $1.714286 < 0.285714$ is False. $\text{closest}$ remains $4$.
- Direction decision:
  $$
  \text{target} > 2 \implies 3.714286 > 2 \quad (\mathbf{\text{Descend Right}})
  $$
  *(Left subtree containing $\{1\}$ is pruned; $|1 - 3.714286| = 2.714286$)*.
- Advance: $\text{curr} \leftarrow \text{curr.right} = \text{Node}(3)$.

---

### Step 3: Visit Node 3
- Current node: $\text{val} = 3$.
- Distance:
  $$
  |3 - 3.714286| = \mathbf{0.714286}
  $$
- Compare: $0.714286 < 0.285714$ is False. $\text{closest}$ remains $4$.
- Direction decision:
  $$
  \text{target} > 3 \implies 3.714286 > 3 \quad (\mathbf{\text{Descend Right}})
  $$
- Advance: $\text{curr} \leftarrow \text{curr.right} = \text{None}$.

---

### Step 4: Termination
- `curr` is $\text{None}$.
- Descent complete.
- Global closest value is $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
root = [4, 2, 5, 1, 3], target = 3.714286

Visit 4: dist = |4 - 3.714286| = 0.285714 -> closest = 4
  target < 4 -> go LEFT

Visit 2: dist = |2 - 3.714286| = 1.714286 > 0.285714 -> closest remains 4
  target > 2 -> go RIGHT

Visit 3: dist = |3 - 3.714286| = 0.714286 > 0.285714 -> closest remains 4
  target > 3 -> go RIGHT -> reaches None

Final Result: 4
```

| Step | Current Node | Node Value | Distance to Target ($|\text{val} - 3.714286|$) | New Best? | Best Value ($\text{closest}$) | Next Direction |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | Root | 4 | $0.285714$ | **Yes** | **4** | Left ($3.714286 < 4$) |
| 2 | Left | 2 | $1.714286$ | No | 4 | Right ($3.714286 > 2$) |
| 3 | Right of 2 | 3 | $0.714286$ | No | 4 | Right ($3.714286 > 3$) |
| **End** | $\text{None}$ | - | - | - | **4** | **Terminates** |

---

## 5. Algorithmic Correctness

**Soundness.** Every visited node is tested against the running best distance. At each branching point, if $\text{target} < \text{node.val}$, any node $x$ in the right subtree has $x > \text{node.val} > \text{target}$, so $|x - \text{target}| = x - \text{target} > \text{node.val} - \text{target} = |\text{node.val} - \text{target}|$. Thus, the right subtree is provably incapable of yielding a closer value than $\text{node.val}$. Symmetrically, if $\text{target} > \text{node.val}$, the left subtree is provably worse. Pruning never discards a better candidate.

**Completeness.** Since the search strictly preserves all potential improvements until reaching a leaf, the final recorded minimum is globally optimal.

---

## 6. Traps This Instance Exposes

- **In-Order Traversal Overhead:** Flattening the entire BST via in-order traversal into an array takes $O(N)$ time and $O(N)$ space. The iterative BST descent eliminates half the tree at each step, operating in $O(H)$ time and $O(1)$ auxiliary space.
- **Tie-Breaking Requirement:** When two values have identical distance (e.g. tree with $\{1, 2\}$ and $\text{target} = 1.5$), $|1 - 1.5| = 0.5$ and $|2 - 1.5| = 0.5$. The problem requires returning the **smaller** value (`min(closest, curr.val)`). Overlooking the tie-breaker returns an incorrect value depending on visit order.
- **Floating-Point Precision:** Comparisons should be performed directly with floating-point absolute differences (`abs(node.val - target)`). Do not round or truncate target values before comparing.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H)$, where $H$ is the height of the binary search tree. Each iteration descends one level down the tree, performing $O(1)$ arithmetic operations. For a balanced BST, $H = O(\log N)$; in the worst case (skewed tree), $H = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space for iterative descent using pointer traversal without recursion or call stack allocation.