## General

Postorder records a node only *after* every child subtree has been completely traversed. For an n-ary node with children $c_1,c_2,\ldots,c_k$, its postorder sequence is:

$$
\operatorname{postorder}(c_1),
\operatorname{postorder}(c_2),
\ldots,
\operatorname{postorder}(c_k),
\text{node}.
$$

The exact recursive helper mirrors this definition: handle a null node, recursively process children from left to right, and append the current value last.

**Why appending happens after the loop**

The crucial lines are:

```python
for child in root.children:
    dfs(child)
ans.append(root.val)
```

When the helper reaches a parent, it postpones that parent’s value. It enters the first child and does not return until the child’s entire subtree is done. It repeats this for every sibling. Only when no child work remains does it append the parent.

Moving `ans.append(root.val)` above the loop would produce preorder. Appending a parent between child calls would produce neither standard traversal. Postorder’s “children first” promise is encoded exactly by placing the append after all recursive calls.

For sample root 1, the subtree rooted at 3 contributes 5, 6, then 3. Leaf 2 contributes 2 and leaf 4 contributes 4. Only afterward does root 1 appear, producing `[5, 6, 3, 2, 4, 1]`.

**Leaves and the base case**

A leaf has an empty `children` list. Its loop executes zero times, then its value is appended. This is correct because a leaf has no descendants that must precede it.

For `root is None`, the helper returns without appending:

```python
if root is None:
    return
```

Thus, an empty input yields the initially empty answer list. The same guard is defensively safe if a child reference is null.

**What the recursive call stack represents**

While the traversal explores a child, the parent call remains suspended with its loop position and the still-unexecuted append. This pending append is exactly the state an iterative implementation would have to store explicitly: “come back to this node after its children.”

Once a child returns, the parent continues with the next child. Once all return, the pending parent append executes. Recursion therefore provides both depth-first movement and the required second phase of each node visit.

Children are visited in their existing list order. Sorting by value would change the defined traversal. If a node lists children `[A, B, C]`, the complete postorder of $A$ must precede the complete postorder of $B$, which precedes $C$, regardless of their values or subtree sizes.

**Why the traversal is correct**

Proceed by structural induction. The helper on an empty tree appends no values, which is the correct empty postorder.

Assume recursively that `dfs` produces the correct postorder for every child subtree of a node $r$. The loop invokes those helpers in left-to-right child order, so `ans` receives exactly the required child-subtree sequences in order. After every child sequence is complete, the helper appends $r$ itself. That concatenation is precisely the definition of postorder for the subtree rooted at $r$.

By induction, calling `dfs(root)` produces the correct traversal for the whole tree. Because a tree has one unique parent for each non-root node, each node receives exactly one helper call and is appended exactly once.

The input’s level-order serialization and `null` separators are only the external encoding. The platform constructs `Node` objects before calling the solution. The traversal follows `children` references rather than parsing the serialized list.

**Why one shared answer list is efficient**

`ans` belongs to the enclosing `postorder` call and is mutated by every recursive invocation. A different design could have each call return a list and concatenate all child lists, but repeated concatenation can copy previously produced values many times. Appending each node once to one list keeps result construction linear.

## Complexity detail

Let $n$ be the number of nodes and $h$ the height. Every node is entered once and appended once. Each parent’s loop scans its children, so across all nodes exactly $n-1$ tree edges are examined. Total time is $O(n)$.

The required result list stores $n$ values. The recursive call stack stores at most one frame per node on the current root-to-leaf path, using $O(h)$ auxiliary space. In the worst case the tree is a chain, $h=n$, so the broad space bound is $O(n)$. Excluding output, the more precise bound is $O(h)$.

The allowed height reaches 1000, near Python’s default recursion limit. The mathematical space analysis remains valid, but a maximally deep valid input can risk `RecursionError`. An iterative method is operationally safer.

## Alternatives and edge cases

- **Stack with visited flag:** Push `(root, False)`. On first pop, push `(node, True)` and then children in reverse order; on the marked pop, append the value. This exactly simulates the recursive pending append.
- **Modified preorder then reverse:** Process root and push children left-to-right, collecting root-right-left order, then reverse the values to obtain left-right-root postorder. It is concise but the reversal reasoning must be understood.
- **Two stacks:** Move nodes from a traversal stack to a second stack, then pop the second into the result. Clear but stores every node in explicit intermediate form.
- **Append before children:** Produces preorder and is incorrect for this task.
- **Reverse child iteration without a compensating stack rule:** Changes sibling order and therefore changes postorder.
- **Empty tree:** Returns `[]` because the helper immediately stops.
- **Single node:** Its child loop is empty, so its value is the sole result.
- **Wide tree:** Every child subtree is completed in left-to-right order before the parent appears.
- **Deep chain:** Recursive frames can approach or exceed Python’s runtime recursion limit; the visited-flag stack avoids it.
- **Repeated node values:** Equal values from different nodes must all appear. Do not use a set or deduplicate output.
- **No visited set:** A proper tree is acyclic and has unique parentage. Graph-like input would need protection, but it is outside the contract.
- **Serialization `null` markers:** They separate child groups while constructing the tree and do not represent visitable nodes.
- **Output versus auxiliary space:** The result necessarily uses $O(n)$ space; recursion itself uses $O(h)$.
