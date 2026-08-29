## General

**General arguments require identity-aware keys**

Unlike a numeric-only memoizer, this function may receive values of any type. Two object arguments count as identical only when they are the same reference under `===`.

Serialization is therefore not safe:

- two distinct empty objects both stringify as `"{}"` but are not identical;
- the same object reference must hit the same cache path;
- argument order and argument count must remain distinct.

The solution represents an argument tuple as a path through nested `Map` objects. Each path edge is keyed by one actual argument value, so JavaScript's map-key identity semantics do the matching.

**The nested maps form a trie of argument sequences**

`root` is a `Map` representing the empty argument prefix.

For arguments $(a_0,a_1,\ldots,a_{k-1})$, the wrapper walks:

$$
\texttt{root}
\xrightarrow{a_0}
M_1
\xrightarrow{a_1}
M_2
\cdots
\xrightarrow{a_{k-1}}
M_k.
$$

If an edge does not exist, `node.set(arg, new Map())` creates the next map. Tuples sharing a prefix share the corresponding initial maps.

For example, tuples `(objectA, 1)` and `(objectA, 2)` share the edge for `objectA` and diverge at their second arguments. Tuple `(objectB, 1)` begins on a different root edge if `objectB !== objectA`.

**Store the result at the terminal node**

After every argument has been consumed, `node` represents exactly that full tuple. The solution needs a marker key that cannot be confused with another argument edge.

`const resultKey = Symbol('result')` creates a unique symbol held privately inside the closure. The terminal map stores the cached value under that symbol.

Even if a caller supplies another symbol with the same description, it has different identity. The closure's symbol is never exposed, so user inputs cannot intentionally reproduce it.

This design also distinguishes a tuple from its prefix. A result for one argument is stored at the map reached after one edge, while a two-argument tuple continues through a second edge from that same node.

**Why membership is checked separately from value**

The wrapper uses:

`if (node.has(resultKey)) return node.get(resultKey)`.

A legitimate result can be undefined, null, false, zero, or an empty string. Checking the retrieved value's truthiness would incorrectly treat such cached results as misses.

The marker's presence records that `fn` has already been called for this tuple, independent of its result.

**Compute a miss with the original receiver**

On a cache miss, the exact implementation invokes:

`fn.apply(this, args)`.

`args` preserves positional order, and `apply` forwards the memoized wrapper's dynamic `this` receiver to the original function.

This is more general than `fn(...args)` for method-like functions. However, the cache path is based only on arguments, not on `this`. Under the stated contract, inputs are the argument list; if a function's output also depends on receiver identity, a fully general utility would need to include `this` in the key.

The result is stored at the terminal node and returned.

**How `Map` matches the required equality**

JavaScript `Map` uses SameValueZero comparison. For almost all values this agrees with `===`:

- primitive values match equal primitives;
- object and function values match only the same reference;
- different objects remain distinct.

SameValueZero treats `NaN` as equal to itself, unlike `===`, but the constraints explicitly exclude `NaN` inputs. It also treats positive and negative zero as equal, as `===` does. Therefore, map keys implement the required identity relation throughout the allowed domain.

**Trace the distinct-object example**

Suppose three calls each receive two newly created empty objects.

On the first call, neither object key exists, so two map edges are created and the result is stored.

On the second call, its first empty object is a different reference from the first call's object. Root lookup misses immediately, creating a separate path. The original function runs again.

This repeats for the third call, giving three underlying calls even though every object has the same visible properties.

If instead all calls reuse one object `o` as both arguments, every call follows the same two edges keyed by `o`. After the first result is stored, later calls hit the terminal marker.

**Zero-argument functions work naturally**

When `args` is empty, the loop creates no edges and terminal `node` remains `root`. The first call stores the result under `resultKey` at the root. Every later zero-argument call finds it there.

No special tuple encoding or empty-key string is needed.

**A trie invariant proves correctness**

Maintain:

> Every path from `root` corresponds to exactly one encountered argument prefix, and a terminal node contains `resultKey` exactly when `fn` has been evaluated for that complete tuple; the associated value is the first returned result.

Creating a missing edge adds the exact next argument to one prefix without affecting other paths. A hit returns the recorded result. A miss calls `fn` once and adds the marker only at that tuple's terminal node.

Thus identical argument sequences always reach the same cached result, while any difference in count, order, primitive value, or reference identity follows a different terminal path.

**Prefix sharing saves structure**

If many tuples begin with the same arguments, their first maps are shared. This can use less space than storing a completely independent key object for every tuple.

The worst case still creates one map edge per argument of every distinct tuple, which is why the space bound depends on both tuple count and arity.

**Memory lifetime**

Ordinary `Map` holds strong references to object keys. As long as the memoized wrapper and its root remain reachable, cached argument objects may remain reachable too.

This is correct for the challenge. A long-lived production memoizer might mix `WeakMap` for object keys, impose cache limits, or expose invalidation to control memory.

## Complexity detail

Let $a$ be the number of arguments in one call. The wrapper performs one expected $O(1)$ map operation per argument and one terminal lookup, for expected $O(a)$ cache-navigation time, plus the cost of `fn` on a miss.

For $u$ distinct argument tuples of maximum or average arity $a$, the worst case creates $O(ua)$ map nodes and edges, so cache space is $O(ua)$. Shared prefixes can reduce actual usage.

The temporary rest-argument array uses $O(a)$ space per invocation.

## Alternatives and edge cases

- **`JSON.stringify(args)`:** Incorrect for unrestricted objects because distinct references can serialize identically.
- **Linear list of prior tuples:** Preserves identity but may require $O(ua)$ comparisons per call.
- **Weak-map hybrid:** Can allow object-key paths to be garbage-collected, but primitive keys still require ordinary maps and implementation becomes more complex.
- **Same object reused:** It follows the same map edge and produces cache hits.
- **Structurally equal new objects:** Their references differ, so they correctly follow different paths.
- **Argument order:** Each position is a separate trie level, so `(a,b)` differs from `(b,a)`.
- **Different arity with common prefix:** Results live at different terminal nodes or marker positions.
- **Zero arguments:** The cached result is stored directly on the root.
- **Falsy or undefined result:** Marker membership prevents recomputation.
- **Receiver-dependent function:** `this` is forwarded for execution but not included in the cache key, consistent with the stated argument-only identity contract.
