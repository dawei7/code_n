# Guided Example: Construct String from Binary Tree

We trace the step-by-step pre-order serialization ($\text{root} \to \text{left} \to \text{right}$), parenthetical hierarchy nesting, asymmetric empty child pruning rules, non-ambiguous 1-to-1 tree mapping preservation (retaining `()` when left is absent but right is present), and string synthesis on representative binary trees:

- **Input:** $root = [1, 2, 3, 4]$
  - Root $1$ has left child $2$ and right child $3$.
  - Node $2$ has left child $4$ and no right child.
  - Nodes $4$ and $3$ are leaves.
- **Required output:** `"1(2(4))(3)"`
  - Serialization rules:
    1. Pre-order traversal with recursive parentheses: `node.val(left)(right)`.
    2. **Right child absent ($right = \text{null}$):** Omit the empty right parentheses `()` completely:
       $$
       \text{val}(\text{left})
       $$
    3. **Left child absent, Right child present ($left = \text{null}, right \ne \text{null}$):** Must **keep** the empty left parentheses `()` to prevent ambiguous interpretation of the right child as a left child:
       $$
       \text{val}()(\text{right})
       $$
    4. **Leaf node ($left = \text{null}, right = \text{null}$):** Omit both sets of parentheses:
       $$
       \text{val}
       $$
- **Asymmetric Child Pruning & Invertible Mapping Trace:**
  - Why is an empty left child preserved while an empty right child is omitted?
    - If Node $2$ with only a right child $4$ were serialized as `"2(4)"`, a parser reconstructing the tree could not distinguish whether $4$ is the left child or the right child. By convention, the first parenthesized expression is the left child.
    - Writing `"2()(4)"` uniquely indicates: "left child is empty, right child is 4".
    - But for a node with only a left child, writing `"2(4)"` unambiguously assigns $4$ to the left child without needing an empty `()` for the non-existent right child!
- **Step-by-Step Recursive Execution Trace on $[1, 2, 3, 4]$:**
  - Call $dfs(\text{Node 1})$:
    - Current node value: `1`.
    - Both left and right subtrees exist.
    - Template:
      $$
      1(dfs(\text{Node 2}))(dfs(\text{Node 3}))
      $$
  - **Subtree Evaluation 1: $dfs(\text{Node 2})$:**
    - Current node value: `2`.
    - Left child is Node 4; right child is `null`.
    - Since $right = \text{null}$, apply Rule 2 (omit right parentheses):
      $$
      2(dfs(\text{Node 4}))
      $$
    - **Leaf Evaluation: $dfs(\text{Node 4})$:**
      - Node 4 has no children (Rule 4).
      - Returns string literal:
        $$
        \mathbf{\text{"4"}}
        $$
    - Assemble Node 2 string:
      $$
      \text{"2(4)"}
      $$
  - **Subtree Evaluation 2: $dfs(\text{Node 3})$:**
    - Current node value: `3`.
    - Node 3 has no children (Leaf, Rule 4).
    - Returns string literal:
      $$
      \mathbf{\text{"3"}}
      $$
  - **Assemble Root String:**
    - Substitute subtree results into root template:
      $$
      1 + \text{"("} + \text{"2(4)"} + \text{")"} + \text{"("} + \text{"3"} + \text{")"}
      $$
    - Resulting serialized string:
      $$
      \mathbf{\text{"1(2(4))(3)"}}
      $$
- **Empty Left Child Instance ($root = [1, 2, 3, \text{null}, 4]$):**
  - Node 2 has $left = \text{null}$ and $right = \text{Node 4}$.
  - Under Rule 3: Left child cannot be omitted $\implies \text{"2()(4)"}$.
  - Root joins with 3:
    $$
    \mathbf{\text{"1(2()(4))(3)"}}
    $$
- **Single Root Node ($root = [1]$):**
  - Leaf rule $\implies \mathbf{\text{"1"}}$.

This instance demonstrates bi-directional parenthesized tree serialization, mathematically proves why asymmetric empty marker retention preserves unique tree reconstruction, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Construct a pre-order parenthesized string representation of the tree:
`val(left)(right)`
Omit empty parentheses pairs that do not affect the 1-to-1 mapping relationship.

