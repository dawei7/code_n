## General

The tasks already form a directed tree rooted at task `0`. Every edge `[u,v]` says that `u` is the parent and `v` is a child, so the direction needed for the computation is supplied directly.

A task's finish time depends on its children's finish times. This immediately implies a bottom-up evaluation order: a leaf can be evaluated from its own `baseTime`, then its parent can be evaluated after all of that parent's children, and so on until the root.

For a non-leaf task `i`, let the child finish times be

$$
f_1,f_2,\ldots,f_c.
$$

Define

$$
e=\min_j f_j
\qquad\text{and}\qquad
q=\max_j f_j.
$$

The statement calls these values `earliest` and `latest`. The task's own duration is

$$
(q-e)+\texttt{baseTime}[i].
$$

Its finish time is the latest child finish plus that duration:

$$
q+\left((q-e)+\texttt{baseTime}[i]\right)
=2q-e+\texttt{baseTime}[i].
$$

The source writes the rule in its unsimplified conceptual form, which closely follows the statement.

**Building child lists**

The line

```python
g = [[] for _ in range(n)]
```

creates one empty child list per task. For each directed pair `u,v`, the source appends `v` only to `g[u]`:

```python
for u, v in edges:
    g[u].append(v)
```

It does not add the reverse edge because `v` is not the parent of `u`. It also needs no visited set or parent parameter: following child lists in a valid rooted tree can never move back upward or enter a cycle.

**What `dfs(i)` returns**

The nested function `dfs(i)` returns the finish time of task `i` after completely evaluating the subtree rooted at `i`.

If `g[i]` is empty, task `i` has no children. The leaf rule applies directly:

```python
if not g[i]:
    return baseTime[i]
```

For a non-leaf, the function recursively calls `dfs(j)` for every child `j`. Each call returns a child finish time only after resolving all descendants below that child. While those values arrive, the source retains just their minimum and maximum:

```python
earliest = min(earliest, a)
latest = max(latest, a)
```

Intermediate child finish times do not otherwise affect the parent's formula, so no list of them is required.

After all children have been processed, the function calculates

```python
own_duration = (latest - earliest) + baseTime[i]
return latest + own_duration
```

which is exactly the rule from the description.

Finally, `dfs(0)` evaluates the entire tree and returns the root's finish time.

**Why the recursive values are the required values**

Every leaf return is correct by the leaf definition. Consider a non-leaf task after assuming each recursive child call has returned that child's correct finish time. The loop computes the minimum and maximum of precisely those values. Substituting them into the given non-leaf formula produces task `i`'s required finish time.

Because a finite tree has leaves and every parent appears above its descendants, this reasoning propagates from the leaves through every subtree to task `0`. Each task is reached exactly once because it has exactly one parent except for the root.

For a node with only one child whose finish time is `a`, both `earliest` and `latest` equal `a`. The spread is zero, so the parent finish is `a+\texttt{baseTime}[i]`. The general code handles this without a special branch.

**The nested function can refer to `g`**

The source defines `dfs` before assigning `g`. This is valid in Python because the function body is not executed at the moment of definition. The closure resolves `g` later, when `dfs(0)` is called; by then the adjacency lists have been created and filled.

**The stored source has missing names**

The exact file annotates `edges` and `baseTime` with `List` but contains no import or definition for `List`. With normal Python annotation evaluation, loading the module fails while defining the method:

```text
NameError: name 'List' is not defined
```

If `List` is supplied externally, a non-leaf call next reaches

```python
earliest, latest = inf, -inf
```

but `inf` is also neither imported nor defined. That raises a second `NameError`. Supplying `List` from `typing` and `inf` from `math` would resolve these two name errors, but those imports are absent from the stored source and must not be assumed silently.

For a one-node tree, `inf` would not be reached because the root is a leaf, but the unresolved `List` annotation still prevents ordinary module loading.

**The recursion depth is another real limitation**

Even after the missing names are supplied, the exact implementation uses one Python call-stack frame per level of the tree. The constraint permits `n` up to `10^5`, and a valid tree may be one chain of that length. Standard Python normally permits only around one thousand nested calls, so a sufficiently deep legal chain raises `RecursionError`.

