## General
**Preserve insertion order in a flat log list**

Append each `(identifier, timestamp)` pair. `put` is constant time, and scanning this list naturally emits matching identifiers in insertion order without a second ordering structure.

**Translate granularity into a prefix length**

The timestamp fields have fixed widths and separators, so each granularity corresponds to a fixed prefix: four characters for `Year`, seven for `Month`, through all nineteen for `Second`. Truncating the stored timestamp and both query endpoints to that length applies the requested precision exactly.

**Use lexicographic order as chronological order**

Every field is zero-padded from most significant to least significant. Therefore, two equal-length timestamp prefixes compare lexicographically in the same order as their represented dates and times. Include a log precisely when `start_prefix <= timestamp_prefix <= end_prefix`.

**Why truncation gives inclusive boundaries**

All timestamps sharing the start prefix belong to the first requested time bucket, even if their omitted fields precede the literal fields in `start`; the same applies to the entire end bucket. Prefix comparison includes both buckets and every complete bucket between them, which is exactly an inclusive granularity query.

## Complexity detail
Let `P` be the number of stored logs and `Q` the number of retrievals in a trace. `put` takes $O(1)$ time, while each `retrieve` scans `P` logs in $O(P)$ time, for $O(QP)$ worst-case trace time. The stored log list uses $O(P)$ space; each returned list uses space proportional to its matches.

## Alternatives and edge cases
- **Keep logs sorted and binary-search bounds:** retrieval can start in $O(\log P)$ time, but array insertion costs $O(P)$ unless a balanced ordered structure is available.
- **Sort a copy on every retrieval:** enables binary search afterward but repeats $O(P \log P)$ work for each query.
- **Bucket maps by every granularity:** can accelerate repeated queries but duplicates indexing state across six precision levels.
- Query endpoints are inclusive after truncation to the selected granularity.
- A `Day` query ignores hours, minutes, and seconds in both endpoint strings.
- Distinct IDs may share an identical timestamp and must all be returned.
- A query with no stored timestamp in its truncated interval returns an empty list.
- Fixed-width zero padding is essential to the equivalence between string and chronological ordering.
