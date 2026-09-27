# Guided Example: Move Sub-Tree of N-Ary Tree

## 1. Instance & Teaching Goal

We examine an N-ary tree where $p$ is an ancestor of $q$:
$$\text{root} = 1, \quad p = 1, \quad q = 4$$
The initial tree structure has root $1$ with children $[2, 3]$, and node $2$ has child $[4]$:

```text
       (1)  <-- p (Root)
      /   \
    (2)   (3)
    /
  (4)       <-- q (Descendant of p)
```

Our teaching goal is to relocate the entire subtree rooted at $p$ to become the direct last child of node $q$. We establish the three fundamental topological cases governing parent-child rewiring in N-ary trees, focusing on the critical ancestor-inversion case (Case 1) where $q$ is promoted to fill the vacancy left by $p$, thereby preserving global graph connectivity without cycle creation.

## 2. Conceptual Foundation & Invariants

Let $T$ be a directed rooted tree where each node maintains an ordered list of children pointers.
When moving subtree $p$ to become a child of $q$:
1. **Case 0 (Identity / Already Direct Child)**:
   If $\text{parent}[p] = q$, $p$ is already a direct child of $q$. Per problem specification, no mutations are performed.
2. **Case 2 & 3 (Independent Subtrees or $p$ Descendant of $q$)**:
   Node $q$ does **not** reside in the subtree of $p$.
   - Node $p$ is safely detached: remove $p$ from $\text{parent}[p].\text{children}$.
   - Node $p$ is grafted onto $q$: append $p$ to $q.\text{children}$.
   - The tree root remains unchanged.
3. **Case 1 (Ancestor Inversion: $q$ in Subtree of $p$)**:
   Node $q$ resides within the subtree of $p$. Detaching $p$ would simultaneously sever $q$ from the main tree, causing disconnection if $p$ were simply made a child of $q$.
   To preserve connectivity:
   - Detach $q$ from its current parent: remove $q$ from $\text{parent}[q].\text{children}$.
   - Elevate $q$ into the topological slot previously occupied by $p$:
     - If $p$ was the global root ($\text{parent}[p] = \text{null}$), $q$ becomes the **new global root**.
     - Otherwise, replace $p$ with $q$ at the exact index in $\text{parent}[p].\text{children}$.
   - Finally, graft $p$ onto $q$: append $p$ as the last child in $q.\text{children}$.

```text
+-------------------------------------------------------------------------------+
|                    CASE 1: ANCESTOR INVERSION REWIRING                        |
|                                                                               |
|  Initial Topology:                Topological Surgery:                        |
|        (1) [p, Root]                1. Detach q (4) from parent 2             |
|       /   \                         2. Promote q (4) to replace p (Root)      |
|     (2)   (3)                       3. Append p (1) as last child of q (4)    |
|     /                                                                         |
|   (4) [q]                         Resulting Topology:                         |
|                                             (4) [New Root]                    |
|                                              |                                |
|                                             (1)                               |
|                                            /   \                              |
|                                          (2)   (3)                            |
+-------------------------------------------------------------------------------+
```

The algorithm maintains the following topological state components:

| State Variable | Domain | Initial Value | Transition / Role |
|---|---|---|---|
| `parent_map` | Dictionary mapping `Node` $\to$ `Node` | $\{\text{root}: \text{null}\}$ | Records the unique parent reference for every node in the tree. |
| `p_parent` | `Node` or `null` | $\text{parent\_map}[p]$ | Immediate parent of node $p$. |
| `q_parent` | `Node` or `null` | $\text{parent\_map}[q]$ | Immediate parent of node $q$. |
| `q_is_below_p` | Boolean | False | Flag indicating whether $q$ is in the directed subtree of $p$. |
| `current_root` | `Node` | `root` | Reference to the current global root, updated if $p = \text{root}$. |

> [!IMPORTANT]
> **Tree Integrity Invariant**: In an ancestor inversion (Case 1), promoting $q$ to the position of $p$ replaces a directed cycle with a valid tree inversion, ensuring every node continues to have in-degree $1$ except the single global root with in-degree $0$.

