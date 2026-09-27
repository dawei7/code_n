# Guided Example: Tree Node

We trace the step-by-step structural role taxonomy evaluation via conditional SQL expressions (`CASE`), root isolation via null parent testing (`p_id IS NULL`), inner node identification via parent reference set containment (`id IN (SELECT p_id FROM Tree)`), complementary leaf node classification (`ELSE 'Leaf'`), and relational attribute projection (`id`, `type`) on representative tree adjacency tables:

- **Input:**
  - `Tree` table:
    | `id` | `p_id` |
    |:---:|:---:|
    | $1$ | `null` |
    | $2$ | $1$ |
    | $3$ | $1$ |
    | $4$ | $2$ |
    | $5$ | $2$ |
- **Required output:**
  | `id` | `type` |
  |:---:|:---:|
  | $1$ | `Root` |
  | $2$ | `Inner` |
  | $3$ | `Leaf` |
  | $4$ | `Leaf` |
  | $5$ | `Leaf` |
  - Structural classification rules:
    1. **`Root`:** The node has no parent (`p_id IS NULL`).
    2. **`Inner`:** The node has a parent (`p_id IS NOT NULL`) AND has at least one child (its `id` appears as a `p_id` in other rows).
    3. **`Leaf`:** The node has a parent (`p_id IS NOT NULL`) AND has zero children (its `id` never appears as a `p_id`).
- **Sequential Conditional Evaluation Logic (`CASE`):**
  - The SQL `CASE` construct evaluates branches sequentially from top to bottom and returns on the **first matching condition**:
    ```sql
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END
    ```
  - **Why this sequence is sound:**
    - Branch 1: `WHEN p_id IS NULL THEN 'Root'`
      - Captures the unique apex of the tree. Even if the root has no children (single-node tree), it is strictly classified as `Root`.
    - Branch 2: `WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'`
      - Any node reaching this branch has already been proven not to be the root ($p\_id \ne \text{null}$).
      - If its `id` appears in the parent column `p_id`, it has at least one child.
      - Having both a parent and a child satisfies the definition of `Inner`.
    - Branch 3: `ELSE 'Leaf'`
      - Any node reaching here is neither root nor inner: it has a parent and has zero children $\implies$ strictly `Leaf`!
- **Step-by-Step Execution Trace:**
  - **Precompute the Set of Active Parents:**
    - Distinct non-null values in column `p_id`:
      $$
      P = \{1, 2\}
      $$
  - **Evaluate Each Node in `Tree`:**
    - **Node $1$ (`p_id = null`):**
      - Test 1: `p_id IS NULL` evaluates to $\mathbf{True}$.
      - Classified immediately as:
        $$
        \mathbf{\text{"Root"}}
        $$
    - **Node $2$ (`p_id = 1`):**
      - Test 1: `p_id IS NULL` $\implies$ False.
      - Test 2: Is $2 \in P$?
        - $2 \in \{1, 2\} \implies \mathbf{True}$ (Node 2 is parent to nodes 4 and 5!).
      - Classified as:
        $$
        \mathbf{\text{"Inner"}}
        $$
    - **Node $3$ (`p_id = 1`):**
      - Test 1: `p_id IS NULL` $\implies$ False.
      - Test 2: Is $3 \in P$?
        - $3 \notin \{1, 2\} \implies \mathbf{False}$ (Node 3 has no children).
      - Falls through to `ELSE`:
        $$
        \mathbf{\text{"Leaf"}}
        $$
    - **Node $4$ (`p_id = 2`):**
      - Test 1: False.
      - Test 2: $4 \notin P \implies$ False.
      - Classified as:
        $$
        \mathbf{\text{"Leaf"}}
        $$
    - **Node $5$ (`p_id = 2`):**
      - Test 1: False.
      - Test 2: $5 \notin P \implies$ False.
      - Classified as:
        $$
        \mathbf{\text{"Leaf"}}
        $$
- **Single-Node Tree ($Tree = [(1, null)]$):**
  - Node 1 has `p_id IS NULL` $\implies$ Evaluates to **`Root`** (correctly not Leaf).
- **Linear Path Graph ($1 \to 2 \to 3$):**
  - Node 1: `Root`.
  - Node 2: has parent 1, parent to 3 $\implies$ `Inner`.
  - Node 3: has parent 2, no children $\implies$ `Leaf`.

