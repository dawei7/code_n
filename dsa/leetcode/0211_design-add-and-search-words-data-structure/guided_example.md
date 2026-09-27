# Guided Example: Design Add and Search Words Data Structure

We trace the step-by-step Trie construction, literal prefix matching, and recursive wildcard branching on representative dictionary operations:

- **Sequential Operations:**
  1. `WordDictionary()` (Initialize root)
  2. `addWord("bad")` (Insert path `b -> a -> d*`)
  3. `addWord("dad")` (Insert path `d -> a -> d*`)
  4. `addWord("mad")` (Insert path `m -> a -> d*`)
  5. `search("pad")` $\implies \mathbf{false}$ (No child `'p'` at root)
  6. `search("bad")` $\implies \mathbf{true}$ (Exact literal match)
  7. `search(".ad")` $\implies \mathbf{true}$ (Wildcard `.` branches to `'b'`, `'d'`, `'m'`; matches `"bad"`)
  8. `search("b..")` $\implies \mathbf{true}$ (Wildcard `.` matches `'a'`, second `.` matches `'d'`)
- **Prefix Length Mismatch Instance:** $\text{search("ba")} \implies \text{false}$ (Prefix exists, but `is_end == false` at `'a'`)
- **Exhausted Dot Instance:** $\text{search("....")} \implies \text{false}$ (All inserted words have length 3)

This instance demonstrates Trie prefix trees augmented with wildcard search, proves why DFS backtracking is required for the dot (`.`) metacharacter, analyzes branching factor bounds ($26^d$), and runs in $O(L)$ for exact searches and $O(26^d \cdot L)$ for wildcard queries.

---

## 1. Instance & Teaching Goal

We trace the behavior of `WordDictionary`:
```text
WordDictionary wd = new WordDictionary();
wd.addWord("bad");
wd.addWord("dad");
wd.addWord("mad");
wd.search("pad"); // -> false
wd.search("bad"); // -> true
wd.search(".ad"); // -> true (matches "bad", "dad", "mad")
wd.search("b.."); // -> true (matches "bad")
```

### Why a Hash Set Is Inadequate for Wildcards
A standard hash table provides $O(L)$ exact lookups, but when given a pattern with wildcards such as `".ad"`:
- The `.` can represent any of the 26 lowercase English letters (`"aad"`, `"bad"`, $\dots$, `"zad"`).
- With 2 wildcards (e.g. `"b.."`), there are $26^2 = 676$ possible strings.
- Generating all replacements and probing a hash set causes redundant work.

A **Trie** structure naturally accommodates wildcard searches:
- For a literal letter (e.g. `'b'`), the search descends the single corresponding child edge.
- For a wildcard `.` (match any letter), the search branches across **all existing children** at the current node via depth-first search (DFS).
- If any branch successfully matches the remaining suffix, the search returns `true`.

---

## 2. Conceptual Foundation & Invariants

### Trie Node Specification
Each node maintains:
- `children`: an array of 26 pointers, where index $\text{ord}(c) - \text{ord}('a')$ maps to the child node for character $c$.
- `is_end`: boolean flag marking the termination of a complete word.

### DFS Search Algorithm with Wildcards
Define `dfs(node, i)` where `node` is the current Trie node and `i` is the index of the character in `word`:
1. **Base Case:**
   If $i == \text{len}(\text{word})$, return `node.is_end`.
2. **Branch 1: Literal Character ($word[i] \ne \text{'.'}`):**
   Let $k = \text{ord}(\text{word}[i]) - \text{ord}('a')$.
   If `node.children[k]` is null, return `false`.
   Return `dfs(node.children[k], i + 1)`.
3. **Branch 2: Wildcard Dot ($word[i] == \text{'.'}`):**
   Iterate through all 26 possible children of `node`:
   If `child` is not null and `dfs(child, i + 1)` is `true`:
     Return `true`.
   Return `false` (no child matches the remaining pattern).

> **Invariant.** `dfs(node, i)` returns `true` if and only if there exists at least one path starting at `node` that matches the suffix `word[i:]` and terminates at a node with `is_end == true`.

---

## 3. Step-by-Step Worked Execution

We trace the dictionary operations:

### Insert Phase: `addWord("bad")`, `addWord("dad")`, `addWord("mad")`
1. `addWord("bad")`: Root creates child `'b'` $\to$ child `'a'` $\to$ child `'d'` (`is_end = true`).
2. `addWord("dad")`: Root creates child `'d'` $\to$ child `'a'` $\to$ child `'d'` (`is_end = true`).
3. `addWord("mad")`: Root creates child `'m'` $\to$ child `'a'` $\to$ child `'d'` (`is_end = true`).

