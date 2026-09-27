# Guided Example: Implement Trie (Prefix Tree)

We trace the step-by-step 26-ary tree node creation, shared prefix path traversal, and terminal flag distinction on representative Trie string operations:

- **Sequential Operations:**
  1. `Trie()` (Initialize root node)
  2. `insert("apple")` (Creates path `a -> p -> p -> l -> e` with `is_end = true` at `'e'`)
  3. `search("apple")` $\implies \mathbf{true}$ (Full path exists and `is_end == true`)
  4. `search("app")` $\implies \mathbf{false}$ (Prefix exists, but `is_end == false` at `'p'`)
  5. `startsWith("app")` $\implies \mathbf{true}$ (Prefix path exists down to `'p'`)
  6. `insert("app")` (Reuses existing nodes `a -> p -> p` and marks `'p'` with `is_end = true`)
  7. `search("app")` $\implies \mathbf{true}$ (`is_end` is now true!)
- **Uninserted Search Instance:** `search("bat") \implies \text{false}` (Root has no child for `'b'`)

This instance demonstrates prefix tree data structures, proves why `search` and `startsWith` differ on the terminal boolean flag (`is_end`), illustrates prefix node sharing without duplicate allocations, and achieves strictly $O(L)$ runtime per operation where $L$ is query string length.

---

## 1. Instance & Teaching Goal

We trace the operational lifecycle of a Trie across a sequence of string mutations and queries:
```text
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // -> true
trie.search("app");     // -> false
trie.startsWith("app"); // -> true
trie.insert("app");
trie.search("app");     // -> true
```

### The Architectural Role of the Trie
In a standard hash set (`set`), searching for a complete word takes $O(L)$ time, but checking whether any stored word begins with prefix `"app"` requires an exhaustive $O(W \cdot L)$ scan across all $W$ stored words.
A **Trie (Prefix Tree)** organizes characters along tree edges:
- The root represents the empty string `""`.
- Each edge represents a character $c \in [a-z]$.
- Successive nodes represent prefix strings: `"" -> "a" -> "ap" -> "app" -> "appl" -> "apple"`.
- A boolean flag `is_end` differentiates **complete inserted words** from **intermediate prefix paths**.

Visualizing the Trie after inserting `"apple"` and `"app"`:
```text
         (root)
           | 'a'
          (a)
           | 'p'
          (p)
           | 'p'
          (p) [is_end = true]  <-- "app" ends here!
           | 'l'
          (l)
           | 'e'
          (e) [is_end = true]  <-- "apple" ends here!
```

---

## 2. Conceptual Foundation & Invariants

### Trie Node Structure
Each node contains:
1. `children`: an array of size 26 (or dictionary), where index $\text{ord}(c) - \text{ord}('a')$ references the child node for character $c$.
2. `is_end`: a boolean flag initialized to `false`.

### Core Operations:
1. **`insert(word)`:**
   Traverse from `root`. For each character $c$:
   - If `children[c]` does not exist, instantiate a new node.
   - Advance `curr = children[c]`.
   - After processing all $L$ characters, set `curr.is_end = true`.
2. **`search(word)`:**
   Traverse from `root`. For each character $c$:
   - If `children[c]` does not exist, return `false`.
   - Advance `curr = children[c]`.
   - Return `curr.is_end` *(must match a complete word!)*.
3. **`startsWith(prefix)`:**
   Traverse from `root`. For each character $c$:
   - If `children[c]` does not exist, return `false`.
   - Advance `curr = children[c]`.
   - Return `true` *(prefix path exists; `is_end` is irrelevant)*.

> **Invariant.** For any node at depth $d$, the sequence of edge characters from the root to that node represents a unique prefix of length $d$. `node.is_end == true` if and only if that exact prefix was explicitly inserted as a full word.

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence:

### Operation 1: `insert("apple")`
- Start at `root`.
- $c = \text{'a'}$: `children['a']` is null $\implies$ create Node(a). Advance to Node(a).
- $c = \text{'p'}$: `children['p']` is null $\implies$ create Node(p1). Advance to Node(p1).
- $c = \text{'p'}$: `children['p']` is null $\implies$ create Node(p2). Advance to Node(p2).
- $c = \text{'l'}$: `children['l']` is null $\implies$ create Node(l). Advance to Node(l).
- $c = \text{'e'}$: `children['e']` is null $\implies$ create Node(e). Advance to Node(e).
- Set `Node(e).is_end = true`.

---

### Operation 2: `search("apple")`
- Start at `root`.
- Traverse path: `root -> 'a' -> 'p' -> 'p' -> 'l' -> 'e'`.
- All nodes exist. Terminal node reached: Node(e).
- Check `Node(e).is_end`:
  $$
  \text{Node(e).is\_end} == \mathbf{true}
  $$
