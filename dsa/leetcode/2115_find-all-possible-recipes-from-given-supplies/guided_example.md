# Guided Example: Find All Possible Recipes from Given Supplies

We trace the step-by-step execution of the optimal topological dependency resolution on a representative problem instance:

- **Recipes:** `["bread", "sandwich", "burger"]`
- **Ingredients:** `[["yeast", "flour"], ["bread", "meat"], ["sandwich", "cheese", "lettuce"]]`
- **Initial Supplies:** `["yeast", "flour", "meat"]`
- **Expected Output:** `["bread", "sandwich"]`

This instance highlights multi-tiered recipe dependencies, the propagation of newly unlocked items into subsequent recipes, and the pruning of recipes with unsatisfied prerequisite chains.

---

## 1. Problem Overview & Representative Instance

We are given a catalog of recipes, where each recipe requires a specified list of ingredients. An ingredient can be an initial supply item or another recipe. We possess an initial inventory of supply items. A recipe can be crafted if and only if all of its constituent ingredients are either initially present in our supplies or have already been crafted.

In our representative instance:
- `bread` requires `yeast` and `flour`.
- `sandwich` requires `bread` and `meat`.
- `burger` requires `sandwich`, `cheese`, and `lettuce`.
- Initial supplies contain `yeast`, `flour`, and `meat`.

Notice the chain: `bread` unlocks through base supplies, which subsequently enables `sandwich` in conjunction with `meat`. However, `burger` remains incomplete because neither `cheese` nor `lettuce` is present in the supply inventory or manufacturable from other recipes.

---

## 2. Mathematical & Algorithmic Principles

### Dependency Directed Acyclic Graph (DAG) Formulation
The system forms a directed bipartite dependency network between items (supplies and recipes) and recipes:
- Let $V_S$ be the set of basic supplies, and $V_R$ be the set of recipes.
- For each recipe $r \in V_R$ and required ingredient $u \in \text{ingredients}(r)$, there exists a directed dependency edge $u \to r$.
- The in-degree of a recipe $r$, denoted $\text{in\_degree}(r)$, is initially set to the total number of required ingredients: $|\text{ingredients}(r)|$.

### Topological Wavefront Propagation (Kahn's Algorithm)
A recipe $r$ becomes craftable if and only if all its incoming dependencies are resolved, which corresponds to:

$$\text{in\_degree}(r) = 0$$

1. **Frontier Initialization:** We populate a processing queue with all items in the initial inventory $V_S$.
2. **Signal Propagation:** When an available item $u$ is dequeued, we traverse all outward edges $u \to r$.
3. **Degree Reduction:** For each dependent recipe $r$, we decrement its remaining dependency counter:

$$\text{in\_degree}(r) \leftarrow \text{in\_degree}(r) - 1$$

4. **Frontier Expansion:** If $\text{in\_degree}(r)$ reaches $0$, all prerequisite requirements have been fulfilled. The recipe $r$ is marked as crafted, recorded in the result collection, and added to the processing queue to potentially satisfy downstream recipes.

| Entity | Role in Graph | Initial Configuration |
|---|---|---|
| `yeast` | Source node (Basic supply) | Available at step 0 |
| `flour` | Source node (Basic supply) | Available at step 0 |
| `meat` | Source node (Basic supply) | Available at step 0 |
| `bread` | Intermediate recipe node | In-degree = 2 (`yeast`, `flour`) |
| `sandwich` | Higher-order recipe node | In-degree = 2 (`bread`, `meat`) |
| `burger` | Leaf-level recipe node | In-degree = 3 (`sandwich`, `cheese`, `lettuce`) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Graph Construction & Initial In-Degrees
- Outgoing adjacency mapping:
  - `yeast` $\to$ `[bread]`
  - `flour` $\to$ `[bread]`
  - `meat` $\to$ `[sandwich]`
  - `bread` $\to$ `[sandwich]`
  - `sandwich` $\to$ `[burger]`
  - `cheese` $\to$ `[burger]`
  - `lettuce` $\to$ `[burger]`
- In-degree table:
  - `bread`: $2$
  - `sandwich`: $2$
  - `burger`: $3$
- Queue initialized with supplies: `["yeast", "flour", "meat"]`
- Crafted result list: `[]`

### Step 1: Processing `yeast`
- Dequeue item: `yeast`
- Successors: `bread`
- Update: $\text{in\_degree}(\text{bread}) = 2 - 1 = 1 \ne 0$.
- Queue state: `["flour", "meat"]`
- Crafted list: `[]`

