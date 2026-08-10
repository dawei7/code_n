## General

The query considers every post and associates it with keyword rows whose word appears as a complete space-delimited token in the content. It then aggregates distinct topic IDs for each post and substitutes `"Ambiguous!"` when no keyword matches.

The exact SQL uses a left join with padded strings and `INSTR`. It does not explicitly lowercase text, and it does not specify an order inside `STRING_AGG`. Those differences from the manifest are material and are described below.

**Preserve every post with a left join**

`Posts LEFT JOIN Keywords` keeps one output-side row for every post even when no keyword satisfies the join condition.

An inner join would discard posts with no topic, making it impossible to return their required ambiguous label without a separate recovery step.

When no keyword matches, columns from `Keywords` are null in the retained joined row.

**Pad both content and keyword with spaces**

The join condition searches

`CONCAT(' ', content, ' ')`

for

`CONCAT(' ', word, ' ')`.

Adding a space on both sides turns beginning and ending word boundaries into the same pattern as internal boundaries. Keyword `"war"` matches `"war stories"`, `"stop war"`, or content exactly `"war"` because the padded text contains `" war "`.

It does not match `"warning"` because that substring is followed by `"ning"` rather than a space.

The content contract contains only English letters and spaces, so spaces are the only token boundaries the query needs to recognize. Multiple spaces do not prevent a word itself from having at least one space immediately before and after it.

**Use `INSTR` as an existence test**

`INSTR(haystack, needle)` returns a positive position when the padded keyword occurs and zero otherwise. Comparing it with `> 0` turns the search into the join predicate.

Only existence matters. A keyword appearing several times in the same post still produces one joined row for that `Keywords` record.

If the same word maps to several topics, there are several keyword rows and all corresponding topics can join.

**Rely on collation for case handling**

The problem requires case-insensitive matching. The exact source does not call `LOWER` or otherwise normalize `content` and `word`.

Its comparison is case-insensitive only when the database collation used by `INSTR` is case-insensitive, which is common for many MySQL text columns but is not guaranteed by the SQL text itself. Under a binary or case-sensitive collation, `"WAR"` would not match `"war"`.

This is an environmental assumption in the stored solution, not an operation shown in the query.

**Aggregate topics per post**

`GROUP BY post_id` collapses all joined keyword rows for one post.

`STRING_AGG(DISTINCT topic_id, ',')` removes duplicate topic IDs before concatenation. This matters when several different matching keywords express the same topic.

The comma separator produces forms such as `"1,3"`.

**Create the ambiguous label**

For a post with no keyword match, the left-joined `topic_id` is null. String aggregation ignores null inputs and returns null when no non-null topic ID is available.

`COALESCE(..., 'Ambiguous!')` replaces that null result with the required label.

Posts with at least one topic retain the aggregate string rather than the fallback.

**Ordering limitation in the exact query**

The contract requires topic IDs sorted ascending. The exact `STRING_AGG` call contains no `ORDER BY` clause.

SQL aggregate input order is not generally guaranteed, so the shown text does not prove that topics will be concatenated numerically. An engine might happen to emit ascending values because of an execution plan, but that behavior is not a portable correctness guarantee.

The manifest says IDs are aggregated in numeric order, but the source does not express that requirement. A fully robust implementation must place an explicit numeric ordering inside the supported string-aggregation syntax.

**Dialect limitation**

The file labels itself as MySQL, while conventional MySQL uses `GROUP_CONCAT` rather than `STRING_AGG`. Other engines support `STRING_AGG` but differ in syntax for `DISTINCT` and ordered aggregation.

Therefore the exact query's executability depends on the target engine or compatibility layer. The conceptual data flow remains left join, whole-word match, distinct aggregation, and null fallback.

## Complexity detail

Let $P$ be the number of posts, $K$ the number of keyword rows, and $L$ an upper bound on the text inspected by one substring search. Without a specialized text index, the join may test every post-keyword pair, costing $O(PKL)$.

Let $T$ be the number of matching joined rows. Distinct aggregation and any required ordering may cost up to $O(T\log T)$ across groups, giving the manifest-style bound $O(PKL+T\log T)$.

The join and grouping engine may materialize $O(T)$ matching state, so algorithmic working space is $O(T)$, subject to database execution choices and temporary-disk spilling.

## Alternatives and edge cases

- **Explicit lowercase normalization:** Apply `LOWER` to both padded operands or a declared case-insensitive collation so correctness does not depend on the database default.
- **Explicit ordered aggregation:** Use the target dialect's syntax to sort distinct numeric topic IDs inside aggregation; this is required for a guaranteed ascending topic string.
- **MySQL `GROUP_CONCAT`:** In native MySQL, distinct ordered aggregation is normally expressed with `GROUP_CONCAT` and an internal `ORDER BY`.
- **Split content into tokens:** Tokenization and equality joins can avoid repeated substring searches, but require engine-specific string-splitting support.
- **Keyword at content start or end:** Padding creates the missing outside boundary and allows the match.
- **Keyword inside a longer word:** Required surrounding spaces prevent false matches such as `war` in `warning`.
- **Several keywords for one topic:** `DISTINCT topic_id` prevents duplicate IDs in the result.
- **One keyword for several topics:** Separate keyword rows cause all those distinct topics to appear.
- **No matching keyword:** The left join retains the post and `COALESCE` returns `Ambiguous!`.
- **Case difference:** Correctness depends on a case-insensitive collation because the exact source performs no lowercase conversion.
- **Output row order:** No final `ORDER BY` is needed because the result table may be returned in any order.
- **Topic-string order:** Unlike row order, numeric order inside the topic string is required and is not guaranteed by the exact aggregate text.
- **Dialect portability:** `STRING_AGG(DISTINCT ..., ',')` is not uniformly supported under the MySQL label.
- **Manifest discrepancy:** The source neither lowercases explicitly nor orders the aggregate explicitly.
