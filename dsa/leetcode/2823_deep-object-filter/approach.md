## General

**Filter leaves and rebuild containers from the bottom up.** The input is a JSON object or array whose nested values form a tree. The filter function applies to primitive leaves, not to container objects themselves. A container survives only if at least one descendant survives. This makes depth-first recursion a natural fit: children must be filtered before the parent can decide whether it became empty.

Each call determines whether its current container is an array with `Array.isArray(obj)`. It creates an empty result of the same container kind: `[]` for an array or `{}` for an object.

**Use one local insertion helper for two container semantics.** The nested `add` function captures `isArray` and `filtered`.

For arrays, surviving child values are appended with `filtered.push(value)`. Their original numeric positions are intentionally compacted. If indices one and four survive, they become result positions zero and one, matching array filtering behavior.

For objects, a surviving child remains under its original key. The source uses `Object.defineProperty` with `enumerable`, `writable`, and `configurable` all true. This produces an ordinary visible data property while safely handling a key such as `"__proto__"`; simple assignment to that name could invoke the inherited prototype setter.

**Distinguish containers from primitive leaves.** The loop reads every own enumerable `[key, value]` through `Object.entries(obj)`.

If `value !== null && typeof value === "object"`, it is treated as a nested container and recursively filtered. JavaScript reports `typeof null === "object"`, so the explicit null check is essential. A non-null JSON object includes both arrays and ordinary objects.

If recursion returns anything other than `undefined`, the nested container has at least one surviving property and is added to the current result. If recursion returns `undefined`, it became empty and is pruned from its parent.

For a primitive value, including `null`, the source calls `fn(value)`. The leaf is added only when that result is truthy. The contract says the function returns a Boolean, so this is precisely its keep/discard decision.

**Containers are never passed to `fn`.** This explains the fourth example. Even if `fn` is `Array.isArray`, the algorithm does not test arrays themselves. It recursively descends until it reaches the numeric leaf five, for which `Array.isArray(5)` is false. Five disappears; then every containing array becomes empty and disappears in turn, so the top call returns undefined.

**Prune empty structures during return.** After all entries have been processed, `Object.keys(filtered).length > 0` checks whether anything survived. Arrays expose their pushed indices as enumerable keys, so the same check works for both container types. A nonempty result is returned; an empty one becomes `undefined`.

That undefined sentinel is safe for JSON input because JSON does not contain an undefined data value. Therefore, it unambiguously means “this subtree was removed,” rather than a legitimate leaf that should remain.
For a primitive child, the code retains it exactly when `fn` returns true, satisfying the filtering definition. Assume recursive calls correctly filter every nested child. The current call adds exactly the surviving child results, preserving object keys and compacting array order. It excludes every rejected leaf and every child container that became empty. Finally, it returns undefined exactly when no child remains. By induction over tree depth, the top-level result is precisely the deep-filtered structure, with every newly empty ancestor removed.

**The result is a deep structural copy of surviving containers.** The source allocates a new object or array at every visited container. Primitive values are reused because JSON primitives are immutable values. Original containers are never assigned into the result without recursion, so surviving nested structure does not alias the original container nodes.

**Enumeration scope.** `Object.entries` ignores inherited properties, symbols, and non-enumerable fields. Valid JSON objects contain only own enumerable string-keyed data, so this is appropriate. Sparse array holes are skipped and surviving actual entries are compacted.

**Recursion depth is a practical consideration.** The serialized-size bound limits total input but can still permit deeply nested one-child arrays or objects. JavaScript engines impose call-stack limits, so sufficiently extreme depth can throw a stack overflow even though total asymptotic work is linear. An iterative postorder traversal can avoid that limitation.

## Complexity detail

Let $V$ be the total number of container entries plus primitive leaves in the input tree, and let $D$ be maximum nesting depth. Each entry is visited once by its parent's `Object.entries` loop. Every surviving entry is inserted once.

`Object.keys(filtered)` scans the keys of each newly built container. Across the entire tree, the total number of such child-key scans is $O(V)$ because every surviving edge belongs to exactly one parent. Thus total time is $O(V)$, excluding the user-supplied cost of `fn`. If evaluating leaf $u$ costs $F_u$, a fuller bound is $O(V+\sum F_u)$.

The returned filtered tree can contain $O(V)$ entries. Temporary `Object.entries` arrays and recursive frames also consume space. At one time, entries arrays along a recursion path may retain references to siblings; in the worst case total live auxiliary data can be $O(V)$. The call stack is $O(D)$. Overall space including the output is $O(V+D)=O(V)$ because $D\le V$.

No mutation of the original tree reduces or changes these bounds.

## Alternatives and edge cases

- **Iterative postorder traversal:** Use an explicit stack with enter/exit markers to process children before parents. This preserves $O(V)$ work and avoids native call-stack overflow at the cost of more bookkeeping.
- **Mutate the input in place:** Deleting rejected object properties and splicing arrays can save output allocations, but it changes caller-owned data and array deletion must be handled carefully to avoid skipped indices.
- **Call `fn` on containers:** That is a different contract. The exact solution filters only primitive leaves, which is why an array predicate does not preserve arrays by itself.
- **Null leaf:** The explicit null guard routes it to `fn` rather than attempting `Object.entries(null)`.
- **Empty input container:** No properties are added, so the top-level result is undefined.
- **Nested container becomes empty:** Its recursive undefined result prevents the parent from retaining an empty placeholder.
- **Array compaction:** Removed entries do not leave holes; surviving values are pushed in original enumeration order.
- **Object key preservation:** Surviving properties retain their names, including special strings handled safely by `defineProperty`.
- **False, zero, and empty string:** They are primitive leaves and may survive if `fn` explicitly returns true; the code tests `fn`'s result, not the leaf's own truthiness.
- **Undefined input outside JSON:** The return sentinel would be ambiguous with a legitimate undefined leaf, which is why the JSON guarantee matters.
- **Deep nesting:** Recursive correctness remains valid, but engine stack limits may require an iterative implementation.
- **Input preservation:** Every surviving container is newly allocated, so structural mutations to the result do not directly mutate the original containers.
