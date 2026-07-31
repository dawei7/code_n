## General

Compare a pair of values recursively. An exact `===` match contributes no difference, so return an empty object immediately.

**Distinguish leaves from compatible containers**

A value is recursively traversable only when it is non-null and has JavaScript type `"object"`. If either value is not such an object, unequal values form the leaf `[obj1Value, obj2Value]`. Arrays need an additional check because `typeof []` is also `"object"`: when exactly one side is an array, the container types differ and the whole pair is a leaf difference.

**Traverse the key intersection**

When both values are arrays or both are objects, enumerate the own keys of the first value. Recurse only when the second value also owns that key. This is precisely the required intersection: additions, removals, and array indices outside the shorter input never enter the result.

For each shared key, retain the recursive result only when it has at least one own key. A primitive or type mismatch returns a two-element array, whose keys are `"0"` and `"1"`; a nested change returns a nonempty object. Equal or difference-free branches return `{}` and are pruned.

The recursion therefore emits a leaf exactly for unequal shared values that cannot be compared as like containers. For compatible containers it applies the same rule to every shared child and no unshared child. Induction on nesting depth shows that every required difference is retained, every omitted key is required to be ignored or unchanged, and no extra branch appears.

## Complexity detail

Let $n$ be the total number of JSON keys, array indices, and values inspected across the shared traversal. Each inspected key is enumerated and compared once, so the running time is $O(n)$. The recursion stack and returned difference tree together contain at most $O(n)$ entries, giving $O(n)$ space including the required output.

## Alternatives and edge cases

- **Repeated `JSON.stringify`:** Serializing both remaining subtrees at every recursive call can skip equal branches, but a deeply nested difference causes the same suffixes to be serialized repeatedly and takes $O(n^2)$ time.
- **Flatten paths first:** Converting both inputs into path-to-value maps makes the intersection explicit, but uses extra maps and must still preserve container-type mismatches.
- **Union of keys:** Traversing every key from both inputs incorrectly reports additions and removals, which the contract says to ignore.
- `null` is a primitive leaf for this comparison even though JavaScript reports `typeof null === "object"`.
- Arrays and objects are different types even when an object has numeric-looking keys.
- Extra array elements have no shared index and must not appear in the result.
- Object property order is irrelevant because lookup uses key identity.
