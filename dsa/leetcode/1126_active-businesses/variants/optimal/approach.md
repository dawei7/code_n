## General
**Compare each row with the correct peer group.** Use `AVG(occurrences) OVER (PARTITION BY event_type)` to attach the average for an event type to every row of that type. The partition excludes businesses that have no row for the event, matching the definition directly.

**Filter before counting.** Keep only rows satisfying `occurrences > average_occurrences`. The strict operator is essential: a row equal to its event average contributes nothing toward active status.

**Count qualifying event types per business.** Because `(business_id, event_type)` is unique, every surviving row represents one distinct qualifying event type. Group those rows by `business_id` and retain groups with `COUNT(*) > 1`. Thus every returned business has at least two above-average event types, while every active business necessarily contributes at least two surviving rows and is returned.

## Complexity detail
The window calculation partitions and may sort the $R$ rows, giving a conservative logical bound of $O(R \log R)$ time; the final filter and grouping are linear after that organization. Window and grouping state can require $O(R)$ space. A database optimizer may use indexes, hashing, or external storage, so physical costs can differ.

## Alternatives and edge cases
- **Grouped averages joined back:** Compute one average per `event_type`, join those averages to `Events`, then filter and group; this has the same semantics and may be preferable on engines without window functions.
- **Correlated average subquery:** Recomputing the matching event average for every row is concise but can repeatedly scan `Events` and degrade toward $O(R^2)$ without optimizer decorrelation or a useful index.
- **Exactly average:** `occurrences = average_occurrences` is not strictly greater and must be excluded.
- **Only one qualifying event:** A business above average for exactly one type is not active because the requirement is more than one.
- **Event recorded by one business:** Its occurrence count equals that event's average, so that row can never qualify.