- Return `true`.

---

### Operation 3: `search("app")`
- Start at `root`.
- Traverse path: `root -> 'a' -> 'p' -> 'p'`.
- All nodes exist. Terminal node reached: Node(p2).
- Check `Node(p2).is_end`:
  $$
  \text{Node(p2).is\_end} == \mathbf{false}
  $$
- While `"app"` exists as a path prefix, it was not inserted as a complete word!
- Return `false`.

---

### Operation 4: `startsWith("app")`
- Start at `root`.
- Traverse path: `root -> 'a' -> 'p' -> 'p'`.
- All 3 characters exist along the path.
- In `startsWith`, the `is_end` flag is ignored!
- Return `true`.

---

### Operation 5: `insert("app")`
- Start at `root`.
- $c = \text{'a'}$: Node(a) already exists $\implies$ Reuse Node(a).
- $c = \text{'p'}$: Node(p1) already exists $\implies$ Reuse Node(p1).
- $c = \text{'p'}$: Node(p2) already exists $\implies$ Reuse Node(p2).
- Word completed. Set `Node(p2).is_end = true`.
- Zero new nodes created; existing prefix path updated!

---

### Operation 6: `search("app")`
- Start at `root`.
- Traverse to Node(p2).
- Check `Node(p2).is_end`:
  $$
  \text{Node(p2).is\_end} == \mathbf{true}
  $$
- Return `true`.

---

## 4. Complete Execution Trace

```text
1. insert("apple"):
   root -> 'a' -> 'p' -> 'p' -> 'l' -> 'e'*
   Created 5 nodes. 'e'* marked is_end=True.

2. search("apple"):
   Follow root->a->p->p->l->e*. Exists and is_end=True -> TRUE

3. search("app"):
   Follow root->a->p->p. Exists but is_end=False       -> FALSE

4. startsWith("app"):
   Follow root->a->p->p. Path exists                   -> TRUE

5. insert("app"):
   Follow existing root->a->p->p*. Mark is_end=True    -> OK

6. search("app"):
   Follow root->a->p->p*. Exists and is_end=True       -> TRUE
```

| Step | Operation Invoked | Argument | Traversed Node Path | Node Status at End of Path | Return Value |
|:---:|:---|:---:|:---|:---:|:---:|
| 1 | `insert` | `"apple"` | `root -> a -> p -> p -> l -> e` | Mark `is_end = true` | `null` |
| **2** | **`search`** | **`"apple"`** | `root -> a -> p -> p -> l -> e` | `is_end == true` | **`true`** |
| **3** | **`search`** | **`"app"`** | `root -> a -> p -> p` | `is_end == false` | **`false`** |
| **4** | **`startsWith`** | **`"app"`** | `root -> a -> p -> p` | Path found | **`true`** |
| 5 | `insert` | `"app"` | `root -> a -> p -> p` | Mark `is_end = true` | `null` |
| **6** | **`search`** | **`"app"`** | `root -> a -> p -> p` | `is_end == true` | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every character in an inserted word defines a unique edge in the 26-ary tree. A word $W$ is confirmed by `search` if and only if all $|W|$ edges exist and the final node's `is_end` flag is set. A prefix $P$ is confirmed by `startsWith` if and only if all $|P|$ edges exist from the root, regardless of whether a word terminates there.

**Completeness.** Traversal advances deterministically one character per step. Since character transitions are indexed by $\text{ord}(c) - \text{ord}('a')$, no valid path can be missed.

---

## 6. Traps This Instance Exposes

- **Confusing `search` and `startsWith`:** Returning `true` in `search` simply because the path exists causes `"app"` to return `true` before being inserted! `search` must verify `node.is_end == true`.
- **Duplicate Insertions:** Inserting `"apple"` multiple times must be idempotent. Traversing existing nodes without overwriting `is_end` to false ensures correct set semantics.
- **Fixed-Size Array vs Hash Map:** For lowercase English letters ($a-z$), an array of size 26 provides $O(1)$ direct indexing with lower pointer overhead than a hash table.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `insert(word)`: $O(L)$, where $L$ is the length of `word`. Exactly $L$ node transitions.
  - `search(word)`: $O(L)$ character comparisons.
  - `startsWith(prefix)`: $O(P)$, where $P$ is the length of `prefix`.
- **Auxiliary Space Complexity:** $O(\Sigma \cdot \sum L)$ in the worst case where no words share prefixes, where $\Sigma = 26$ is the alphabet size. Reusing common prefixes significantly reduces actual node allocations.
