## General
**Separate each employee's timeline.** Convert every `"HH:MM"` timestamp to minutes after midnight and append it to a list keyed by the corresponding name. Because all events belong to the same day, ordinary integer order is chronological order; there is no wraparound interval across midnight.

**Only consecutive triples need inspection.** Sort each employee's times. For a sorted list, examine every index $i \ge 2$ and compare the third time with the time two positions earlier. If `uses[i] - uses[i - 2] <= 60`, those three consecutive uses fit in an inclusive one-hour window, so that employee must be reported.

This test is also sufficient when an alerting window contains more than three uses: any three consecutive members of that window still span at most 60 minutes. Conversely, if every consecutive triple spans more than 60 minutes, any non-consecutive triple spans at least as much as the consecutive triple between its endpoints and cannot qualify. Sort the names found by this test to satisfy the output contract.

## Complexity detail
Grouping all $n$ events takes $O(n)$ time and space. If employee $j$ has $k_j$ uses, sorting their list costs $O(k_j \log k_j)$. Since $\sum_j k_j=n$, the combined sorting cost is at most $O(n \log n)$. The consecutive-triple scans take another $O(n)$ time, and the grouped timestamps occupy $O(n)$ space.

## Alternatives and edge cases
- **Globally sort `(name, time)` records:** This also places each employee's events together and has the same $O(n \log n)$ time bound, but grouping first makes the per-name reasoning more direct.
- **Try every triple of uses:** Exhaustive combination checking is correct but can require cubic work for one employee; sorting reveals that consecutive triples are sufficient.
- **Scan all records again for every distinct name:** This can take $O(un)$ time for $u$ employees and repeat nearly the entire input scan for every name.
- A span of exactly 60 minutes triggers an alert; use `<= 60`, not `< 60`.
- Times such as `"23:58"` and `"00:01"` are far apart within the stated single day; the interval does not wrap through midnight.
- An employee with fewer than three events can never be reported, while four or more events still produce that name only once.
- The input order is arbitrary, and the final list must be sorted independently of record order or hash-map iteration order.
