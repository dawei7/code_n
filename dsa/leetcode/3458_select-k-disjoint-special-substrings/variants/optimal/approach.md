## General

For each letter, record its first and last occurrence. Any substring containing that letter must include this entire occurrence range; otherwise the same character would appear both inside and outside the substring.

Consider a candidate whose left boundary is the first occurrence of some letter. Start its right boundary at that letter's last occurrence and scan the growing interval. Whenever the scan encounters another letter, extend the right boundary to include that letter's last occurrence as well. If an encountered letter first appears before the candidate's left boundary, the candidate cannot be special: it already has an occurrence outside the interval, and moving the left boundary would mean this was not the candidate associated with the original starting letter. Otherwise the expansion ends at the smallest closed interval for that start. Exclude it if it spans the entire string.

There are at most 26 resulting candidates. Sort them by their right endpoint and repeatedly select the first candidate whose left endpoint lies after the previous selection. Earliest-finish interval scheduling maximizes the number selected: replacing the first interval in any feasible selection with the available interval that ends earliest cannot reduce the room left for later intervals. The generated minimal intervals are sufficient because any special substring contains the closed interval generated from a character at its leftmost first occurrence; replacing it with that contained interval preserves disjointness. Therefore the greedy count is the maximum possible, and the answer is whether it reaches `k`.

## Complexity detail

Let $n=\lvert s\rvert$. Computing occurrence bounds takes $O(n)$ time. Expansion starts at most once per lowercase English letter, so its total worst-case work is $O(26n)=O(n)$. Sorting at most 26 intervals is constant with respect to $n$. The occurrence tables and candidate list each contain at most 26 entries, giving $O(1)$ auxiliary space under the fixed alphabet contract.

## Alternatives and edge cases

- **Dynamic programming over candidate endpoints:** A small interval DP also finds the maximum count, but earliest-finish scheduling is simpler because every selected interval has equal value.
- **Enumerating every substring:** Testing every pair of endpoints can be made correct, but it takes at least $O(n^2)$ time and ignores the fact that only first and last occurrences can define minimal candidates.
- **Using only each letter's initial range:** A range may contain another letter whose last occurrence lies farther right, so failing to expand transitively can accept an invalid substring.
- **Moving an invalid left boundary:** Encountering a letter that starts earlier invalidates this candidate; extending left can create a different closure but cannot produce the minimal interval for the current start.
- **Whole string:** A closed interval equal to all of `s` must be discarded even though it satisfies the occurrence condition.
- **Nested candidates:** Choosing the inner interval that ends sooner leaves at least as much room for later selections as choosing its enclosing interval.
- **Zero requested substrings:** `k = 0` is immediately feasible without constructing any interval.
