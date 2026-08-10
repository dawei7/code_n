## General

**Traverse containers, replace leaf values in place**

The input is a nested arrangement of objects and arrays. Any property or array element whose value is exactly JavaScript `undefined` must become `null`. The exact solution performs an iterative depth-first traversal with an explicit `stack`.

The stack initially contains the root `obj`. Each loop iteration pops one container, inspects all of its own enumerable string-keyed properties with `Object.keys(current)`, replaces direct undefined values, and schedules nested non-null objects for later inspection.

The same mechanism works for both plain objects and arrays because arrays are JavaScript objects and their present elements appear as enumerable keys such as `"0"`, `"1"`, and so on.

**Why an explicit stack is useful**

Nested data naturally suggests recursion, but a deeply nested object can exceed JavaScript's function call-stack limit. The explicit array stores pending containers on the heap and keeps the function's own call depth constant.

Traversal order does not affect the result. Because `stack.pop()` uses last-in, first-out order, the code behaves like depth-first search, but breadth-first search would replace exactly the same values. What matters is that every reachable container is eventually inspected.

**Inspect the current value before deciding to descend**

For each key, the code reads `const value = current[key]` once.

- If `value === undefined`, it assigns `current[key] = null`.
- Otherwise, if `value !== null && typeof value === "object"`, it pushes that nested container.
- All other primitive values are left unchanged.

The order of these conditions is significant. `undefined` must be replaced rather than ignored. Also, JavaScript historically reports `typeof null` as `"object"`, so the explicit `value !== null` guard is necessary. Pushing `null` would later cause `Object.keys(null)` to throw.

Strings, numbers, booleans, and other non-object primitives contain no nested properties relevant to this JSON-like input and require no action.

**Why `Object.keys` matches the data model**

`Object.keys(current)` returns the container's own enumerable string keys. Those are the properties and array elements that ordinary JSON object data exposes for serialization. Inherited properties are not part of the object itself and should not be rewritten.

For an array, explicit entries with value `undefined` are keys and are replaced. The array length and order remain unchanged. For a plain object, property names remain unchanged and only values are assigned.

Non-enumerable properties and symbol-keyed properties are outside ordinary JSON data and are not visited by this exact implementation. That aligns with the contract's JSON object or array model.

**The transformation is intentionally in place**

The method mutates each encountered container and finally returns the original root reference `obj`. It does not create a deep copy.

For example, if the caller stores the same object in another variable, that alias observes the replacements after the function returns. Nested object identities are also preserved. Only direct property values equal to `undefined` change to `null`.

This differs from a recursive mapping solution that constructs entirely new objects and arrays. In-place mutation reduces allocation and is exactly what the source code does.

**A walkthrough**

Consider a root equivalent to:

`{ a: undefined, b: ["x", undefined, { c: undefined }], d: null }`.

The stack begins with the root. Processing it changes `a` to null, pushes array `b`, and leaves `d` alone because it is already null. Processing the array leaves `"x"` unchanged, changes its second element to null, and pushes the object at its third element. Processing that object changes `c` to null. The stack then empties, and the root now contains no explicit undefined value.

No container is returned separately and reattached; every assignment is made through the parent that owns the key.

**Why every target value is replaced**

Under the promised acyclic JSON-like structure, every nested container is reachable from the root by following object-valued properties or array entries. The root is pushed initially. Whenever a processed container has a non-null object child, that child is pushed. By induction on nesting depth, every reachable container is eventually popped.

When a container is popped, `Object.keys` enumerates each relevant own property. An undefined value is replaced immediately. Therefore every explicit undefined property or array entry is changed.

Conversely, the code assigns only in the strict `value === undefined` branch, and the assigned value is always `null`. Defined primitives, existing nulls, and container references remain unchanged. The transformation therefore changes exactly the requested values.

**Serialization motivation**

`JSON.stringify` treats undefined inconsistently with explicit null: an undefined object property is omitted, while an undefined array entry serializes as null. Replacing explicit undefined values before serialization preserves object keys and makes absence explicit in both contexts. Existing `null` values already have the desired representation and are deliberately left alone.

**Assumptions about cycles and aliases**

The constraint describes a valid JSON object or array. JSON data is acyclic, so the exact solution does not keep a visited set. A circular JavaScript object would cause containers to be pushed forever. Such input is outside the contract.

If an acyclic object is shared through multiple properties, it may be pushed more than once. The transformation is idempotent—after the first visit there are no undefined direct values left in that shared object—but repeated visits add work. Ordinary parsed JSON has a tree structure without shared object identities, which is the model used by the stated complexity.

## Complexity detail

Let `n` be the total number of own enumerable properties and present array elements across the JSON-like structure. Every container is popped once in the ordinary tree-shaped input, and every key is inspected once. `Object.keys` itself produces a list proportional to the current container's key count; summed across all containers, time is `O(n)`.

The explicit stack can hold `O(n)` pending containers in the worst case, such as a root with many nested object children. The temporary key array from one `Object.keys` call can also contain `O(n)` entries. Auxiliary space is therefore `O(n)` in the worst case. For a single deep chain, the LIFO stack may stay small, whereas a recursive solution would use `O(depth)` call frames; the broad worst-case bound remains linear.

The transformation allocates no replacement object graph. The input's existing storage is not counted as auxiliary space, and the returned value is the same root reference.

## Alternatives and edge cases

- **Recursive deep copy:** Recursively map arrays and rebuild objects for concise immutable-style code, but it allocates `O(n)` output and may overflow the call stack on deep input.
- **Recursive in-place traversal:** It preserves identity like the exact method but uses call-stack space proportional to nesting depth.
- **JSON stringify/parse round trip:** A replacer can sometimes convert undefined values, but serialization has special rules, loses object identity, and is unnecessary for direct traversal.
- **Existing `null`:** The explicit guard leaves it unchanged and prevents `Object.keys(null)` from throwing.
- **Explicit undefined array entry:** It appears in `Object.keys` and is assigned null at the same index.
- **Sparse array hole:** A hole is not an own key, so the exact implementation leaves it sparse. The contract and examples concern explicit undefined values.
- **Empty object or array:** `Object.keys` returns an empty list; the container is popped and returned unchanged.
- **Deep nesting:** The explicit stack avoids recursive call-stack overflow.
- **Wide root object:** Many child containers can be pending simultaneously, producing the `O(n)` stack bound.
- **Circular reference outside the contract:** Without a visited set, traversal would not terminate.
- **Shared acyclic child outside ordinary JSON trees:** It may be inspected more than once, but replacements remain correct because setting undefined to null is idempotent.
- **Inherited property:** `Object.keys` excludes it, which is appropriate because inherited data is not an own JSON property.
- **Symbol or non-enumerable property:** It is not visited by this exact implementation and is outside the stated JSON data model.
- **Root identity:** The returned object is strictly the original `obj` after mutation, not a clone.
- **Primitive nested value:** It is neither undefined nor a non-null object, so it remains unchanged.
