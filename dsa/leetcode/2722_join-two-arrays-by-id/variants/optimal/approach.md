## General

Use a map from `id` to the object currently assembled for that identifier. Insert shallow copies of all `arr1` objects first. This records every first-array-only identifier and provides the lower-priority properties for overlapping identifiers.

Then scan `arr2`. For each object, spread the existing mapped object, if present, followed by the second-array object. JavaScript evaluates later spread properties last, so every shared key receives the value from `arr2`, while keys exclusive to either object remain. Because each identifier is a single map key, the final map contains exactly one joined object per distinct `id`.

Convert the map values to an array and sort numerically by `id`. Every input object contributes once to its identifier's state, the spread order implements the required precedence, and the final sort establishes the mandated ascending order. Spreading is intentionally shallow: a nested value associated with a shared key is replaced as one value.

## Complexity detail

Let $N$ be the total input-object count and $U\le N$ the number of distinct identifiers. Expected map access takes $O(1)$ per object, while sorting costs $O(U\log U)$, giving $O(N\log N)$ worst-case time in terms of $N$. The map and output hold $O(U)$ objects, which is $O(N)$ auxiliary space. The benchmark uses `size` as $N$.

## Alternatives and edge cases

- **Sort both arrays then merge:** Sorting each input and advancing two pointers also takes $O(N\log N)$ time and can avoid a hash map, but it mutates inputs unless copies are made.
- **Linear search in the growing output:** Searching all accumulated objects for every second-array identifier is correct but can require $O(N^2)$ comparisons.
- **Plain object keyed by `id`:** This can work, but a `Map` preserves numeric keys without string coercion or prototype-key concerns.
- Identifiers present in only one input retain all their original properties.
- When both objects contain a key, `arr2` wins even if its value is `null`, an array, or another object.
- Nested objects are replaced rather than recursively merged.
- Input order does not determine output order; the result must be sorted numerically by `id`.
- Neither input object needs to be mutated.
