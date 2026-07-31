# Maximize Items

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3052 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-items/) |

## Problem Description

### Goal

An `Inventory` row describes one item, its type and category, and the square
footage needed to store it. The warehouse has exactly `500000` square feet.
Items are stocked in complete batches by type: one batch contains every
inventory row of that type, so a batch's item count and area are respectively
the number and total square footage of its rows.

Fill the warehouse lexicographically by priority. First store as many complete
`prime_eligible` batches as fit. After those batches reserve their space, use
only the remainder for as many complete `not_prime` batches as fit. Report the
resulting integer item count for both types, including `0` for `not_prime` when
no complete batch fits, and order rows by `item_count` descending.

### Function Contract

**Inputs**

- `Inventory(item_id, item_type, item_category, square_footage)`: `item_id` is
  unique. `item_type` identifies `prime_eligible` or `not_prime`, and
  `square_footage` is the positive decimal storage area for that item.

Let $n$ be the number of inventory rows.

**Return value**

- A table with columns `item_type` and `item_count`. The two allocations use
  complete batches, prioritize `prime_eligible`, and are ordered by item count
  descending; equal counts place `prime_eligible` first.

### Examples

**Example 1**

The six prime-eligible rows occupy `555.20` square feet per batch. The
warehouse holds `900` such batches, or `5400` prime items, and leaves `320`
square feet. The four non-prime rows occupy `128.50` square feet per batch, so
two further batches add `8` items:

| item_type | item_count |
|---|---:|
| prime_eligible | 5400 |
| not_prime | 8 |

**Example 2**

If prime batches exactly fill all `500000` square feet, the returned
`not_prime` count is `0` because no complete non-prime batch fits.

**Example 3**

If prime storage leaves `100000` square feet and one non-prime batch occupies
`70000`, exactly one non-prime batch is counted; the unused `30000` square
feet cannot hold a partial batch.
