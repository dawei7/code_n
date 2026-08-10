## General

**A difference can be a leaf pair or a nested object**

The recursive function returns one of two shapes:

- `{}` when there is no reportable difference;
- `[obj1, obj2]` when the two current values differ as leaves or incompatible container types;
- an object whose keys contain deeper differences when both values are comparable containers.

Using an empty object as the “no difference” marker makes it possible for a parent to prune unchanged children uniformly.

**Stop immediately for strict equality**

The first test is `obj1 === obj2`.

For JSON primitives, this recognizes equal numbers, strings, Booleans, and null. It also recognizes the same object reference, although separately parsed equal containers usually have different identities.

An equal value contributes nothing to the output, so the function returns `{}` without descending.

**Decide whether recursive comparison is meaningful**

A value is treated as a container only when it is non-null and has JavaScript type `"object"`.

The explicit null test is necessary because `typeof null` is historically `"object"` even though null has no keys to traverse.

If either value is not a container, strict equality has already failed, so the correct leaf difference is `[obj1, obj2]`.

**Arrays and objects are incompatible types**

Both arrays and ordinary objects have type `"object"`, but the problem treats a change from one kind to the other as a direct value replacement.

`Array.isArray(obj1) !== Array.isArray(obj2)` detects that mismatch and returns the pair immediately.

The algorithm does not recursively compare array indices against object properties in this case.

**Traverse only keys shared by both sides**

When both values are arrays or both are ordinary objects, the function loops over `Object.keys(obj1)`.

For each key, it uses `Object.prototype.hasOwnProperty.call(obj2, key)`. A key absent from `obj2` is skipped because removals must not appear in the result.

Keys that exist only in `obj2` are never visited because iteration begins from `obj1`, so additions are also ignored.

The own-property form avoids inherited properties and works even if an object has a key named `hasOwnProperty`.

**Arrays are compared through index keys**

`Object.keys` on a JSON array returns its present indices as strings such as `"0"` and `"1"`.

The recursive result container is still initialized as `{}`, not `[]`. This allows a sparse difference such as only index 500 to be represented without hundreds of empty array slots.

Indices beyond the shorter array are additions or removals and are ignored by the shared-key rule.

**Prune an unchanged child**

For a shared key, the function computes `difference = objDiff(obj1[key], obj2[key])`.

`Object.keys(difference).length > 0` distinguishes a real result from empty `{}`. A leaf difference array has keys `"0"` and `"1"`, so it is retained.

Only nonempty child differences are assigned to `differences[key]`. This produces an output containing changed paths and no unchanged structural padding.

**Trace primitive changes and missing keys**

If `obj1` contains `{a: 1, removed: 5}` and `obj2` contains `{a: 2, added: 7}`:

- key `a` exists in both and returns `[1, 2]`;
- `removed` is absent from the second object and is skipped;
- `added` is not an iterated first-object key.

The output is only `{a: [1, 2]}`.

**Trace a nested array**

For arrays `[1, 2, 4, [2, 5]]` and `[1, 2, 3, [1]]`:

- indices zero and one recurse to empty differences;
- index two produces `[4, 3]`;
- shared nested index three recurses, where index zero produces `[2, 1]`;
- removed nested index one is ignored.

The array difference is represented as an object with string keys two and three.

**Object key order does not matter**

Two JSON objects may list the same keys in different insertion order.

The function looks up each key by name rather than comparing key sequences. If all shared values are recursively equal and neither side has a reportable common-key change, the result remains empty.


At a current pair of values, the base cases return no result exactly for strict equality and return a leaf pair exactly when unequal values cannot be recursively compared under the problem's type rules.

For comparable containers, the loop examines exactly the intersection of own keys. By induction, each recursive result contains precisely the changes below that key. Empty results are omitted, while all nonempty results are retained.

Thus the final object contains every and only changed shared-key path, with the required old/new leaf pair.

## Complexity detail

Let $n$ be the total number of keys and array indices visited across comparable shared structure. Each is processed once with expected constant-time property lookup, so time is $O(n)$.

Recursion uses $O(d)$ call-stack space for maximum nesting depth $d$. The returned difference can contain $O(n)$ entries in the worst case, giving $O(n+d)=O(n)$ total space including output.

## Alternatives and edge cases

- **Serialize and compare whole objects:** Detects equality but does not produce the required nested changed paths and is sensitive to key order.
- **Iterative stack traversal:** Avoids recursion depth while preserving shared-key semantics.
- **Include union of keys:** Would report additions and removals, which the problem explicitly excludes.
- **Equal primitives:** Return no difference.
- **Null versus value:** Return a direct two-element difference array.
- **Array versus object:** Return a direct difference rather than comparing keys.
- **Different array lengths:** Extra indices on either side are ignored.
- **Empty containers:** Two empty containers of the same kind produce `{}`.
- **Different key order:** Has no effect because comparison is by key.
- **Same object reference:** Strict-equality shortcut avoids traversal.
- **Sparse output:** Array-index changes are stored in an object, not padded array.
- **Input preservation:** The function creates new result containers and never mutates either input.
