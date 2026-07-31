## General

Deep equality depends first on the kind of each JSON value and then, for containers, on their recursively compared contents. Handle the cheapest decisive checks before descending.

**Separate primitives from containers**

If `o1 === o2`, the pair is immediately equal; this covers every matching primitive and two `null` values. If exactly one value is `null`, or either remaining value is not an object, the pair cannot be equal because the unequal primitives already failed strict equality.

JavaScript reports arrays as objects, so compare `Array.isArray` results explicitly. An array and an ordinary object are never deeply equal, even if the object has numeric keys matching the array's indices.

**Compare matching container structures**

For two arrays, unequal lengths fail immediately. Otherwise compare corresponding positions from left to right, recursively returning `false` at the first mismatch.

For two ordinary objects, first compare their key counts. Then iterate over every key in the first object, require it to be an own key of the second object, and recursively compare the associated values. Key membership rather than enumeration position makes object insertion order irrelevant.

Every successful recursive pair satisfies the rule for its exact JSON type. Array positions and object keys account for all children, while every mismatch returns `false` immediately. Therefore the top-level result is `true` exactly when the two complete JSON structures are deeply equal.

## Complexity detail

Let $n$ be the number of primitive values, array entries, and object properties inspected, and $d$ the greatest nesting depth reached. Each inspected component is processed once, with expected $O(1)$ object-property lookup, so time is $O(n)$. Recursion holds at most one frame per nesting level, giving $O(d)$ stack space. Temporary key arrays across the active recursion path can contain $O(n)$ references in the worst case. Because $d \le n$, total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Iterative pair stack:** Store value pairs explicitly and process them until a mismatch appears. This avoids call-stack depth limits but uses $O(n)$ explicit storage in a broad structure.
- **Canonical serialization:** Recursively sort object keys and compare serialized results. It can be correct for JSON values but adds sorting work, temporary strings, and potentially $O(n \log n)$ time.
- **Lodash `_.isEqual`:** It handles many JavaScript types beyond JSON, but the problem explicitly forbids using it.
- **Raw `JSON.stringify` comparison:** It incorrectly treats objects with identical properties inserted in different orders as unequal.
- **Arrays versus objects:** `typeof` alone is insufficient because both arrays and ordinary objects report `"object"`; compare `Array.isArray` results.
- **Null:** Although `typeof null` is `"object"`, only another `null` is deeply equal to it.
- **Primitive types:** Strict equality keeps values such as `1` and `"1"`, or `true` and `1`, distinct.
- **Early mismatch:** Different lengths, missing keys, and unequal primitive children may stop the traversal before all $n$ components are inspected.
