## General
**View candidates as three ordered product streams**

Every ugly number after one is an earlier ugly number multiplied by 2, 3, or 5. Maintain one pointer into the generated sequence for each multiplier and append the smallest current product.

The list contains the sorted distinct sequence prefix. For multiplier `p`, its pointer identifies the first product `ugly[index] * p` greater than the last appended value.

**The smallest stream head is the next missing ugly number**

Every ugly number greater than one can be written as an earlier ugly number multiplied by `2`, `3`, or `5`, so it appears in at least one stream. Each pointer skips exactly the products already emitted, making its head the smallest unseen value from that stream. The minimum of the three heads is therefore the smallest unseen ugly number overall. Advancing every pointer tied at that value removes duplicate representations without skipping the next candidate.

## Complexity detail
Each of three pointers moves at most `n` times, so generating `n` values costs $O(n)$ time and the sequence uses $O(n)$ space.

## Alternatives and edge cases
- **Heap with deduplication:** is correct but costs $O(n \log n)$.
- **Rescan every earlier product for the next value:** takes $O(n^2)$.
- The first value is explicitly seeded as one.
