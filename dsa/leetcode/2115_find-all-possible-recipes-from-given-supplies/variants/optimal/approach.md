## General

**Reverse each requirement**

Treat every available item as a fact that can satisfy recipe requirements. For
each ingredient name, store the recipes that depend on it. Also store, for
each recipe, how many of its required ingredients have not yet become
available.

Initialize a queue with all supplies. When an item leaves the queue, visit
each recipe waiting for that item and decrease its missing count once. If a
count becomes zero, every distinct requirement of that recipe has now been
processed. Add the recipe to the answer and to the queue, because its name can
serve as an ingredient for other recipes.

Each requirement edge is processed only when its ingredient becomes
available. A recipe is released exactly after all its edges have been
satisfied, so every returned recipe is constructible. Conversely, consider
any constructible recipe in an order that prepares all of its prerequisite
recipes first. Its initial supplies and those earlier recipes all enter the
queue, which eventually removes every missing requirement and releases it.
Thus every constructible recipe is returned. A cycle without an available
entry point retains positive missing counts and is correctly excluded.

## Complexity detail

Let $V$ be the number of distinct item names and $E$ the total number of
ingredient occurrences. Building and traversing the reverse graph processes
each relevant name and each requirement once, for $O(V + E)$ time. The graph,
missing counts, queue, and result use $O(V + E)$ space.

## Alternatives and edge cases

- **Repeated full scans:** Revisit every unmade recipe and produce those whose
  requirements are currently available. This reaches the same fixed point but
  may rescan all $E$ requirements for each dependency level, taking
  $O(nE)$ time.
- **Depth-first dependency resolution:** Memoized DFS with three-state cycle
  detection also takes $O(V + E)$ time and space, but its cycle and missing
  external-item handling is more intricate.
- An ingredient name that is neither an initial supply nor a preparable recipe
  can never enter the queue.
- A recipe cycle is not inherently productive; it needs dependencies that can
  all be satisfied without relying solely on that unresolved cycle.
- Several recipes may wait for the same item, and one newly available recipe
  must update every such dependent.
- The answer order is unrestricted, so queue discovery order does not need to
  match the input order.