```text
Tree:
      1
     / \
    2   3
   /
  4

Node 4: "4"
Node 2: has left child 4, right is null -> "2(4)" (omit right empty parens)
Node 3: "3"
Node 1: "1(2(4))(3)"
```

### The Invariant of Reconstructible Syntax
- If a node has a right child but no left child, we **must retain the empty parentheses `()`** for the left child:
  $$
  val()(right)
  $$
- Otherwise, `val(right)` would be interpreted as `val(left)`.
- If a node has a left child but no right child, the trailing `()` for the right child can be safely dropped without causing any ambiguity:
  $$
  val(left)
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Four Structural Cases in `dfs(node)`:
1. **Empty node:** `return ""`
2. **Leaf node:** `return str(node.val)`
3. **Left child only ($right = \text{null}$):**
   $$
   \text{return } \text{f"}\{node.val\}(\{dfs(node.left)\})\text{"}
   $$
4. **Right child present ($right \ne \text{null}$):**
   $$
   \text{return } \text{f"}\{node.val\}(\{dfs(node.left)\})(\{dfs(node.right)\})\text{"}
   $$
   *(If $left$ is null, $dfs(node.left)$ returns `""`, naturally producing `()`)*.

> **Grammatical Disambiguation Invariant.** Retaining empty left parentheses ensures that the first parenthesized child expression always binds strictly to the left child relation.

---

## 3. Step-by-Step Worked Execution

We trace $root = [1, 2, 3, 4]$:

---

### Step 1: Base Calls at Leaves
- $dfs(4) = \text{"4"}$.
- $dfs(3) = \text{"3"}$.

---

### Step 2: Node 2 (Left 4, Right None)
- Right child is null $\implies$ omit right parens.
- Format: `2(` + $dfs(4)$ + `)` = `"2(4)"`.

---

### Step 3: Node 1 (Left 2, Right 3)
- Both children present.
- Format: `1(` + $dfs(2)$ + `)(` + $dfs(3)$ + `)`
- Substitution:
  $$
  \text{"1(2(4))(3)"}
  $$

---

## 4. Complete Execution Trace

| Recursion Target | Left Child | Right Child | Applied Grammar Rule | Subtree Output String |
|:---:|:---:|:---:|:---:|:---:|
| **Node 4** | None | None | Leaf (Rule 2) | `"4"` |
| **Node 2** | Node 4 | None | Left-Only (Rule 3) | `"2(4)"` |
| **Node 3** | None | None | Leaf (Rule 2) | `"3"` |
| **Node 1** | Node 2 | Node 3 | Both Present (Rule 4) | **`"1(2(4))(3)"`** |

---

## 5. Boundary Cases & Failure Modes

- **Right Child Without Left Child ($root = [1, \text{null}, 2]$):** Returns `"1()(2)"`.
- **Single Node Tree ($root = [1]$):** Returns `"1"`.
- **Negative Node Values ($[-1, -2, -3]$):** Formats minus signs cleanly: `"-1(-2)(-3)"`.
- **Skewed Left Tree ($1 \to 2 \to 3$):** Nesting without trailing empty parens: `"1(2(3))"`.

---

## 6. Traps & Common Anti-Patterns

- **Omitting `()` When Left is Null and Right is Present:** Writing `"1(2)"` when 2 is the right child collapses the tree to a left child, violating 1-to-1 invertibility.
- **Adding `()` Around Leaf Nodes:** Writing `"4()()"` or `"4()"` adds redundant characters. Leaves must have zero parentheses.
- **Repeated String Concatenation ($O(N^2)$):** In languages without string builders, recursive string joins can cause quadratic copies. In Python, small trees ($N \le 10^4$) finish rapidly with f-strings.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every node is visited once during the post-order recursive assembly.
  - Total time to traverse and format string: $\mathcal{O}(N)$ where $N \le 10^4$.
  - Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack depth proportional to tree height ($H \le N$).
  - $\mathcal{O}(N)$ memory to construct the output serialized string.
