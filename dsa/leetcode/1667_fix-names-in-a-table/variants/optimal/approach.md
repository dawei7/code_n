## General
**Normalize the two parts separately.** Extract the first character of `name` and pass it through `UPPER`. Extract the substring beginning at the second character and pass that entire suffix through `LOWER`. Concatenating those results enforces the requested capitalization regardless of how the original letters were cased.

**Preserve every row.** The query performs only scalar transformations in its projection. It does not filter, join, group, or deduplicate, so every input `user_id` contributes exactly one output row and remains paired with its own transformed name.

**Apply the required ordering.** Sort by `user_id` ascending after computing the projected columns. Since `user_id` is the primary key, there are no ties and the result order is fully determined.

**Why the transformation is exact.** For a one-character name, the suffix is empty and the result is simply the uppercase first character. For a longer name, the first expression guarantees an uppercase initial while the second guarantees that every later character is lowercase. These two pieces cover every character exactly once, so the concatenation has precisely the required form.

## Complexity detail
An ordered scan of the primary-key index visits each of the $R$ rows once. Under the bounded name-length constraint, the scalar string operations take constant work per row, so the query runs in $O(R)$ time. Apart from the returned rows and database execution buffers, the projection needs $O(1)$ auxiliary space. Reading all rows is also necessary because changing any one name can change its required output.

## Alternatives and edge cases
- **Title-case function:** A database-specific title-case helper may appear concise, but it can alter letters after separators and is unnecessary when names are guaranteed to contain only letters.
- **Regular expression replacement:** Regex can isolate and rewrite the initial and suffix, but it is more complex and less portable than basic substring functions.
- **Only uppercase the initial:** Leaving the suffix untouched fails for inputs such as `bOB`, where later uppercase letters must become lowercase.
- A one-character name has an empty suffix and must still be returned as its uppercase form.
- An already normalized name remains unchanged.
- An all-uppercase or all-lowercase name is normalized by the same expression; no conditional branch is needed.
- Nonconsecutive identifiers must be returned in numeric ascending order rather than input row order.
