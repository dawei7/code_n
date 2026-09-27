# Guided Example: Closest Binary Search Tree Value II

We trace the step-by-step in-order sorted traversal streaming, sliding window deque maintenance of capacity $k$, and early termination cutoff on representative BST instances:

- **Input:** $\text{root} = [4, 2, 5, 1, 3], \quad \text{target} = 3.714286, \quad k = 2$
- **Required output:** $[3, 4]$ (or $[4, 3]$; the 2 closest values to target $3.714286$)
- **Single Node Base Case:** $\text{root} = [1], \quad \text{target} = 0.0, \quad k = 1 \implies [1]$
- **Complete Tree Selection:** $k = N \implies \text{returns all tree elements in sorted order}$
- **Early Termination:** Once an incoming node is farther from `target` than the oldest element in the deque ($q[0]$), strictly increasing monotonicity guarantees all future nodes will be farther still, enabling immediate pruning

This instance demonstrates combining binary search tree in-order monotonic ordering with sliding window optimization, explains why the $k$ closest values form a contiguous subsegment in the sorted array, details the $O(1)$ deque replacement step (`popleft` and `append`), and contrasts $O(N)$ traversal with $O(H + k)$ predecessor/successor iterator expansion.

---

## 1. Instance & Teaching Goal

Given the root of a binary search tree, a target value $\text{target} = 3.714286$, and $k = 2$:
```text
Tree structure:
        4
       / \
      2   5
     / \
    1   3
```
Find the $k = 2$ node values whose numerical distance $|\text{val} - \text{target}|$ is minimal.
Sorted in-order traversal: $[1, 2, 3, 4, 5]$.
Evaluating distances to $3.714286$:
- $|1 - 3.714286| = 2.714286$
- $|2 - 3.714286| = 1.714286$
- $|3 - 3.714286| = \mathbf{0.714286}$ (Selected)
- $|4 - 3.714286| = \mathbf{0.285714}$ (Selected)
- $|5 - 3.714286| = 1.285714$
The two closest values are $\mathbf{[3, 4]}$ (or $\mathbf{[4, 3]}$).

### The Contiguous Window Theorem
In any sorted list of numbers, the $k$ elements closest to a real target $T$ must form a **single contiguous subarray**.
Proof: If we select two elements $A < B$, any element $C$ strictly between them ($A < C < B$) cannot be farther from $T$ than both $A$ and $B$.
Therefore, as we stream elements in sorted in-order sequence from the BST, the optimal subset slides continuously across the stream.

---

## 2. Conceptual Foundation & Invariants

### In-Order Deque Sliding Protocol
Maintain a double-ended queue `q` with maximum capacity $k$:
Perform an in-order traversal (Left $\to$ Node $\to$ Right):
1. **Initial Fill ($\text{len}(q) < k$):**
   Append visited node:
   $$
   q.\text{append}(\text{node.val})
   $$
2. **Window Sliding ($\text{len}(q) == k$):**
   Compare incoming node with the oldest element currently retained ($q[0]$):
   - **Case A: Incoming element is closer:**
     $$
     |\text{node.val} - \text{target}| < |q[0] - \text{target}|
     $$
     The new element is superior to the oldest element in the window!
     Evict the left endpoint and append the new element:
     $$
     q.\text{popleft}(), \quad q.\text{append}(\text{node.val})
     $$
   - **Case B: Incoming element is equal or farther:**
     $$
     |\text{node.val} - \text{target}| \ge |q[0] - \text{target}|
     $$
     Since the in-order traversal produces strictly increasing values ($x > \text{node.val} > \text{target}$), every future node in the tree will have an even larger distance:
     $$
     |x - \text{target}| > |\text{node.val} - \text{target}| \ge |q[0] - \text{target}|
     $$
     No future node can ever replace $q[0]$! We **terminate the traversal early**.

> **Invariant.** Deque `q` always stores a sorted contiguous subsegment of the in-order traversal of length at most $k$. When traversal concludes, `q` holds the exact $k$ globally closest values.

---

## 3. Step-by-Step Worked Execution

We trace the in-order traversal on $\text{root} = [4, 2, 5, 1, 3]$ with $\text{target} = 3.714286$ and $k = 2$:
In-order sequence of nodes visited: $1 \to 2 \to 3 \to 4 \to 5$.
Initialize `q = deque()`.

---

### Step 1: Visit Node 1
- `len(q) == 0 < 2`.
- Append value: $q = [1]$.

---

### Step 2: Visit Node 2
- `len(q) == 1 < 2`.
- Append value: $q = [1, 2]$.
- Deque has reached target capacity $k = 2$.

---

### Step 3: Visit Node 3
- `len(q) == 2`. Window is full.
- Compare incoming $\text{val} = 3$ against oldest element $q[0] = 1$:
  $$
  d_{\text{new}} = |3 - 3.714286| = \mathbf{0.714286}
  $$
  $$
  d_{\text{old}} = |1 - 3.714286| = \mathbf{2.714286}
  $$
