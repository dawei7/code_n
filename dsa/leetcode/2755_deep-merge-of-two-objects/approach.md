## General

**First decide whether recursive merging is allowed**

Recursive merging happens only when both current values are non-null objects and both are the same container kind: either both arrays or both non-array objects.

The code computes object flags explicitly because JavaScript reports `typeof null === "object"` even though null must behave like a primitive replacement value here.

If either value is primitive or null, or one is an array while the other is an object, the function returns `obj2` immediately. This implements the rule that incompatible or non-container pairs are replaced by the second value.

**Create a new top-level container from obj1**

For compatible arrays, `[...obj1]` shallowly copies the first array. For compatible objects, `{ ...obj1 }` shallowly copies its enumerable own properties.

This establishes every key or index that exists only in `obj1`. Such entries remain in the result unless `obj2` has the same key.

The top-level compatible container is not mutated in place; a new result container is returned.

**Traverse keys from obj2**

`Object.keys(obj2)` lists its enumerable own string keys. For a JSON object, these are its properties. For a JSON array, they are its existing numeric index strings.

Each key from `obj2` must appear in the result. The only question is whether to merge it with a corresponding `obj1` value or copy it as a new key.

**Shared key: recurse**

`Object.prototype.hasOwnProperty.call(obj1, key)` safely tests whether `obj1` owns the key, even if the JSON object itself contains a property named `hasOwnProperty`.

When the key exists in both, the code calls:

`deepMerge(obj1[key], obj2[key])`.

If the child values are matching containers, their keys are merged recursively. Otherwise, the child from `obj2` replaces the child from `obj1`.

The recursive result is assigned to the copied container.

**Key only in obj2: assign it**

If `obj1` lacks the key, the result receives `obj2[key]` directly. No recursive clone is needed for merging because there is no competing first value.

This means unique nested arrays or objects from either input may be shared by reference with the returned structure. The solution creates new containers along overlapping compatible paths, but it is not a full deep clone of every unique subtree.

**How arrays use the same logic**

The shallow copy initially has `obj1.length` and all its entries. Processing `obj2` indices replaces or recursively merges overlapping positions. Extra indices from a longer `obj2` extend the result.

If `obj1` is longer, its tail remains from the initial copy. The final array length is therefore the longer length, as required.

Arrays and objects do not merge with each other. For example, an empty object at index zero paired with an empty array returns the second value, the empty array.

**Trace the nested example**

At shared object key `b`, both values are objects, so recurse. Key `c` is shared and contains arrays, so copy the first array and merge common indices.

At a primitive conflict such as one versus six, return six. At nested array index one, both values are arrays, so merge their indices; the second array's first element replaces the first, while the longer first array's remaining value seven survives.

Keys `d` and `e` exist on only one side and are retained or added. This produces the described nested result.

**Primitive root example**

For `obj1=true` and `obj2=null`, the first object flag is false and the second is false because null is explicitly excluded. The fallback returns null immediately.

**Input mutation and reference sharing**

The function does not assign into `obj1` or `obj2` containers directly. Matching containers are copied before changes.

However, shallow copying and direct unique-key assignment preserve references to untouched nested containers. Mutating such a shared nested object after the merge could be observable from both input and result. The problem asks for a merged value, not a fully independent deep copy.


For incompatible or primitive pairs, returning `obj2` exactly follows the replacement rule. For matching containers, the initial copy preserves every first-only key. Iterating all second keys adds every second-only key and recursively applies the same correct rules to shared keys. Arrays are treated as indexed containers and retain the longer tail. By structural induction on JSON depth, the returned value is exactly the required deep merge.

## Complexity detail

Let $N$ be the total number of keys, indices, and primitive values visited across both structures. Shallow copies enumerate first-container keys at every compatible recursive level, and `Object.keys` enumerates second-container keys. Each visited property performs constant expected work, so total time is $O(N)$, commonly written $O(n+m)$ for the two input sizes.

New matching containers and their properties can occupy $O(N)$ output/auxiliary space. Recursion uses $O(D)$ call-stack space for maximum nesting depth $D$, which is bounded by $O(N)$. The manifest's $O(n+m)$ space is a safe total bound.

Unique nested subtrees assigned by reference are not traversed or cloned, so practical work may be smaller than both serialized sizes.

## Alternatives and edge cases

- **Mutate obj1 in place:** Uses fewer new containers but changes caller-owned input and differs from this source.
- **JSON serialization clone:** Loses the recursive override logic and performs unnecessary copying.
- **Array versus object:** Types are incompatible, so the entire second value replaces the first.
- **Null:** Explicitly treated as a replacement value, not a mergeable object.
- **Primitive conflict:** Always choose `obj2`, even when the primitive values have different types.
- **Key only in obj1:** Preserved by the initial shallow copy.
- **Key only in obj2:** Added directly and may share a nested reference.
- **Different array lengths:** Overlapping indices merge and the longer tail survives.
- **Deep nesting:** Correct recursively but may approach JavaScript call-stack limits.
- **Reference independence:** Only overlapping compatible container paths are newly copied; unique nested objects are shared.
