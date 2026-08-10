## General

The competitive implementation represents the BFS frontier with a plain list instead of a queue. `current` contains all nodes at one depth. A complete pass over that list creates both the value row for that depth and a new list containing the next depth.

This “two frontier” structure makes the level boundary explicit: nodes added to `next_level` cannot be processed until the outer loop assigns that list to `current`.

**Empty-tree handling**

If `root is None`, the method returns `[]`. No placeholder row is needed because the contract asks for node values, and an empty tree has no depths containing nodes.

For a real tree, initialization is `result = []` and `current = [root]`. The invariant is that `current` contains exactly the real nodes of the next output level in left-to-right order.

**Building one output row**

At the beginning of each outer iteration, `next_level` and `vals` are fresh empty lists.

The `for node in current` loop visits the current frontier from its first element to its last. It appends each `node.val` to `vals`, so values preserve the frontier's order.

For each parent, the code appends its left child before its right child when they exist. Parents are themselves visited left to right. Therefore `next_level` becomes the exact left-to-right sequence of all real nodes at the following depth.

After the loop, `current = next_level` advances the frontier, and `result.append(vals)` records the completed row. Either assignment order would work here because both lists have already been fully built and are independent objects.

**Trace through three levels**

For root three with children nine and twenty:

- `current = [3]` produces `vals = [3]` and `next_level = [9, 20]`.
- After replacement, `[9, 20]` produces its row. Nine contributes no children; twenty contributes fifteen and seven, yielding `[15, 7]`.
- That frontier produces `[15, 7]` and an empty next list.

The outer loop ends when `current` becomes empty, after every nonempty level has been recorded.

**Why levels never mix**

The code iterates over `current`, not over the list being appended to. `next_level` is separate. Even while children are discovered, the current loop's input remains unchanged, so a child cannot be visited in its parent's row.

This differs from appending to the same list during iteration, which could extend the loop and blend depths or even create confusing termination behavior.

**Why every node is included once**

The root is inserted once initially. Every other node has one parent and is appended once when that parent is processed. A node in `current` contributes one value and is never placed back into the same or an earlier frontier.

Induction over depths proves the invariant: the root frontier is correct; processing a correct frontier appends real children in correct parent and child order, creating a correct next frontier. Thus all returned rows have the required depth and left-to-right ordering.

Consider a sparse frontier containing parents `A`, `B`, and `C`. If `A` has only right child `x`, `B` has none, and `C` has children `y` and `z`, the next list becomes `[x, y, z]`. Missing positions create no entries, but `x` still precedes `y` and `z` because parent `A` precedes parent `C`. This is exactly the horizontal left-to-right order; null placeholders are unnecessary.

The top-level `TreeNode` definition supplies the platform-like node fields and is not a separate part of the traversal.

## Complexity detail

Each of the $n$ nodes is visited once, has its value appended once, and has at most two child checks, so time is $O(n)$.

Let $w$ be maximum tree width. `current` and `next_level` coexist during a transition. Their combined number of node references is bounded by a constant multiple of the maximum adjacent-level width, hence $O(w)$. `vals` is retained as part of the output once appended.

The manifest's $O(w)$ is the auxiliary frontier bound. The source header's $O(n)$ space statement is a valid looser bound and also matches total memory when the required `result`, containing all $n$ values, is counted.

Plain-list iteration is efficient because no element is removed from the front of `current`. The code scans it once and then discards the whole list reference. Repeated `pop(0)` operations would shift elements and could destroy the linear-time guarantee.

## Alternatives and edge cases

- **Deque with a saved level size:** Keep one queue and process exactly its initial length per outer iteration. It has the same time and frontier bounds.
- **Depth-indexed recursion:** DFS can append into the correct row using a depth parameter, using $O(h)$ call-stack space.
- **Sentinel separator:** Put a marker after each BFS level. It works but introduces special marker handling that two frontier lists avoid.
- **Empty root:** Returns no rows.
- **Single root:** One frontier produces one one-value row.
- **Wide tree:** Frontier memory reaches $O(w)$, which can be $O(n)$ for a nearly complete last level.
- **Skewed tree:** Width is one, so frontier auxiliary storage remains constant.
- **Missing children:** They are skipped; output contains values only, not serialization placeholders.
- **Order guarantee:** Left child must be appended before right child for each parent.
- **Separate list identity:** `next_level` must be newly allocated each iteration. Clearing the active `current` object while iterating would destroy the frontier.
- **Independent output rows:** A fresh `vals` prevents later levels from modifying an earlier row already stored in `result`.