### Step 2: Processing `flour`
- Dequeue item: `flour`
- Successors: `bread`
- Update: $\text{in\_degree}(\text{bread}) = 1 - 1 = 0$.
- In-degree reaches zero: `bread` is successfully crafted.
- Append `bread` to crafted list: `["bread"]`.
- Enqueue `bread` into processing queue: `["meat", "bread"]`.

### Step 3: Processing `meat`
- Dequeue item: `meat`
- Successors: `sandwich`
- Update: $\text{in\_degree}(\text{sandwich}) = 2 - 1 = 1 \ne 0$.
- Queue state: `["bread"]`
- Crafted list: `["bread"]`

### Step 4: Processing `bread`
- Dequeue item: `bread`
- Successors: `sandwich`
- Update: $\text{in\_degree}(\text{sandwich}) = 1 - 1 = 0$.
- In-degree reaches zero: `sandwich` is successfully crafted.
- Append `sandwich` to crafted list: `["bread", "sandwich"]`.
- Enqueue `sandwich` into processing queue: `["sandwich"]`.

### Step 5: Processing `sandwich`
- Dequeue item: `sandwich`
- Successors: `burger`
- Update: $\text{in\_degree}(\text{burger}) = 3 - 1 = 2 \ne 0$.
- In-degree of `burger` is $2 > 0$ (still waiting on `cheese` and `lettuce`).
- Queue state: `[]` (empty).

### Queue Exhaustion and Termination
The queue is now empty. No further items can be unlocked.
Final crafted list: `["bread", "sandwich"]`.

---

## 4. Comprehensive State Trace

The state of all recipes across the successive queue processing rounds is summarized below.

| Step | Item Dequeued | Dependent Recipes Visited | Updated In-Degrees | Newly Unlocked Recipe | Queue at End of Step |
|---|---|---|---|---|---|
| Initialization | None | None | `bread`: 2, `sandwich`: 2, `burger`: 3 | None | `["yeast", "flour", "meat"]` |
| 1 | `yeast` | `bread` | `bread`: 1 | None | `["flour", "meat"]` |
| 2 | `flour` | `bread` | `bread`: 0 | `bread` | `["meat", "bread"]` |
| 3 | `meat` | `sandwich` | `sandwich`: 1 | None | `["bread"]` |
| 4 | `bread` | `sandwich` | `sandwich`: 0 | `sandwich` | `["sandwich"]` |
| 5 | `sandwich` | `burger` | `burger`: 2 | None | `[]` |

Output produced: `["bread", "sandwich"]`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** A recipe is added to the output list if and only if its in-degree reaches $0$. Since the initial in-degree corresponds exactly to the count of unique required ingredients and every decrement corresponds to a validated item being produced or supplied, a recipe reaching in-degree $0$ is guaranteed to have all prerequisites satisfied.

**Completeness.** Topological sort processes every reachable dependency path. If a recipe can be produced, there must exist a topological ordering of its constituent dependencies originating from the initial supplies. Because BFS traverses along all valid dependency edges without omissions, every craftable recipe is guaranteed to be reached. Any recipe trapped in a circular dependency (e.g., $A$ requires $B$ and $B$ requires $A$) or missing an external supply will maintain an in-degree strictly greater than $0$ and will correctly remain unproduced.

---

## 6. Edge Cases & Anti-Patterns

- **Direct Supplies Only:** When every recipe's ingredients are present in `supplies`, each recipe unlocks in the first wave of supply dequeues.
- **Missing Raw Ingredients:** If an ingredient is neither provided in `supplies` nor produced by any recipe, its dependent recipes will never reach an in-degree of zero.
- **Circular Dependencies:** If recipe $X$ requires recipe $Y$, and recipe $Y$ requires recipe $X$, neither recipe can ever have its in-degree reduced to zero from the initial supplies. Topological sorting naturally handles and ignores cycles without infinite recursion.
- **Disjoint Subgraphs:** Unrelated recipes that do not share ingredients are processed independently without interference.
- **Anti-Pattern — Naive Iterative Scanning:** Repeatedly iterating through all recipes until no new recipe can be made takes $\mathcal{O}(N \cdot \sum |\text{ingredients}|)$ in the worst case. The topological approach processes each dependency edge exactly once, yielding optimal linear-time performance.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(V + E)$, where $V$ is the total number of distinct strings (supplies and recipes) and $E$ is the total number of ingredient requirements across all recipes ($\sum |\text{ingredients}[i]|$). Graph construction scans each ingredient edge once, and the BFS traversal decrements each edge at most once.
- **Auxiliary Space Complexity:** $\mathcal{O}(V + E)$ to store the adjacency list mapping each ingredient to its dependent recipes, the in-degree hash table for recipe requirements, and the BFS queue.
