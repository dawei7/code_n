## General

Group rows by `artist`; each group then contains exactly the ranking-list occurrences credited to that artist. `COUNT(*)` counts every row in the group and names the result `occurrences`. Track names do not participate because the requested quantity is appearances, not distinct songs.

Apply two explicit sort keys. `occurrences DESC` places more frequent artists first. `artist ASC` resolves every equal-count group deterministically in the required alphabetical order. Grouping emits one row per distinct artist, so no additional deduplication is necessary.

## Complexity detail

Let $R$ be the number of Spotify rows. General grouping and result ordering require $O(R\log R)$ time and $O(R)$ working space. The benchmark uses `size` as $R$ and repeats one artist across all rows; a correlated query that recounts an artist for every input row completes all tiers but performs $O(R^2)$ work.

## Alternatives and edge cases

- **Window count plus distinct:** A window function can annotate every row before deduplication, but ordinary grouping is more direct.
- **Correlated count:** Counting matching rows separately for each source row repeats work and can become quadratic.
- `COUNT(DISTINCT track_name)` is wrong because separate ranking rows count even when their track names match.
- Equal counts require ascending artist names as a second ordering key.
- A single-row table produces one artist with one occurrence.
