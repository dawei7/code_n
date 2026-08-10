## General

**Place one shared method where every array can find it**

JavaScript arrays inherit from `Array.prototype`. When code evaluates `arr.last` and `arr` has no own property named `last`, JavaScript follows the array's prototype link and finds the method defined by the solution.

Assigning

`Array.prototype.last = function() { ... }`

therefore enhances every ordinary array without copying a separate function into every instance. Arrays that already exist and arrays created later both use the same prototype method.

This is the exact interface requested by the problem: the caller invokes `array.last()` rather than passing an array to a standalone helper.

**Why the method is a normal function**

Inside a method call such as `arr.last()`, a normal function receives `arr` as its dynamic `this` value. The body can consequently inspect `this.length` and index `this`.

An arrow function would be wrong here because arrow functions do not create their own `this` binding. They capture `this` from the surrounding lexical scope, which would not reliably be the calling array.

The normal function syntax is therefore not cosmetic. It is what connects the shared prototype method to the particular array on which it is invoked.

**Distinguish an empty array by length**

The last valid zero-based index of a nonempty array of length $n$ is $n-1$. The method uses the conditional expression:

`this.length === 0 ? -1 : this[this.length - 1]`.

If length is zero, index negative one is not a normal last-element lookup in JavaScript. Array bracket access with `-1` asks for a property literally named `"-1"`, not an element counted from the end. Returning the required sentinel explicitly avoids that trap.

If the array is nonempty, `this.length - 1` is a valid final index, and direct bracket access returns that element.

**Why checking length is better than checking the value**

The input is produced by `JSON.parse`, so valid array elements include:

- `null`;
- `false`;
- zero;
- an empty string;
- objects and nested arrays.

All of those values can legitimately occupy the final position. A test such as `if (!this[this.length - 1])` would incorrectly treat many of them as if the array were empty.

Even nullish coalescing, such as `this.at(-1) ?? -1`, would replace a legitimate final `null` with `-1`. The contract distinguishes “no element” from “the last element is null,” so array length is the authoritative condition.

**Why the method does not mutate the array**

Direct indexing only reads an element. The solution does not call `pop`, `splice`, or any other mutating operation.

This matters because calling a query-like method named `last` should not remove data. Repeated calls on the same nonempty array return the same final value unless some other code changes the array.

For `[null, {}, 3]`, length is three, final index is two, and the result is three. The array remains unchanged.

For `[]`, length is zero, so the method returns `-1` without reading an element.

**Prototype lookup step by step**

Consider:

`const arr = [1, 2, 3]`.

The array does not normally have its own `last` property. JavaScript checks `Array.prototype`, finds the function installed by the solution, and calls it with `this = arr`.

Inside the function:

- `this.length` is three;
- the empty branch is skipped;
- `this.length - 1` is two;
- `this[2]` is three.

Only the method is inherited. The element data and length remain properties of the individual array.

**Why one prototype assignment is sufficient**

Prototype inheritance means the runtime performs lookup dynamically. The solution does not need to loop through arrays or know how many arrays will be created.

Memory is also shared: the prototype holds one function object, while each array merely already has its standard prototype link. This is different from attaching a new closure to every array instance.

**Contract-specific safety**

Extending a built-in prototype can be risky in a general production library because another package or a future language version could use the same name. In this isolated challenge, however, modifying `Array.prototype` is the required mechanism.

The assignment creates a writable, enumerable, configurable property using ordinary assignment defaults. Enumerability can affect code that uses `for...in` over arrays, although modern array iteration normally uses `for...of` or indexed loops. A production-quality library might use `Object.defineProperty` to make the method non-enumerable, but the exact stored solution favors the simplest contract-satisfying definition.

**Arrays containing arbitrary JSON values**

No conversion is performed on the returned element. A final object is returned by reference, a final nested array remains that same array, and primitive values retain their types.

The documented return union includes null, Boolean, number, string, array, and object because JSON arrays may contain any JSON value. The `-1` sentinel is returned only for zero length, even if another element elsewhere equals `-1`.

**Why direct indexing is optimal**

Array length is already stored by the JavaScript runtime, and indexed access does not require scanning preceding elements. The method's work is independent of how many items the array contains.

Copying with `slice(-1)` or searching with `findLast` would add machinery without improving correctness. Removing with `pop` would violate non-mutation.

## Complexity detail

Reading `length`, subtracting one, and accessing one array index are constant-time operations. Each call to `last()` therefore takes $O(1)$ time.

The call uses no data structure whose size depends on the array. Auxiliary space per call is $O(1)$.

The prototype itself stores one shared function, also $O(1)$ total additional space regardless of the number of arrays.

## Alternatives and edge cases

- **`Array.prototype.at(-1)`:** It provides end-relative indexing, but a separate length check is still needed to distinguish an empty array from a legitimate final undefined-like value.
- **`pop()`:** It returns the last element but removes it, violating the expected query behavior.
- **`slice(-1)[0]`:** Non-mutating but allocates a new one-element array and is needlessly indirect.
- **Arrow-function method:** It captures lexical `this` and will not reliably refer to the receiving array.
- **Empty array:** Return `-1` based on length.
- **Final `null`:** Return null, not the empty sentinel.
- **Final false or zero:** Falsy values are real elements and must be returned unchanged.
- **Nested final array or object:** Return the original reference without copying or serialization.
- **Repeated calls:** They do not mutate the array and therefore remain stable.
- **Prototype collision:** Relevant in production design, but extending `Array.prototype` is explicitly required by this challenge.
