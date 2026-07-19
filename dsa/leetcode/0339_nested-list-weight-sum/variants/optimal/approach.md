## General
**Carry the current depth through the traversal**

The nested input is naturally a forest: each integer is a value node, while each list owns the nodes one level below it. The only context an integer needs is the depth of the list that directly contains it, so a depth-first traversal can carry that depth as a parameter.

Begin with depth `1` for the outermost list. For each element:

- If it is an integer, add `integer * depth` to the running total.
- If it is a list, recursively process its children at `depth + 1`.

**Trace one chain of nested lists**

For `[1, [4, [6]]]`, the traversal adds `1` at depth `1`, descends once to add `8` for the `4`, then descends again to add `18` for the `6`. The three contributions total `27`.

**Why every integer contributes exactly once**

Each recursive call returns the complete weighted contribution of its own nested list at the supplied depth. This statement is immediate for an empty list. For a non-empty list, integer elements contribute exactly their required weighted values, and recursive elements return the correct contributions of all descendants one level deeper. Adding those disjoint contributions therefore gives the correct sum for the current list and, at depth `1`, for the entire input.

## Complexity detail
Let `N` count every integer and list entry visited by the traversal, and let `D` be the maximum nesting depth. Each element is inspected once, so the running time is $O(N)$. A depth-first traversal keeps at most one recursive frame per nesting level, using $O(D)$ auxiliary space. The result itself is a scalar.

## Alternatives and edge cases
- **Breadth-first traversal:** is equally valid and remains $O(N)$ time, but its queue may hold an entire level and use $O(W)$ space for maximum width `W`.
- **Explicit depth-first stack:** avoids recursion but can still hold $O(N)$ pending elements in the worst case.
- **One traversal per depth:** can cost $O(ND)$ because the same structure is revisited for each of `D` levels.
- Zero contributes nothing at any depth, while a negative integer retains its sign after weighting.
- Empty nested lists contribute zero and should not alter the total.
- A deeply nested single integer must be multiplied by every containing level, including the outermost list.