```mermaid
flowchart TD
    accTitle: N-ary Subtree Movement Logic Flow
    accDescr: Decision tree identifying topological relationship between p and q and executing corresponding edge rewiring.
    A["Build parent_map for all nodes"] --> B{"Is parent[p] == q ?"}
    B -->|Yes| C["Return unchanged root (Case 0)"]
    B -->|No| D["Trace ancestry of q to check if p is an ancestor"]
    D --> E{"Is q in subtree of p (Case 1) ?"}
    E -->|Yes| F["Detach q from parent[q]"]
    F --> G{"Is p the global root ?"}
    G -->|Yes| H["Set root = q"]
    G -->|No| I["Replace p with q in parent[p].children"]
    H --> J["Append p to q.children"]
    I --> J
    E -->|No (Case 2/3)| K["Remove p from parent[p].children"]
    K --> L["Append p to q.children"]
    J --> M["Return root"]
    L --> M
```

## 3. Step-by-Step Worked Execution

We walk through the representative instance $\text{root} = 1$, $p = 1$, $q = 4$.

### Phase 1: Parent Mapping via Tree Traversal

We traverse the tree starting from root $1$:
- Node $1$: children $[2, 3]$ $\implies \text{parent}[2] = 1, \text{parent}[3] = 1$.
- Node $2$: children $[4]$ $\implies \text{parent}[4] = 2$.
- Node $3$: children $[]$.
- Node $4$: children $[]$.

Parent directory:
$$\text{parent} = \{1: \text{null}, 2: 1, 3: 1, 4: 2\}$$

### Phase 2: Relationship Identification

1. We check if $p$ is already a direct child of $q$:
   - $\text{parent}[p] = \text{parent}[1] = \text{null} \ne 4$. (Not Case 0).
2. We trace the ancestry path from $q = 4$ upwards toward the root:
   - Start at $q = 4$.
   - $\text{parent}[4] = 2$.
   - $\text{parent}[2] = 1$. This matches $p = 1$!
   - Result: $q$ is in the subtree of $p$ ($\text{q\_is\_below\_p} = \text{True}$).
   - Classification: **Case 1 (Ancestor Inversion)**.

### Phase 3: Topological Surgery (Case 1)

1. **Detach $q$ from its current parent**:
   - $\text{q\_parent} = \text{parent}[4] = 2$.
   - Remove $4$ from $2.\text{children}$:
     $$2.\text{children} \leftarrow []$$
2. **Promote $q$ into $p$'s position**:
   - $\text{p\_parent} = \text{parent}[1] = \text{null}$.
   - Because $p$ was the global root, node $q = 4$ is promoted to become the **new global root**:
     $$\text{root} \leftarrow 4$$
3. **Graft $p$ onto $q$**:
   - Append $p = 1$ to $q.\text{children}$:
     $$4.\text{children} \leftarrow [1]$$
   - Node $1$'s children remain intact: $1.\text{children} = [2, 3]$.

Final resulting structure:
- Root: $4$
- Children of $4$: $[1]$
- Children of $1$: $[2, 3]$
- Children of $2$: $[]$
- Children of $3$: $[]$

## 4. Complete Execution Trace

We tabulate the state mutations and pointer updates across all algorithmic steps.

| Step Index | Action Executed | Target Pointer | State Before Mutation | State After Mutation | Verification Check |
|---|---|---|---|---|---|
| 0 | Ancestry Discovery | `parent_map` | Empty | $\{1: \text{null}, 2: 1, 3: 1, 4: 2\}$ | Unique parent per node |
| 1 | Direct Child Check | `parent[p]` | $\text{null}$ | $\text{null}$ | $\text{null} \ne 4 \implies$ Proceed |
| 2 | Subtree Membership | `q_is_below_p` | False | **True** | Path $4 \to 2 \to 1$ reaches $p$ |
| 3 | Detach $q$ | $2.\text{children}$ | $[4]$ | $[]$ | Node 4 freed from node 2 |
| 4 | Promote $q$ | Global `root` | $1$ | **$4$** | Node 4 becomes new root |
| 5 | Graft $p$ onto $q$ | $4.\text{children}$ | $[]$ | $[1]$ | Node 1 is last child of 4 |
| 6 | Completion | Return Value | `Node(1)` | **`Node(4)`** | Single connected tree valid |