- Since $0.714286 < 2.714286$, the new element is closer!
- Slide window:
  $$
  q.\text{popleft}() \implies [2]
  $$
  $$
  q.\text{append}(3) \implies q = [2, 3]
  $$

---

### Step 4: Visit Node 4
- `len(q) == 2`. Window is full.
- Compare incoming $\text{val} = 4$ against oldest element $q[0] = 2$:
  $$
  d_{\text{new}} = |4 - 3.714286| = \mathbf{0.285714}
  $$
  $$
  d_{\text{old}} = |2 - 3.714286| = \mathbf{1.714286}
  $$
- Since $0.285714 < 1.714286$, the new element is closer!
- Slide window:
  $$
  q.\text{popleft}() \implies [3]
  $$
  $$
  q.\text{append}(4) \implies q = [3, 4]
  $$

---

### Step 5: Visit Node 5 (Early Cutoff Triggered!)
- `len(q) == 2`. Window is full.
- Compare incoming $\text{val} = 5$ against oldest element $q[0] = 3$:
  $$
  d_{\text{new}} = |5 - 3.714286| = \mathbf{1.285714}
  $$
  $$
  d_{\text{old}} = |3 - 3.714286| = \mathbf{0.714286}
  $$
- $1.285714 \ge 0.714286$ (**True!**).
- Incoming value is farther than $q[0]$.
- Since all subsequent values would be $> 5 > 3.714286$, distances will only continue to increase.
- **Terminate traversal immediately!**

Final window:
$$
\mathbf{[3, 4]}
$$

---

## 4. Complete Execution Trace

```text
In-order Sequence: 1, 2, 3, 4, 5 | Target: 3.714286, k = 2

Node 1: q = [1]
Node 2: q = [1, 2] (Full)
Node 3: |3 - 3.714| = 0.714 < |1 - 3.714| = 2.714 -> pop 1, push 3 -> q = [2, 3]
Node 4: |4 - 3.714| = 0.286 < |2 - 3.714| = 1.714 -> pop 2, push 4 -> q = [3, 4]
Node 5: |5 - 3.714| = 1.286 >= |3 - 3.714| = 0.714 -> Prune & Stop!

Result: [3, 4]
```

| In-Order Node | $q$ State Before Step | Distance Comparison ($d_{\text{new}}$ vs $d_{q[0]}$) | Closer? | Window Action | $q$ State After Step |
|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `[]` | - | - | Append | `[1]` |
| 2 | `[1]` | - | - | Append (Capacity 2 reached) | `[1, 2]` |
| **3** | `[1, 2]` | $\lvert 3 - 3.714 \rvert = 0.714 < \lvert 1 - 3.714 \rvert = 2.714$ | **Yes** | Evict 1, append 3 | `[2, 3]` |
| **4** | `[2, 3]` | $\lvert 4 - 3.714 \rvert = 0.286 < \lvert 2 - 3.714 \rvert = 1.714$ | **Yes** | Evict 2, append 4 | `[3, 4]` |
| **5** | `[3, 4]` | $\lvert 5 - 3.714 \rvert = 1.286 \ge \lvert 3 - 3.714 \rvert = 0.714$ | **No** | **Early Termination** | **`[3, 4]` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** At any point where $d_{\text{new}} \ge d_{q[0]}$ for $node.val > target$, any subsequent value $x > node.val$ has $x - target > node.val - target \ge |q[0] - target|$. Hence, no future value can be closer to $target$ than $q[0]$. Stopping early cannot discard any better element.

**Completeness.** Before the cutoff triggers, every newly visited node is compared against the farthest element currently in $q$. If it is closer, $q$ is updated; if not, monotonicity guarantees that all subsequent elements are worse. Thus, the final contents of $q$ are guaranteed to be the $k$ closest elements.

---

## 6. Traps This Instance Exposes

- **Full In-Order Array Allocation:** Collecting all $N$ elements into an array and using binary search requires $O(N)$ memory. Streaming into a size-$k$ deque requires only $O(k)$ memory plus recursion stack.
- **Missing the Early Termination:** Continuing in-order traversal after finding that the distance has increased wastes time exploring the rest of the tree. Checking `d_new >= d_old` allows immediate pruning.
- **Heap Overhead:** Maintaining a max-heap of size $k$ during traversal takes $O(N \log k)$ time and ignores the sorted nature of in-order traversal. The deque approach operates in $O(1)$ amortized time per node.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ in the worst case (e.g. when `target` is greater than all nodes in the tree), but often substantially faster $O(H + k)$ in practice due to early termination after passing the target. Each visited node requires $O(1)$ deque operations.
- **Auxiliary Space Complexity:** $O(H + k)$, where $H$ is the tree height (recursion call stack) and $k$ is the deque size storing the closest values.
