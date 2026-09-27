# Guided Example: Serialize and Deserialize N-ary Tree

We trace the step-by-step preorder recursive tree serialization, explicit child-degree prefix encoding $(val, count)$, token-stream state tracking, and deterministic structural tree reconstruction on representative $N$-ary hierarchies:

- **Input:** $N$-ary tree with root $1$, children $3, 2, 4$, where node $3$ has children $5, 6$:
  ```text
        1
      / | \
     3  2  4
    / \
   5   6
  ```
- **Required output:** Identical reconstructed $N$-ary tree object:
  - Serialized token stream:
    $$
    \text{"1 3 3 2 5 0 6 0 2 0 4 0"}
    $$
  - Encoding trace:
    - Node $1$: value $1$, $3$ children $\implies \text{"1 3"}$
    - Node $3$: value $3$, $2$ children $\implies \text{"3 2"}$
    - Node $5$: value $5$, $0$ children $\implies \text{"5 0"}$
    - Node $6$: value $6$, $0$ children $\implies \text{"6 0"}$
    - Node $2$: value $2$, $0$ children $\implies \text{"2 0"}$
    - Node $4$: value $4$, $0$ children $\implies \text{"4 0"}$
  - Decoding trace:
    - Read $(1, 3)$: instantiate root $1$, recursively parse $3$ children
    - Read $(3, 2)$: instantiate node $3$, recursively parse $2$ children
    - Read $(5, 0)$: instantiate leaf node $5$
    - Read $(6, 0)$: instantiate leaf node $6$
    - Node $3$ receives children $[5, 6]$
    - Read $(2, 0)$: instantiate leaf node $2$
    - Read $(4, 0)$: instantiate leaf node $4$
    - Root $1$ receives children $[3, 2, 4]$
  - Reconstructed tree matches original structure identically.
- **Empty Tree Instance:** $root = \text{None} \implies$ Serialized: `"#"` $\implies$ Deserialized: `None`
- **Single Node Instance:** $root = \text{Node}(10) \implies$ Serialized: `"10 0"` $\implies$ Deserialized: $\text{Node}(10, [])$

This instance demonstrates linear preorder tokenization of variable-degree trees without null placeholders, mathematically proves why recording the child degree $(val, count)$ uniquely preserves arbitrary branching structures, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of an $N$-ary tree:
Design an algorithm to **serialize** (convert to a string) and **deserialize** (convert from that string back to the original tree structure).

```text
Tree Topology:
        1
      / | \
     3  2  4
    / \
   5   6

Preorder Stream Representation:
  (Node 1, degree 3) -> [ (Node 3, degree 2) -> [ (5, 0), (6, 0) ] ] -> (2, 0) -> (4, 0)

Serialized String: "1 3 3 2 5 0 6 0 2 0 4 0"
```

### Why Binary Tree Serialization Does Not Scale to N-ary Trees
- In a binary tree, every node has at most two children (left and right). Marking missing children with `null` uniquely defines the tree.
- In an $N$-ary tree, a node may have 0, 1, 5, or 100 children. We cannot mark non-existent children with `null` because the maximum number of potential children is unbounded.
- **The Child Degree Solution:** Alongside each node's value, we explicitly store its **child count** (out-degree). This allows the deserializer to know exactly how many subsequent subtrees belong to the current node.

---

## 2. Conceptual Foundation & Invariants

### 1. The Preorder Pair Grammar:
Every node in the tree is encoded as an ordered pair of integers:
$$
\langle \text{value}, \; \text{child\_count} \rangle
$$
Following this pair, the encodings of all its children appear sequentially in preorder:
$$
\text{Encode}(u) = \langle u.val, \; |u.children| \rangle \circ \text{Encode}(child_1) \circ \dots \circ \text{Encode}(child_k)
$$

### 2. Recursive Decoding Invariant:
A recursive parser function `decode()` operates on the iterator of tokens:
1. Extract `value = int(next(tokens))`.
2. Extract `child_count = int(next(tokens))`.
3. Construct the list of children by recursively invoking `decode()` exactly `child_count` times:
   $$
   children = [\text{decode}() \quad \text{for } \_ \text{ in } 0 \dots child\_count - 1]
   $$
4. Return `Node(value, children)`.

> **Grammar Invariant.** Because every node explicitly specifies its degree $k$, exactly $\sum_{i=1}^k \text{subtree\_size}(child_i)$ subsequent tokens are consumed to build its children, guaranteeing zero ambiguity and requiring no closing tags or parentheses.

---

## 3. Step-by-Step Worked Execution

We trace the representative tree with root $1$:

---

### Phase 1: Serialization Walk

1. Visit Root Node $1$:
   - Value: $1$, Children: $[3, 2, 4]$ (Count: $3$).
   - Emits: `"1 3"`.
2. Visit First Child of 1 $\to$ Node $3$:
   - Value: $3$, Children: $[5, 6]$ (Count: $2$).
   - Emits: `"3 2"`.
