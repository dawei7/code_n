## General

Recursively process one container at a time. Create an empty array when the current value is an array and an empty object otherwise.

For each child, distinguish a nested container from a primitive leaf. A non-null object or array is filtered recursively. Keep its returned structure only when recursion does not return `undefined`; that condition means at least one descendant survived. For a primitive, call `fn(value)` and keep the value only when the result is true.

Append retained array children with `push`, which compacts removed positions while preserving relative order. Assign retained object children under their original keys. Use an own data-property definition for object keys so valid JSON names such as `__proto__` remain ordinary properties.

After every child has been considered, return the new container when it has at least one enumerable key. Otherwise return `undefined`, allowing the parent to prune that newly empty branch.

**Why bottom-up pruning is necessary**

Whether a container survives is unknown until all of its descendants have been filtered. The recursive call establishes exactly one of two outcomes: a nonempty filtered container, or `undefined` when no descendant passed. A parent therefore keeps precisely the branches containing at least one accepted leaf.

For a leaf, the decision matches `fn` directly. By induction from leaves toward the root, every returned container contains all and only accepted leaves reachable through nonempty branches. Array insertion order and object key assignment preserve the required structure. If the root receives no retained child, the same rule correctly returns `undefined`.

## Complexity detail

Let $V$ be the number of enumerable entries visited and $D$ the maximum nesting depth. Each entry is inspected once and each retained entry is written once, so time is $O(V)$. The filtered output requires $O(V)$ space in the worst case, while the recursive call stack uses $O(D)$ additional space. Because $D le V$, the combined bound is $O(V)$ space.

The benchmarks use nested single-child objects. This traversal performs constant work per level, while a correct alternative that serializes each recursive result to test emptiness repeatedly processes the same suffix at every ancestor and grows quadratically.

## Alternatives and edge cases

- **Serialize to test emptiness:** Checking `JSON.stringify(filtered)` at every recursive return is correct but can take $O(V^2)$ time on a deep chain.
- **Mutate in place:** Deleting properties and splicing arrays can work, but repeated splices shift later entries and may become quadratic while violating the non-mutating expectation.
- **Apply the predicate to containers:** Containers are structural; testing them changes the contract and makes predicates such as `Array.isArray` retain branches without accepted leaves.
- **Use array index assignment:** Preserving original indices leaves holes. Append surviving elements to compact the output.
- **Null:** Although `typeof null === "object"`, JSON `null` is a primitive leaf and must be passed to the predicate.
- **Empty input:** An empty root object or array returns `undefined`.
- **Newly empty branches:** Remove a container even if it was nonempty before filtering.
- **Special object keys:** Keys such as `__proto__` must remain own data properties rather than altering the result's prototype.
- **Input preservation:** Build fresh containers throughout; never delete or overwrite entries in `obj`.

