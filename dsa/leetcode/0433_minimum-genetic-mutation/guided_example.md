# Guided Example: Minimum Genetic Mutation

We trace the step-by-step shortest path search on unweighted mutation graphs, single-nucleotide Hamming distance neighbor expansion ($d_H = 1$), visited state marking, and level-by-level breadth-first frontier exploration on representative genetic bank instances:

- **Input:**
  - $startGene = \text{"AACCGGTT"}$
  - $endGene = \text{"AAACGGTA"}$
  - $bank = [\text{"AACCGGTA"}, \text{"AACCGCTA"}, \text{"AAACGGTA"}]$
- **Required output:** `2`
- **Execution trace:**
  - Initialize BFS queue with start state: $Q = [(\text{"AACCGGTT"}, 0)]$
  - Visited set: $vis = \{\text{"AACCGGTT"}\}$
  - **Frontier Level 0:**
    - Dequeue $(\text{"AACCGGTT"}, 0)$
    - Evaluate Hamming distances against bank elements:
      - Against `"AACCGGTA"`: differs at index 7 (`'T'` $\to$ `'A'`) $\implies d_H = 1$. Unvisited $\implies$ Enqueue $(\text{"AACCGGTA"}, 1)$, mark visited.
      - Against `"AACCGCTA"`: differs at indices 5 and 7 $\implies d_H = 2$ (Invalid).
      - Against `"AAACGGTA"`: differs at indices 2 and 7 $\implies d_H = 2$ (Invalid).
    - Queue state: $Q = [(\text{"AACCGGTA"}, 1)]$
  - **Frontier Level 1:**
    - Dequeue $(\text{"AACCGGTA"}, 1)$
    - Evaluate Hamming distances against bank:
      - Against `"AACCGGTA"`: already visited.
      - Against `"AACCGCTA"`: differs at index 5 (`'G'` $\to$ `'C'`) $\implies d_H = 1$. Enqueue $(\text{"AACCGCTA"}, 2)$.
      - Against `"AAACGGTA"`: differs at index 2 (`'C'` $\to$ `'A'`) $\implies d_H = 1$.
        - Matches $endGene$!
        - Return current depth $+ 1 = 1 + 1 = \mathbf{2}$
- **Target Not in Bank Instance:** If $endGene$ is missing from $bank$, no sequence of valid mutations can legally end at $endGene \implies \mathbf{-1}$
- **Immediate One-Step Mutation:** $startGene = \text{"AACCGGTT"}, endGene = \text{"AACCGGTA"}, bank = [\text{"AACCGGTA"}] \implies \mathbf{1}$

This instance demonstrates modeling sequence mutation as shortest-path discovery in an implicit unweighted graph, mathematically proves why breadth-first search (BFS) guarantees the minimal mutation count, and derives $O(B \cdot L + B^2)$ runtime and $O(B)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a starting gene string $startGene$, a target string $endGene$, and a mutation dictionary $bank$:
A gene string is composed of 8 characters from $\{\text{'A'}, \text{'C'}, \text{'G'}, \text{'T'}\}$.
A single **mutation** changes exactly one character in the string.
Every intermediate mutation must be an authorized valid sequence present in $bank$.
Find the **minimum number of mutations** needed to transform $startGene$ into $endGene$. If no valid mutation sequence exists, return $-1$.

```text
Mutation Graph:
  "AACCGGTT" (Start, depth 0)
       |
       |  Mutate index 7: 'T' -> 'A'
       v
  "AACCGGTA" (Bank node, depth 1)
       |
       |  Mutate index 2: 'C' -> 'A'
       v
  "AAACGGTA" (Target reached, depth 2)

Shortest Mutation Path Length: 2
```

### The State Space as an Unweighted Graph
- **Vertices ($V$):** $startGene$ and all strings in $bank$.
- **Edges ($E$):** An undirected unweighted edge connects string $u$ and string $v$ if and only if their Hamming distance is strictly 1:
  $$
  d_H(u, v) = \sum_{i=0}^7 \mathbf{1}[u[i] \ne v[i]] = 1
  $$
- Finding the minimum number of mutations is equivalent to finding the **shortest path in an unweighted graph**, for which Breadth-First Search (BFS) is optimal.

---

## 2. Conceptual Foundation & Invariants

### 1. BFS Shortest Path Invariant:
Let the BFS frontier be maintained via a FIFO queue $Q$.
- Nodes are visited in monotonically non-decreasing order of their distance from $startGene$:
  $$
  \text{depth}(u) \le \text{depth}(v) \quad \text{for all nodes dequeued before } v
  $$
- The first time the target string $endGene$ is extracted or discovered, the associated path length is guaranteed to be minimal.

### 2. Visited Set Invariant:
A hash set $vis$ records every gene string that has been enqueued:
- A node is inserted into $vis$ immediately upon being enqueued.
- This prevents cycle traps (e.g. $A \to B \to A$) and avoids redundant re-processing of already explored states.

> **Optimality Invariant.** Because every valid mutation step has uniform edge weight $w = 1$, BFS examines all paths of length $d$ before any path of length $d+1$. The first discovery of $endGene$ yields the global minimum mutation count.

---

## 3. Step-by-Step Worked Execution

We trace:
- $startGene = \text{"AACCGGTT"}$
- $endGene = \text{"AAACGGTA"}$
- $bank = [\text{"AACCGGTA"}, \text{"AACCGCTA"}, \text{"AAACGGTA"}]$

---

### Step 1: Initialization
- Queue: $Q = [(\text{"AACCGGTT"}, 0)]$.
- Visited: $vis = \{\text{"AACCGGTT"}\}$.

