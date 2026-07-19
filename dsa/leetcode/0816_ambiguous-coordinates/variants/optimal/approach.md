## General
**Choose the comma before choosing decimal points**

Remove the outer parentheses and try each of the $n - 1$ splits between consecutive digits. The prefix and suffix are independent number fragments. Generate every legal textual number for each fragment, then take their Cartesian product and format each pair as a coordinate.

**Classify a fragment by its boundary zeros**

A one-digit fragment always has one representation. For a longer fragment:

- if it begins and ends with `0`, it has no valid representation;
- if it begins with `0`, its only possible form is `0.` followed by the remaining digits;
- if it ends with `0`, only its integer form is valid;
- otherwise, its integer form and every internal decimal position are valid.

These cases follow directly from the two forbidden patterns: a multi-digit integer part may not start with zero, and a fractional part may not end with zero. They also generate every allowed form, because a number can contain at most one decimal point and every internal position is considered whenever neither boundary rule forbids it.

For each comma split, pairing all legal left and right forms produces exactly the coordinates using that comma. Different comma or decimal positions produce different strings, so collecting the products across all splits is complete and introduces no duplicates.

**Keep validation local to each side**

Rejecting a fragment before forming coordinate pairs avoids enumerating combinations that a leading or trailing zero has already made impossible. This is especially important for inputs dominated by zeros.

## Complexity detail
Let `n` be the number of interior digits and `K` the number of returned coordinates. Across all comma splits, constructing the possible left and right representations costs $O(n^3)$ in the worst case because strings are copied. Formatting the `K` output strings costs $O(nK)$, for total $O(n^3 + nK)$ time. Temporary representations for one split occupy $O(n^2)$ characters, while the returned strings occupy $O(nK)$ space.

## Alternatives and edge cases
- **Enumerate all marker placements, then validate:** Trying every comma and both decimal positions is straightforward but spends time constructing candidates whose boundary zeros make them immediately invalid.
- **Backtracking over punctuation:** A recursive generator can choose comma and decimal markers, but it needs the same validity rules and is less direct for a fixed maximum of three markers.
- **All nonzero digits:** Every comma split and every internal decimal position is legal, producing the largest output.
- **Fragment equal to `0`:** The single zero is valid; only multi-digit leading zeros are forbidden.
- **Leading and trailing zero together:** A multi-digit fragment such as `00` or `010` has no representation.
- **Output order:** Any order is valid, so the judge compares the coordinate strings as an unordered collection.
