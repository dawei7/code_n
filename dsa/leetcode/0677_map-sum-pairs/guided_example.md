# Guided Example: Map Sum Pairs

We trace the step-by-step prefix tree (Trie) node weight augmentation, differential delta update calculation ($\Delta = val_{new} - val_{old}$), prefix path value propagation ($node.val \leftarrow node.val + \Delta$), existing key overwrite handling ($d[key] = val$), and $\mathcal{O}(P)$ instant prefix sum retrieval on representative string-value query operations:

- **Input:**
  - Operation sequence:
    ```text
    MapSum mapSum = new MapSum();
    mapSum.insert("apple", 3);
    mapSum.sum("ap");           // return 3
    mapSum.insert("app", 2);
    mapSum.sum("ap");           // return 5
    ```
- **Required outputs:** `[null, null, 3, null, 5]`
  - MapSum behavior:
    - `insert(key, val)`: Binds $key$ to integer $val$. If $key$ already exists, its value is overridden.
    - `sum(prefix)`: Returns the sum of values of all keys that begin with $prefix$.
    - Performance requirement: Querying prefix sums must run in time proportional only to the length of the prefix ($\mathcal{O}(|prefix|)$), without scanning all dictionary words.
- **Trie Path Weighting & Differential Delta Invariant:**
  - **Subtree Sum Pre-accumulation:**
    - Each node in the Trie maintains a field `node.val` representing the **sum of all values** belonging to completed keys that pass through or terminate at this node.
    - If a prefix node exists, its `node.val` directly answers the sum query in $\mathcal{O}(1)$ additional time after walking the prefix!
  - **The Differential Delta ($\Delta$):**
    - A simple addition $node.val \leftarrow node.val + val$ fails when an existing key is updated with a new value (double-counting the old value).
    - To support seamless overwrites:
      - Maintain a hash map $d$ storing the latest value of each key ($d[key]$).
      - When inserting $(key, val)$, compute the net difference:
        $$
        \Delta = val - d[key]
        $$
      - If $key$ is new, $d[key] = 0 \implies \Delta = val$.
      - If $key$ was previously $3$ and is updated to $5$, $\Delta = 5 - 3 = +2$.
      - If $key$ was previously $5$ and is updated to $2$, $\Delta = 2 - 5 = -3$.
      - Update map: $d[key] \leftarrow val$.
      - Walk the Trie path for $key$, incrementing every node by $\Delta$:
        $$
        node.val \leftarrow node.val + \Delta
        $$
- **Step-by-Step Worked Execution Trace:**
  - Initialize empty Trie with root value $0$, and empty map $d = \{\}$.
  - **Operation 1: `insert("apple", 3)`:**
    - Key is new: $d[\text{"apple"}] = 0$.
    - Calculate delta:
      $$
      \Delta = 3 - 0 = \mathbf{+3}
      $$
    - Update dictionary: $d[\text{"apple"}] = 3$.
    - Propagate $+3$ down the Trie path `'a' \to 'p' \to 'p' \to 'l' \to 'e'`:
      - Node `'a'`: $val = 0 + 3 = \mathbf{3}$
      - Node `'p'` (1st): $val = 0 + 3 = \mathbf{3}$
      - Node `'p'` (2nd): $val = 0 + 3 = \mathbf{3}$
      - Node `'l'`: $val = 0 + 3 = \mathbf{3}$
      - Node `'e'`: $val = 0 + 3 = \mathbf{3}$
  - **Operation 2: `sum("ap")`:**
    - Prefix: `"ap"`.
    - Walk down Trie along characters:
      - Step 1: Follow link to `'a'`.
      - Step 2: Follow link to `'p'` (1st `'p'`).
    - We have reached the terminal node of prefix `"ap"`.
    - Read precomputed node value:
      $$
      node.val = \mathbf{3}
      $$
    - Return **`3`**.
  - **Operation 3: `insert("app", 2)`:**
    - Key is new: $d[\text{"app"}] = 0$.
    - Calculate delta:
      $$
      \Delta = 2 - 0 = \mathbf{+2}
      $$
    - Update dictionary: $d[\text{"app"}] = 2$.
    - Propagate $+2$ down the path `'a' \to 'p' \to 'p'`:
      - Node `'a'`: $val \leftarrow 3 + 2 = \mathbf{5}$
      - Node `'p'` (1st): $val \leftarrow 3 + 2 = \mathbf{5}$
      - Node `'p'` (2nd): $val \leftarrow 3 + 2 = \mathbf{5}$
    - Notice: Nodes `'l'` and `'e'` under `"apple"` remain unaffected ($val = 3$).
  - **Operation 4: `sum("ap")`:**
    - Prefix: `"ap"`.
    - Walk down Trie to first `'p'`:
      - Root $\to$ `'a'` $\to$ `'p'`.
    - Read node value:
      $$
      node.val = \mathbf{5}
      $$
    - Explanation: Both `"apple"` (value 3) and `"app"` (value 2) share the prefix `"ap"`. Their combined sum is $3 + 2 = \mathbf{5}$.
    - Return **`5`**.
