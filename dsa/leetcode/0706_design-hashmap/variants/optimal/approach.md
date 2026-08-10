## General

The exact map uses direct addressing rather than ordinary hashing. Since every key lies between `0` and `1,000,000`, the key itself can be used as an array index. The array entry stores that key's current mapped value.

The legal values are nonnegative, while the required “not found” result is `-1`. This makes `-1` a safe sentinel for an unused key.

**Storage representation**

The constructor creates:

`self.data = [-1] * 1000001`.

For each legal key `x`:

- `data[x] == -1` means no mapping for `x` exists;
- any value from `0` through `1,000,000` means `x` currently maps to that value.

The inclusive key range needs exactly `1,000,001` positions.

**Why the sentinel is unambiguous**

The map interface returns `-1` when a key is missing. If `-1` were also a legal stored value, reading an entry could not distinguish “mapped to -1” from “not mapped.”

The source guarantees `value >= 0`, so `-1` never represents a genuine pair. One integer slot can therefore encode both presence and value without a separate Boolean array.

**Putting a pair**

`put(key, value)` executes:

`self.data[key] = value`.

If the key was absent, this replaces the sentinel and creates a mapping. If it already existed, the assignment overwrites its old value, implementing the required update semantics.

No duplicate entry is created because each key owns exactly one slot.

**Getting a value**

`get(key)` returns `self.data[key]` directly.

For a present key, the slot holds its current value. For an absent key, it holds `-1`, exactly the required result. No conditional is necessary because the internal sentinel and public missing result are the same.

**Removing a mapping**

`remove(key)` assigns `-1` to the slot.

That erases a present mapping. If the key was already absent, it writes the sentinel over itself and has no observable effect.

The old value does not need to be returned or preserved.

**The representation invariant**

After every operation:

> For each legal key `x`, `data[x]` equals its current mapped value if the mapping exists, and equals `-1` otherwise.

The constructor establishes this invariant for an empty map. `put` establishes it for the chosen key with a real value, `remove` establishes absence, and `get` simply reports it. Other indices remain unchanged.

**Why collision handling is absent**

An ordinary hash map often computes `key % bucket_count`, mapping many keys into fewer buckets. Different keys can collide and must then be distinguished inside a bucket.

Here the address is the key itself. If `x != y`, then array indices `x` and `y` differ. Collisions are mathematically impossible within the legal universe.

This trades memory for very simple, deterministic constant-time operations.

**An operation trace**

Begin with every slot `-1`.

- `put(1, 1)` stores one at index one.
- `put(2, 2)` stores two at index two.
- `get(1)` returns one.
- `get(3)` reads untouched sentinel `-1`.
- `put(2, 1)` overwrites index two, updating rather than duplicating the key.
- `get(2)` now returns one.
- `remove(2)` restores `-1` at index two.
- `get(2)` returns `-1`.

Changes to index two never alter the mapping at index one.

**Why key and value play different roles**

The key selects where data is stored. The value is the content of that selected slot.

Using `value` as an index or searching for it would be incorrect because many keys may legally map to the same value. Direct addressing requires only keys to be unique addresses; values need no uniqueness.

**Why the implementation is correct**

Every abstract map state is completely represented by independent slots. A put makes the chosen slot equal the required value, a remove resets it to the unique absence sentinel, and a get returns precisely that representation.

By induction over the operation sequence, the array and abstract map agree for every key at all times.

## Complexity detail

Let `U = 1,000,001` be the key-universe size and `q` the number of calls after construction.

Initializing all slots to `-1` takes `O(U)` time and stores `U` integers, using `O(U)` space.

Each `put`, `get`, and `remove` performs one direct array operation, so each is `O(1)` worst-case time. Across all calls, operation time is `O(q)`, or `O(U+q)` including initialization.

Persistent memory is

$$
O(U).
$$

It does not depend on how many mappings are present.

## Alternatives and edge cases

- **Modulo hashing with buckets:** Uses a smaller primary array and stores only inserted mappings, but collisions require list or tree searches.

- **Open addressing:** Keeps pairs in one table and probes after collisions. It needs load-factor management, resizing, and deletion markers.

- **Two parallel direct-address arrays:** A presence Boolean plus a value array would support any integer value, including `-1`, at twice the logical storage.

- **Key zero:** It maps to index zero and can store value zero without confusion; absence is `-1`.

- **Maximum key:** The last valid index exists because of the plus one in the array length.

- **Value zero:** It is a genuine present value and differs from the `-1` sentinel.

- **Updating an existing key:** Direct assignment replaces its old value.

- **Removing an absent key:** The sentinel remains unchanged.

- **Several keys with one value:** Each key has a separate slot, so identical values do not interact.

- **Sparse map:** The full array is allocated even if only a few keys are used.

- **Negative value support:** This implementation relies on the contract forbidding `-1` as data. Expanding the value domain would require separate presence information.

- **Invalid keys:** Negative and above-range indices are outside the contract and are not defensively checked.

- **No built-in hash table:** The list is an indexed storage array, not a `dict`.