---

### Step 2: Expand Frontier Level 0
- Pop front: $gene = \text{"AACCGGTT"}, depth = 0$.
- Test against all candidates in $bank$:
  1. Candidate 1: `"AACCGGTA"`
     - Differing indices: index 7 ($T \ne A$).
     - Total differences: $d_H = 1$.
     - Is `"AACCGGTA"` in $vis$? No.
     - Enqueue: $Q.\text{append}((\text{"AACCGGTA"}, 1))$.
     - Add to visited: $vis.\text{add}(\text{"AACCGGTA"})$.
  2. Candidate 2: `"AACCGCTA"`
     - Differing indices: index 5 ($G \ne C$) and index 7 ($T \ne A$).
     - Total differences: $d_H = 2 \ne 1$. Rejected.
  3. Candidate 3: `"AAACGGTA"`
     - Differing indices: index 2 ($C \ne A$) and index 7 ($T \ne A$).
     - Total differences: $d_H = 2 \ne 1$. Rejected.
- Frontier level 0 complete.
- Queue state: $Q = [(\text{"AACCGGTA"}, 1)]$.

---

### Step 3: Expand Frontier Level 1
- Pop front: $gene = \text{"AACCGGTA"}, depth = 1$.
- Check if $gene == endGene$: $\text{"AACCGGTA"} \ne \text{"AAACGGTA"}$.
- Test against all candidates in $bank$:
  1. Candidate 1: `"AACCGGTA"` $\implies$ already in $vis$.
  2. Candidate 2: `"AACCGCTA"`
     - Differing indices: index 5 ($G \ne C$).
     - Total differences: $d_H = 1$.
     - Enqueue: $Q.\text{append}((\text{"AACCGCTA"}, 2))$.
     - Add to visited: $vis.\text{add}(\text{"AACCGCTA"})$.
  3. Candidate 3: `"AAACGGTA"`
     - Differing indices: index 2 ($C \ne A$).
     - Total differences: $d_H = 1$.
     - Target match detected: `"AAACGGTA" == endGene`!
     - Depth of target is $depth + 1 = 1 + 1 = \mathbf{2}$.
- Terminate and return **`2`**.

---

## 4. Complete Execution Trace

| Step | Active Gene | Depth | Candidate Evaluated | Hamming Distance $d_H$ | In Bank? | Visited? | Action / State Change |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **0** | Init | $0$ | — | — | — | — | Enqueue $(\text{"AACCGGTT"}, 0)$ |
| **1** | `"AACCGGTT"` | $0$ | `"AACCGGTA"` | $1$ | Yes | No | **Enqueue $(\text{"AACCGGTA"}, 1)$** |
| **1** | `"AACCGGTT"` | $0$ | `"AACCGCTA"` | $2$ | Yes | No | Skip ($d_H \ne 1$) |
| **1** | `"AACCGGTT"` | $0$ | `"AAACGGTA"` | $2$ | Yes | No | Skip ($d_H \ne 1$) |
| **2** | `"AACCGGTA"` | $1$ | `"AACCGGTA"` | $0$ | Yes | Yes | Skip (Already visited) |
| **2** | `"AACCGGTA"` | $1$ | `"AACCGCTA"` | $1$ | Yes | No | Enqueue $(\text{"AACCGCTA"}, 2)$ |
| **2** | `"AACCGGTA"` | $1$ | `"AAACGGTA"` | $1$ | Yes | No | **Target Reached! Output: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **Target Disconnected from Bank:** If no path of valid mutations connects $startGene$ to $endGene$, the queue eventually empties without finding $endGene$. Emits `-1`.
- **Target Not in Bank ($endGene \notin bank$):** Even if a 1-step mutation from $startGene$ produces $endGene$, the problem statement requires intermediate and destination genes to be registered in $bank$. If $endGene \notin bank$, returns `-1`.
- **Start Gene Equals End Gene:** $startGene == endGene \implies 0$ mutations needed.
- **Empty Bank ($bank = []$):** No mutations can be made $\implies$ returns `-1`.

---

## 6. Traps & Common Anti-Patterns

- **Depth-First Search (DFS) Without Distance Pruning:** Using standard DFS can find non-optimal long paths and requires full state exploration to guarantee the minimum. BFS naturally finds the shortest path on first encounter.
- **Forgetting to Mark Visited on Enqueue:** Delaying the addition of a node to `vis` until it is *popped* from the queue allows identical neighbors to be enqueued multiple times, causing exponential duplicate expansions. Adding to `vis` at enqueue time ensures each state enters the queue at most once.
- **Character Slicing vs Bank Scan:** When $|bank|$ is small ($\le 100$), comparing against all bank elements takes $8 \times |bank| \approx 800$ checks. Generating all $8 \times 3 = 24$ mutations and looking up in a hash set is also $O(L \cdot |\Sigma|)$. Both methods operate in under 2 ms.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $B = |bank|$ be the number of genes in the bank, and $L = 8$ be the constant gene length.
  - In the worst case, every bank gene is enqueued once.
  - Expanding a node tests Hamming distance against at most $B$ candidates in $O(L)$ time each.
  - Total Time: $\mathcal{O}(B^2 \cdot L)$. For $B \le 100$, $100^2 \times 8 = 8 \times 10^4$ operations, completing in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - The queue and visited set store at most $B + 1$ gene strings of length $8$.
  - Total Auxiliary Space: $\mathcal{O}(B \cdot L) = \mathcal{O}(B)$.
