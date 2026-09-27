# Guided Example: Smallest String With Swaps

## 1. Problem Essence & Algorithmic Mental Model

Given a string $s$ of length $n$ and a collection of index pairs $\text{pairs} = [[a_0, b_0], [a_1, b_1], \dots]$, each pair indicates that the characters at indices $a$ and $b$ may be swapped. We are allowed to execute swaps in any order and any number of times. Our goal is to determine the lexicographically smallest string obtainable through these allowable transpositions.

At first glance, one might perceive this as a shortest-path or graph-search problem over the factorial state space of string permutations ($n!$ configurations). However, group theory and graph connectivity yield an immediate simplification:
1. **Transitivity of Permutation Generators**:
   If we can swap index $a$ with index $b$, and swap index $b$ with index $c$, we can swap index $a$ with index $c$ via the sequence:
   $$\text{swap}(a, b) \to \text{swap}(b, c) \to \text{swap}(a, b)$$
   More generally, in abstract algebra, the set of all transpositions on a connected graph forms a generating set for the full **Symmetric Group** $\mathcal{S}_k$ on those vertices.
2. **Component-Wise Arbitrary Reordering**:
   If a subset of indices forms a single connected component in the graph whose edges are the given pairs, **any arbitrary permutation of characters residing on those indices is reachable**.
3. **Independent Greedy Minimization**:
   Different connected components share no edges and cannot exchange characters with one another. To minimize the overall string lexicographically, we must make each individual position as small as possible from left to right. Therefore, within each connected component:
   - Extract the subset of index coordinates.
   - Extract the multiset of characters residing at those coordinates.
   - Sort the characters in ascending alphabetical order.
   - Reassign the sorted characters back to the sorted index coordinates in 1-to-1 correspondence.

```
String: "d c a b"
Pairs:  (0, 3), (1, 2)

Graph Components:
Component 1: Indices {0, 3} -> Characters {'d', 'b'} -> Sorted: ['b', 'd']
Component 2: Indices {1, 2} -> Characters {'c', 'a'} -> Sorted: ['a', 'c']

Reassembled String:
Index 0 receives 'b'
Index 1 receives 'a'
Index 2 receives 'c'
Index 3 receives 'd'
Result: "b a c d"
```

---

## 2. Mathematical Formalism & Invariants

Let $V = \{0, 1, \dots, n-1\}$ be the set of character indices of string $s$.
Define an undirected graph $G = (V, E)$ where an undirected edge $(u, v) \in E$ exists if and only if $[u, v] \in \text{pairs}$.

### Equivalence Relation
Define the reachability relation $\sim$ on $V$:
$$u \sim v \iff \text{there exists a path in } G \text{ between } u \text{ and } v$$
Because reachability in an undirected graph is reflexive, symmetric, and transitive, $\sim$ is an equivalence relation partitioning $V$ into $k$ disjoint connected components:
$$V = \mathcal{C}_1 \cup \mathcal{C}_2 \cup \dots \cup \mathcal{C}_k \quad \text{where } \mathcal{C}_i \cap \mathcal{C}_j = \emptyset \text{ for } i \neq j$$

### Symmetric Group Invariant
For any connected component $\mathcal{C}_m = \{i_1 < i_2 < \dots < i_p\}$, the allowable swap operations can generate any permutation $\pi \in \mathcal{S}_p$ acting on the positions $(i_1, \dots, i_p)$.
The set of accessible character configurations at positions $\mathcal{C}_m$ is the set of all rearrangements of the multiset:
$$\mathcal{M}_m = \{s[i] \mid i \in \mathcal{C}_m\}$$

### Lexicographical Minimization Mapping
Let the sorted elements of $\mathcal{M}_m$ be:
$$c_1 \le c_2 \le \dots \le c_p$$
The unique assignment minimizing the string lexicographically assigns character $c_j$ to index $i_j$:
$$\forall j \in \{1, \dots, p\}, \quad s_{\text{opt}}[i_j] = c_j$$

---

## 3. Concrete Example Execution & State Evolution

Consider the input:
- $s = \text{"dcab"}$
- $\text{pairs} = [[0, 3], [1, 2], [0, 2]]$

### Step 1: Disjoint Set Union (DSU) Trace

Initially, each index is its own parent: $P = [0, 1, 2, 3]$.

| Processing Pair $[a, b]$ | Find Root of $a$ | Find Root of $b$ | Union Action | Parent Array State $P$ |
|---|---|---|---|---|
| Initial | - | - | - | $[0, 1, 2, 3]$ |
| $[0, 3]$ | $\text{find}(0) = 0$ | $\text{find}(3) = 3$ | Set $P[3] = 0$ | $[0, 1, 2, 0]$ |
| $[1, 2]$ | $\text{find}(1) = 1$ | $\text{find}(2) = 2$ | Set $P[2] = 1$ | $[0, 1, 1, 0]$ |
| $[0, 2]$ | $\text{find}(0) = 0$ | $\text{find}(2) = 1$ | Set $P[1] = 0$ | $[0, 0, 1, 0]$ |

All four indices collapse into a **single connected component** with root 0:
$$\mathcal{C} = \{0, 1, 2, 3\}$$

```mermaid
flowchart TD
    accTitle: Transitive Equivalence Component Partitioning
    accDescr: Graph connectivity merging indices into a single component followed by sorting and distribution.
    
    I0(["Index 0: d"]) ---|"Pair 0, 3"| I3(["Index 3: b"])
    I1(["Index 1: c"]) ---|"Pair 1, 2"| I2(["Index 2: a"])
    I0 ---|"Pair 0, 2"| I2
    
    subgraph Comp ["Single Connected Component"]
        I0
        I1
        I2
        I3
    end
    
    Comp --> Extract["Gather Indices: [0, 1, 2, 3]<br/>Gather Characters: [d, c, a, b]"]
    Extract --> Sort["Sort Characters: [a, b, c, d]"]
    Sort --> Assign["Assign to Indices:<br/>Index 0 -> a<br/>Index 1 -> b<br/>Index 2 -> c<br/>Index 3 -> d"]
    Assign --> Output["Result: abcd"]
```

