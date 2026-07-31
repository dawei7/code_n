## General

JavaScript inheritance is represented by a chain of prototype objects. A value has access to a class's methods precisely when `classFunction.prototype` occurs somewhere along the value's method-lookup chain. That turns the task into an identity search over prototype links rather than a comparison of constructor names or source text.

First reject `null` and `undefined`, because neither has a usable wrapper prototype. Also reject a `classFunction` that is not a function. For every remaining value, `Object(obj)` is the key normalization: it leaves objects usable as they are and boxes primitives in their standard wrapper objects. Consequently, `Object(5)` leads to `Number.prototype`, which implements the problem's special primitive behavior.

Start from `Object.getPrototypeOf(Object(obj))`. At each step, compare that prototype object by identity with `classFunction.prototype`. A match proves that method lookup from the value reaches the requested class. Otherwise move to the current prototype's prototype. If the traversal reaches `null`, the requested prototype is absent and the result is `false`.

This also explains why a constructor is generally not its own instance. Starting from the function object `Date` follows `Function.prototype` and then `Object.prototype`; it does not visit `Date.prototype`.

## Complexity detail

Let $h$ be the number of prototype links inspected. Each link is visited once, so the time complexity is $O(h)$. The traversal stores only the current and target prototypes, giving $O(1)$ auxiliary space.

The linear time bound is asymptotically optimal. In the worst case, the target is absent or appears only at the last possible link. Chains that differ only at that last link force any correct method to inspect all $h$ relevant links, establishing an $\Omega(h)$ lower bound.

## Alternatives and edge cases

- **Native `instanceof`:** This already walks prototypes for ordinary objects, but it reports `false` for primitive values such as `5`, conflicting with the required wrapper-method semantics.
- **Recursive traversal:** Recursion expresses the same search but consumes $O(h)$ call-stack space and can overflow on an unusually deep custom chain.
- **Constructor-name comparison:** Names are neither unique nor stable, and checking only `obj.constructor` misses superclass relationships.
- **Nullish values:** `null` and `undefined` must return `false` before attempting to box or inspect them.
- **Invalid class value:** A non-function cannot act as the requested class and must return `false`.
- **Null-prototype objects:** An object created with `Object.create(null)` has no inherited `Object.prototype`, so it is not considered an instance of `Object`.
