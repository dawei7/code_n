## General

**Summarize one complete batch of each type.** Group `Inventory` by
`item_type`. For each type, count its rows to obtain the number of items in one
batch and sum `square_footage` to obtain that batch's storage cost. Keeping
these values together is essential: the warehouse repeats the entire type
inventory, not whichever individual item has the smallest footprint.

**Allocate prime batches before measuring the remainder.** Divide `500000` by
the prime batch area and take the floor. Multiplying that batch count by the
prime items per batch gives the first result. Subtract the exact area occupied
by those complete batches from `500000`; division must use the unrounded
decimal sum so the remainder remains exact.

Use that remainder in the same floor calculation for the non-prime batch.
Flooring guarantees that only complete batches are counted. Emit both item
types, including a zero non-prime count when the remainder is too small, then
sort by item count descending. A secondary priority places `prime_eligible`
first when both counts are equal.

## Complexity detail

Let $n$ be the number of inventory rows. The grouped summary reads every row
once and stores only the two item-type aggregates, taking $O(n)$ time and
$O(1)$ auxiliary space. The two divisions, union, and ordering of two result
rows are constant work. Database engines may choose different physical
aggregation plans, but the asymptotic bound is unchanged.

## Alternatives and edge cases

- **Choose the smallest individual items:** This can report more items but violates the complete-batch contract, which requires every item of a type in each repetition.
- **Allocate both types independently from 500000:** This double-counts warehouse area; non-prime batches may use only the remainder after the maximal prime allocation.
- **Round batch square footage before division:** Premature rounding can add an illegal batch near a capacity boundary; preserve the decimal sum and floor only the quotient.
- A prime batch that divides the capacity exactly leaves a non-prime count of zero.
- Leftover space that fits only part of a non-prime batch also yields zero.
- `item_count` is the number of batches times the number of rows in that type, not the batch count alone.
- Descending item count can place `not_prime` before `prime_eligible`; equal counts use prime first.
