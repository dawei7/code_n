## General
**View candidates as three ordered product streams**

Every ugly number after one is an earlier ugly number multiplied by 2, 3, or 5. Maintain one pointer into the generated sequence for each multiplier and append the smallest current product.

The list contains the sorted distinct sequence prefix. For each multiplier, its matching pointer (`index_two`,
`index_three`, or `index_five`) identifies the first product greater than the last appended value.

**The smallest stream head is the next missing ugly number**

Every ugly number greater than one can be written as an earlier ugly number multiplied by `2`, `3`, or `5`, so it appears in at least one stream. Each pointer skips exactly the products already emitted, making its head the smallest unseen value from that stream. The minimum of the three heads is therefore the smallest unseen ugly number overall. Advancing every pointer tied at that value removes duplicate representations without skipping the next candidate.

## Complexity detail

The outer loop appends $n - 1$ values, and each of the three pointers advances at most $n$ times. Generation therefore
takes $O(n)$ time. The `ugly` sequence holds $n$ values, while the pointers and current candidate use $O(1)$ additional
state, for $O(n)$ total auxiliary space.

## Alternatives and edge cases

- **Heap with deduplication:** is correct but costs $O(n \log n)$.
- **Rescan every earlier product for the next value:** takes $O(n^2)$.
- **First position:** seeding `ugly` with one makes `n = 1` return without entering the generation loop.
