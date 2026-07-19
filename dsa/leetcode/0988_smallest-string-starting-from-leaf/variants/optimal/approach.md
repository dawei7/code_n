## General
**Maintain one root-to-current path:** Perform depth-first traversal with explicit enter and exit stack events. On entry, append the node's letter to one mutable path. Schedule its exit event before its children; on exit, remove the letter. This reproduces recursive backtracking without risking Python's recursion limit on a deeply skewed tree.

**Reverse only at leaves:** When a node has no children, the maintained path runs from root to leaf, opposite the requested direction. Read it in reverse and join its letters into the leaf-to-root candidate. Compare that candidate with the smallest one seen so far.

Every leaf is reached exactly once, and at that moment the path contains exactly its ancestors in root-to-leaf order. Reversing therefore creates precisely that leaf's required string. Taking the minimum over all such candidates returns the global lexicographic minimum, including the rule that a shorter matching prefix wins.

## Complexity detail
Tree traversal itself is $O(N)$. Constructing and comparing a leaf candidate can inspect up to $H$ characters, and there can be $O(N)$ leaves, giving the safe bound $O(NH)$ time. The traversal stack and mutable path each contain at most $O(H)$ entries; the best string also has length at most $H$, so space is $O(H)$.

## Alternatives and edge cases
- **Collect and sort every leaf string:** This is correct but stores all candidates and adds sorting work when only the minimum is needed.
- **Recursive backtracking:** The logic is compact, but a skewed tree near $8500$ nodes can exceed the language recursion limit.
- **Build a new path string at every node:** Immutable concatenation duplicates prefixes and can use substantially more memory than one mutable path.
- **Single node:** The root is also the only leaf, so its one-letter string is returned.
- **Prefix tie:** If one leaf string is a complete prefix of another, normal string comparison correctly selects the shorter one.
