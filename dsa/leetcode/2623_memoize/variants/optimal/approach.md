## General

The wrapper needs private state that survives between calls, so create a `Map` in `memoize` and return a closure over it. Each exact ordered argument tuple must map to one saved result. Because every legal argument is a number, `JSON.stringify(args)` gives a stable representation that preserves both arity and order: `[3,2]` differs from `[2,3]`, and `[2]` differs from `[2,0]`.

On each wrapper call, serialize the argument array and test `cache.has(key)`. Membership must be checked explicitly rather than testing the cached value's truthiness, because a correct result can be `0`. If the key exists, return its value immediately. Otherwise invoke `fn` with the original arguments, store the result, and return it.

The cache belongs to one memoized wrapper. Different calls to `memoize` therefore do not share results. After the first call for a tuple, the map permanently records its result, so induction over later calls shows that `fn` is never invoked twice for that tuple.

## Complexity detail

The legal functions accept at most two bounded integers, so serializing a tuple takes bounded constant work. With expected constant-time map operations, a cache hit takes expected $O(1)$ time; a miss adds the time required by `fn` itself. If $u$ distinct tuples have appeared, the cache uses $O(u)$ space.

The bounded-domain certificate records why the usual argument-serialization factor is constant for this specific contract rather than claiming that arbitrary JavaScript arguments can always be keyed in constant time.

## Alternatives and edge cases

- **Nested maps:** A trie of maps keyed by individual arguments avoids serialization and generalizes better to object identity, but is more machinery for at most two numeric arguments.
- **Plain object cache:** This can store string keys, but a `Map` avoids prototype-name collisions and provides explicit membership semantics.
- **Commutative sum key:** Sorting sum arguments would reuse `(3, 2)` for `(2, 3)`, directly violating the requirement that ordered tuples remain distinct.
- **Falsy cached result:** Use `cache.has`, since `0` must not be mistaken for a miss.
- **Recursive functions:** Only top-level calls to the returned wrapper are memoized; recursion performed internally by the supplied function belongs to one underlying invocation.
- **Independent wrappers:** Each invocation of `memoize` must create its own cache closure.
