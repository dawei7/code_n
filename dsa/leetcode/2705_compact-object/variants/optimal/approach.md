## General

Process each container according to its type. For an array, create a new array and visit elements in order. Skip an element when its Boolean coercion is false. Otherwise, append the primitive directly or recursively compact it when it is a non-null object.

For a plain JSON object, iterate its own key-value entries. Apply the same falsy test before recursion, and assign every retained value to a new object under its original key. Because `null` is falsy, it is discarded before JavaScript's `typeof null === "object"` behavior could incorrectly trigger recursion.

**Why empty compacted containers remain**

The truthiness decision is made on the original child value. Arrays and objects are truthy even when empty or when all their descendants will be removed. Once such a container passes the test, recursion returns its compact form and the parent retains that result. This yields `[]` from a nested `[0]`, as required.

Every original key or array position is examined once. A falsy child is omitted immediately; a truthy primitive is copied unchanged; and a truthy container is retained with exactly the recursively valid descendants. Induction over nesting depth therefore shows that the output removes all and only falsy values while preserving every required key, order, and container.

## Complexity detail

Let $n$ be the number of properties, array elements, containers, and primitive values visited in the JSON structure. Each is tested and copied at most once, so time is $O(n)$. The returned compact structure and recursion stack together require $O(n)$ space in the worst case. The benchmark uses `size` as nesting depth and contrasts this traversal with a correct implementation that repeatedly serializes each recursive result.

## Alternatives and edge cases

- **Repeated `JSON.stringify` cloning:** Serializing each recursive result preserves the compact output, but a deeply nested value serializes the same suffix at every ancestor and takes $O(n^2)$ time.
- **JSON replacer function:** A replacer can omit object properties but cannot directly remove array entries without leaving `null` placeholders, so array compaction still needs special handling.
- **Mutate in place:** Deleting object properties and splicing arrays can work, but repeated array splices shift elements and may become quadratic while also changing the input.
- `null`, `false`, `0`, and `""` are falsy JSON values and must be removed.
- Negative numbers, nonempty strings, arrays, and objects are truthy and remain.
- Array order is preserved and removed positions do not leave holes.
- Empty arrays and objects remain when their original container was retained.
- The root is guaranteed to be an object or array, so the function returns a container.
