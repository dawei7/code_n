## General
**Translate the basket rules into a window**

Any valid trip visits a contiguous segment with at most two fruit types, and every such segment can be collected by starting at its left endpoint. The problem is therefore the longest subarray with at most two distinct values.

Move a right boundary through the array and count fruit types inside the current window. When adding a fruit creates a third type, advance the left boundary, decrementing counts and deleting a type when its count reaches zero, until at most two types remain. Record the largest valid window length after every extension.

Before each maximum update, the window ends at the current right boundary and contains at most two types. Shrinking only while a third type exists leaves the earliest possible valid left boundary for that right endpoint, so this is the longest valid segment ending there. Every possible right endpoint is processed, hence the maximum includes an optimal trip. Each reported segment also obeys both basket capacities, proving the result is attainable.

## Complexity detail
The right boundary visits each of the $n$ trees once, and the left boundary also moves right at most $n$ times, giving $O(n)$ time. Although a map is used, it contains at most three types temporarily and at most two after shrinking, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try every starting tree:** Extending independently until a third type appears is correct but takes $O(n^2)$ time when the whole suffix remains valid.
- **Track two most recent runs:** A specialized constant-space scan can maintain the last type, its trailing run, and the current two-type length, but is easier to implement incorrectly.
- **Prefix positions by type:** Extra indexing does not remove the need to identify contiguous two-type ranges.
- **One tree:** The only fruit can always be collected.
- **One fruit type:** The entire row fits in one basket.
- **Exactly two types:** The entire row is valid regardless of alternation frequency.
- **Third type:** Shrink only enough to remove one old type; resetting the whole window loses valid overlap.
- **Type zero:** Fruit identifiers are ordinary map keys, including `0`.
