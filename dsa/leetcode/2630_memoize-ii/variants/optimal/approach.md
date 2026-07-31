## General

A serialized composite key cannot preserve the required relation. Stringification merges distinct object references that happen to have equal properties, and separator-based encodings can collide. Instead, represent an argument tuple as a path through a trie whose edges are JavaScript `Map` keys.

Start with one root `Map`. For each argument, use that argument itself as the key into the current map, creating a child `Map` when the edge is absent. JavaScript `Map` key matching follows SameValueZero; because the contract excludes `NaN`, this agrees with `===` for every allowed argument, including identity-based matching for objects and functions.

**Tuple boundaries and cached values remain unambiguous**

After all arguments have been consumed, the reached map represents exactly that complete tuple. Store its computed result under a private `Symbol`. This distinguishes `[x]` from `[x, y]`, even though the first tuple's terminal map can also contain an edge for `y`.

Use `node.has(resultKey)` to test whether the result exists. Checking the stored value itself would recompute valid cached results such as `false`, `0`, `null`, or `undefined`. On a miss, call `fn` with `fn.apply(this, args)`, store the result, and return it. On a hit, return the saved result immediately.

Every strictly identical tuple follows the same sequence of map edges and reaches the same terminal node. Conversely, any difference in arity, position, primitive value, type, or object identity changes or extends that path. Therefore a hit occurs exactly for the input tuples the contract defines as identical.

## Complexity detail

Let $a$ be the number of arguments in the current invocation and $u$ the number of distinct tuples cached. Descending one map edge per argument takes expected $O(a)$ time. A cache hit needs no call to the wrapped function; a miss adds the cost of that function separately from the memoization overhead.

Each distinct tuple can create at most $a$ new map nodes, so the cache occupies $O(u a)$ space in the worst case. Shared prefixes reduce the actual number of nodes. The returned closure also retains each argument used as a map key and each cached result.

## Alternatives and edge cases

- **Linear list of prior calls:** Keeping saved argument arrays and comparing them element by element is correct, but a new tuple may scan all $u$ entries, giving $O(u a)$ lookup time and quadratic total work across distinct calls.
- **`JSON.stringify` key:** Serialization loses reference identity, cannot represent every JavaScript value, and may depend on property order, so it does not implement positional `===` semantics.
- **Nested `WeakMap` only:** A `WeakMap` accepts only object keys, while valid arguments also include primitives; a mixed structure is possible but unnecessary because `Map` handles both kinds.
- **Different arities:** A private terminal marker keeps a tuple distinct from every strict extension of that tuple.
- **Falsy and `undefined` results:** Test key presence with `has`; never use result truthiness to decide whether computation already occurred.
- **Object and function arguments:** Cache them by reference. Two separately allocated but structurally identical values must follow different edges.
- **Zero arguments:** The root itself is the terminal node, so repeated empty calls use one cached result.
- **Receiver context:** Forward the miss call with `apply(this, args)` so the first computation observes the wrapper's receiver; later identical calls return that tuple's cached value without invoking `fn` again.
