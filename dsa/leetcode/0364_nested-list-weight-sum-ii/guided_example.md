# Guided Example: Nested List Weight Sum II

We trace the step-by-step single-pass recursive traversal (`dfs`), simultaneous unweighted sum ($s$) and forward-weighted sum ($ws$) accumulation, maximum depth tracking ($D$), and algebraic inverse-weight reconstruction ($(D + 1)s - ws$) on representative nested list instances:

- **Input:** `nestedList = [[1, 1], 2, [1, 1]]`
- **Required output:** $8$
  - Maximum nesting depth across all elements: $D = 2$
  - Inverse weights calculation: $\text{weight}(d) = D - d + 1$
    - Element $2$ at depth 1: weight $2 - 1 + 1 = 2 \implies 2 \times 2 = 4$
    - Four elements of value $1$ at depth 2: weight $2 - 2 + 1 = 1 \implies 4 \times (1 \times 1) = 4$
    - Total inverse weighted sum: $4 + 4 = \mathbf{8}$
  - Single-pass algebraic decomposition:
    - Unweighted sum: $s = 1 + 1 + 2 + 1 + 1 = 6$
    - Forward-weighted sum: $ws = (1 \times 2) + (1 \times 2) + (2 \times 1) + (1 \times 2) + (1 \times 2) = 10$
    - Maximum depth: $D = 2$
    - Final result: $(D + 1) \cdot s - ws = (2 + 1) \times 6 - 10 = 18 - 10 = \mathbf{8}$
- **Deep Nesting Instance:** `nestedList = [1, [4, [6]]]`
  - Depth 1: $1$, Depth 2: $4$, Depth 3: $6 \implies D = 3$
  - $s = 1 + 4 + 6 = 11$, $ws = 1(1) + 4(2) + 6(3) = 27$
  - Result: $(3 + 1) \times 11 - 27 = 44 - 27 = 17$

This instance demonstrates algebraic optimization of non-local tree properties, mathematically proves how factoring $\sum v_i(D - d_i + 1) = (D + 1)\sum v_i - \sum v_i d_i$ eliminates the need for a separate pre-traversal depth discovery pass, and operates in $O(N)$ linear time and $O(D)$ recursion stack space.

---

## 1. Instance & Teaching Goal

Given a nested list of integers:
$$
\text{nestedList} = [[1, 1], \; 2, \; [1, 1]]
$$
The inverse depth weight of an integer at depth $d$ is:
$$
\text{weight}(d) = \text{maxDepth} - d + 1
$$
where $\text{maxDepth}$ is the maximum nesting depth of any integer in the structure.
Compute the sum of each integer multiplied by its inverse depth weight:

```text
Hierarchical Depths:
Level 1 (d = 1):  [ ... , 2 , ... ]  -> maxDepth - 1 + 1 = 2
Level 2 (d = 2):   [1, 1]   [1, 1]   -> maxDepth - 2 + 1 = 1

maxDepth = 2

Weighted Contributions:
  Value 2 at depth 1: 2 * 2 = 4
  Value 1 at depth 2: 1 * 1 = 1
  Value 1 at depth 2: 1 * 1 = 1
  Value 1 at depth 2: 1 * 1 = 1
  Value 1 at depth 2: 1 * 1 = 1

Total Sum: 4 + 1 + 1 + 1 + 1 = 8
```

### The Single-Pass Mathematical Identity
In a standard approach, one must traverse once to find $\text{maxDepth} = D$, and then traverse a second time to compute the weights.
However, by distributing the formula:
$$
\sum_{i=1}^M v_i (D - d_i + 1) = \sum_{i=1}^M \big( (D + 1) v_i - v_i d_i \big) = (D + 1) \sum_{i=1}^M v_i - \sum_{i=1}^M v_i d_i
$$
We define:
- $s = \sum v_i$ (the unweighted sum of all values)
- $ws = \sum v_i d_i$ (the forward depth-weighted sum)
Both $s$, $ws$, and $D$ can be accumulated **simultaneously in a single DFS pass**!
At the end, evaluate $(D + 1) \cdot s - ws$.

---

## 2. Conceptual Foundation & Invariants

### 1. State Variables:
- `maxDepth`: Maximum depth $d$ reached during traversal.
- `s`: Cumulative sum of integer values.
- `ws`: Cumulative sum of $(value \times d)$.

### 2. Recursive Protocol `dfs(x, d)`:
1. Update global depth:
   $$
   maxDepth \leftarrow \max(maxDepth, \; d)
   $$
2. **If `x.isInteger()` is True:**
   $$
   val = x.\text{getInteger}()
   $$
   $$
   s \leftarrow s + val, \quad ws \leftarrow ws + val \times d
   $$
3. **If `x.isInteger()` is False:**
   For each child $y \in x.\text{getList}()$:
   $$
   dfs(y, \; d + 1)
   $$

### 3. Final Calculation:
$$
\text{Result} = (maxDepth + 1) \times s - ws
$$

> **Invariant.** At all times, $s$ is the exact sum of visited integers, $ws$ is their forward depth product sum, and $maxDepth$ tracks the deepest level reached.

---

## 3. Step-by-Step Worked Execution

