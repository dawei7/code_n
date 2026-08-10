## General

**Compare values according to their structural category**

Deep equality is recursive. Two outer containers are equal only when their corresponding contents are deeply equal.

The solution distinguishes four relevant JSON situations in a careful order:

1. values already equal by `===`;
2. null or non-object values that failed strict equality;
3. arrays;
4. ordinary objects.

This order matters because JavaScript reports `typeof null` as `"object"`, and arrays also have object type even though their comparison rules require order and length.

**Accept strict equality immediately**

The first line is:

`if (o1 === o2) return true`.

This handles equal primitives directly:

- the same number;
- the same string;
- the same Boolean;
- null with null.

It also accepts two references to the exact same array or object. A value is necessarily deeply equal to itself, so traversing it would be wasted work.

The inputs come from valid JSON, so problematic primitive cases such as `NaN` do not occur.

**Reject incompatible leaves**

If strict equality failed, the code checks whether either value is null or either type is not `"object"`.

At this point, any primitive pair is unequal by definition because it already failed `===`. A primitive cannot be deeply equal to a container. Null must be handled explicitly because its type string misleadingly says object.

Returning false here ensures recursion proceeds only when both values are non-null containers.

**Keep arrays distinct from objects**

`Array.isArray(o1)` records whether the first value is an array. If that Boolean differs from `Array.isArray(o2)`, the result is false.

This prevents an array such as `[1,2]` from being treated as equal to an object with keys `"0"` and `"1"`. They may expose superficially similar enumerable properties, but JSON gives arrays and objects different structural meanings.

**Compare arrays by length and position**

Two arrays must first have equal lengths. If not, one contains an unmatched element and equality is impossible.

For equal lengths, the loop recursively compares:

`o1[index]` with `o2[index]`

for every index in increasing order. The first mismatch returns false immediately.

If the loop finishes, every position has a deeply equal partner and the arrays are equal.

Order is essential. Arrays `[1,2]` and `[2,1]` contain the same multiset but are not deeply equal because corresponding positions differ.

**Compare objects by their own keys**

`Object.keys(o1)` returns the first object's enumerable own string keys. The code compares its length with `Object.keys(o2).length`.

Equal key counts are necessary but not sufficient: `{a:1}` and `{b:1}` each have one key. Therefore, for every key from the first object, the solution also checks:

`Object.prototype.hasOwnProperty.call(o2, key)`.

Only then does it recursively compare the associated values.

If all first-object keys exist in the second and the counts match, the second object cannot have any additional unmatched own key. The key sets are equal, and recursive value equality completes the object comparison.

**Why property order does not affect objects**

The code iterates keys in the first object's order, but it looks each one up by name in the second object. It never compares the arrays returned by `Object.keys` position by position.

Thus `{"x":1,"y":2}` and `{"y":2,"x":1}` are equal. JSON object member order is not part of this problem's equality relation.

Arrays deliberately use positional comparison, so the algorithm applies different order semantics to the two container kinds.

**Why call `hasOwnProperty` safely**

Calling `o2.hasOwnProperty(key)` directly assumes the object has not shadowed that name and inherits the standard method.

`Object.prototype.hasOwnProperty.call(o2, key)` invokes the canonical method with `o2` as its receiver. This is robust even for an object containing its own property named `hasOwnProperty`.

Values parsed from JSON normally inherit `Object.prototype`, but the safer form accurately expresses “own key” without relying on the object's contents.

**Trace a nested mismatch**

Compare:

`{"x":null,"L":[1,2,3]}`

with:

`{"x":null,"L":["1","2","3"]}`.

The outer objects have the same keys. Values for `x` are both null, so strict equality accepts them.

Values for `L` are arrays of the same length. At index zero, number one and string `"1"` fail strict equality, and both are primitives, so recursion returns false. That false propagates through the array and object calls to the final result.

**Recursive correctness**

Use induction on structural depth.

At depth zero, values are primitives or null. The strict-equality and rejection branches exactly implement the primitive rule.

Assume recursive calls correctly compare structures of smaller depth. For arrays, equal type and length plus equality at every position is precisely the array definition. For objects, equal own-key sets plus equality of every associated value is precisely the object definition.

The algorithm implements those conditions using recursive calls on smaller children, so it is correct at the current depth. Induction covers the full JSON values.

**Early exits improve common cases**

The function stops at the first conclusive mismatch: unequal primitive, type mismatch, array length mismatch, missing key, or unequal child.

Worst-case equal structures still require examining everything, which is unavoidable because a difference could occur at the last leaf.

## Complexity detail

Let $n$ be the total number of primitive values, array elements, and object keys across the compared structures. In the worst case, each corresponding node and key is examined once, so time is $O(n)$.

`Object.keys` creates key arrays. Across a recursive traversal, their total contents are $O(n)$. The recursion stack uses $O(D)$ for maximum nesting depth $D$, bounded by $O(n)$. Total auxiliary space is therefore $O(n)$ in the worst case.

Early mismatches can use much less time.

## Alternatives and edge cases

- **Serialize both values:** Plain `JSON.stringify` is sensitive to object key order, so logically equal objects can produce different strings.
- **Iterative stack:** Avoid recursive call-stack limits while applying the same category checks.
- **Lodash `isEqual`:** General-purpose but explicitly forbidden and broader than JSON semantics.
- **Both values null:** The initial strict-equality branch returns true.
- **One null:** The explicit null guard returns false before object traversal.
- **Array versus object:** `Array.isArray` distinguishes their structural categories.
- **Different object key order:** Lookup by key still returns true when values match.
- **Same key count but different keys:** The own-property check detects the mismatch.
- **Number versus numeric string:** Strict equality rejects them.
- **Maximum nesting:** Recursive depth follows the JSON tree and may motivate an iterative implementation in runtimes with small stacks.
