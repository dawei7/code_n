# Guided Example: Find Duplicate Subtrees

We trace the step-by-step post-order recursive traversal ($dfs(left), dfs(right)$), canonical subtree structural serialization ($v = \text{"val,left,right"}$ with sentinel null markers), signature frequency tracking ($counter[v]$), deduplicated representative collection ($\text{count} == 2 \implies ans.\text{append}(root)$), and isomorphism detection on representative binary tree hierarchies:

- **Input:**
  - $root = [1, 2, 3, 4, \text{null}, 2, 4, \text{null}, \text{null}, 4]$
  - Tree topology:
    ```text
            1
           / \
          2   3
         /   / \
        4   2   4
           /
          4
    ```
- **Required output:** `[[2, 4], [4]]` (Roots representing identical subtrees)
  - Definition of duplicate subtrees: Two subtrees are identical if they possess the **exact same graph structure** and the **exact same node values** at corresponding positions.
  - Frequency policy: For each distinct duplicate structure, return the root of **any one instance**. Do not add duplicates multiple times if a subtree appears 3 or more times.
- **Canonical Serialization & Post-Order Invariant:**
  - **The Structural Signature:**
    - To compare subtrees without doing $O(N)$ pair-wise tree traversals, serialize each subtree into a canonical text token:
      $$
      v = \text{val} + \text{","} + \text{serialize}(left) + \text{","} + \text{serialize}(right)
      $$
    - Use a fixed sentinel symbol (such as `"#"` or `"null"`) to represent missing child pointers.
    - Post-order serialization ensures that before a parent computes its own signature, both of its children have already computed and returned their complete signatures.
  - **Singleton Output Gate ($\text{count} == 2$):**
    - Store occurrences of signature $v$ in a frequency map $counter$.
    - When an identical signature is encountered for the **first duplicate time** ($counter[v] == 2$):
      - We append the current node to $ans$.
    - If the same signature appears a 3rd or 4th time ($counter[v] > 2$):
      - It is ignored, guaranteeing that each unique isomorphism class appears **exactly once** in the output list.
- **Step-by-Step Worked Execution Trace:**
  - Nodes identified by label and position:
    - Node 1: Root
    - Node $2_L$: Left child of 1
    - Node $4_A$: Left child of $2_L$
    - Node 3: Right child of 1
    - Node $2_R$: Left child of 3
    - Node $4_B$: Left child of $2_R$
    - Node $4_C$: Right child of 3
  - **Post-Order Subtree Traversal Trace:**
    - **Visit $4_A$ (Leaf):**
      - Left is null (`"#"`), Right is null (`"#"`).
      - Signature: `"4,#,#"`
      - Register: `counter["4,#,#"]` increases to 1.
      - Returns `"4,#,#"`.
    - **Visit $2_L$:**
      - Left child is $4_A$ (`"4,#,#"`), Right child is null (`"#"`).
      - Signature: `"2,4,#,#,#"`
      - Register: `counter["2,4,#,#,#"]` increases to 1.
      - Returns `"2,4,#,#,#"`.
    - **Visit $4_B$ (Leaf under $2_R$):**
      - Children are null.
      - Signature: `"4,#,#"`
      - Register: `counter["4,#,#"]` reaches **2**.
      - Condition count is 2 is met!
      - Add root $4_B$ to answers: Node 4.
      - Returns `"4,#,#"`.
    - **Visit $2_R$:**
      - Left child is $4_B$ (`"4,#,#"`), Right child is null (`"#"`).
      - Signature: `"2,4,#,#,#"`
      - Register: `counter["2,4,#,#,#"]` reaches **2**.
      - Condition count is 2 is met!
      - Add root $2_R$ to answers: Node 2.
      - Returns `"2,4,#,#,#"`.
    - **Visit $4_C$ (Leaf under 3):**
      - Signature: `"4,#,#"`
      - Register: `counter["4,#,#"]` reaches 3.
      - Notice: count is $3 \ne 2 \implies$ Node $4_C$ is **not** added again (preventing duplicates).
      - Returns `"4,#,#"`.
    - **Visit 3:**
      - Left child is $2_R$ (`"2,4,#,#,#"`), Right child is $4_C$ (`"4,#,#"`).
      - Signature: `"3,2,4,#,#,#,4,#,#"`
      - Register: count is 1. Returns signature.
    - **Visit 1 (Root):**
      - Combines signatures of $2_L$ and 3.
      - Register: count is 1.
  - **Step 4: Output Assembly:**
    - Collected duplicate subtree roots:
      1. Node with value $4$ (representing leaf tree `[4]`)
      2. Node with value $2$ (representing branch tree `[2, 4]`)
    - Result:
      $$
      ans = [[\mathbf{2, 4}], \; [\mathbf{4}]]
      $$
- **Triple-Instance Leaf Handling:**
  - Leaf `4` appeared 3 times ($4_A, 4_B, 4_C$).
  - Appended when count reached 2 (at $4_B$).
  - Ignored when count reached 3 (at $4_C$).
  - Appears exactly once in output.
