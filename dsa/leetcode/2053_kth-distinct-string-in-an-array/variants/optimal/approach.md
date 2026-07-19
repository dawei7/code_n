## General
**Frequency must be known globally**

First count every string with a hash map. A value seen for the first time cannot yet be returned because another copy may occur later; completing the frequency pass resolves that uncertainty for every position.

**Recovering original order**

Scan `arr` again rather than iterating over the map. Whenever a string's stored count is one, decrement `k`. The string that makes `k` zero is the requested answer. If the scan ends first, return `""`.

The first pass labels exactly the values satisfying the definition of distinct. The second pass visits precisely those qualifying occurrences in their original order, so its countdown assigns ranks one through the number of distinct strings and returns exactly the requested rank.

## Complexity detail
Both passes inspect $n$ strings, and source strings have a fixed maximum length of five, so the total expected time is $O(n)$. The frequency map stores at most $n$ different strings and uses $O(n)$ space.

## Alternatives and edge cases
- **Repeated linear counting:** Calling `arr.count(value)` at every position avoids an explicit map but rescans the array up to $n$ times, costing $O(n^2)$.
- **Set alone:** A set records presence but not whether a value occurs once or multiple times, so it cannot identify distinct strings by itself.
- Duplicate copies are all excluded; the first copy of a repeated string is not distinct.
- When all values repeat, every valid `k` produces `""`.
- The rank is one-based and applies only after non-distinct values are removed.
