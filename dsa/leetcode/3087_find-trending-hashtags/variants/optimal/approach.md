## General

**Restrict the calendar interval first.** Keep dates in the half-open range from `2024-02-01` through, but not including, `2024-03-01`. This includes leap day automatically and avoids time-of-day or month-length boundary mistakes.

**Extract one token from every remaining tweet.** Locate the `#` marker and take characters through the next space, or through the end of the text when no later space exists. The native MySQL query expresses this token rule with `REGEXP_SUBSTR`; the app-local SQLite query uses `INSTR`, `SUBSTR`, and a conditional length so both artifacts implement the same contract in their respective runtimes.

**Aggregate before ranking.** Group the extracted tokens and use `COUNT(*)`, because each qualifying tweet contains exactly one hashtag and must contribute exactly once. Sort groups by the count descending and then by the hashtag text descending. Applying `LIMIT 3` only after both sort keys produces the requested deterministic top three.

The date filter admits exactly the relevant tweets, token extraction maps each admitted row to its sole hashtag, and grouping counts every such row once. The final ordering is the problem's ranking relation, so its first three rows are precisely the requested result.

## Complexity detail

Let $n$ be the number of February rows and $S$ their total tweet-character count. Filtering and extraction take $O(S)$ time. General database grouping and ordering can take $O(n\log n)$ time, yielding $O(S+n\log n)$ overall. Derived rows, grouped counts, and sort state use $O(n)$ working space in the worst case.

## Alternatives and edge cases

- **Correlated count per hashtag:** Counting matching rows separately for every extracted hashtag is correct but can rescan the data $n$ times and take $O(n^2)$ work.
- **Take everything after `#`:** This incorrectly includes later words when the hashtag occurs before the end of the tweet.
- **Use `MONTH(tweet_date) = 2`:** Without also fixing the year, this admits February rows from every year and can inhibit an index-friendly date range.
- **Sort only by frequency:** Equal counts then have no guaranteed order; the hashtag itself must be the descending secondary key.
- **Apply `LIMIT` before grouping or sorting:** Early row truncation discards evidence and cannot determine the global top three.
- The half-open date range includes `2024-02-29` and excludes both `2024-01-31` and `2024-03-01`.
- A hashtag at the end of a tweet has no following space, so extraction must use the rest of the text.
- Fewer than three distinct February hashtags produce fewer than three output rows.
