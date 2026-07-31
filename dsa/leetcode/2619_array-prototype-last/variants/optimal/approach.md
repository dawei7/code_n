## General

The required behavior belongs to every array, so define `last` on `Array.prototype`. It must be a normal function rather than an arrow function: a normal method call binds `this` to the receiving array, while an arrow function captures `this` lexically and therefore cannot reliably inspect that receiver.

The receiver's `length` separates the only two cases. If it is zero, return the required sentinel `-1`. Otherwise, the final valid index is `this.length - 1`, and direct indexed access returns the stored value unchanged. This works equally for primitive JSON values, objects, and nested arrays, and it does not remove or modify anything.

Testing `length` is important; testing the final element's truthiness would be wrong because `false`, `null`, `0`, and an empty string are all valid last elements.

## Complexity detail

Both reading `length` and accessing one array index take constant time, so the method runs in $O(1)$ time. It allocates no data structure depending on the array length and therefore uses $O(1)$ auxiliary space.

This time class is already asymptotically optimal: returning a result takes $\Omega(1)$ work, and the method's fixed number of property operations matches that lower bound.

## Alternatives and edge cases

- **`pop()`:** This also obtains the final element, but it mutates the receiver and returns `undefined` for an empty array instead of the required `-1`.
- **`at(-1)`:** This is concise for non-empty arrays, but still needs a separate empty check to produce the required sentinel and offers no complexity advantage.
- **Arrow-function prototype method:** An arrow function does not receive the calling array through `this`, so it violates the method contract.
- **Empty array:** Return the numeric sentinel `-1` without attempting an out-of-range read.
- **Falsy final element:** Return `null`, `false`, `0`, or `""` exactly as stored; array length, not truthiness, determines emptiness.
- **Final element equal to `-1`:** The result is still correct even though it is indistinguishable by value from the empty-array sentinel.
