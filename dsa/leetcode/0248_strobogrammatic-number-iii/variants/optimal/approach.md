## General
**Generate only rotationally valid structures**

For every length from `len(low)` through `len(high)`, recursively place compatible digit pairs from outside inward. The middle of an odd length can be only $0$, $1$, or $8$.

**Length handles most bounds; lexical order handles ties**

Reject a leading zero for multi-digit candidates. At complete candidates, compare lexicographically only against a bound having the same length; equal-length decimal strings preserve numeric order.

Candidates shorter than `low` or longer than `high` are never generated. For an interior length, every valid candidate is automatically inside the numeric range. Only the two boundary lengths need comparison, avoiding integer conversion even when the bounds exceed native numeric types.

**Outer-to-inner pairs give each valid number one construction path**

Every recursive partial assignment contains only mirrored pairs that rotate into one another, so each completed candidate is strobogrammatic. Conversely, every strobogrammatic number uniquely determines those outer-to-inner pairs and its optional middle digit, giving it one construction path. The leading-zero, length, and inclusive boundary checks retain that candidate exactly when it represents a number in `[low, high]`.

## Complexity detail
For maximum bound length $d$, the search explores $O(5^{d/2})$ pair assignments. Constructing or comparing a completed candidate costs $O(d)$, so a direct string-building implementation takes $O(d \cdot 5^{d/2})$ time in the worst case. Depth-first construction uses $O(d)$ working space; retaining generated strings instead of counting immediately would add output-sized storage.

## Alternatives and edge cases
- **Scan every integer in the range:** depends on numeric magnitude rather than digit length.
- Single-value ranges, zero, and bounds with different lengths require inclusive handling.
