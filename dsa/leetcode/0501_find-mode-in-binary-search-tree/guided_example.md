# Guided Example: Find Mode in Binary Search Tree

We trace the step-by-step BST in-order traversal property (sorted sequence generation), consecutive duplicate clustering ($root.val == prev$), current streak counter management ($cnt$), peak frequency tracking ($mx$), and dynamic mode list updating ($ans$) on representative binary search trees:

- **Input:** $root = [1, \text{null}, 2, 2]$
  - Tree structure:
    - Root: $1$
    - Right child: $2$
    - Left child of $2$: $2$
- **Required output:** `[2]`
  - Objective: Return the most frequently occurring value(s) in the BST.
- **BST In-order traversal execution trace:**
  - BST In-order traversal ($Left \to Node \to Right$) visits nodes in **non-decreasing numerical order**:
    $$
    \text{In-order sequence: } [1, \; 2, \; 2]
    $$
  - State tracking variables:
    - $prev = \text{None}$: previous visited value
    - $cnt = 0$: current contiguous streak length
    - $mx = 0$: maximum frequency observed so far
    - $ans = []$: list of current modes
  - **Node 1 ($val = 1$):**
    - $prev = \text{None} \implies cnt \leftarrow 1$
    - Since $cnt (1) > mx (0)$:
      - New maximum frequency found: $mx \leftarrow 1$
      - Reset mode list: $ans \leftarrow [1]$
    - Update previous: $prev \leftarrow 1$
  - **Node 2 ($val = 2$):**
    - $val (2) \ne prev (1) \implies$ streak resets: $cnt \leftarrow 1$
    - Since $cnt (1) == mx (1)$:
      - Tied for maximum frequency: append to mode list!
      - Mode list: $ans \leftarrow [1, 2]$
    - Update previous: $prev \leftarrow 2$
  - **Node 3 ($val = 2$):**
    - $val (2) == prev (2) \implies$ streak extends:
      $$
      cnt \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Compare with $mx = 1$:
      - Since $cnt (2) > mx (1)$:
      - Strictly new maximum frequency! All previous candidates are disqualified:
        $$
        mx \leftarrow 2, \quad ans \leftarrow [2]
        $$
    - Update previous: $prev \leftarrow 2$
  - In-order traversal finishes.
  - Final mode list: **`[2]`**.
- **Single Node Instance ($root = [0]$):** Visits $0$ with frequency $1 \implies \mathbf{[0]}$
- **Multiple Modes Tie ($root = [1, null, 2]$):** Values $[1, 2]$ each appear once $\implies \mathbf{[1, 2]}$
- **All Identical Nodes ($root = [3, 3, 3]$):** Value $3$ appears 3 times $\implies \mathbf{[3]}$

This instance demonstrates in-order traversal on binary search trees with duplicate keys, mathematically proves why contiguous grouping avoids $O(N)$ hash tables, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary search tree (BST) with duplicates:
Return all the **mode(s)** (i.e. the most frequently occurred elements) in the BST.
If the tree has multiple modes with the same maximum frequency, return them in any order.

```text
Tree:
      1
       \
        2
       /
      2

In-order Traversal (L -> Root -> R):
  1  ->  2  ->  2

Frequencies:
  Value 1: Count = 1
  Value 2: Count = 2  <- Mode!
Output: [2]
```

### The BST In-Order Traversal Invariant
- A binary search tree has the fundamental invariant:
  $$
  \text{Left.val} \le \text{Node.val} \le \text{Right.val}
  $$
- An **in-order traversal** ($Left \to Root \to Right$) visits every node in **monotonically non-decreasing order**.
- Consequently, all duplicate copies of any value appear **contiguously** in the traversal sequence!
- This reduces the problem of finding modes in a tree to finding the longest runs in a sorted array, without needing any hash map or external dictionary.

---

## 2. Conceptual Foundation & Invariants

### 1. Run-Length State Machine During Traversal:
As we visit each node during in-order traversal:
1. **Count Update:**
   $$
   cnt =
   \begin{cases}
   cnt + 1 & \text{if } root.val == prev \\
   1 & \text{if } root.val \ne prev
   \end{cases}
   $$
2. **Mode List Update:**
   - If $cnt > mx$:
     A new strictly higher frequency has been found!
     Reset the mode list to only include this value:
     $$
     mx \leftarrow cnt, \quad ans \leftarrow [root.val]
     $$
   - If $cnt == mx$:
     This value ties the current maximum frequency:
     $$
     ans.\text{append}(root.val)
     $$
