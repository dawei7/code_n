# Guided Example: Alien Dictionary

We trace the step-by-step lexicographical mismatch edge extraction, prefix violation invalidation, directed acyclic graph (DAG) construction, and Kahn's BFS topological sort on representative alien language dictionary instances:

- **Input:** $\text{words} = [\text{"wrt"}, \text{"wrf"}, \text{"er"}, \text{"ett"}, \text{"rftt"}]$
- **Required output:** `"wertf"` (The unique topological ordering of all 5 observed alphabet characters: $w < e < r < t < f$)
- **Direct Cycle Contradiction:** $\text{words} = [\text{"z"}, \text{"x"}, \text{"z"}] \implies \text{""}$ ($z < x$ and $x < z$ form a 2-cycle; no linear ordering exists)
- **Prefix Violation Instance:** $\text{words} = [\text{"abc"}, \text{"ab"}] \implies \text{""}$ (A longer word cannot appear before its proper prefix in any valid lexicographical order)
- **Two-Letter Alphabet:** $\text{words} = [\text{"z"}, \text{"x"}] \implies \text{"zx"}$

This instance demonstrates modeling lexicographical precedence relations as a directed graph, explains why only the first mismatching character between adjacent words produces a valid ordering edge, shows how Kahn's algorithm detects cycles via processed node count verification, and details the prefix corruption trap.

---

## 1. Instance & Teaching Goal

Given a list of words sorted according to an unknown alien alphabet:
$$
\text{words} = [\text{"wrt"}, \text{"wrf"}, \text{"er"}, \text{"ett"}, \text{"rftt"}]
$$
Deduce the order of characters in the alien language. If inconsistent or cyclical, return `""`.

### Lexicographical Comparison Rules
To establish which letter comes before another in a dictionary:
1. Words are compared **left-to-right**.
2. If two words share a common prefix, the **first character that differs** establishes the relative order between those two letters:
   - For `"wrt"` and `"wrf"`: `w == w`, `r == r`, but `t != f`.
   - Because `"wrt"` appears before `"wrf"`, the alien alphabet must have $\mathbf{t < f}$!
   - All subsequent characters after the first mismatch are **completely unconstrained** by this word pair.
3. **The Prefix Violation:** If word $A$ is a prefix of word $B$ and $A$ is longer than $B$ (e.g. `"abc"` before `"ab"`), the dictionary is mathematically invalid, because a prefix must always precede its extension.

We translate these precedence pairs into directed edges $u \to v$ and compute the **topological sort** of the graph.

---

## 2. Conceptual Foundation & Invariants

### 1. Graph Formulation
- **Vertices ($V$):** Every distinct character present across all words in `words`.
- **Directed Edges ($E$):** An edge $u \to v$ indicates letter $u$ must appear before letter $v$ in the alphabet.
- **In-Degree Table:** $\text{indegree}[c]$ tracks the number of immediate predecessors of character $c$.

### 2. Edge Extraction Algorithm
For each adjacent pair of words $(w_i, w_{i+1})$:
- Find the minimum length $L = \min(\text{len}(w_i), \text{len}(w_{i+1}))$.
- Scan index $j$ from $0$ to $L - 1$:
  - If $w_i[j] \ne w_{i+1}[j]$:
    Add directed edge $w_i[j] \to w_{i+1}[j]$.
    Increment $\text{indegree}[w_{i+1}[j]]$ (if edge is new).
    **Break immediately** (do not inspect later indices).
- If no mismatch was found and $\text{len}(w_i) > \text{len}(w_{i+1})$:
  $$
  \text{return "" } \quad (\text{Invalid prefix order})
  $$

### 3. Kahn's BFS Topological Sort Protocol
1. Initialize queue $Q$ with all characters having $\text{indegree}[c] == 0$.
2. While $Q$ is not empty:
   - Dequeue $u$, append $u$ to result string.
   - For each neighbor $v$ of $u$:
     - Decrement $\text{indegree}[v] \leftarrow \text{indegree}[v] - 1$.
     - If $\text{indegree}[v] == 0$: enqueue $v$.
3. **Cycle Verification:**
   - If $\text{len}(\text{result}) == |V|$: All characters ordered successfully $\implies \text{return result}$.
   - If $\text{len}(\text{result}) < |V|$: A directed cycle prevented some vertices from reaching in-degree 0 $\implies \text{return ""}$.