### Component Character Redistribution Trace

| Component Root | Constituent Indices | Original Substring Multiset | Sorted Characters | Reassigned String Content |
|---|---|---|---|---|
| 0 | $\{0, 1, 2, 3\}$ | $\{'d', 'c', 'a', 'b'\}$ | `['a', 'b', 'c', 'd']` | $s[0] = \text{'a'}, s[1] = \text{'b'}, s[2] = \text{'c'}, s[3] = \text{'d'}$ |

Final result: `"abcd"`.

---

## 4. Multi-Approach Comparison & Trade-Offs

| Metric / Dimension | Permutation BFS / Dijkstra | Repeated Local Bubble-Swapping | DSU / DFS Component Sorting (Optimal) |
|---|---|---|---|
| **Underlying Principle**| State graph over string permutations | Greedily swap adjacent inversions | Algebraic symmetric group equivalence |
| **Time Complexity** | Exponential ($\mathcal{O}(N!)$) | $\mathcal{O}(N^3)$ or higher; fails on cycles | $\mathcal{O}(N \log N + M \alpha(N))$ |
| **Auxiliary Memory** | Explodes rapidly | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ for DSU and component buckets |
| **Termination Guarantee**| Infeasible for $N > 10$ | Can oscillate or stall | Deterministic linear-logarithmic completion |
| **Completeness** | Full search | Vulnerable to local minima | Mathematically provably optimal |

```
Execution Comparison on N = 100,000:
- Permutation BFS: 100,000! states (Completely impossible)
- Simulation: Millions of manual swaps (Time Limit Exceeded)
- DSU Sorting:
  1. Find connected components: ~0.02s
  2. Sort character buckets: ~0.03s
  Total Time: ~0.05 seconds!
```

---

## 5. Algorithmic Edge Cases & Boundary Analysis

| Boundary Scenario | Configuration Condition | System Behavior & Invariant |
|---|---|---|
| **Empty Pairs List** | $\text{pairs} = []$ | Every index forms an isolated component of size 1. String returned completely unchanged. |
| **Fully Connected Graph** | Edges span all indices | Entire string forms one component; entire string is sorted globally. |
| **Disconnected Islands** | Pairs form isolated subgraphs | Each island sorts its characters independently without leaking across boundaries. |
| **Duplicate Identical Pairs** | $\text{pairs} = [[0, 1], [0, 1]]$ | DSU `union` detects identical roots; redundant edges ignored in $\mathcal{O}(\alpha(N))$. |
| **Self-Loops** | $\text{pairs} = [[i, i]]$ | Handled seamlessly; $\text{find}(i) == \text{find}(i)$ performs zero state mutation. |

---

## 6. Mathematical Verification & Complexity Derivation

Let $N = |s|$ be the length of the string, and $M = |\text{pairs}|$ be the number of swap pairs.

### Phase 1: Connected Component Identification (DSU)
1. Initialize parent array of size $N$: $\mathcal{O}(N)$ time.
2. For each of the $M$ pairs, execute $\text{find}$ with path compression and $\text{union}$:
   $$\mathcal{O}(M \cdot \alpha(N))$$
   where $\alpha$ is the inverse Ackermann function ($\alpha(N) \le 4$ for all practical inputs).
3. Total DSU time: $\mathcal{O}(N + M \alpha(N))$.

### Phase 2: Bucket Grouping and Sorting
1. Iterate through indices $0$ to $N-1$, appending character $s[i]$ to the bucket of its root $\text{find}(i)$: $\mathcal{O}(N \alpha(N))$.
2. Let the components have sizes $p_1, p_2, \dots, p_k$, where $\sum p_m = N$.
3. Sorting each bucket using comparison sort takes:
   $$\sum_{m=1}^k \mathcal{O}(p_m \log p_m) \le \mathcal{O}\left( \sum_{m=1}^k p_m \log N \right) = \mathcal{O}(N \log N)$$
   *(Note: Using counting sort over the 26 lowercase English letters reduces bucket sorting to strictly $\mathcal{O}(26 \cdot N) = \mathcal{O}(N)$ linear time).*

### Phase 3: String Reconstruction
1. For each index $i \in [0, N-1]$, pop or read the next smallest character from bucket $\text{find}(i)$: $\mathcal{O}(N)$ operations.

### Total Asymptotics:
- **Total Time Complexity:** $\mathcal{O}(N \log N + M \alpha(N))$ with standard sort, or $\mathcal{O}(N + M \alpha(N))$ with bucket counting sort.
- **Total Auxiliary Space Complexity:** $\mathcal{O}(N)$ memory to store the DSU parent array and component character buckets.

---

## 7. Synthesis & Strategic Takeaways

1. **Permutation Generation on Connected Graphs**: Any set of allowable transpositions spanning a connected component of size $k$ generates the entire symmetric group $\mathcal{S}_k$. The ability to swap pairs transitively allows any arbitrary reordering of elements within that component.
2. **Equivalence Class Decoupling**: Once transitivity is proven, the problem decouples into independent component subproblems. What happens inside component $A$ has zero impact on component $B$.
3. **DSU for Static Component Partitioning**: Disjoint Set Union with path compression provides near-linear $\mathcal{O}((N + M) \alpha(N))$ partitioning, bypassing the need to construct full explicit graph adjacency lists.
