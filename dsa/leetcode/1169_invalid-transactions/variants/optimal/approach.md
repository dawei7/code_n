## General
**Parse without losing identity.** Convert each string into its name, numeric time, numeric amount, city, and original index. Mark an index immediately when its amount is greater than `1000`, and group the parsed records by name. Using indices rather than string values preserves separate duplicate occurrences.

**Sort each person's timeline.** Sort every name group by time. For a transaction at time $t$, the only relevant same-name records lie in the inclusive interval $[t-60,t+60]$. Maintain two monotone boundaries around that interval and a frequency map of cities inside it. As the center advances, add records whose time is at most `t + 60` and remove records whose time is less than `t - 60`.

**Detect a different city in constant time.** The current window contains another city exactly when its total record count is greater than the count for the center transaction's city. If so, mark the center's original index. Each qualifying counterpart is independently marked when it becomes the center, so the symmetric rule is fully covered without enumerating every pair. Finally, return the original strings at marked indices.

## Complexity detail
Parsing and grouping cost $O(n)$. Sorting all name groups costs at most $O(n \log n)$, and the sliding boundaries add and remove every record once, taking $O(n)$ expected time with hash maps. Parsed records, groups, window counts, and invalid markers use $O(n)$ space.

## Alternatives and edge cases
- **Compare every same-name pair:** This is direct and correct but takes $O(n^2)$ time when many records share one name.
- **Check only adjacent sorted records:** A transaction may conflict with a non-adjacent record inside the 60-minute window, so adjacency alone is insufficient.
- **Amount exactly `1000`:** The rule says exceeds `$1000`, so this amount is not invalid by itself.
- **Difference exactly `60`:** The time boundary is inclusive, so different-city records exactly 60 minutes apart invalidate each other.
- **Same city:** Time proximity alone is not enough; the cities must differ.
- **Different names:** Their records never invalidate one another through the city-and-time rule.
- **Duplicate strings:** Each array position is a separate occurrence and must be retained if that position is invalid.