Trie graph:
```text
         (root)
        /  |  \
      'b' 'd' 'm'
       |   |   |
      'a' 'a' 'a'
       |   |   |
      'd'*'d'*'d'*  (* marks is_end = true)
```

---

### Query 1: `search("pad")`
- At `root`, check literal character `'p'`.
- Index $k = \text{ord}('p') - \text{ord}('a') = 15$.
- `root.children[15]` is null!
- Return $\mathbf{false}$.

---

### Query 2: `search("bad")`
- At `root`, character `'b'` exists $\implies$ descend to Node(b).
- At Node(b), character `'a'` exists $\implies$ descend to Node(a).
- At Node(a), character `'d'` exists $\implies$ descend to Node(d).
- Path ends. Check `Node(d).is_end`:
  $$
  \text{is\_end} == \mathbf{true}
  $$
- Return $\mathbf{true}$.

---

### Query 3: `search(".ad")` (Wildcard First Character)
- At `root`, character is `'.'`.
- Explore all non-null children of `root`:
  1. **Branch 'b':** Call `dfs(Node(b), 1)`.
     - Next char `'a'`: exists in Node(b) $\implies$ descend to Node(a).
     - Next char `'d'`: exists in Node(a) $\implies$ descend to Node(d).
     - At end: `Node(d).is_end == true` $\implies \mathbf{true!}$
- Since Branch `'b'` succeeded, short-circuit and return $\mathbf{true}$ immediately!

---

### Query 4: `search("b..")` (Consecutive Wildcards)
- At `root`, character `'b'` exists $\implies$ descend to Node(b).
- At Node(b), character is `'.'`:
  - Explore non-null children of Node(b): only `'a'` exists.
  - Call `dfs(Node(a), 2)`.
- At Node(a), character is `'.'`:
  - Explore non-null children of Node(a): only `'d'` exists.
  - Call `dfs(Node(d), 3)`.
- Index reaches length 3. Check `Node(d).is_end`:
  $$
  \text{is\_end} == \mathbf{true}
  $$
- Return $\mathbf{true}$.

---

## 4. Complete Execution Trace

```text
Trie: stores "bad", "dad", "mad"

1. search("pad"):
   root -> 'p' (null) -> FALSE

2. search("bad"):
   root -> 'b' -> 'a' -> 'd'* (is_end=True) -> TRUE

3. search(".ad"):
   root -> '.' branches:
     Branch 'b': 'b' -> 'a' -> 'd'* -> TRUE! (Short-circuit)

4. search("b.."):
   root -> 'b' -> '.' (Node 'a') -> '.' (Node 'd'*) -> TRUE!
```

| Operation | Query String | Traversal Path / Active Branch | Node Evaluated | Terminal Check | Result |
|:---:|:---:|:---|:---:|:---:|:---:|
| `search` | `"pad"` | Literal `'p'` from root | `root.children['p'] == null` | - | **`false`** |
| `search` | `"bad"` | `root -> b -> a -> d` | Node(d) | `is_end == true` | **`true`** |
| `search` | `".ad"` | Dot at root $\implies$ Branch `'b'` | `Node(b) -> a -> d` | `is_end == true` | **`true`** |
| `search` | `"b.."` | `root -> b -> . -> .` | `Node(b) -> a -> d` | `is_end == true` | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** For literal characters, the algorithm follows the unique deterministic edge. For `.` wildcards, it branches across all existing children. A match is returned if and only if there exists a valid sequence of character transitions of length $|\text{word}|$ that terminates at a node with `is_end == true`.

**Completeness.** DFS branching exhausts all available edges matching the wildcard. If any word in the dictionary matches the wildcard pattern, at least one recursive search branch will find it and return `true`.

---

## 6. Traps This Instance Exposes

- **Failing to Check `is_end`:** For pattern `"ba"`, all characters exist in the path `b -> a`, but `Node(a).is_end` is `false`. The search must verify that a complete word terminates at the end of the query.
- **Length Mismatch with Dots:** A pattern `"...."` has 4 dots. If words have length 3, the fourth dot reaches `null` children, correctly returning `false`.
- **Branching Factor:** While a wildcard theoretically branches up to 26 times, problem constraints specify at most 2 dots per query ($26^2 = 676$), ensuring that DFS recursion remains extremely fast.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `addWord(word)`: $O(L)$, where $L$ is the length of `word`.
  - `search(word)`: $O(L)$ for queries without dots; $O(26^d \cdot L)$ in the worst case for queries containing $d$ dots.
- **Auxiliary Space Complexity:** $O(L)$ auxiliary call stack memory for recursion depth, where $L \le 25$.