- **Asymmetric Structure Invariance:**
  - A node with left child 4 and right null (`"2,4,#,#,#"`) has a different signature than a node with left null and right child 4 (`"2,#,4,#,#"`), correctly distinguishing chiral orientations.

This instance demonstrates bottom-up graph isomorphism hashing and canonical serialization, mathematically proves why bi-parental sentinel encoding eliminates tree structural ambiguity, and derives $O(N)$ runtime (or $O(N^2)$ string concatenation) and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree:
Find all **duplicate subtrees**.
Return the root node of one representative for each duplicate structure.

```text
Tree:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

Duplicate subtrees:
  1. Leaf node [4] (appears 3 times)
  2. Branch [2, 4] (appears 2 times: left of 1, and left of 3)

Result: roots of [2, 4] and [4]
```

### The Invariant of Canonical Serialization
- A binary tree's structure and contents are uniquely identified by its post-order serialization with null sentinels:
  `val,left_sig,right_sig`.
- Two subtrees produce the exact same serialization string if and only if they are isomorphic.

---

## 2. Conceptual Foundation & Invariants

### 1. The Serialization Mapping:
$$
\text{sig}(u) = \begin{cases} \text{"\#"} & \text{if } u = \text{null} \\ u.val + \text{","} + \text{sig}(u.left) + \text{","} + \text{sig}(u.right) & \text{otherwise} \end{cases}
$$

### 2. The Singleton Duplicate Condition:
For node $u$ with signature $S$:
$$
counter[S] \leftarrow counter[S] + 1
$$
$$
counter[S] == 2 \implies ans.\text{append}(u)
$$

> **Bijective Tree Isomorphism Invariant.** By the fundamental theorem of binary tree parsing, a post-order traversal with distinct non-null delimiters and null sentinels forms a bijective encoding between labeled ordered rooted trees and words over $\Sigma^*$.

---

## 3. Step-by-Step Worked Execution

We trace the occurrences of each signature:

---

### Step 1: Leaf Node 4
- Signature: `"4,#,#"`.
- 1st time (under $2_L$): count 1.
- 2nd time (under $2_R$): count 2 $\implies$ Add to $ans$.
- 3rd time (under 3): count 3 $\implies$ Skip.

---

### Step 2: Branch Node 2
- Signature: `"2,4,#,#,#"`.
- 1st time ($2_L$): count 1.
- 2nd time ($2_R$): count 2 $\implies$ Add to $ans$.

---

### Step 3: Other Nodes (3, 1)
- Signatures appear only once $\implies$ Not added.

---

### Step 4: Final Collection
$$
[[\mathbf{2, 4}], \; [\mathbf{4}]]
$$

---

## 4. Complete Execution Trace

| Node Evaluated | Subtree Root Value | Left Signature | Right Signature | Full Subtree Signature | Frequency After | Added to $ans$? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $4_A$ | $4$ | `"#"` | `"#"` | `"4,#,#"` | $1$ | No |
| $2_L$ | $2$ | `"4,#,#"` | `"#"` | `"2,4,#,#,#"` | $1$ | No |
| $4_B$ | $4$ | `"#"` | `"#"` | `"4,#,#"` | **$2$** | **Yes (Leaf 4)** |
| $2_R$ | $2$ | `"4,#,#"` | `"#"` | `"2,4,#,#,#"` | **$2$** | **Yes (Branch 2)** |
| $4_C$ | $4$ | `"#"` | `"#"` | `"4,#,#"` | $3$ | No ($> 2$) |
| $3$ | $3$ | `"2,4,#,#,#"` | `"4,#,#"` | `"3,2,4,#,#,#,4,#,#"` | $1$ | No |
| $1$ | $1$ | ... | ... | Unique | $1$ | No |

---

## 5. Boundary Cases & Failure Modes

- **No Duplicates:** Empty list returned.
- **Tree of All Identical Values ($1 \to 1 \to 1$):** Signatures encode depth and child orientation accurately.
- **Single Node:** No duplicate subtrees $\implies []$.
- **Many Identical Leaves ($10^3$ leaves):** Each leaf triggers count increment; only the 2nd encounter appends to output.

---

## 6. Traps & Common Anti-Patterns

- **Adding to Answer on Every Match ($counter[v] \ge 2$):** If a subtree appears 5 times, testing $\ge 2$ appends it 4 times. You must check strictly `== 2`.
- **Omitting Null Sentinels:** Serializing `"1,2"` without null markers confuses a node with left child 2 and right null with a node with left null and right child 2.
- **Comparing Trees Node-by-Node ($O(N^2)$):** Pairwise subtree comparison takes $O(N^2)$ comparisons of $O(N)$ nodes ($O(N^3)$ time). Serialization with a hash map runs in linear time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard DFS visits all $N$ nodes once: $\mathcal{O}(N)$.
  - Serializing strings of length $L$ and hashing takes $\mathcal{O}(L)$. In worst case (skewed tree), $\mathcal{O}(N^2)$ string work; using integer ID tuples $(val, left\_id, right\_id)$ reduces it to strictly $\mathcal{O}(N)$.
  - For $N \le 5000$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the hash map of signatures and recursion stack.
