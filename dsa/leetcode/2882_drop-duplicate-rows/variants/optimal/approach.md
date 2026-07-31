## General

Duplicate status is determined only by `email`. pandas can scan that column while tracking the addresses it has already encountered. Calling `drop_duplicates` with `email` as the subset and `keep="first"` retains the complete first row for every address and discards each later row with the same address.

Because the operation selects rows from the existing DataFrame rather than reconstructing individual fields, each retained `customer_id`, `name`, and `email` stays together. The stable first-occurrence behavior also preserves their original relative order, exactly matching the requested result.

## Complexity detail

Let $n$ be the number of customer rows. Hash-based duplicate detection examines each email once on average, so the method takes $O(n)$ time. The seen-address structure, duplicate mask, and returned DataFrame can each scale with the number of rows, giving $O(n)$ additional space.

## Alternatives and edge cases

- **Boolean `duplicated` mask:** Selecting `customers[~customers.duplicated(subset=["email"], keep="first")]` expresses the same operation explicitly and has the same $O(n)$ expected time and space bounds.
- **Python set scan:** Iterating over the emails with a set can also be $O(n)$ expected time, but reconstructing the matching DataFrame rows manually is more verbose and easier to get wrong.
- **List of seen emails:** Linear membership checks preserve correctness but require $O(n^2)$ time when many addresses are distinct.
- **First occurrence:** The earliest row for an email must survive; keeping the last occurrence would retain the wrong customer information.
- **Duplicate key:** Equality of `name` or `customer_id` is irrelevant because only `email` defines duplicates.
- **Stable order:** The retained rows must remain in input order; sorting by email is unnecessary and changes the requested presentation.