We trace `nestedList = [[1, 1], 2, [1, 1]]`:
Initialized: `maxDepth = 0, s = 0, ws = 0`.
Top-level calls start at depth $d = 1$.

---

### Step 1: Element 0 (`[1, 1]` at $d = 1$)
- `x.isInteger()` is False. `maxDepth = \max(0, 1) = 1`.
- Recurse on children at $d = 1 + 1 = 2$:
  - **Child 0 ($val = 1$ at $d = 2$):**
    - $maxDepth = \max(1, 2) = \mathbf{2}$.
    - $s \leftarrow 0 + 1 = 1$.
    - $ws \leftarrow 0 + 1 \times 2 = 2$.
  - **Child 1 ($val = 1$ at $d = 2$):**
    - $s \leftarrow 1 + 1 = 2$.
    - $ws \leftarrow 2 + 1 \times 2 = 4$.

---

### Step 2: Element 1 ($2$ at $d = 1$)
- `x.isInteger()` is True.
- Update depth: $maxDepth = \max(2, 1) = 2$.
- Value: $val = 2$.
- Updates:
  $$
  s \leftarrow 2 + 2 = \mathbf{4}
  $$
  $$
  ws \leftarrow 4 + 2 \times 1 = \mathbf{6}
  $$

---

### Step 3: Element 2 (`[1, 1]` at $d = 1$)
- `x.isInteger()` is False.
- Recurse on children at $d = 2$:
  - **Child 0 ($val = 1$ at $d = 2$):**
    - $s \leftarrow 4 + 1 = 5$.
    - $ws \leftarrow 6 + 1 \times 2 = 8$.
  - **Child 1 ($val = 1$ at $d = 2$):**
    - $s \leftarrow 5 + 1 = \mathbf{6}$.
    - $ws \leftarrow 8 + 1 \times 2 = \mathbf{10}$.

---

### Step 4: Final Algebraic Combination
All elements processed.
- $maxDepth = 2$
- $s = 6$
- $ws = 10$
Compute formula:
$$
(maxDepth + 1) \times s - ws = (2 + 1) \times 6 - 10 = 18 - 10 = \mathbf{8}
$$

---

## 4. Complete Execution Trace

```text
DFS Traversal:
dfs([1, 1], d=1):
  dfs(1, d=2) -> s=1, ws=2, maxDepth=2
  dfs(1, d=2) -> s=2, ws=4, maxDepth=2
dfs(2, d=1):
  int 2       -> s=4, ws=6, maxDepth=2
dfs([1, 1], d=1):
  dfs(1, d=2) -> s=5, ws=8, maxDepth=2
  dfs(1, d=2) -> s=6, ws=10, maxDepth=2

Totals: maxDepth = 2, s = 6, ws = 10
Formula: (2 + 1) * 6 - 10 = 8
```

| Element Inspected | Type | Value | Depth $d$ | Running Sum $s$ | Running Weighted $ws$ | Running $maxDepth$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `[1, 1]` | List | - | 1 | 0 | 0 | 1 |
| Child 0 | Integer | 1 | 2 | 1 | 2 | 2 |
| Child 1 | Integer | 1 | 2 | 2 | 4 | 2 |
| **Integer 2** | Integer | 2 | 1 | 4 | 6 | 2 |
| `[1, 1]` | List | - | 1 | 4 | 6 | 2 |
| Child 0 | Integer | 1 | 2 | 5 | 8 | 2 |
| Child 1 | Integer | 1 | 2 | 6 | 10 | 2 |
| **Formula Result** | - | - | - | **$(2 + 1) \times 6 - 10$** | - | **$\mathbf{8}$ (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let integers $v_1, \dots, v_M$ have depths $d_1, \dots, d_M$. By algebraic distributivity, $\sum v_i(D - d_i + 1) = (D + 1)\sum v_i - \sum v_i d_i$. Since $s$ computes $\sum v_i$ and $ws$ computes $\sum v_i d_i$ exactly, evaluating $(D + 1)s - ws$ is mathematically identical to applying inverse weights to each element individually.

**Completeness.** The recursion visits every node and sub-list in the hierarchical structure. Tracking $maxDepth = \max(maxDepth, d)$ at every call ensures that the global maximum depth is discovered even if deeper elements appear in later sibling branches.

---

## 6. Traps This Instance Exposes

- **Empty Lists Affecting Depth:** The definition specifies that max depth is determined by the deepest **integer** or list structure. Updating `maxDepth = max(maxDepth, d)` at node entry ensures empty lists at deep levels still establish valid depth geometry.
- **Negative Integer Values:** Inverse weights are strictly positive ($D - d + 1 \ge 1$). A negative integer at a shallow depth (high inverse weight) will contribute a more negative value to the total. The algebraic formula handles signs accurately.
- **Two-Pass Traversal Overhead:** Running an initial DFS to compute $D$ and a second DFS to compute weights is redundant; the distributed formula solves it in a single pass.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of integers and nested list objects. Every object is visited exactly once in the single-pass DFS.
- **Auxiliary Space Complexity:** $O(D)$, where $D$ is the maximum nesting depth of the structure, bounding the call stack.