3. **Advance Pointer:**
   $$
   prev \leftarrow root.val
   $$

> **Contiguity Invariant.** Because the in-order traversal is sorted, the complete count of any value is known the moment $val \ne prev$ occurs, guaranteeing that $cnt$ reflects its true global multiplicity.

---

## 3. Step-by-Step Worked Execution

We trace in-order traversal on $[1, \text{null}, 2, 2]$:

---

### Step 1: Initialization
- $prev = \text{None}$
- $cnt = 0, \; mx = 0, \; ans = []$

---

### Step 2: Visit First Node ($val = 1$)
- In-order reaches node $1$.
- $prev == \text{None} \implies cnt \leftarrow 1$.
- Check $cnt > mx \iff 1 > 0$:
  - $mx \leftarrow 1$
  - $ans \leftarrow [1]$
- Update $prev \leftarrow 1$.

---

### Step 3: Visit Second Node ($val = 2$)
- In-order moves to left child of 2 (first copy of value 2).
- $val (2) \ne prev (1) \implies$ streak resets:
  $$
  cnt \leftarrow 1
  $$
- Check $cnt == mx \iff 1 == 1$:
  - Ties maximum frequency $1$.
  - $ans.\text{append}(2) \implies ans = [1, 2]$.
- Update $prev \leftarrow 2$.

---

### Step 4: Visit Third Node ($val = 2$)
- In-order moves to parent node 2 (second copy of value 2).
- $val (2) == prev (2) \implies$ streak increments:
  $$
  cnt \leftarrow 1 + 1 = \mathbf{2}
  $$
- Check $cnt > mx \iff 2 > 1$:
  - Strictly new maximum frequency!
  - $mx \leftarrow 2$
  - $ans \leftarrow [2]$ (Discards $1$).
- Update $prev \leftarrow 2$.

---

### Step 5: Traversal Complete
Output mode list:
$$
\mathbf{[2]}
$$

---

## 4. Complete Execution Trace

| In-Order Sequence Step | Node Value | Previous Value $prev$ | Current Streak $cnt$ | Max Streak $mx$ | Mode List $ans$ | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Init** | — | `None` | $0$ | $0$ | `[]` | Initial state |
| **Node 1** | $1$ | `None` | $1$ | $1$ | `[1]` | $cnt > mx \implies$ New mode |
| **Node 2** | $2$ | $1$ | $1$ | $1$ | `[1, 2]` | $cnt == mx \implies$ Tied mode |
| **Node 3** | $2$ | $2$ | $2$ | $2$ | **`[2]`** | $cnt > mx \implies$ Overwrite mode |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($root = [0]$):** Visits $0$ with $cnt = 1 \implies \mathbf{[0]}$.
- **All Nodes Unique ($root = [1, null, 2, null, 3]$):** All nodes have frequency 1 $\implies$ returns all node values $\mathbf{[1, 2, 3]}$.
- **Multiple Modes Tied ($root = [1, 1, 2, 2]$):** Both 1 and 2 achieve frequency 2 $\implies \mathbf{[1, 2]}$.
- **Negative Node Values ($root = [-2, -2, -1]$):** $prev = \text{None}$ correctly avoids collision with any initial integer value.

---

## 6. Traps & Common Anti-Patterns

- **Building a Full Frequency Hash Map:** Collecting all node values in a hash map `collections.Counter` takes $O(N)$ extra heap memory. In-order traversal uses the BST property to achieve $O(1)$ auxiliary space (excluding recursion stack).
- **Two-Pass vs One-Pass Updating:** Some solutions make a first pass to find the maximum frequency and a second pass to collect modes. Updating $ans$ on the fly with `ans = [root.val]` on strictly greater frequencies achieves the same result in a single pass.
- **Initializing $prev = 0$:** If the BST contains nodes with value $0$, initializing $prev = 0$ falsely treats the first $0$ as a duplicate of a non-existent earlier node. Initializing $prev = \text{None}$ prevents this bug.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard in-order DFS visits each of the $N$ nodes exactly once.
  - Each node takes $O(1)$ operations to update $cnt$, $mx$, and $prev$.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ where $H$ is tree height for the recursion call stack ($O(\log N)$ average, $O(N)$ worst-case). Zero external hash table memory.