## General

Iterate through `Object.entries(obj)`, which supplies each enumerable key as a string and works for both ordinary objects and arrays. Maintain a `Map` from each input value to the key or keys seen so far.

On the first occurrence of a value, store its key string directly. On the second occurrence, replace that string with a two-element array containing the first and second keys. For every later occurrence, append the new key to the existing array. This preserves the required output shape without an extra cleanup pass.

Finally, convert the map to an ordinary object with `Object.fromEntries`.

**Why the incremental representation is correct**

After processing any prefix of the entries, each map value represents exactly the keys in that prefix whose original value equals its map key. One occurrence is represented by a string; two or more occurrences are represented by an array in encounter order. Processing the next entry either creates the correct singleton group or extends exactly its matching group, so the property remains true for the entire input.

A `Map` also treats every input string as data. Values such as `"__proto__"`, `"constructor"`, and `"toString"` cannot collide with inherited object properties. `Object.fromEntries` then creates those names as own data properties in the returned object.

## Complexity detail

Let $n$ be the number of enumerable entries in `obj`. Each entry performs expected $O(1)$ map work and each original key is written to the result once, giving $O(n)$ expected time. The groups and returned object contain $n$ key references in total, so auxiliary and output storage are $O(n)$.

The benchmark uses unique input values, forcing a correct repeated-search alternative to rescan all original entries for every output property and exhibit quadratic growth, while the map-based implementation remains linear.

## Alternatives and edge cases

- **Repeated filtering by distinct value:** Find every key matching each value with a fresh pass over the input. It is correct but can require $O(n^2)$ time when values are unique.
- **Plain object accumulator with truthiness checks:** Inherited names such as `__proto__` and `constructor` can be mistaken for existing groups. A null-prototype object with explicit ownership checks can avoid this, but a `Map` states the key semantics directly.
- **Always store arrays, then collapse singletons:** This is correct and still linear, but it needs a second pass and temporarily obscures the required singleton output shape.
- **Duplicate values:** The second matching key changes the output value from a string into an array; later keys append to that same array.
- **Arrays:** `Object.entries` exposes indices as strings, exactly as required.
- **Empty object or array:** Both serialize to length $2$ and invert to an empty object.
- **Enumeration order:** Integer-like object keys follow JavaScript's standard enumerable-property ordering before other string keys.
- **Special value strings:** Treat `__proto__`, `constructor`, empty strings, and numeric-looking strings as ordinary output keys.

