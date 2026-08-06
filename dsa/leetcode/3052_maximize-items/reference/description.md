## Description

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
