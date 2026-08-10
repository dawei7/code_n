## General

**Avoid searching the array for every operation**

A direct implementation could scan `nums` to locate the old value for each replacement. With up to `10^5` values and operations, that could take quadratic time.

Because all current values are distinct, each value identifies exactly one array index. The dictionary comprehension

`d = {x: i for i, x in enumerate(nums)}`

records that index for every initial value.

**Apply one replacement in constant expected time**

For operation `[x,y]`, the contract guarantees `x` currently exists and `y` currently does not.

`d[x]` retrieves the unique index holding `x`. The code writes `y` into that position:

`nums[d[x]] = y`.

It then records the new lookup:

`d[y] = d[x]`.

After these statements, future operations can find `y` at the same index without scanning the list.

**Why operation order is preserved**

Operations must be applied sequentially because a value introduced by one may be replaced later. The loop processes `operations` in input order and updates the dictionary immediately.

For `[1,3]` followed later by `[3,2]`, the first operation creates `d[3]` at the old position of one. The later operation retrieves that updated position and replaces it correctly.

The method never attempts to batch independent-looking replacements, so chains and reintroduced values follow their exact temporal semantics.

**Understand the stale old-value key**

The exact source does not execute `del d[x]` after replacing `x`. Its mapping remains as a stale historical entry even though `x` is no longer in the array.

This cannot cause an incorrect lookup. The guarantee says an operation's old value exists at the moment of that operation, so an absent stale `x` will not be queried. If value `x` is later reintroduced as some operation's new value, `d[x]` is overwritten with its new current index before it can validly be used again.

Similarly, `y` is guaranteed absent from the current array, but it may have a stale historical key. The assignment `d[y]=d[x]` overwrites that stale entry.

**Preserve the position structure**

Replacement changes only a value, never an index. The mapping transfers the same index from the old logical key to the new current key.

All current values remain distinct because every new value is absent before insertion. Therefore, the one-value-to-one-index invariant continues to hold for current values after every operation.

**Trace a replacement chain**

Start with `nums=[1,2]` and mappings one to zero, two to one.

- Replacing one with three writes index zero and records three to zero.
- Replacing two with one writes index one and overwrites the stale mapping for one to index one.
- Replacing three with two uses three's current index zero, writes two there, and overwrites two's old stale mapping.

The final list is `[2,1]`. Stale keys never interfere because every valid old-value lookup points to the latest mapping created when that value entered the current array.

**Why the final array is correct**

Initially, the dictionary maps every current value to its exact index. Assume that property holds before an operation for all values actually in the array. The old value lookup finds the mandated position, the list assignment performs the exact replacement, and recording `y` maps the new current value to that position.

Other current values and indices are unchanged. The stale `x` entry concerns a value no longer current and is outside the invariant. By induction, every operation is applied correctly and the returned mutated list is the required final array.

**Account for mutation and retained history**

The method returns the same `nums` list object after modifying it. Callers observe all replacements directly.

Because old keys are never deleted, `d` can retain historical values no longer in the array. This affects the exact memory bound even though it does not affect results.

## Complexity detail

Let `n` be the array length and `m` the number of operations. Building the initial dictionary takes `O(n)` expected time. Each operation performs expected-constant-time dictionary accesses and one list assignment, so total expected time is `O(n+m)`.

The dictionary starts with `n` keys and may gain a distinct new historical key on every operation. Since stale old keys remain, exact worst-case auxiliary space is `O(n+m)`, not merely `O(n)` as the manifest summary suggests.

If old keys were deleted, the map would retain exactly the current `n` values and use `O(n)` space.

## Alternatives and edge cases

- **Delete the old key:** Saving `idx=d[x]`, deleting `x`, and inserting `y` preserves correctness while keeping map size `O(n)`.
- **Scan for each old value:** It avoids a dictionary but can take `O(nm)` time.
- **Value-to-value chain map:** Deferred replacements are harder because output positions and temporal reintroductions must still be resolved.
- **Direct-address array:** Values are bounded by `10^6`, but it allocates for the whole domain rather than current and historical keys.
- **Replacement chain:** Immediate mapping updates let a newly introduced value be replaced later.
- **Reintroducing an old value:** Assigning it as `y` overwrites its stale mapping with the new current index.
- **New value has a stale key:** Current absence is sufficient; the dictionary assignment corrects that key.
- **Distinctness:** It guarantees one current index per value and removes ambiguity.
- **One element:** Every operation simply changes index zero and updates its mapping.
- **No position movement:** Only values change, so unaffected elements retain their order.
- **Expected dictionary time:** The linear time bound uses ordinary expected hash-table behavior.
- **Input mutation:** The returned object is the modified original `nums` list.
- **Operations preservation:** `operations` is read sequentially and never changed.
