## General

**Invert from original values to original keys.** Each own entry of the input has an original key and a string value. In the output, that value becomes a property name. If only one original key had the value, the output value is that key string. If several original keys shared it, the output value is an array of all corresponding key strings.

Arrays follow the same rule because `Object.entries(array)` exposes their present indices as string keys such as `"0"` and `"1"`.

**Use a Map while grouping.** The method creates `inverted = new Map()`. A Map is useful during construction because it supports direct string-key lookup, distinguishes absence through `has`, preserves insertion order, and safely accepts strings such as `"__proto__"` without interacting with object prototypes.

For each `[key, value]` from `Object.entries(obj)`, the code checks whether `value` already has a group.

If not, it stores `key` directly. This keeps the common one-key case in the exact output shape required by the problem rather than wrapping every result in an array.

If the value has appeared before, there are two cases. When the previous stored result is already an array, the new key is pushed onto it. Otherwise, this is the second occurrence, so the source replaces the single string with `[previous, key]`.

This creates a compact representation that changes shape exactly once: string after the first occurrence, array after the second, then growing array for all later occurrences.

**Order inside duplicate arrays.** `Object.entries` enumerates own enumerable string-keyed properties in JavaScript's standard property order. The algorithm processes and appends keys in that order. For a normal JSON object with non-integer-like keys, this is insertion order. For an array, indices appear in ascending numeric order. Thus duplicate-key arrays reflect the original entry enumeration order.

The problem examples expect keys as strings. Array indices naturally arrive as strings from `Object.entries`, so no explicit conversion is needed.

**Materialize an ordinary object at the end.** `Object.fromEntries(inverted)` iterates the Map entries and creates a plain object whose property names are the original string values and whose property values are the grouped key string or key array.

Using `fromEntries` is safer than repeatedly writing `result[value] = ...` for unusual property names because the standardized operation creates own data properties. It does not treat `"__proto__"` as a request to mutate the new object's prototype.
After processing the first $t$ input entries, for every string value seen so far, the Map contains exactly the keys among those $t$ entries having that value, in entry order. It stores the one key directly when the count is one and stores the ordered key array when the count is at least two.

The invariant begins true for an empty Map. A first occurrence creates the correct one-key group. A later occurrence either converts the correct singleton into a two-key array or appends to the already correct array. No other value's group changes. After all entries, every original entry contributes its key to exactly the group named by its value. `Object.fromEntries` changes only the outer container type, so the returned object is the required inversion.

**Why values being strings matters.** Object property keys are strings or symbols. Since every input value is guaranteed to be a string, using it as a Map key and later as an object property name preserves it directly. If arbitrary objects were allowed as values, distinct objects could be valid Map keys but would both stringify to `"[object Object]"` when materialized, causing collisions.

**Input properties versus inherited properties.** `Object.entries` considers only own enumerable string-keyed entries. Valid JSON objects and arrays have exactly the relevant data in those entries; inherited properties and symbols are outside the JSON contract. Sparse array holes are not entries and therefore produce no inverted key.

**The input is not modified.** The method allocates new grouping structures. The only in-place changes are pushes into arrays created inside the Map. Original objects, arrays, keys, and string values remain untouched.

## Complexity detail

Let $n$ be the number of enumerable input entries. `Object.entries` materializes an array containing $n$ pairs, taking $O(n)$ time and $O(n)$ space under a unit-cost string-reference model. The loop performs an expected $O(1)$ Map lookup/update per entry, and each original key is appended at most once.

`Object.fromEntries` visits each distinct input value group. Across all group values, the stored key strings total $n$, so materialization is $O(n)$. Overall expected time is $O(n)$ and additional space, including the returned structure and the temporary entries/Map, is $O(n)$.

If total character data matters, let $S$ be the sum of key and value string lengths. Hashing strings and creating property keys can introduce $O(S)$ work, so a content-sensitive description is $O(n+S)$. The JSON-size constraint bounds this total.

Map lookup bounds are expected rather than worst-case guarantees because they depend on the JavaScript engine's hash-table implementation.

## Alternatives and edge cases

- **Plain object accumulator:** It can group values directly, but naive assignment is vulnerable to special names such as `"__proto__"` and requires careful own-property checks.
- **Null-prototype accumulator:** `Object.create(null)` avoids inherited-name collisions and can replace the Map, though final conversion and duplicate shape logic are still needed.
- **Always store arrays first:** Group every value into an array and convert length-one arrays to strings afterward. This simplifies updates but requires a second normalization pass.
- **Exactly one occurrence:** The output value is the original key string, not a one-element array.
- **Two occurrences:** The second occurrence converts the stored string into an array in the correct order.
- **Three or more occurrences:** Later keys append to the existing array without nesting it.
- **Array input:** Present numeric indices become strings. Sparse holes, if any, do not appear in `Object.entries`.
- **String value `"__proto__"`:** Map grouping and `Object.fromEntries` create a safe own property rather than mutating the prototype.
- **Integer-like object keys:** JavaScript enumeration may order them numerically before other strings; the output duplicate array follows actual `Object.entries` order.
- **Inherited properties:** They are ignored, as appropriate for JSON data.
- **Input preservation:** No input property or array element is changed.
- **Non-string values outside the contract:** Object materialization would coerce keys and could merge values that were distinct in a Map, so the guarantee is essential.
