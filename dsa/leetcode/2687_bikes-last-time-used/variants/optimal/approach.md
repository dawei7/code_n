## General

Group all ride rows by `bike_number`. Each group then contains exactly the recorded uses of one bike, so `MAX(end_time)` is precisely that bike's final recorded use. Alias the aggregate as `end_time` to match the requested output schema.

The aggregation emits one row per bike regardless of how many rides that bike has. Sort those rows by the aggregated `end_time` in descending order so the bike with the newest final ride appears first. `start_time` does not affect the answer: only the greatest ride-ending timestamp determines last use.

## Complexity detail

Let $R$ be the number of rows in `Bikes`. A general grouping and result-ordering plan has an $O(R\log R)$ upper bound and uses $O(R)$ working space. An index or database-specific grouping plan may improve realized performance. The benchmark uses `size` as $R$ and contrasts the grouped scan with a correlated query that recomputes a bike's maximum end time for every ride row.

## Alternatives and edge cases

- **Window maximum plus deduplication:** `MAX(end_time) OVER (PARTITION BY bike_number)` can annotate rows before removing duplicates, but ordinary grouping is simpler.
- **Rank each bike's rides:** A descending row number per bike can select the newest ride, but computes more information than the required maximum.
- **Correlated maximum:** Recomputing `MAX(end_time)` separately for every source ride repeats work and can become quadratic.
- A bike with one ride returns that ride's `end_time` directly.
- Interleaved source rows do not matter because grouping is by bike identifier.
- Use `end_time`, not the latest `start_time`, to define last use.
- The final ordering is descending by the aggregated timestamp, not by bike number or ride identifier.
