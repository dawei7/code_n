## General

Create one result object and scan the receiver from left to right. For each item, call `fn(item)` exactly once to obtain its string key. If the result does not yet own that key, define an empty array for it; then append the current item to that array.

**Stable order follows directly from the traversal**

Consider any one selector key. The algorithm encounters precisely the source items assigned to that key in increasing source-index order, and it appends each encounter to the end of the same group. That group's final order is therefore the original relative order. Since every item produces one key and is appended once, no item is omitted or duplicated.

Check ownership with `Object.prototype.hasOwnProperty.call`. A truthiness check is less explicit, and the `in` operator would also see inherited names. When a group is first encountered, use `Object.defineProperty` to create an enumerable own data property. This makes strings such as `__proto__` ordinary safe group keys instead of triggering the legacy prototype setter on a plain object.

After the scan, each produced key owns exactly the items for which the selector returned that string. An empty receiver performs no iterations and leaves the result object empty.

## Complexity detail

Let $n$ be the receiver length and treat each callback evaluation as $O(1)$. The method visits and appends each item once, so its expected time is $O(n)$. The returned groups contain all $n$ item references and at most $n$ keys, requiring $O(n)$ output space. Apart from that output, the loop uses $O(1)$ auxiliary state.

## Alternatives and edge cases

- **`reduce`:** An object accumulator can implement the same $O(n)$ method compactly, but a loop makes callback count, stable order, and safe first-key creation easier to inspect.
- **List of key/group pairs:** This avoids object-name collisions, but finding an existing key by linear scan can make distinct groups cost $O(n^2)$ total time.
- **`Map` accumulator:** A `Map` provides clean key handling and insertion order, but the required result is an object, so it still needs a conversion step and string-key semantics must be preserved.
- **Empty receiver:** Return an empty object without calling the selector.
- **Repeated keys:** Reuse the existing array and append; replacing it would discard earlier members.
- **Stable item order:** Traverse left to right and push once. Sorting either the source or a completed group violates the contract.
- **Inherited and special names:** Treat `constructor`, `toString`, and `__proto__` as possible selector outputs, not as existing groups or prototype operations.
- **Arbitrary item types:** Store each original value itself, including objects and nested arrays; do not clone, stringify, or transform group members.
