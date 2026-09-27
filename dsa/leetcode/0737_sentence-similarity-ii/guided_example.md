# Guided Example: Sentence Similarity II

We trace the step-by-step word-to-index mapping ($words[w] = idx$), Disjoint Set Union (Union-Find) connected component construction on word graphs ($find(u) == find(v)$), equivalence relation transitive closure ($\sim^*$), sentence length validation, aligned word pair equivalence testing, and multi-hop synonym verification on representative sentence pairs:

- **Input:**
  $$
  sentence_1 = [\text{"great"}, \; \text{"acting"}, \; \text{"skills"}]
  $$
  $$
  sentence_2 = [\text{"fine"}, \; \text{"drama"}, \; \text{"talent"}]
  $$
  $$
  similarPairs = [[\text{"great"}, \text{"good"}], \; [\text{"fine"}, \text{"good"}], \; [\text{"drama"}, \text{"acting"}], \; [\text{"skills"}, \text{"talent"}]]
  $$
- **Required output:** `true`
  - Similarity criteria (Equivalence Relation):
    - Sentences must have identical length ($|sentence_1| == |sentence_2|$).
    - Words at each aligned position $i$ must be similar under the full equivalence relation:
      1. **Reflexive:** $w \sim w$ (any word is similar to itself).
      2. **Symmetric:** $x \sim y \iff y \sim x$.
      3. **Transitive (Key Difference from Similarity I):** If $x \sim y$ and $y \sim z$, then $x \sim z$.
    - For the input:
      - At index 0: `"great"` is paired with `"good"`, and `"fine"` is paired with `"good"`.
        - Via the intermediate pivot `"good"`, `"great"` and `"fine"` are **transitively similar**!
      - At index 1: `"acting"` is directly paired with `"drama"`.
      - At index 2: `"skills"` is directly paired with `"talent"`.
      - All positions hold valid equivalence relations $\implies$ output is **`true`**.
- **Equivalence Class Clustering via Union-Find Invariant:**
  - **The Graph Formulation:**
    - Words represent vertices in an undirected graph.
    - Each pair in $similarPairs$ adds an undirected edge $(u, v)$.
    - The transitive closure of similarity is identical to the **connected components** of this graph:
      $$
      w_1 \sim^* w_2 \iff w_1 \text{ and } w_2 \text{ belong to the same connected component}
      $$
  - **Disjoint Set Union (DSU):**
    - Assign each unique word a discrete integer identifier $0, 1, \dots, V - 1$.
    - For each pair $[a, b] \in similarPairs$:
      $$
      uf.union(words[a], \; words[b])
      $$
  - **Pair Evaluation Predicate:**
    - For each aligned pair $(w_1, w_2) = (sentence_1[i], sentence_2[i])$:
      1. If $w_1 == w_2$: trivially similar by reflexivity $\implies$ Pass.
      2. If $w_1 \notin words$ or $w_2 \notin words$: at least one word has no registered relations and is not identical to the other $\implies$ Fail (`return false`).
      3. If $uf.find(words[w_1]) == uf.find(words[w_2])$: both words share the same component root $\implies$ Pass.
      4. Otherwise: different components $\implies$ Fail (`return false`).
- **Step-by-Step Worked Execution Trace on the Transitive Example:**
  - **Phase 0: Length Check:**
    $$
    |sentence_1| = 3, \quad |sentence_2| = 3 \quad \mathbf{(Valid)}
    $$
  - **Phase 1: Build Word Index & DSU Components:**
    - Register words:
      - `"great"` $\to 0$
      - `"good"` $\to 1$
      - `"fine"` $\to 2$
      - `"drama"` $\to 3$
      - `"acting"` $\to 4$
      - `"skills"` $\to 5$
      - `"talent"` $\to 6$
    - Union pairs:
      1. Pair `["great", "good"]`:
         $$
         union(0, 1) \implies \text{Component: } \{ \text{"great"}, \text{"good"} \}
         $$
      2. Pair `["fine", "good"]`:
         $$
         union(2, 1) \implies \text{Component: } \{ \text{"great"}, \text{"good"}, \text{"fine"} \}
         $$
         *(Transitive bridge formed! Root of 0, 1, 2 is now unified)*
      3. Pair `["drama", "acting"]`:
         $$
         union(3, 4) \implies \text{Component: } \{ \text{"drama"}, \text{"acting"} \}
         $$
      4. Pair `["skills", "talent"]`:
         $$
         union(5, 6) \implies \text{Component: } \{ \text{"skills"}, \text{"talent"} \}
         $$
  - **Phase 2: Evaluate Aligned Word Pairs:**
    - **Position $i = 0$ ($w_1 = \text{"great"}, w_2 = \text{"fine"}$):**
      - $w_1 \ne w_2$.
      - Lookup roots in DSU:
        $$
        uf.find(words[\text{"great"}]) = uf.find(0) = \mathbf{1}
        $$
        $$
        uf.find(words[\text{"fine"}]) = uf.find(2) = \mathbf{1}
        $$
      - Both share root $1$!
      - $\text{"great"} \sim^* \text{"fine"}$ verified transitively. Valid!
    - **Position $i = 1$ ($w_1 = \text{"acting"}, w_2 = \text{"drama"}$):**
      - $w_1 \ne w_2$.
      - Lookup roots:
        $$
        uf.find(words[\text{"acting"}]) = uf.find(4) = \mathbf{4}
        $$
        $$
        uf.find(words[\text{"drama"}]) = uf.find(3) = \mathbf{4}
        $$
      - Both share root $4$. Valid!
    - **Position $i = 2$ ($w_1 = \text{"skills"}, w_2 = \text{"talent"}$):**
      - $w_1 \ne w_2$.
      - Lookup roots:
        $$
        uf.find(words[\text{"skills"}]) = uf.find(5) = \mathbf{6}
        $$
        $$
        uf.find(words[\text{"talent"}]) = uf.find(6) = \mathbf{6}
        $$
      - Both share root $6$. Valid!
  - **Phase 3: Final Output:**
    - All aligned positions validated.
    - Output:
      $$
      ans = \mathbf{true}
      $$
