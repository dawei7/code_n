## General

Scan the parallel arrays from left to right so that encounter order and duplicate priority agree. Convert the current key exactly once with `String(keysArr[i])`. A `Set` records every converted name already accepted; membership in that set determines whether the pair is the first occurrence.

**Why a separate set is necessary**

Testing only `key in obj` would confuse new input keys with inherited names such as `"toString"` or `"constructor"`. Testing `Object.hasOwn(obj, key)` avoids that inheritance issue, but a dedicated set states the first-occurrence rule directly and remains independent of how the result object stores properties.

**Create a real own property**

For an accepted key, use `Object.defineProperty` with `enumerable`, `configurable`, and `writable` all enabled. Ordinary assignment to `obj["__proto__"]` invokes the legacy prototype setter instead of reliably creating the required data property. Explicit definition treats `"__proto__"`, `"constructor"`, and every other string uniformly.

Because indices are visited in increasing order, the first converted occurrence is inserted before any collision can be seen. The set then rejects every later occurrence, so each returned value comes from exactly the earliest matching index.

## Complexity detail

Let $n$ be the common array length, and let $K$ be the total number of characters produced while converting all keys. The scan and expected constant-time set operations take $O(n + K)$ time. The set, returned properties, and stored key strings require $O(n + K)$ space in the worst case.

## Alternatives and edge cases

- **Object assignment plus `Object.hasOwn`:** This can enforce first occurrence for ordinary names, but assignment mishandles `"__proto__"` on a normal object unless that property is defined specially.
- **Null-prototype result:** `Object.create(null)` makes assignment safe for inherited names, but the contract asks for a normal new object and consumers may expect `Object.prototype` behavior.
- **Repeated prefix search:** Comparing each converted key with all earlier keys is correct but takes $O(n^2)$ comparisons when every key is distinct.
- Conversion happens before duplicate detection, so `"1"` and `1`, or `false` and `"false"`, collide.
- Empty inputs return an empty object without entering the loop.
- Object and array keys use JavaScript's normal `String()` conversion; structurally different JSON values can therefore map to the same property name.
- Property names inherited by `{}`, including `"toString"` and `"constructor"`, are still valid first occurrences.
- `"__proto__"` must be an own enumerable data property rather than a prototype mutation.

