## General

**Use each id as the identity of one output object**

The result contains one object per distinct `id` across both arrays. That makes a map the natural central structure: the key is `id`, and the value is the currently merged object for that identity.

The input guarantee says IDs are unique within each individual array. Therefore at most one object from `arr1` and at most one object from `arr2` can contribute to a given map entry.

**Load arr1 as the base layer**

The first loop visits every object in `arr1` and executes:

`merged.set(object.id, { ...object })`.

The object spread creates a new top-level object containing the same enumerable properties. This avoids placing the original top-level object itself in the result. At this stage, each map entry is simply the corresponding `arr1` object copied under its ID.

An object that appears only in `arr1` remains this copy through the end of merging.

**Overlay arr2 after arr1**

The second loop handles each `arr2` object with:

`{ ...(merged.get(object.id) || {}), ...object }`.

If the ID already exists, the existing `arr1`-based properties are spread first. The `arr2` properties are spread afterward, so a duplicate key from `arr2` overwrites the earlier value. Keys found only in the base object survive because nothing replaces them.

If the ID does not exist, `merged.get(...)` is `undefined`, so `|| {}` supplies an empty base. Spreading the `arr2` object then copies it unchanged into a new top-level object.

The new merged object is stored back under the same ID.

**Why spread order implements the contract**

JavaScript object construction processes spreads from left to right. Writing a property whose key already exists updates that property's value. It does not create two copies of the key.

For an ID with base `{"id": 2, "x": 3, "y": 6}` and overlay `{"id": 2, "x": 10, "y": 20}`, the second spread replaces both `x` and `y`, producing `{"id": 2, "x": 10, "y": 20}`.

For the nested example, the base value of `b` is `{"b": 94}` and the overlay value is `{"c": 84}`. The result's `b` is exactly the overlay object. This is a shallow merge, as required: the nested objects are not recursively combined into `{"b": 94, "c": 84}`.

**Shallow copying and reference behavior**

Object spread copies top-level property values. Primitive values are copied directly, while nested arrays and objects remain references to the same nested values. The problem asks for property-level merging, not deep cloning, so this behavior matches the examples.

The exact code does not mutate the top-level objects from either input. It creates a fresh top-level object when loading `arr1` and another fresh object for every `arr2` entry. Nested referenced values are not cloned.

**Convert the map to the result array**

After both loops, `merged.values()` contains exactly one object for every distinct ID. `Array.from` materializes those values into an array.

Map insertion order alone is not enough for the required result because IDs may arrive in arbitrary order and an `arr2`-only ID is inserted after all `arr1` IDs. The code explicitly sorts:

`left.id - right.id`.

A negative difference puts `left` before `right`, a positive difference puts it after `right`. Unique result IDs mean the comparator does not need a tie-breaker.

**Trace a shared and an unshared ID**

Suppose `arr1` contains IDs one and two, while `arr2` contains IDs two and three.

After the first loop, the map has base copies for one and two. Processing ID two creates a replacement object containing all base-only keys and the overriding `arr2` values. Processing ID three uses an empty base and inserts its copy. Converting gives three objects, and sorting returns them in ID order one, two, three.

**Why the result is correct**

For every distinct ID, the map creates exactly one entry. Loading `arr1` establishes all first-array properties. Loading `arr2` afterward preserves nonconflicting properties and replaces conflicting ones because later spreads win. No other entry shares that map key, so the merged object is unique. Finally, numerical sorting places all unique entries in ascending ID order. These properties exactly match the requested join.

## Complexity detail

Let $N=\lvert\texttt{arr1}\rvert+\lvert\texttt{arr2}\rvert$, let $U$ be the number of unique IDs, and let $P$ be the total number of top-level properties copied across all spread operations. Expected map lookup and insertion are $O(1)$ per object. Property spreading costs $O(P)$ in total, materializing values costs $O(U)$, and sorting costs $O(U\log U)$ comparisons.

Thus a precise time bound is $O(P+U\log U)$ expected. If each object has a bounded number of properties, $P=O(N)$ and this becomes the manifest's $O(N\log N)$ worst-case shorthand because $U\le N$.

The map and result array hold $U$ top-level objects or references, while copied properties occupy $O(P)$ space. With bounded-size objects this is $O(N)$ auxiliary/output storage. JavaScript's sorting implementation may also use $O(U)$ temporary space.

## Alternatives and edge cases

- **Nested search for matching IDs:** Avoids a map but can take $O(\lvert arr1\rvert\lvert arr2\rvert)$ time.
- **Sort both inputs and use two pointers:** Works in $O(N\log N)$ time and then linear merging, but mutates or copies both arrays and is more elaborate.
- **Plain object keyed by ID:** Can work for integer IDs, though `Map` avoids property-name and prototype concerns and makes key intent explicit.
- **Deep merge:** Incorrect; when both objects contain a nested property, the entire `arr2` value must replace the `arr1` value.
- **ID only in arr1:** Its copied base object reaches the result without an overlay.
- **ID only in arr2:** The empty fallback creates a copy containing exactly that object's properties.
- **Conflicting property:** The later `...object` spread from `arr2` wins.
- **Nonconflicting property:** It survives from whichever source contains it.
- **Input mutation:** Top-level input objects are not mutated, although nested values remain shared references.
- **Large object bodies:** Property-copy cost may dominate sorting, which is why the detailed bound includes $P$.