> **Invariant.** Vertices enter queue $Q$ if and only if all their incoming dependency edges have been satisfied. If the graph is an acyclic DAG, every vertex is eventually dequeued.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{words} = [\text{"wrt"}, \text{"wrf"}, \text{"er"}, \text{"ett"}, \text{"rftt"}]$:

### Step 1: Initialize Vertices
Collect all unique characters:
$$
V = \{w, r, t, f, e\} \quad (|V| = 5)
$$
Initialize:
$$
\text{indegree} = \{w: 0, \; r: 0, \; t: 0, \; f: 0, \; e: 0\}
$$
Adjacency lists: $\{w: [], \; r: [], \; t: [], \; f: [], \; e: []\}$.

---

### Step 2: Compare Adjacent Word Pairs

- **Pair 1: `"wrt"` vs `"wrf"`**
  - Index 0: `'w' == 'w'`
  - Index 1: `'r' == 'r'`
  - Index 2: `'t' != 'f'` $\implies$ Add edge: $\mathbf{t \to f}$.
  - Update: $\text{adj}[t].\text{append}(f), \quad \text{indegree}[f] \leftarrow 1$.

- **Pair 2: `"wrf"` vs `"er"`**
  - Index 0: `'w' != 'e'` $\implies$ Add edge: $\mathbf{w \to e}$.
  - Update: $\text{adj}[w].\text{append}(e), \quad \text{indegree}[e] \leftarrow 1$.

- **Pair 3: `"er"` vs `"ett"`**
  - Index 0: `'e' == 'e'`
  - Index 1: `'r' != 't'` $\implies$ Add edge: $\mathbf{r \to t}$.
  - Update: $\text{adj}[r].\text{append}(t), \quad \text{indegree}[t] \leftarrow 1$.

- **Pair 4: `"ett"` vs `"rftt"`**
  - Index 0: `'e' != 'r'` $\implies$ Add edge: $\mathbf{e \to r}$.
  - Update: $\text{adj}[e].\text{append}(r), \quad \text{indegree}[r] \leftarrow 1$.

### Summary of Extracted Graph
- Edges: $w \to e, \quad e \to r, \quad r \to t, \quad t \to f$.
- In-degrees:
  - $w: 0$
  - $e: 1$
  - $r: 1$
  - $t: 1$
  - $f: 1$

---

### Step 3: Kahn's BFS Topological Sort
- Initial Queue ($Q$ containing nodes with $\text{indegree} == 0$):
  $$
  Q = [w]
  $$
  $\text{result} = []$.

- **Iteration 1:**
  - Dequeue $w \implies \text{result} = [\text{'w'}]$.
  - Neighbors of $w$: $[e]$.
  - Decrement $\text{indegree}[e]: 1 - 1 = 0 \implies \text{Enqueue } e$.
  - State: $Q = [e]$.

- **Iteration 2:**
  - Dequeue $e \implies \text{result} = [\text{'w'}, \text{'e'}]$.
  - Neighbors of $e$: $[r]$.
  - Decrement $\text{indegree}[r]: 1 - 1 = 0 \implies \text{Enqueue } r$.
  - State: $Q = [r]$.

- **Iteration 3:**
  - Dequeue $r \implies \text{result} = [\text{'w'}, \text{'e'}, \text{'r'}]$.
  - Neighbors of $r$: $[t]$.
  - Decrement $\text{indegree}[t]: 1 - 1 = 0 \implies \text{Enqueue } t$.
  - State: $Q = [t]$.

- **Iteration 4:**
  - Dequeue $t \implies \text{result} = [\text{'w'}, \text{'e'}, \text{'r'}, \text{'t'}]$.
  - Neighbors of $t$: $[f]$.
  - Decrement $\text{indegree}[f]: 1 - 1 = 0 \implies \text{Enqueue } f$.
  - State: $Q = [f]$.

- **Iteration 5:**
  - Dequeue $f \implies \text{result} = [\text{'w'}, \text{'e'}, \text{'r'}, \text{'t'}, \text{'f'}]$.
  - Neighbors of $f$: None.
  - State: $Q = []$.

Queue empty!
Check length: $\text{len}(\text{result}) = 5 == |V| = 5$.
Topological sort is complete and valid:
$$
\mathbf{\text{"wertf"}}
$$

---

