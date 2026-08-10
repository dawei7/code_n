## General

**Remove falsy children while rebuilding containers**

The function recursively creates a new array or object rather than deleting from the input.

At every container, a child is retained only if the child's original value is truthy. Retained nested containers are then compacted recursively.

The distinction between filtering and recursion order is important because an empty object or array is truthy in JavaScript and must remain present even if all of its own children are removed.

**Base case for primitives and null**

The first condition is:

`if (!obj || typeof obj !== "object") return obj`.

It returns any falsy value immediately and also returns truthy primitives such as numbers and strings.

Under valid JSON, falsy values include `null`, `false`, zero, and the empty string. `undefined` and `NaN` are not JSON values.

The parent container decides whether a falsy child is retained, so returning it here is safe.

**Handle arrays with filter before map**

For an array, the exact expression is:

`obj.filter(Boolean).map(compactObject)`.

`filter(Boolean)` removes every element whose Boolean conversion is false. It also packs surviving values into consecutive indices, which is the required array behavior after removals.

`map(compactObject)` then recursively rebuilds every truthy survivor.

**Why filtering before recursion matters**

Consider nested array `[0]`. The array itself is truthy, so its parent retains it.

Inside that array, zero is filtered out, producing `[]`. The empty result remains in the parent's result because the retention decision already concerned the original truthy container.

If code recursively compacted first and then filtered the recursive result by truthiness, empty containers would still be truthy in JavaScript, so they would also remain. But filtering recursive return values with an incorrect custom emptiness test could violate examples.

The exact source makes the intended rule clear: remove falsy values, not empty containers.

**Handle ordinary objects with reduction**

`Object.entries(obj)` produces every own enumerable key and value.

`reduce` starts from `{}`. For each pair, it tests `if (value)`:

- a falsy value is omitted;
- a truthy value is recursively compacted and assigned to the same key.

Keys are preserved exactly for retained properties. Unlike arrays, object keys do not shift when another key is removed.

**Trace a simple array**

For `[null, 0, false, 1]`, Boolean filtering rejects the first three elements and retains 1.

Mapping the primitive 1 returns it unchanged. The result is `[1]`.

No placeholder holes remain because `filter` creates a packed array.

**Trace a nested object**

For `{a: null, b: [false, 1]}`:

- key `a` is skipped because null is falsy;
- key `b` is retained because arrays are objects and truthy;
- recursive array processing removes false and keeps 1.

The result is `{b: [1]}`.

**Trace retained empty containers**

For an outer array containing `[0]`, the nested array is truthy and passes the outer filter.

Its recursive call removes zero and returns `[]`. The outer result includes that empty array.

This matches the definition: the key or index held a truthy array, while only the array's falsy child was removed.

**No input mutation**

`filter` and `map` create new arrays. The object reduction creates a new object and assigns compacted children into it.

The original JSON graph is read but not modified. Nested output containers are newly constructed, while primitive leaf values are reused because they are immutable values.

**Every retained path is recursively clean**

For a truthy primitive, the base case returns it and there is no deeper content.

For a truthy container, recursion applies the same filtering rule to all children. By induction, every returned nested container contains no falsy immediate child and every deeper retained container is also compact.


At an array, `filter(Boolean)` retains exactly truthy indexed values and removes exactly falsy ones; recursive mapping produces their compact forms in original order.

At an object, the reduction retains exactly truthy property values under their original keys and recursively compacts them. The base case preserves leaf values.

These cases cover all valid JSON values, so the newly built result is exactly the recursively compact object.

**Why truthiness must be checked before retaining**

It would be wrong to recurse into null because JavaScript reports `typeof null` as object. The initial falsy check prevents that.

It would also be wrong to remove values merely because they look empty, such as `[]` or `{}`. Boolean conversion correctly treats both as true.

## Complexity detail

Let $n$ be the total number of array elements and object properties across the JSON structure. Every child is examined once and every retained container is rebuilt once, so total time is $O(n)$.

The returned compact structure can contain $O(n)$ values. Recursion uses $O(d)$ stack frames for nesting depth $d$. Total space including output is $O(n)$, with $O(d)$ auxiliary call-stack space.

## Alternatives and edge cases

- **Mutate containers in place:** Can reduce allocations but risks index-shift bugs and violates input preservation.
- **Iterative explicit stack:** Avoids call-stack overflow for extremely deep JSON while keeping $O(n)$ work.
- **Delete empty containers:** Incorrect because empty arrays and objects are truthy.
- **Zero:** Removed wherever it is a child value.
- **False:** Removed even though it is a meaningful Boolean in other applications.
- **Empty string:** Removed because its Boolean conversion is false.
- **Null:** Removed and never traversed.
- **Empty array or object:** Retained because it is truthy.
- **Nested container becomes empty:** Still retained if its original container value was truthy.
- **Array removal:** Survivors shift left into a packed array.
- **Object removal:** Other property names remain unchanged.
- **Valid JSON guarantee:** Excludes functions, symbols, undefined, and cyclic structures.
