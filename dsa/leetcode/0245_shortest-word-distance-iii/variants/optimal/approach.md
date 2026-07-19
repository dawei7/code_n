## General
**Equal target words change which positions may pair**

For distinct targets, retain each latest index as in Problem 243. For equal targets, retain the previous occurrence and compare it with every new occurrence.

The stored positions are the latest valid endpoints, and the running answer is the smallest distance among pairs ending within the processed prefix.

**Consecutive compatible occurrences are sufficient**

For distinct words, the closest earlier compatible endpoint is the latest occurrence of the other word. When both targets are equal, it is the immediately preceding occurrence of that same word. Any older compatible position is farther from the current index, so checking the latest valid partner for every occurrence necessarily checks an optimal pair.

## Complexity detail
The list is scanned once for $O(n)$ time, and only indices plus the minimum are stored.

## Alternatives and edge cases
- **Occurrence lists:** simplify post-processing but use linear space.
- **All-pairs comparison:** is quadratic.
- Equal targets require at least two occurrences and must never pair one position with itself.
