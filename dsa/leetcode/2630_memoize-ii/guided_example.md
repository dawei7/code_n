# Guided Example: Memoize II

## 1. The instance and the outcome to derive

A memoized function must never run its underlying work twice on identical inputs; it returns the cached value instead. Identical here does **not** mean structurally similar: the statement defines two inputs as identical when they are `===` to each other, so two separately constructed objects with the same contents are different inputs, while one object passed twice is the same input twice. The memoized function may accept any number of arguments of any type, and every distinct argument tuple is its own cache entry.

The instance traced here merges pairs of objects. Two shared references are created once — `left` holding `{x: 1}` and `right` holding `{y: 2}` — together with structurally equal but separately constructed copies `leftCopy` and `rightCopy`. The call plan and the required outcome are:

| Call | Arguments | Required value | Underlying work allowed |
|---|---|---|---|
| 1 | `left`, `right` | `{x: 1, y: 2}` | yes, this tuple is new |
| 2 | `left`, `right` | `{x: 1, y: 2}` | no, both references were already seen together |
| 3 | `left`, `rightCopy` | `{x: 1, y: 2}` | yes, `rightCopy` is a different object from `right` |
| 4 | `leftCopy`, `right` | `{x: 1, y: 2}` | yes, `leftCopy` is a different object from `left` |

The final call must return `{x: 1, y: 2}` and the underlying function must have run exactly `3` times. The instance is chosen because it mixes identity and structure in one plan: calls 1 and 2 differ only in whether the references were seen before, while calls 3 and 4 keep one shared reference and replace the other with a look-alike.

## 2. The key is a path, not a string

Because an argument may be any value, including an object with no natural textual form, the cache cannot flatten a tuple into a printable key without losing the identity distinction the statement requires. The structure that preserves it is a tree of lookup nodes: one level per argument, and one child per distinct argument reference observed at that level.

| Element of the structure | Role | Why it is needed |
|---|---|---|
| root node | stands for the empty prefix of every argument tuple | it is also the entry point for a zero-argument call |
| one node per argument position | a distinct child is created the first time a given argument reference appears at that position | object arguments are distinguished by identity rather than by contents |
| terminal marker inside a node | records that the tuple ending at this node has a computed result | a node can be both a prefix of longer tuples and the end of a shorter one, so "prefix exists" must be distinguished from "result computed" |
| stored result | the value the underlying function produced for that exact tuple | includes falsy values such as `false` and `undefined`, which are legitimate cached results |

The lookup depth of a tuple is its arity, so tuples of different lengths end at different nodes and can never collide.

## 3. Step-by-step trace of the instance

| Call | Path walked from the root | Work performed | Terminal marker state | Underlying calls so far |
|---|---|---|---|---|
| 1 | `left`, then `right` | both levels are new, so nodes are created for `left` and for `right` beneath it; the underlying merge runs and its result is stored at the end of the path | newly set at `left` then `right` | 1 |
| 2 | `left`, then `right` | the same two nodes are found, the terminal marker is already present, and the stored result is returned | unchanged | 1 |
| 3 | `left`, then `rightCopy` | the `left` level already exists and is reused; `rightCopy` is a different reference, so a new child node is created and the merge runs again | newly set at `left` then `rightCopy` | 2 |
| 4 | `leftCopy`, then `right` | the root has no child for `leftCopy`, so a new branch is created; `right` is then a new child of that node | newly set at `leftCopy` then `right` | 3 |

The final state of the cache, with three terminal markers, is a small tree rather than a flat table:

```text
root
  |-- left -------- right      [result {x:1, y:2}]
  |                 rightCopy  [result {x:1, y:2}]
  |-- leftCopy ---- right      [result {x:1, y:2}]
```

Node `left` proves the point of the design: it is simultaneously an interior node on two cached paths and, if the memoized function were later called with `left` alone, the place where a result for that shorter tuple would be stored. The stored value for calls 3 and 4 is the same object content as call 1, yet each was computed separately, because the argument references differ.

## 4. The cache invariant and correctness

Let the *signature* of a call be its argument tuple, with equality defined position by position using the strict identity the statement specifies. The cache maintains one invariant:

> For every signature $s$ that has been called, the node reached by walking $s$ from the root holds a terminal marker, and the value stored behind that marker is the value the underlying function produced for $s$. No node holds a result for a signature that was never called.

**Hits are sound.** A returned value is only ever read from a terminal marker that was written by an earlier call. That earlier call had exactly the same references in exactly the same positions, because the walk compares each argument against the children of the current node one position at a time; a differing reference at any position diverts the walk to a different node or to no node at all. So every hit returns the result of the same signature, which is what memoization promises.

