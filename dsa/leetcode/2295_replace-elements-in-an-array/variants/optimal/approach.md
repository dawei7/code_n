## General

**Index every current value**

Build a hash map from each distinct value in `nums` to its array index.
Distinctness makes this correspondence one-to-one.

For an operation `[old, new]`, remove `old` from the map to obtain its index,
write `new` at that array position, and map `new` to the same index. These
updates keep the map synchronized with the current array before the next
operation.

Initially the map records every value's exact position. One operation changes
only the located position, deletes precisely the value that left the array,
and inserts precisely the value that entered it. By induction, every later
lookup targets the correct current occurrence. Since positions never move, the
array after the final update is exactly the requested result.

## Complexity detail

Let $n$ be the array length and $m$ the number of operations. Building the map
takes $O(n)$ expected time, and each operation performs expected $O(1)$ hash
work, for $O(n+m)$ expected time overall. The position map uses $O(n)$ space.

## Alternatives and edge cases

- **Linear search per operation:** Finding `old` by scanning the array is correct but can take $O(nm)$ time.
- **Direct-address table:** The value bound permits an index array of size $10^6+1$, trading fixed memory for deterministic constant-time lookup.
- **Single position:** Any valid chain repeatedly updates the same index.
- **Reusing a removed value:** Once `old` leaves the array, a later operation may legally introduce it as `new`.
- **Operation order:** Replacements are sequential; applying pairs against only the initial values is incorrect.
- **Value uniqueness:** The guarantee means one map entry always identifies the entire replacement target.
- **Position stability:** Only the stored value changes; no operation shifts or sorts the array.
- **Long chains:** A value introduced by one operation can immediately become the `old` value of the next.
