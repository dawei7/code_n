## General
**Store occurrences by tweet name.** A hash map associates each name with a list of all recorded timestamps. Recording an occurrence appends its time, so duplicate timestamps remain distinct and the update takes constant amortized time.

**Translate the frequency into a bucket width.** Select 60, 3600, or 86400 seconds and compute `bucket_count = (endTime - startTime) // width + 1`. Initialize exactly that many zero counts; this formula includes the possibly shorter final bucket.

**Assign each relevant record once.** Scan the timestamps stored for the requested name. Ignore times outside the inclusive query interval. For every time inside it, `(time - startTime) // width` is its unique bucket index, so increment that count. These half-open bucket calculations agree with the inclusive query because the final accepted second `endTime` still maps within the allocated last bucket. Each qualifying occurrence is counted once, and every returned bucket corresponds to exactly one requested subinterval.

## Complexity detail
`recordTweet` takes $O(1)$ amortized time. A query initializes $b$ counts and scans $r$ timestamps, for $O(r+b)$ time. Across all names, storage is linear in the total number of recorded occurrences; for the queried name its contribution is $O(r)$.

## Alternatives and edge cases
- **Scan records once per bucket:** Testing all $r$ timestamps separately for each of $b$ buckets is correct but costs $O(rb)$ time.
- **Sorted timestamps plus binary search:** Maintaining or lazily sorting each name's times can answer sparse-range queries with boundary searches, but insertion and sorting tradeoffs complicate a workload where the direct linear scan already satisfies the contract.
- **Unknown tweet name:** No timestamps exist, but the method must still return the correct number of zero buckets.
- **Duplicate timestamps:** Every recording is a separate occurrence and must increment the same bucket.
- **Partial final bucket:** The last bucket ends at `endTime`, not necessarily at a full frequency boundary.
- **Inclusive endpoint:** A record exactly at `endTime` belongs to the last bucket.