### Comparison Across All Three Topological Cases

Using the same baseline tree with root $1$:
- **Case 0 ($p=2, q=1$)**: Node $2$ is already a child of $1$. Do nothing, return root $1$.
- **Case 1 ($p=1, q=4$)**: $q$ is below $p$. Detach $4$, promote $4$ to root, append $1$ to $4$'s children. Output root $4$.
- **Case 3 ($p=3, q=4$)**: $3$ and $4$ are in disjoint subtrees. Detach $3$ from $1$, append $3$ to $4$'s children. Output root $1$.

## 5. Algorithmic Correctness

### Soundness

In a directed tree with $n$ nodes and $n - 1$ edges, connectivity is maintained if and only if every node has in-degree $1$ except the single designated root which has in-degree $0$.
- In Case 1, detaching $q$ from $\text{parent}[q]$ reduces the in-degree of $q$ to $0$.
- If $p$ was the root, $p$ had in-degree $0$. Setting $q$ as root and adding edge $q \to p$ increases $p$'s in-degree to $1$ while maintaining $q$'s in-degree at $0$.
- If $p$ was not root, replacing $p$ with $q$ in $\text{parent}[p].\text{children}$ transfers the parent's incoming edge to $q$, restoring $q$'s in-degree to $1$. Adding edge $q \to p$ gives $p$ an in-degree of $1$.
- In all cases, no cycles are introduced because $q$ was removed from $p$'s sub-hierarchy before $p$ became a child of $q$.
Thus, the graph remains a valid single-rooted tree.

### Completeness

The classification exhausts all possible configurations of two distinct nodes in a tree:
1. $q = \text{parent}[p]$ (Case 0)
2. $p$ is an ancestor of $q$ (Case 1)
3. $p$ is not an ancestor of $q$ (Cases 2 & 3)
Because all mutually exclusive topological configurations are handled deterministically, the algorithm completely covers any valid input instance.

## 6. Traps This Instance Exposes

- **Disconnected Tree Trap in Case 1**: Simply removing $p$ from its parent and adding it to $q$ without detaching and promoting $q$. Because $q$ was inside $p$'s subtree, moving $p$ under $q$ creates an isolated cycle between $p$ and $q$ completely severed from the original tree.
- **Root Pointer Stagnation**: Failing to update the `root` reference when $p$ is the original root of the entire tree. Returning the original pointer $p$ returns an internal node rather than the true global root $q$.
- **Preserving Child Order in Parent Replacement**: When $p$ is not the root and $q$ replaces $p$ in $\text{parent}[p].\text{children}$, replacing $p$ in-place (`children[idx] = q`) preserves the siblings' relative order, whereas appending $q$ to the end of the children list alters structural sibling relationships.
- **Direct Child Redundant Repositioning**: In Case 0, removing and re-appending $p$ to $q$'s children list would change $p$'s order if $q$ has other children after $p$, violating the rule that no changes should occur if $p$ is already a child of $q$.

## 7. Complexity Derivation

### Time Complexity

Let $N$ denote the total number of nodes in the N-ary tree ($N \le 1000$).
- **Parent Mapping**: Breadth-first or depth-first search visits every node and edge once, consuming $\mathcal{O}(N)$ time.
- **Ancestry Check**: Climbing from $q$ upwards to the root checks at most $\text{depth}(T) \le N$ nodes, taking $\mathcal{O}(N)$ time.
- **List Operations**: Removing an element and appending an element to a node's children list takes $\mathcal{O}(\text{degree}) \le \mathcal{O}(N)$ time.
- Total time complexity is strictly $\mathcal{O}(N)$, which is optimal.

### Auxiliary Space Complexity

- The `parent_map` stores an entry for each of the $N$ nodes: $\mathcal{O}(N)$.
- The traversal queue or recursion stack holds at most $\mathcal{O}(N)$ nodes.
- Auxiliary space complexity is strictly $\mathcal{O}(N)$.