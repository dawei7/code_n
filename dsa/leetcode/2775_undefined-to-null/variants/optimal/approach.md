## General

Traverse the nested structure with an explicit stack of containers. Start with the root object or array. Whenever a container is removed from the stack, enumerate its own enumerable keys and inspect each associated value.

If a value is exactly `undefined`, assign `null` to that same location. Otherwise, if it is a non-null object, it is another array or object that may contain target values, so push it for later inspection. Primitive values and `null` need no work. Testing `value !== null` before following an object is essential because JavaScript reports `typeof null === "object"` even though `null` has no properties to traverse.

**Why one traversal is sufficient**

Every reachable container is placed on the stack when its parent entry is inspected, and every own enumerable entry of that container is then examined. An entry equal to `undefined` is replaced immediately. Any entry not equal to `undefined` either leads to a nested container that will receive the same treatment or is a value the contract says to preserve. Consequently, after the stack becomes empty, no reachable `undefined` value remains and no other value has been changed.

An explicit stack avoids depending on the JavaScript call-stack limit for deeply nested input. Mutating the supplied structure also avoids allocating a second copy, and returning the root afterward satisfies the required interface.

## Complexity detail

Let $n$ be the total number of enumerable object properties and array elements in the nested input. Each entry is inspected once, so the running time is $O(n)$. In the worst case, the explicit stack can hold $O(n)$ nested containers awaiting traversal, giving $O(n)$ auxiliary space. The transformation reuses the input structure rather than allocating output proportional to its size.

## Alternatives and edge cases

- **Recursive depth-first traversal:** Recursion expresses the same $O(n)$ walk compactly, but a sufficiently deep legal structure can exceed the JavaScript call-stack limit.
- **Immutable reconstruction:** Building fresh arrays and objects can preserve the original input, but repeatedly spreading a growing object may take $O(n^2)$ time; a careful one-pass reconstruction still needs $O(n)$ output space.
- **Serialization round trip:** `JSON.stringify` does not preserve object properties whose values are `undefined`, so stringify/parse alone cannot implement the required replacement semantics.
- **Existing `null`:** Preserve it. The explicit null check also prevents treating it as a traversable object.
- **Arrays:** Enumerate their present indices just like object keys and replace an `undefined` element at its original position.
- **Falsy primitives:** Values such as `false`, `0`, and `""` are not `undefined` and must remain unchanged.
- **Deep nesting:** Use the explicit work stack so traversal depth is limited by available memory rather than recursive call depth.