**Misses are complete.** If a signature has never been called, then either some level of the walk has no matching child — which happens for a never-seen reference — or the walk reaches an existing node that carries no terminal marker, which happens when every argument was seen before but never as this exact tuple, for instance `left` alone after `left` `right` was cached. Both situations produce a miss, so no uncomputed signature can be served from the cache.

**Falsy results survive.** The marker is tested for presence, not for truthiness, so a cached `false`, `0`, empty string, or `undefined` is returned as a hit. A truthiness test would silently recompute those signatures on every call and break the "never called twice" guarantee.

**Termination and stability.** Each call walks a fixed number of levels — one per argument — and each level performs a constant lookup, so the walk always finishes. Nodes are only ever added, never removed, and a node's stored result is never overwritten by a later call, because a later call with the same signature short-circuits before reaching the underlying function. The cache is therefore monotone: it grows with the number of distinct tuples and never changes a value it has already committed.

## 5. Boundary and trap analysis

| Situation | Concrete plan | Observed outcome | The trap it exposes |
|---|---|---|---|
| Structurally equal but fresh objects | three calls, each passing two newly built empty objects | the underlying function runs 3 times | structural similarity is irrelevant; only identity decides, so all three tuples are distinct |
| Repeated shared references | three calls, all passing the same two objects | the underlying function runs 1 time | the same tuple reaches the same node every time, so the marker is found immediately |
| Argument order | `(1, 2)`, `(2, 1)`, `(1, 2)` | two underlying calls, final value `3` | order is part of the signature: the two tuples occupy different branches and only the repeat of the first one hits |
| Different arity | `(7)`, `(7)`, `(7, 8)`, `(7, 8)` | two underlying calls, final value `2` | tuple length is part of the signature; `(7)` ends at the node for `7`, while `(7, 8)` continues one level deeper |
| No arguments at all | three calls with an empty argument list | one underlying call, final value `7` | the empty tuple is cached at the root itself, so the root must be able to hold a terminal marker |
| A result of `undefined` | three calls with `(5)` where the underlying function returns nothing | one underlying call, value `undefined` | presence of the marker, not the value, decides a hit |
| A result of `false` | two calls with `(0)` where the underlying function returns `false` | one underlying call, value `false` | a falsy result is a cacheable result like any other |
| Number against string | `(1)`, `("1")`, `(1)`, `("1")` | two underlying calls, final value `"1"` | identity is strict, so a number and its textual form take different branches |
| Value serving as both prefix and result | caching `left` `right` and later calling with `left` alone | the second call misses and computes | an interior node is not a cache entry; the terminal marker is a separate fact from the node's existence |

## 6. Alternatives this instance eliminates

| Alternative | Behaviour here | Why it is eliminated |
|---|---|---|
| Serializing the arguments to a string | would report calls 3 and 4 as hits for call 1 | serialized text cannot see reference identity, so look-alike objects collapse into one entry |
| Joining the arguments with a separator into one flat key | same collapse, plus collisions when an argument's own text contains the separator | it inherits every weakness of serialization and adds ambiguity |
| A single flat lookup with numeric coercion | would treat the tuple carrying `1` and the tuple carrying `"1"` as one signature | identity is strict, and the corpus pins that the number and its textual form are different inputs |
| A recursive lookup that treats a returned child as a result | would return an internal node as the cached value for a shorter tuple | a node's existence means a prefix was seen, not that a value was computed |
| Testing the stored value for truthiness to decide a hit | would recompute the `undefined`, `false`, and `0` cases on every call | the contract forbids a second call with the same inputs regardless of the result's truthiness |
| A per-arity map plus one shared cache | correct for one arity but wrong as soon as tuples of different lengths share a prefix | the signature includes the length, and a single tree handles every arity uniformly |

## 7. Time and auxiliary space complexity

Let $A$ be the total number of argument values passed across the whole call plan, bounded by $0 \le \text{inputs.flat}().length \le 10^{5}$, and let $d$ be the arity of a single call. One call walks $d$ levels and performs a constant lookup per level, so producing the answer for a call costs $O(d)$ expected time — the caveat is the ordinary expected cost of a hash lookup, not a worse worst case — and the whole plan costs $O(A)$ expected time, because each argument value is visited once per call that carries it. No call ever scans the cache: the walk visits only the nodes on its own path, which is what separates this structure from a linear search over stored signatures.

The auxiliary space is the cache itself, whose size is bounded by the number of distinct prefixes observed. Every new prefix consumes exactly one node created while processing one argument occurrence, so with $A \le 10^{5}$ argument occurrences the tree holds at most $A + 1$ nodes, counting the root; the argument tuples whose arity is $0$ add nothing beyond the root's own terminal marker. Each node stores one lookup table for its children and, once computed, one result, so the total retained state is $O(A)$, and the working memory of an individual call beyond the cache is $O(1)$: a single cursor walks the path level by level.
