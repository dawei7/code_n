## General

Assign the four permitted business lines ranks from zero through three in their required output order. This map serves both as a membership test and as the primary sort key.

Scan the three parallel arrays together. A record survives only if it is active, its business line appears in the rank map, its code is nonempty, and every code character is alphanumeric or `_`. The inputs are guaranteed to contain printable ASCII, so the language's alphanumeric predicate has exactly the intended meaning here.

Store each survivor as `(business rank, code)`. Ordinary tuple sorting first compares the numeric rank and then the code, which exactly matches the two required ordering rules. Project the code from each sorted pair for the result. Filtering before sorting avoids spending comparison work on invalid records.

This procedure includes every valid coupon because it tests all and only the stated validity rules. Every excluded record violates at least one rule. Finally, the sort keys establish the prescribed total order, so the projected list is the required answer; equal valid records remain separate entries.

## Complexity detail

Let $S$ be the total number of characters across all coupon codes, let $v$ be the number of valid coupons, and let $L$ be the maximum length of a valid code. Validation takes $O(S)$ time. Sorting performs $O(v \log v)$ comparisons, each taking up to $O(L)$ time, so total time is $O(S + vL \log v)$. The stored pairs and returned list use $O(v)$ auxiliary space, excluding the returned strings themselves, which are reused from the input.

## Alternatives and edge cases

- **Four category buckets:** Append valid codes to one list per business line, sort each bucket, and concatenate them. This has the same asymptotic bound but requires explicit concatenation in the fixed order.
- **Regular expression validation:** A full match against `[A-Za-z0-9_]+` is correct, but a direct character scan avoids regex setup and keeps the allowed alphabet explicit.
- **Alphabetical business-line sorting:** This is incorrect because the required category order is custom, not lexicographical.
- **Empty and punctuation-bearing codes:** Empty strings and codes containing spaces, hyphens, `@`, or any other punctuation besides `_` are invalid.
- **Underscore-only codes:** A nonempty string such as `"___"` is valid because every character belongs to the allowed set.
- **Duplicate valid records:** Each valid input coupon contributes one output entry; sorting does not deduplicate them.