3. Visit First Child of 3 $\to$ Node $5$:
   - Value: $5$, Children: $[]$ (Count: $0$).
   - Emits: `"5 0"`.
4. Visit Second Child of 3 $\to$ Node $6$:
   - Value: $6$, Children: $[]$ (Count: $0$).
   - Emits: `"6 0"`.
5. Visit Second Child of 1 $\to$ Node $2$:
   - Value: $2$, Children: $[]$ (Count: $0$).
   - Emits: `"2 0"`.
6. Visit Third Child of 1 $\to$ Node $4$:
   - Value: $4$, Children: $[]$ (Count: $0$).
   - Emits: `"4 0"`.
- Assembled string:
  $$
  \text{"1 3 3 2 5 0 6 0 2 0 4 0"}
  $$

---

### Phase 2: Deserialization Walk

Stream iterator: `tokens = ["1", "3", "3", "2", "5", "0", "6", "0", "2", "0", "4", "0"]`.

1. `decode()` Frame 1 (Root):
   - Read `val = 1, count = 3`. Needs 3 children.
   - Call `decode()` for Child 1:
     - Read `val = 3, count = 2`. Needs 2 children.
     - Call `decode()` for Child 1.1:
       - Read `val = 5, count = 0`. Leaf node! Return `Node(5, [])`.
     - Call `decode()` for Child 1.2:
       - Read `val = 6, count = 0`. Leaf node! Return `Node(6, [])`.
     - Assemble `Node(3, [Node(5), Node(6)])`. Return to Frame 1.
   - Call `decode()` for Child 2:
     - Read `val = 2, count = 0`. Leaf node! Return `Node(2, [])`.
   - Call `decode()` for Child 3:
     - Read `val = 4, count = 0`. Leaf node! Return `Node(4, [])`.
2. Assemble Root:
   - `Node(1, [Node(3), Node(2), Node(4)])`.
3. Stream fully consumed. Return reconstructed root.

---

## 4. Complete Execution Trace

| Step | Operation | Node Processed | Value | Child Count | Serialized Substring | Call Stack Depth |
|:---:|:---|:---:|:---:|:---:|:---|:---:|
| **1** | Encode | Node $1$ | $1$ | $3$ | `"1 3"` | $1$ |
| **2** | Encode | Node $3$ | $3$ | $2$ | `"1 3 3 2"` | $2$ |
| **3** | Encode | Node $5$ | $5$ | $0$ | `"1 3 3 2 5 0"` | $3$ |
| **4** | Encode | Node $6$ | $6$ | $0$ | `"1 3 3 2 5 0 6 0"` | $3$ |
| **5** | Encode | Node $2$ | $2$ | $0$ | `"1 3 3 2 5 0 6 0 2 0"` | $2$ |
| **6** | Encode | Node $4$ | $4$ | $0$ | `"1 3 3 2 5 0 6 0 2 0 4 0"` | $2$ |
| **Done**| Serialize Complete | — | — | — | **Length: 12 tokens** | — |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{None}$):** Serialized as `"#"` or empty string. Deserializer checks sentinel and returns `None` without attempting to parse tokens.
- **Single Node Without Children ($root = \text{Node}(42)$):** Emits `"42 0"`. Deserializer reads $42$ with count $0$, loops $0$ times, returns `Node(42, [])`.
- **Deeply Nested Skewed Tree ($1 \to 2 \to 3$ with 1 child each):** Emits `"1 1 2 1 3 0"`. Correctly reconstructs linear chain of depth 3.
- **High-Degree Star Tree (Root with 100 leaves):** Emits `"root 100"` followed by 100 pairs of `(leaf_val, 0)`. Efficiently parsed in linear time without stack overflow.

---

## 6. Traps & Common Anti-Patterns

- **Using Null Sentinels for Unbounded Degree:** Attempting to mark children boundaries with `null` or brackets without degree counts leads to complex nesting logic or quadratic parsing. Storing the integer child count directly makes parsing linear and deterministic.
- **String Splitting Overhead:** Repeatedly popping from the beginning of a list with `tokens.pop(0)` takes $O(N^2)$ time because each pop shifts all remaining elements. Using an iterator `iter(tokens)` or maintaining an index pointer guarantees $O(1)$ token retrieval.
- **Delimiter Ambiguity:** Failing to delimit multi-digit numbers (e.g. concatenating without spaces) makes numbers like $12$ indistinguishable from $1$ and $2$. Space-separated tokens avoid parsing ambiguity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Serialization:** DFS visits each of the $N$ nodes once, appending 2 tokens per node in $O(1)$ time. Total time: $\mathcal{O}(N)$.
  - **Deserialization:** Token splitting takes $O(N)$ time. The recursive decoder visits each token pair once in $O(1)$ time. Total time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ to store the token string and recursion call stack bounded by tree height $H \le N$.