- **Unregistered Non-Identical Word Trace ($w_1 = \text{"apple"}, w_2 = \text{"banana"}$):**
  - Neither word is in $similarPairs$.
  - $w_1 \ne w_2 \implies$ returns **`false`**.
- **Identical Unregistered Words ($w_1 = \text{"the"}, w_2 = \text{"the"}$):**
  - Handled by reflexivity guard $sentence_1[i] == sentence_2[i]$ before DSU lookup.
  - Passes without requiring presence in $words$.

This instance demonstrates equivalence relation transitive closure computation and graph component partitioning using Disjoint Set Union, mathematically proves why path compression enables nearly constant-time transitive query evaluation, and derives $O((N + P) \alpha(P))$ runtime and $O(P)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two sentences and a list of word pairs:
Determine if they are **similar** under **transitive similarity**.
Transitivity means: if $A \sim B$ and $B \sim C$, then $A \sim C$.

```text
sentence1 = [ "great", "acting", "skills" ]
sentence2 = [ "fine",  "drama",  "talent" ]
pairs = [ ["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"] ]

i = 0: "great" ~ "good" and "fine" ~ "good" -> "great" ~ "fine" TRANSITIVELY!
i = 1: "acting" ~ "drama" DIRECTLY
i = 2: "skills" ~ "talent" DIRECTLY

All positions valid!
Result: true
```

### The Invariant of the Transitive Equivalence Class
- In Sentence Similarity II, similarity is an **equivalence relation** (reflexive, symmetric, and transitive).
- Using Union-Find, words in the same connected component share the exact same root: `find(w1) == find(w2)`.

---

## 2. Conceptual Foundation & Invariants

### 1. DSU Word Graph Clustering:
For each $[a, b] \in similarPairs$:
$$
uf.union(words[a], \; words[b])
$$

### 2. Transitive Positional Predicate:
$$
\text{similar}(w_1, w_2) \iff (w_1 == w_2) \ \lor \ (w_1, w_2 \in words \ \land \ uf.find(words[w_1]) == uf.find(words[w_2]))
$$

> **Transitive Closure Quotient Invariant.** The similarity equivalence relation $\sim^*$ is the reflexive-transitive-symmetric closure of the generator graph $G = (V, E)$, whose quotient set $V / \sim^*$ corresponds bijectively to the set of trees in the disjoint-set forest.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: DSU Construction
- Union `"great"` and `"good"` $\implies$ $\{great, good\}$.
- Union `"fine"` and `"good"` $\implies$ $\{great, good, fine\}$.
- Union `"drama"` and `"acting"` $\implies$ $\{drama, acting\}$.
- Union `"skills"` and `"talent"` $\implies$ $\{skills, talent\}$.

---

### Step 2: Compare Sentences
- Index 0: `find("great") == find("fine")` (Both root to good) $\implies$ Valid.
- Index 1: `find("acting") == find("drama")` $\implies$ Valid.
- Index 2: `find("skills") == find("talent")` $\implies$ Valid.

---

### Step 3: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Position $i$ | $sentence_1[i]$ | $sentence_2[i]$ | Direct Match? | DSU Root $w_1$ | DSU Root $w_2$ | Transitive Match? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `"great"` | `"fine"` | No | `good` (Root 1) | `good` (Root 1) | **Yes (Transitive)** |
| $1$ | `"acting"` | `"drama"` | No | `acting` (Root 4)| `acting` (Root 4)| **Yes (Direct)** |
| $2$ | `"skills"` | `"talent"` | No | `talent` (Root 6)| `talent` (Root 6)| **Yes (Direct)** |
| **Final** | — | — | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Different Length Sentences:** Fails immediately $\implies$ returns `false`.
- **Identical Words Not in Pairs:** Handled by $w_1 == w_2$ before dictionary lookup $\implies$ returns `true`.
- **Long Transitive Chains ($A \sim B \sim C \sim D \sim E$):** DSU path compression finds root in $O(\alpha(P))$ time.
- **Disjoint Equivalence Classes:** Different roots $\implies$ returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Using Direct Set Lookup from Similarity I:** Direct set lookup fails on transitive bridges like `"great"` and `"fine"`. DSU or BFS/DFS graph search is required.
- **Dictionary KeyErrors on Unseen Words:** If $w_1$ or $w_2$ never appeared in $similarPairs$, attempting `words[w1]` without checking throws a KeyError. Check `if w1 not in words or w2 not in words:` first.
- **Forgetting Identity Check ($w_1 == w_2$):** A word is always similar to itself, even if it never appears in $similarPairs$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building word index and executing $P$ union operations: $\mathcal{O}(P \alpha(P))$.
  - Querying $N$ word positions with find: $\mathcal{O}(N \alpha(P))$.
  - Total Time: nearly linear $\mathcal{O}((N + P) \alpha(P))$. Completes in $< 5$ ms for $N, P = 2000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(P)$ space for the word mapping dictionary and union-find parent array.
