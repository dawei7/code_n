# Guided Example: Employee Importance

We trace the step-by-step organizational hierarchy dictionary indexing ($d[id] = employee$), depth-first recursive subtree aggregation ($dfs(i) = imp[i] + \sum dfs(j)$), multi-level subordinate transitive traversal, leaf employee evaluation ($subordinates = \emptyset$), and total corporate importance value summation on representative company staffing structures:

- **Input:**
  - Employee roster:
    ```text
    Employee 1: importance = 5, subordinates = [2, 3]
    Employee 2: importance = 3, subordinates = []
    Employee 3: importance = 3, subordinates = []
    ```
  - Target employee: $id = 1$
- **Required output:** `11`
  - Problem objective:
    - Return the combined total importance of the specified employee plus **all their direct and indirect subordinates**.
    - For Employee 1:
      - Direct importance: $5$
      - Subordinate 2: $3$
      - Subordinate 3: $3$
      - Combined total importance: $5 + 3 + 3 = \mathbf{11}$.
- **Organizational Tree & Subtree Summation Invariant:**
  - **The Corporate Tree Topology:**
    - Corporate hierarchies are directed rooted trees: each subordinate reports to exactly one direct manager, and there are **zero cyclic reporting dependencies**.
    - An employee's total organizational importance is the sum of their own importance plus the complete recursive subtree importance of every direct report.
  - **Lookup Table & DFS Recurrence:**
    - Index the list of employees by their unique ID in a hash table $d$:
      $$
      d[e.id] \leftarrow e
      $$
    - Define recursive subtree sum $dfs(i)$:
      $$
      dfs(i) = d[i].importance + \sum_{j \in d[i].subordinates} dfs(j)
      $$
    - When an employee has no subordinates ($d[i].subordinates = \emptyset$), the sum over subordinates is $0$, terminating recursion naturally at leaf employees.
- **Step-by-Step Worked Execution Trace for Target $id = 1$:**
  - **Step 1: Construct Hash Map $d$:**
    - Key $1 \implies \{importance: 5, \; subordinates: [2, 3]\}$
    - Key $2 \implies \{importance: 3, \; subordinates: []\}$
    - Key $3 \implies \{importance: 3, \; subordinates: []\}$
  - **Step 2: Start DFS at Employee 1 ($dfs(1)$):**
    - Retrieve Employee 1: importance $= 5$, direct reports $= [2, 3]$.
    - Initial contribution:
      $$
      \text{sum}_1 = 5
      $$
    - Subordinates to process: Employee 2, then Employee 3.
  - **Step 3: Recurse on Subordinate Employee 2 ($dfs(2)$):**
    - Retrieve Employee 2: importance $= 3$, direct reports $= []$.
    - Because the subordinates list is empty:
      $$
      dfs(2) = 3 + 0 = \mathbf{3}
      $$
    - Return $3$ to manager Employee 1.
  - **Step 4: Recurse on Subordinate Employee 3 ($dfs(3)$):**
    - Retrieve Employee 3: importance $= 3$, direct reports $= []$.
    - Because the subordinates list is empty:
      $$
      dfs(3) = 3 + 0 = \mathbf{3}
      $$
    - Return $3$ to manager Employee 1.
  - **Step 5: Accumulate Total Importance at Employee 1:**
    - Combine manager importance with both subordinate returns:
      $$
      dfs(1) = 5 + dfs(2) + dfs(3) = 5 + 3 + 3 = \mathbf{11}
      $$
  - **Step 6: Output Result:**
    $$
    ans = \mathbf{11}
    $$
- **Multi-Level Deep Hierarchy Trace ($1 \to [2] \to [3]$):**
  - Employee 1 (importance 5) manages Employee 2.
  - Employee 2 (importance 3) manages Employee 3.
  - Employee 3 (importance 4) manages nobody.
  - Query $id = 1$:
    - $dfs(3) = 4$.
    - $dfs(2) = 3 + dfs(3) = 3 + 4 = 7$.
    - $dfs(1) = 5 + dfs(2) = 5 + 7 = \mathbf{12}$.
  - Correctly sums all levels of indirect subordinates.