## 4. Complete Execution Trace

```text
Words: ["wrt", "wrf", "er", "ett", "rftt"]
Unique Characters: {'w', 'r', 't', 'f', 'e'}

Edge Extraction:
  wrt vs wrf  -> t -> f
  wrf vs er   -> w -> e
  er  vs ett  -> r -> t
  ett vs rftt -> e -> r

Topology: w -> e -> r -> t -> f
Indegrees: {w: 0, e: 1, r: 1, t: 1, f: 1}

Kahn BFS:
  Pop w -> Indegree e becomes 0 -> Queue: [e]
  Pop e -> Indegree r becomes 0 -> Queue: [r]
  Pop r -> Indegree t becomes 0 -> Queue: [t]
  Pop t -> Indegree f becomes 0 -> Queue: [f]
  Pop f -> Queue empty

Final Order: "wertf"
```

| Adjacent Pair | First Mismatch | Added Directed Edge | In-Degree State After Edge |
|:---|:---:|:---:|:---|
| Initial | - | - | $w: 0, \; e: 0, \; r: 0, \; t: 0, \; f: 0$ |
| `"wrt"` vs `"wrf"` | `'t'` vs `'f'` | $t \to f$ | $f: 1$ |
| `"wrf"` vs `"er"` | `'w'` vs `'e'` | $w \to e$ | $e: 1$ |
| `"er"` vs `"ett"` | `'r'` vs `'t'` | $r \to t$ | $t: 1$ |
| `"ett"` vs `"rftt"` | `'e'` vs `'r'` | $e \to r$ | $r: 1$ |

| Step | Dequeued Vertex | Neighbors Processed | In-Degree Decrements | Enqueued Vertices | Running Result |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $w$ | $[e]$ | $\text{indegree}[e]: 1 \to 0$ | $e$ | `"w"` |
| 2 | $e$ | $[r]$ | $\text{indegree}[r]: 1 \to 0$ | $r$ | `"we"` |
| 3 | $r$ | $[t]$ | $\text{indegree}[t]: 1 \to 0$ | $t$ | `"wer"` |
| 4 | $t$ | $[f]$ | $\text{indegree}[f]: 1 \to 0$ | $f$ | `"wert"` |
| 5 | $f$ | None | None | None | **`"wertf"`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every directed edge $u \to v$ corresponds to an observed adjacent lexicographical precedence $w_i < w_{i+1}$ where $u = w_i[j]$ and $v = w_{i+1}[j]$. Kahn's algorithm outputs vertices in an order where every prerequisite is placed before its successors. Thus, every lexicographical condition is satisfied.

**Completeness.** By graph theory, a directed graph admits a topological sort if and only if it contains no directed cycles. If a cycle exists (e.g. $A \to B \to A$), Kahn's algorithm terminates with unprocessed nodes whose in-degrees remain $\ge 1$, correctly triggering the cycle guard $\text{len}(\text{result}) < |V|$ to return `""`.

---

## 6. Traps This Instance Exposes

- **Extracting Edges Past the First Mismatch:** In `"wrt"` vs `"wrf"`, the first mismatch is `t != f`. One must NOT add edges between subsequent characters. Later characters do not indicate precedence once an earlier character differs.
- **The Prefix Invalidation Trap:** For `words = ["abc", "ab"]`, all characters of `"ab"` match the prefix of `"abc"`, but `"abc"` appears first. Since `"abc"` is strictly longer than `"ab"`, this violates lexicographical ordering. The code must detect `len(w1) > len(w2)` when no mismatch occurs and return `""`.
- **Isolated Characters with Zero Constraints:** A character appearing in words that never mismatches (e.g. single-letter words or shared characters with no differences) has $\text{indegree} = 0$. It must still be included in the output string in any valid position.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C + V + E)$, where $C$ is the total number of characters across all words in `words`, $V \le 26$ is the number of unique letters in the alien alphabet, and $E \le V^2 \le 26^2$ is the number of precedence edges. Extracting edges takes $O(C)$ time. Kahn's BFS visits each vertex and edge once in $O(V + E) = O(1)$ time relative to fixed alphabet size. Total runtime is strictly linear $O(C)$ in the input text size.
- **Auxiliary Space Complexity:** $O(V + E) = O(1)$ auxiliary memory for the adjacency graph and in-degree table over the 26 lowercase English letters.
