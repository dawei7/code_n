## General

**Emptiness asks whether even one enumerable entry exists**

An object is non-empty as soon as it has one key-value pair. An array is non-empty as soon as it has one element. The actual key name, array index, and stored value do not matter.

This permits an early-exit test. There is no reason to collect every key or count all elements when finding the first one already proves the answer is false.

**Use for-in as an existence probe**

The loop:

`for (const x in obj)`

iterates enumerable property names. For a plain JSON object, its JSON keys are enumerable own properties. For a JSON array, populated indices such as `"0"`, `"1"`, and `"2"` are enumerable properties.

If the loop body executes even once, `obj` contains an entry. The function immediately returns `false`. The variable `x` is intentionally unused because the property's existence, not its name, is the evidence.

If no enumerable property exists, the loop body never executes, control reaches `return true`, and the object or array is empty.

**Falsey values still make an array non-empty**

Emptiness is structural, not based on truthiness. In `[null, false, 0]`, all three values are falsey in different ways, but the array owns indices zero, one, and two. `for...in` sees the first index and immediately returns false.

Similarly, an object such as `{"x": null}` is not empty. The key `x` exists even though its value is null.

The function never evaluates `obj[x]`, so it cannot accidentally confuse a falsey property value with an absent property.

**Why the JSON.parse guarantee matters**

In general JavaScript, `for...in` visits enumerable properties inherited through the prototype chain as well as enumerable own properties. A custom object with no own keys but an inherited enumerable property would be reported as non-empty.

The input is guaranteed to be a JSON object or array produced by `JSON.parse`. Such data uses ordinary object or array prototypes, whose built-in inherited methods are non-enumerable. The JSON text cannot install a custom prototype chain. Under this contract, every property observed by the loop corresponds to actual parsed object content or an array index.

This restriction is what makes the concise loop match the intended definition without a `hasOwn` check.

**Arrays fit the same mechanism**

An empty array `[]` has length zero and no indexed enumerable properties, so the loop does not enter and the function returns true.

A non-empty JSON array is dense in its serialized representation. Even an entry written as `null` creates an index. The non-enumerable `length` property itself is not visited, but at least one index is enough to return false.

General hand-created sparse arrays can have a positive `length` with no enumerable indices, which would make this loop call them empty. Such sparse arrays are not direct outputs of JSON parsing because JSON arrays encode a value, often `null`, at each listed position.

**Objects need no special branch**

One possible implementation would check `Array.isArray(obj)`, inspect `length` for arrays, and use another method for objects. The loop unifies both cases because their contents are represented by enumerable property names.

Avoiding a type branch makes the proof simple: at least one enumerated content property means non-empty; no such property means empty for the legal input domain.

**Trace all three examples**

For `{"x": 5, "y": 42}`, the loop obtains a property name such as `"x"` and returns false before examining the second key.

For `{}`, there is no property name to produce, so the loop ends without a body execution and returns true.

For `[null, false, 0]`, the first enumerable array index is enough to return false. Neither null nor false nor zero changes that conclusion.

**Why this avoids unnecessary allocation**

`Object.keys(obj)` would build an array containing all own enumerable key names and then inspect its length. `JSON.stringify(obj)` would build a text representation. Both process and allocate data that the boolean question does not require.

The exact solution consumes the iterator only until its first item. It retains no list of keys and does not serialize values.


If the function returns false, the loop has produced an enumerable property. Under the JSON input guarantee, that property is a key-value pair of the object or an element index of the array, so the input is not empty. If the function returns true, the loop produced no enumerable property. A parsed plain object then has no JSON key-value pairs, and a parsed array has no elements, so it is empty. Both return directions are therefore correct.

## Complexity detail

The loop body executes at most once because it immediately returns. In the abstract iterator model used by the problem and editorial, probing for the first property is $O(1)$ time, and the solution uses $O(1)$ auxiliary space. This realizes the follow-up and matches the manifest.

JavaScript's language specification does not prescribe the internal complexity of preparing `for...in` enumeration. A particular engine could perform setup related to the object's property structure before yielding the first key. The $O(1)$ statement describes the algorithm's visible iteration count and avoids the explicit $O(n)$ key array created by `Object.keys`.

No space proportional to the number or serialized size of values is allocated by the function.

## Alternatives and edge cases

- **`Object.keys(obj).length === 0`:** Very clear and checks own keys, but explicitly constructs all key names in $O(n)$ time and space.
- **`JSON.stringify(obj).length === 2`:** Works for legal empty arrays and objects but serializes the entire structure in $O(n)$ time and space.
- **Array/object type branch:** Checking array length separately is valid but unnecessary for parsed dense arrays.
- **Empty object:** The loop yields nothing and returns true.
- **Empty array:** It has no enumerable index and returns true.
- **Falsey entry:** `null`, `false`, zero, and an empty string are still values at existing properties, so the result is false.
- **Nested empty value:** `{"x": {}}` is not empty at the top level because key `x` exists.
- **Inherited enumerable property:** Could affect arbitrary custom objects, but the `JSON.parse` guarantee excludes custom prototype data.
- **Sparse array:** A manually created holes-only array is outside the JSON-parsed input model and may not be detected by this exact loop.
- **Property name `"__proto__"`:** Parsed JSON data treats it as an ordinary own data key, so it is correctly recognized as non-empty.