- **Leaf Employee Query ($id = 2$):**
  - Querying Employee 2 directly sums only Employee 2's importance ($3$).

This instance demonstrates directed acyclic graph reachability and bottom-up tree weight accumulation, mathematically proves why hash indexing achieves linear subtree summation over hierarchical structures, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an employee hierarchy with importance values and subordinate lists:
Find the **total importance** of a given employee and all direct and indirect subordinates.

```text
Employees:
  ID 1: importance = 5, reports = [2, 3]
  ID 2: importance = 3, reports = []
  ID 3: importance = 3, reports = []

Query: ID 1

Tree Structure:
       1 (5)
      /    \
    2 (3)   3 (3)

Total Importance = 5 + 3 + 3 = 11
```

### The Invariant of Subtree Accumulation
- In a valid management tree without circular reporting, an employee's total score is strictly the sum of their own importance plus the total scores of each child subtree.
- Indexing by ID enables $O(1)$ node lookups during the traversal.

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Table Indexing:
$$
d = \{e.id: e \mid e \in employees\}
$$

### 2. The Tree DFS Recurrence:
$$
dfs(i) = d[i].importance + \sum_{j \in d[i].subordinates} dfs(j)
$$

> **Hierarchical Arborescence Weight Invariant.** The cumulative organizational weight of any employee $u$ is isomorphic to the subgraph mass of the descendant closure $\text{Desc}(u)$, which is strictly computable in a single post-order tree traversal.

---

## 3. Step-by-Step Worked Execution

We trace Target $id = 1$:

---

### Step 1: Map Indexing
- $d[1] = (5, [2, 3])$.
- $d[2] = (3, [])$.
- $d[3] = (3, [])$.

---

### Step 2: DFS at 2
- $subordinates = [] \implies dfs(2) = 3$.

---

### Step 3: DFS at 3
- $subordinates = [] \implies dfs(3) = 3$.

---

### Step 4: DFS at 1
- $dfs(1) = 5 + dfs(2) + dfs(3) = 5 + 3 + 3 = \mathbf{11}$.

---

### Step 5: Output
$$
\mathbf{11}
$$

---

## 4. Complete Execution Trace

| Traversed Employee ID | Self Importance | Subordinate IDs | Children Evaluated | Subordinate Sum | Total Subtree Value |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ | $3$ | `[]` | None (Leaf) | $0$ | $3$ |
| $3$ | $3$ | `[]` | None (Leaf) | $0$ | $3$ |
| **$1$** | **$5$** | **`[2, 3]`** | **$2$ and $3$** | **$3 + 3 = 6$** | **`11`** |

---

## 5. Boundary Cases & Failure Modes

- **Employee Has No Subordinates:** Returns only their own importance value.
- **Single Employee Company:** Returns single importance.
- **Deep Single-Chain Hierarchy ($N = 2000$):** Traverses chain without cycles, bounded by standard recursion depth.

---

## 6. Traps & Common Anti-Patterns

- **Searching the Input List Linearly for Each Child ($O(N^2)$):** Searching the list for employee objects by ID takes $O(N)$ per lookup, making the traversal quadratic. Pre-building a hash table $d$ guarantees $O(1)$ lookups.
- **Worrying About Visited Sets:** The problem structure guarantees a strict tree (no employee has multiple managers and no cycles exist). A visited set is not needed.
- **Omission of Indirect Subordinates:** Only summing direct children ignores grandchildren and lower levels. Recursive DFS guarantees all depths are included.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building map: $\mathcal{O}(N)$ where $N$ is total employees.
  - DFS visits each subordinate in the target's subtree at most once: $\mathcal{O}(K) \le \mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 2000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the hash map and recursion call stack.