- **Value Overwrite Scenario (`insert("apple", 5)`):**
    - $d[\text{"apple"}]$ was $3$.
    - Delta: $\Delta = 5 - 3 = \mathbf{+2}$.
    - $d[\text{"apple"}]$ updated to $5$.
    - Path `'a' \to 'p' \to 'p' \to 'l' \to 'e'` each increments by $+2$.
    - Node for `"ap"` increases from $5$ to $5 + 2 = \mathbf{7}$ (sum of `"apple"`=5 and `"app"`=2).
- **Non-Existent Prefix Query (`sum("xyz")`):**
    - Traversal from root fails on first character `'x'` (child link is `null`).
    - Prefix does not exist $\implies$ Returns **`0`**.

This instance demonstrates augmented retrieval trees and telescopic differential updates, mathematically proves why prefix node values maintain exact subtree weight sums under key value overwrites, and derives $O(L)$ insertion time, $O(P)$ prefix query time, and $O(N \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement `MapSum`:
- `insert(key, val)`: Sets `key` to `val`, overriding previous values.
- `sum(prefix)`: Returns the sum of values of all keys starting with `prefix`.

```text
1. insert("apple", 3):
   Trie path: 'a'(3) -> 'p'(3) -> 'p'(3) -> 'l'(3) -> 'e'(3)

2. sum("ap"):
   Walk to 'p': returns 3

3. insert("app", 2):
   Delta = 2 - 0 = +2
   Trie path: 'a'(3+2=5) -> 'p'(3+2=5) -> 'p'(3+2=5)

4. sum("ap"):
   Walk to 'p': returns 5 (sum of "apple"=3 and "app"=2)
```

### The Invariant of the Differential Delta Update
- To support overrides without retraversing subtrees, track each key's previous value in a dictionary $d$.
- The update weight added to each node along the path is strictly:
  $$
  \Delta = val_{new} - d[key]
  $$
- This correctly handles new keys ($\Delta = val$), increases ($\Delta > 0$), and decreases ($\Delta < 0$).

---

## 2. Conceptual Foundation & Invariants

### 1. The Delta Formula:
$$
\Delta = val - d[key]
$$
$$
d[key] \leftarrow val
$$
For each node $u$ along path $key$:
$$
u.val \leftarrow u.val + \Delta
$$

### 2. The Prefix Query:
Walk Trie along characters of $prefix$:
- If link missing: return $0$.
- At final prefix node $u_{prefix}$: return $u_{prefix}.val$.

> **Subtree Mass Conservation Invariant.** In an augmented prefix tree, the invariant $u.val = \sum_{w \in \mathcal{L}(u)} d[w]$ holds for all nodes $u$ under any sequence of key additions, updates, or deletions via pathwise delta propagation.

---

## 3. Step-by-Step Worked Execution

We trace the sample operations:

---

### Step 1: `insert("apple", 3)`
- $\Delta = 3 - 0 = 3$.
- Path `'a' \to 'p' \to 'p' \to 'l' \to 'e'` gets $+3$.

---

### Step 2: `sum("ap")`
- Walk to `'a'`, then `'p'`.
- Return $node.val = \mathbf{3}$.

---

### Step 3: `insert("app", 2)`
- $\Delta = 2 - 0 = 2$.
- Path `'a' \to 'p' \to 'p'` gets $+2$.
- First `'p'` becomes $3 + 2 = 5$.

---

### Step 4: `sum("ap")`
- Walk to first `'p'`.
- Return $node.val = \mathbf{5}$.

---

## 4. Complete Execution Trace

| Step | Operation | Key / Prefix | Delta $\Delta$ | Node Reached | Node Value Read / Set | Output |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `insert` | `"apple", 3` | $+3$ | Path to `'e'` | All $+3$ | `null` |
| $2$ | `sum` | `"ap"` | — | First `'p'` | Read $3$ | **`3`** |
| $3$ | `insert` | `"app", 2` | $+2$ | Path to 2nd `'p'` | First `'p'` $\to 5$ | `null` |
| **$4$** | **`sum`** | **`"ap"`** | — | **First `'p'`** | **Read `5`** | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **Overriding Same Key (`insert("apple", 3)` then `insert("apple", 3)`):** $\Delta = 3 - 3 = 0 \implies$ node values unchanged.
- **Reducing Key Value (`insert("apple", 1)`):** $\Delta = 1 - 3 = -2 \implies$ cleanly decrements path sums by 2.
- **Prefix Equals Full Key:** Returns that key's value plus any keys that extend it.
- **Non-Existent Prefix:** Safely returns 0 when child link is null.

---

## 6. Traps & Common Anti-Patterns

- **Searching Subtrees on Every `sum` Query ($O(N \cdot L)$):** Performing a DFS over the prefix subtree at each query is slow when many words share the prefix. Pre-accumulating sums on insertion makes queries strictly $O(|prefix|)$.
- **Forgetting Key Overwrite Tracking:** Simply adding $val$ without subtracting $d[key]$ causes double-counting when a key is updated.
- **Linear Scan of Map:** Checking `key.startswith(prefix)` over all dictionary keys takes $O(N \cdot L)$ per query; Trie lookups take $O(|prefix|)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `insert(key, val)`: Walks path of length $L_k \implies \mathcal{O}(L_k)$.
  - `sum(prefix)`: Walks path of length $L_p \implies \mathcal{O}(L_p)$.
  - Both operations are strictly proportional to string length, independent of the number of dictionary entries $N$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\Sigma \cdot \sum L_k)$ for the Trie nodes and hash map.
