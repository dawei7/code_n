## General

**Cache by the complete ordered argument tuple**

A memoized function should call `fn` only the first time a particular input tuple appears. Later calls with the same inputs must return the stored result.

For this problem, arguments are integers and the supported functions take either one or two arguments. The order matters: `sum(3, 2)` and `sum(2, 3)` must occupy different cache entries even though their mathematical results happen to match.

The solution converts the entire argument array to a JSON string and uses that string as a `Map` key.

Examples include:

- arguments `[2, 2]` become key `"[2,2]"`;
- arguments `[1, 2]` become `"[1,2]"`;
- arguments `[2, 1]` become `"[2,1]"`.

These strings preserve argument count, order, signs, and numeric values under the stated input domain.

**Create one private cache per memoized function**

Calling `memoize(fn)` creates `const cache = new Map()` and returns an inner function.

The inner function closes over both `fn` and `cache`. Those references remain available after `memoize` returns, while callers cannot directly mutate the map.

Each separate call to `memoize` creates a separate map. Memoizing two different functions therefore cannot cause one function's result to be returned for the other, even if they receive identical arguments.

**Collect arbitrary arguments with rest syntax**

The returned function is declared as `function(...args)`. Rest syntax gathers the invocation's positional arguments into a new array in their original order.

That array serves two purposes:

- `JSON.stringify(args)` creates the cache key;
- `fn(...args)` spreads the same values back into positional arguments for the original function.

The wrapper does not reverse, sort, or otherwise normalize arguments. This preserves the contract's distinction between $(a,b)$ and $(b,a)$.

**Check membership, not cached-value truthiness**

The code uses:

`if (cache.has(key)) return cache.get(key);`

This two-step pattern is important. A valid function result might be zero, false, an empty string, null, or undefined in a more general memoizer. Testing `cache.get(key)` in a Boolean condition would mistake falsy cached results for misses and call `fn` again.

`Map.has` records whether the tuple was computed, independently of what value was stored.

For the three functions in this challenge, results are numeric, but using membership still gives the correct general cache semantics.

**Compute only on a cache miss**

If the key is absent, the wrapper evaluates `fn(...args)` exactly once, stores that result under the key, and returns it.

The store happens before the wrapper finishes, so every later call with the same serialized tuple follows the hit branch.

The underlying factorial and Fibonacci functions supplied by the harness may themselves perform recursive work internally, but one top-level invocation of the memoized wrapper counts as one call to `fn`. The wrapper caches the final returned result for that argument list.

**Why JSON serialization is safe here**

General-purpose memoization cannot blindly serialize arbitrary JavaScript arguments because:

- object property order and identity may matter;
- unsupported values can disappear or collide;
- cyclic objects cannot be stringified;
- different values can share a serialization.

This problem restricts arguments to small tuples of integers. JSON arrays of finite integers have an unambiguous representation, so distinct ordered tuples create distinct strings.

That scope distinction is essential. The same method is appropriate for problem 2623 but not for the unrestricted identity semantics of a general memoizer.

**Trace a cache hit**

Suppose `memoizedSum(2, 2)` is called for the first time.

1. `args` becomes `[2,2]`.
2. The key becomes `"[2,2]"`.
3. The map does not contain it.
4. `fn(2, 2)` returns four.
5. Four is stored and returned.

On the second identical call, the key is the same. `cache.has` is true, so the wrapper returns the stored four without invoking `fn`.

A call with `(1,2)` produces a different key and causes one new underlying evaluation.

**Why equal results do not imply equal inputs**

Memoization is keyed by input identity under the problem's definition, not by output value.

For example, `sum(1, 2)` and `sum(2, 1)` both return three. They must still trigger separate first computations because their ordered arguments differ. The serialized keys make that distinction automatically.

Similarly, factorial of two and a hypothetical different input yielding two would not share a record unless their complete argument arrays were identical.

**A cache invariant proves correctness**

Maintain this statement:

> For every key in `cache`, its value is exactly the result returned by the first call to `fn` with the corresponding ordered argument tuple; no tuple absent from the map has yet been computed through this wrapper.

The empty map satisfies the invariant. A hit returns the recorded correct result without changing state. A miss computes the tuple once and adds exactly its result, preserving the statement.

Therefore, all wrapper return values match `fn`, and no tuple causes more than one underlying call.

**Purity assumption**

Memoization is behavior-preserving only when repeated calls with the same arguments are expected to have the same relevant result and side effects are not meant to repeat. The three supplied functions are deterministic mathematical functions.

The observed call count intentionally changes: avoiding repeated execution is the point of the task.

## Complexity detail

Let $a$ be the number of arguments and $L$ the length of their serialized representation. Creating the key takes $O(L)$ time, map lookup is expected $O(L)$ for hashing/comparison in a precise string-cost model, and a miss additionally pays the cost of `fn`.

Under this problem's fixed one- or two-integer argument shapes and bounded numeric representation, key work is treated as $O(1)$ per wrapper call, matching the manifest.

If $u$ distinct tuples have appeared, the map stores $u$ keys and results, using $O(u)$ cache entries. Serialized key characters add storage proportional to their total length.

## Alternatives and edge cases

- **Nested maps by argument:** Avoid serialization and support identity-based objects, but add structure unnecessary for bounded integer tuples.
- **Concatenate with a delimiter:** Easy to implement incorrectly because signs, lengths, or delimiters can create collisions; JSON supplies unambiguous tuple syntax.
- **Cache by result:** Incorrect because different inputs may produce the same output and still require separate first calls.
- **Reversed sum arguments:** They serialize differently and must be cached separately.
- **Falsy cached result:** `cache.has` prevents accidental recomputation.
- **First call:** It always invokes `fn` and stores the returned value.
- **Repeated call:** It returns the stored result without invoking `fn`.
- **Separate memoized functions:** Each owns an independent closure cache.
- **Recursive work inside `fn`:** The wrapper caches the top-level result; it does not rewrite internal recursive calls.
- **Arbitrary objects:** Outside this problem's numeric scope, JSON serialization would not preserve strict identity and should not be used.
