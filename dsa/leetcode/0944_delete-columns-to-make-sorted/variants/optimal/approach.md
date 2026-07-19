## General
**An adjacent inversion is the complete test.** A column is in non-decreasing order exactly when every adjacent pair satisfies `strs[row][column] <= strs[row + 1][column]`. If any adjacent pair violates that relation, the column is not sorted and must be counted once. There is no need to compare more distant rows: if all adjacent relations hold, transitivity orders every earlier character before every later one.

Scan each of the $c$ columns. Within a column, compare consecutive rows from top to bottom. On the first inversion, increment the deletion count and stop scanning that column, because additional violations cannot change its contribution from one. If no inversion appears, leave the count unchanged. Since every column is classified independently and the scan uses exactly the defining condition, the final count is the required number of deletions.

## Complexity detail
In the worst case, every one of the $c$ columns examines $r-1$ adjacent row pairs, giving $O(rc)$ time. The deletion count and loop indices occupy constant space, so the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Sort each column:** Build the column characters, sort them, and compare the result with their original order. This is correct but uses extra storage and $O(cr\log r)$ time.
- **Compare every row pair:** A column is sorted if no earlier row contains a larger character than a later row. Checking all pairs is correct but takes $O(cr^2)$ time instead of using transitivity.
- **One row:** Every column is automatically sorted because there are no row pairs to violate the order.
- **Equal adjacent characters:** Equality is allowed by non-decreasing order and must not cause a deletion.
- **Early inversion:** Once one adjacent pair decreases, the column contributes exactly one deletion regardless of later characters.
- **All columns invalid:** The answer can equal $c$; deletions are counted by column, not by the number of inversions.