This instance demonstrates tree topological role partitioning in relational models, mathematically proves why sequential condition evaluation resolves overlapping ancestor-descendant predicates, and derives $O(N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Tree` table with `id` and `p_id` (parent ID):
Classify each node into one of three mutually exclusive categories:
- **`Root`**: Has no parent (`p_id` is null).
- **`Inner`**: Has a parent and has at least one child.
- **`Leaf`**: Has a parent and has no children.

```text
Tree:
        1 (Root)
       / \
      2   3 (Leaf)
     / \
    4   5 (Leaves)

Node 1: p_id is null -> Root
Node 2: has parent (1) and has children (4, 5) -> Inner
Node 3: has parent (1) and no children -> Leaf
Node 4: has parent (2) and no children -> Leaf
Node 5: has parent (2) and no children -> Leaf
```

### The Invariant of Ordered Evaluation
- Instead of testing all three conditions symmetrically with complex boolean logic, the sequential execution order of `CASE` guarantees that:
  1. Once `Root` is handled, all remaining rows have parents.
  2. Once `Inner` is handled, all remaining rows have no children.
  3. The remaining rows are automatically `Leaf`.

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Implementation:
```sql
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
```

### 2. Set Containment:
- The subquery `SELECT p_id FROM Tree` extracts the set of all parent identifiers.
- A non-root node is an `Inner` node if and only if its identifier belongs to this parent set.

> **Topological Exclusion Invariant.** In any finite directed rooted tree, the three sets $\{u \mid \text{deg}_{in}(u) = 0\}$, $\{u \mid \text{deg}_{in}(u) > 0 \land \text{deg}_{out}(u) > 0\}$, and $\{u \mid \text{deg}_{in}(u) > 0 \land \text{deg}_{out}(u) = 0\}$ form a complete disjoint partition of the vertex set $V$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Parent Identifier Set
- Values in `p_id`: `[null, 1, 1, 2, 2]`.
- Parent set $P = \{1, 2\}$.

---

### Step 2: Classify Each Row
- ID 1: `p_id IS NULL` $\implies$ **`Root`**.
- ID 2: `p_id = 1`, $2 \in P \implies$ **`Inner`**.
- ID 3: `p_id = 1`, $3 \notin P \implies$ **`Leaf`**.
- ID 4: `p_id = 2`, $4 \notin P \implies$ **`Leaf`**.
- ID 5: `p_id = 2`, $5 \notin P \implies$ **`Leaf`**.

---

## 4. Complete Execution Trace

| `id` | `p_id` | `p_id IS NULL`? | In Parent Set $\{1, 2\}$? | Final Assigned `type` |
|:---:|:---:|:---:|:---:|:---:|
| **$1$** | `null` | **Yes** | (Skipped) | **`Root`** |
| **$2$** | $1$ | No | **Yes** | **`Inner`** |
| **$3$** | $1$ | No | No | **`Leaf`** |
| **$4$** | $2$ | No | No | **`Leaf`** |
| **$5$** | $2$ | No | No | **`Leaf`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Root Node ($id=1, p\_id=\text{null}$):** Matches first branch $\implies$ returns `Root`.
- **Tree With Only Root and Leaves (Star Tree):** Root is `Root`, all other nodes are `Leaf`, 0 `Inner` nodes.
- **Deep Linear Chain ($1 \to 2 \to 3 \to 4$):** Node 1 is Root, Node 4 is Leaf, Nodes 2 and 3 are Inner.

---

## 6. Traps & Common Anti-Patterns

- **Null Handling with `NOT IN`:** If you try `WHEN id NOT IN (SELECT p_id FROM Tree)`, the presence of a `NULL` in `p_id` causes `NOT IN` to evaluate to `UNKNOWN` for all rows! Using `WHEN id IN (SELECT p_id ...)` with an `ELSE 'Leaf'` fallback is completely immune to this SQL NULL trap.
- **Testing Leaf Before Inner:** If you test `Leaf` first with an anti-join, null values in `p_id` must be explicitly filtered with `WHERE p_id IS NOT NULL`.
- **Assuming Root is Always ID 1:** Root can have any arbitrary ID; always check `p_id IS NULL`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Subquery `SELECT p_id FROM Tree` builds a hash set of parents: $\mathcal{O}(N)$.
  - Evaluating the `CASE` statement for all $N$ rows: $\mathcal{O}(N)$ hash lookups.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the parent ID hash set.
