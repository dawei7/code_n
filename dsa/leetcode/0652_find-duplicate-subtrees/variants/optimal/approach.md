## General

**Give every subtree a complete structural signature**

Two subtrees are duplicates only when both their node values and their entire shapes match. Comparing every subtree directly against every other subtree would repeat a great deal of tree traversal.

The exact solution instead converts each subtree into a canonical string. Equal subtrees produce equal strings, and structurally or numerically different subtrees produce different strings. A counter then reveals which signatures occur more than once.

For a non-null node, its signature has three comma-separated parts:

`node value, left-subtree signature, right-subtree signature`.

A null child has the special signature `#`.

For example, a leaf with value four becomes `4,#,#`. A node with value two, that leaf on the left, and no right child becomes `2,4,#,#,#`.

**Why null markers cannot be omitted**

Values alone do not describe shape. A node with a left child but no right child must differ from a node with no left child but the same-valued right child. The `#` markers preserve those empty positions:

- left-child shape: `1,2,#,#,#`;
- right-child shape: `1,#,2,#,#`.

Without null markers, both could collapse into the same value sequence and create a false duplicate.

**Why commas are needed**

Node values may be negative or contain multiple digits. Delimiters prevent ambiguous token boundaries. For example, the sequence of values one and twenty-three must not be confused with twelve and three.

The combination of comma-separated value tokens, explicit null markers, and fixed root-left-right order makes the serialization uniquely decodable as a preorder tree representation. Therefore, string equality is equivalent to subtree equality.

**Compute child signatures before the parent signature**

`dfs(root)` first recursively computes `dfs(root.left)` and `dfs(root.right)` as part of constructing the f-string. Only after both results are available can it create the current node's signature.

The computation is therefore postorder even though the resulting signature lists the root value first. Postorder evaluation is necessary because a parent signature depends on complete child signatures.

For a null pointer, `dfs` immediately returns `#`. It does not add null signatures to the counter because null is not a subtree root that should appear in the answer.

**Count signatures and append only on the second occurrence**

After constructing a non-null signature `v`, the algorithm increments `counter[v]`.

If the count becomes exactly two, it appends the current node to `ans`. The equality check against two is deliberate:

- count one means this subtree kind has not yet been proven duplicate;
- count two is the first moment duplication is established, so add one representative;
- count three or more means this duplicate kind is already represented and must not be added again.

The problem asks for one root node for each kind of duplicate subtree, not one root for every occurrence. Appending only at count two satisfies that requirement.

The chosen representative is the root of the second encountered copy. The contract permits any one occurrence, so there is no need to save the first node or choose by position.

**A simple repeated-leaf example**

Suppose two different leaf nodes both contain value four. Each recursive call returns `4,#,#`. The first increments its count to one. The second increments the same key to two and appends that second leaf node. If a third identical leaf exists, the count becomes three but no additional result entry is added.

If two larger subtrees both have a root value two and an identical value-four leaf on the same side, their complete recursive strings also match. They are counted independently as another duplicate kind. It is valid for the output to include both the repeated leaf kind and the repeated larger-subtree kind.

**Why every duplicate kind is found**

Proceed from leaves upward. Null children always have the same `#` representation. For non-null nodes, assume recursively that equal child subtrees return equal signatures and unequal child subtrees return unequal signatures.

Two current subtrees are equal exactly when their root values match, their left subtrees match, and their right subtrees match. Those are exactly the three components of `v`. Therefore, equal current subtrees produce equal signatures. If any value, child structure, or child value differs, at least one component differs, so the signatures differ.

Every non-null node is visited once and contributes its subtree signature to the counter. Hence every signature occurring at least twice reaches count two and contributes one representative. Signatures occurring once never enter the answer, and counts above two do not create duplicate output entries. This proves the returned list has exactly one root for every duplicate-subtree kind.

**The result order is incidental**

Nodes are appended when their signatures reach count two during recursive traversal. The problem does not prescribe an output order, so this postorder-dependent order is acceptable. Consumers should not infer a sorting rule from it.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height.

The traversal invokes `dfs` once per node and once per null edge, but constructing a signature is not constant work. A node's string contains a serialization of its entire subtree. In a highly skewed tree, subtree signature lengths are proportional to `N, N - 1, N - 2, ...`. Copying and hashing all of those strings takes `O(N^2)` time in the worst case.

The counter can retain one string for every distinct subtree signature. In the same skewed worst case, the total number of characters across stored keys is `O(N^2)`. The recursion stack uses `O(H)` space, and the result may store `O(N)` node references in a broad bound. String storage dominates, so literal worst-case auxiliary space is `O(N^2)`.

For a balanced tree, the sum of all subtree sizes is closer to `O(N log N)`, but worst-case analysis must include skewed trees.

The manifest advertises `O(N)` time and space. Those bounds correspond to the editorial's optimized method that interns each constant-size tuple `(node value, left ID, right ID)` into an integer subtree ID. The exact source shown here uses full strings and therefore has the quadratic worst-case bounds above. The approach document describes the literal source honestly without changing that protected solution.

Python recursion has a default depth limit far below the maximum possible skewed height of 5000. On such an adversarial tree, the exact recursive source may require an increased recursion limit or an iterative postorder conversion to run successfully.

## Alternatives and edge cases

- **Intern tuple signatures into integer IDs:** Map `(value, left_id, right_id)` to a unique integer, count IDs, and return each ID on its second occurrence. The tuple has constant size, giving expected `O(N)` time and `O(N)` space and matching the manifest.

- **Direct pairwise subtree comparison:** Comparing every root with every other root and recursively checking equality can reach cubic time because the same descendants are revisited many times.

- **Hash-only signatures:** Combining child hashes can reduce stored size, but a collision could merge different subtrees unless equality is independently verified. Interned structural tuples avoid probabilistic correctness.

- **Iterative postorder traversal:** It can compute signatures without recursion-depth risk, but requires explicit stack state to distinguish first visits from the moment both children are complete.

- **Repeated leaves:** Each repeated leaf value forms a duplicate kind. The second occurrence is appended once, even if many more identical leaves exist.

- **A duplicate contained inside another duplicate:** Both subtree kinds should appear. Counting every node's signature naturally finds the inner and outer duplicates independently.

- **Same values, different shape:** Null markers and fixed left-right order keep the signatures different.

- **Mirror-image subtrees:** Swapping left and right children changes component order, so mirror images are not considered duplicates unless they are structurally identical after the swap.

- **Negative and multi-digit values:** Commas and the `#` token keep serialization boundaries clear.

- **Three or more copies:** Checking `counter[v] == 2` prevents repeated representatives for the same subtree kind.

- **No duplicates:** Every signature remains at count one and `ans` stays empty.

- **Single-node tree:** Its leaf signature appears once, so the result is empty.

- **Null root:** The reference guarantees at least one node, but the helper would safely return `#` and the outer method would return an empty list.

- **Output order:** The contract allows any order. Sorting node objects is neither required nor naturally defined.

- **Deeply skewed tree:** Besides quadratic string work, recursive depth can exceed Python's limit. This is a practical limitation of the exact implementation.

- **Delimiter changes:** Removing commas or null markers can make different trees serialize identically. Any alternative encoding must remain uniquely decodable.
