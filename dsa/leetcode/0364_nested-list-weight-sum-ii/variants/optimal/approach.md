## General
**Collect sums by integer depth**

Inverse weights are not known until the deepest integer is known. Traverse the nested structure once with depth-first search, starting the outer list at depth `1`. Maintain an array where entry $d - 1$ accumulates integers found at depth `d`, and track the greatest depth at which an integer actually appears.

Entering an empty list may increase structural nesting, but it does not change the maximum integer depth. Updating the maximum only when an integer is visited preserves that distinction.

**Convert depth totals into inverse weights**

After the traversal, let `D` be the maximum integer depth. The accumulated sum at depth `d` receives weight $D - d + 1$. Multiply each depth total by its weight and add the results. Grouping integers by depth is valid because every integer at the same depth has the same inverse weight.

**Why every contribution gets the required weight**

The depth-first traversal visits each integer exactly once and adds it to exactly one depth bucket. The tracked `D` is the deepest level containing any integer, so the postprocessing formula assigns weight one there, two one level above, and so on through the outermost integer level. Distributing multiplication over each bucket sum gives the same result as weighting each contained integer individually, including negative and zero values.

**Trace three levels**

For `[1,[4,[6]]]`, the depth sums are `[1,4,6]` and $D = 3$. Their weights are `3,2,1`, producing $1 \cdot 3 + 4 \cdot 2 + 6 \cdot 1 = 17$.

## Complexity detail
Let `N` count all visited integer and list entries and `D` be the maximum structural nesting depth. The traversal is $O(N)$, and combining at most `D` depth buckets is also within $O(N)$. The depth-sum array and recursive call stack use $O(D)$ auxiliary space.

## Alternatives and edge cases
- **Breadth-first cumulative sums:** adding the running unweighted sum once per level yields inverse weights in one pass, but trailing empty-only levels must not inflate the maximum integer depth.
- **Two-pass depth-first search:** can first find maximum integer depth and then compute weights, remaining $O(N)$ but revisiting the structure.
- **Traverse separately for every depth:** repeats shared prefixes and can degrade to $O(ND)$.
- Empty nested lists contribute nothing and do not establish a deeper integer level.
- Negative integers retain their sign after inverse weighting.
- A single integer, regardless of structural position, has weight one when it is the only integer.
- Several integers at the deepest level all receive weight one.