This is not a mathematical flaw in the recurrence. An iterative traversal followed by reverse-order evaluation would compute the same values safely for a deep tree. However, the stored source does not implement that iterative approach. Its manifest summary says it evaluates in reverse traversal order, while the exact code is recursive DFS. A source-faithful explanation must record that mismatch.

Independent checking confirms the distinction: after injecting only the two missing names, the recurrence matches an iterative model on ordinary trees, but a legal 2,000-node chain already reproduces `RecursionError` in the current environment.

## Complexity detail

For the intended execution, let `n` be the number of tasks and let `h` be the height of the rooted tree.

Building `g` creates `n` lists and processes `n-1` edges, taking `O(n)` time. The DFS visits every task once. Across all loops, it examines every parent-child edge once and performs constant work per edge. The intended time complexity is therefore `O(n)`.

The adjacency lists store `n-1` child references and `n` list objects, requiring `O(n)` space. The recursive call stack reaches depth `O(h)`, which is `O(n)` in the worst case. Total auxiliary space is consequently `O(n)`.

Those asymptotic bounds describe the algorithm after `List` and `inf` have been made available and for inputs shallow enough to complete under Python's recursion limit. As stored, ordinary module loading stops at the first missing name, so it does not successfully realize the advertised bounds. On a very deep legal tree, execution can stop with `RecursionError` rather than return a result.

An iterative implementation would still use `O(n)` time and `O(n)` space, but would place its traversal order on the heap instead of relying on the bounded interpreter call stack. That is the behavior suggested by the manifest summary, not the behavior of this exact source.

The returned values may exceed 32-bit range, but Python integers retain exact values. The stated guarantee that finish times stay below `2^{53}` is therefore comfortably representable.

## Alternatives and edge cases

- **Iterative preorder plus reversed order:** Build an order in which every parent precedes its children, then process that list backward. This preserves `O(n)` time and space while safely supporting a chain of `10^5` tasks. It would also match the manifest's reverse-traversal summary, but it is not what the stored source currently does.

- **Memoized recursion:** Memoization is unnecessary on a tree because every non-root node has one parent and is requested once. It would not repair missing imports or the call-stack limit.

- **Recompute each subtree repeatedly:** Evaluating descendants anew for every ancestor can become quadratic on a chain. Returning each subtree's finish time once gives the linear traversal.

- **Store all child values:** A list followed by `min` and `max` is correct but unnecessary. Updating `earliest` and `latest` while iterating uses constant additional state inside each active call.

- **Simplified recurrence:** Returning `2 * latest - earliest + baseTime[i]` is algebraically equivalent. The source retains `own_duration`, which mirrors the problem's two-stage definition.

- **One task:** The root is a leaf and its finish time is exactly `baseTime[0]`. No edge or non-leaf calculation is needed.

- **One child:** `earliest` and `latest` are equal, so the spread contributes zero and the parent's base time is simply added to the child's finish time.

- **Many children with tied times:** Equal minimum or maximum values cause no difficulty; repeated comparisons leave the same extrema and the formula depends only on their values.

- **Directed-edge interpretation:** Adding reverse edges without a parent check would permit immediate traversal back to the parent and cause infinite recursion. The source correctly respects the supplied parent-to-child direction.

- **Missing `List`:** The file cannot normally finish defining `Solution` because the annotation name is unresolved.

- **Missing `inf`:** Supplying `List` alone is insufficient for non-leaf trees; the extrema initialization then fails at runtime.

- **Deep legal tree:** A chain can satisfy every input constraint while exceeding Python's recursion limit. The source does not catch or prevent `RecursionError`.

- **Raising the recursion limit:** Increasing the interpreter limit may postpone failure, but it depends on environment stack capacity and is less robust than an iterative traversal for `n=10^5`.

- **Manifest/source mismatch:** The declared `O(n)` mathematical class is appropriate, but the summary's reverse-order mechanism does not describe the recursive source. Complexity class alone does not erase that implementation difference.
