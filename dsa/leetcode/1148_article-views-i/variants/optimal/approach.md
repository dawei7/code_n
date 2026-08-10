## General

**Translate “viewed their own article” into an equality**

Each row identifies the article's author and the person who viewed it. The schema explicitly says equal `author_id` and `viewer_id` values represent the same person. Therefore, a row is evidence of a self-view exactly when

`author_id = viewer_id`.

The `WHERE` clause applies this condition before the result is projected. Rows where somebody viewed another person's article are discarded. The article identifier and date do not affect qualification: the problem asks whether an author viewed at least one of their own articles, not which article it was or when it occurred.

This is a row-level predicate, so `WHERE` is the correct SQL stage. `HAVING` is intended for conditions on groups or aggregate values and would introduce unnecessary grouping here.

**Return each qualifying person only once**

One author may view the same self-authored article many times, may view several of their own articles, and may have duplicate rows because the table has no primary key. The requested output is a set of authors, not a list of view events. Consequently, the selected expression is

`DISTINCT author_id`.

`DISTINCT` collapses all identical selected author identifiers after the `WHERE` filter. It handles both meaningful multiple self-views and literal duplicate table rows. A qualifying author contributes exactly one output row no matter how many pieces of evidence exist.

The query aliases `author_id` as `id` because the required result column is named `id`. The alias changes only the output label; the underlying value remains the qualifying person's identifier.

**Sort by the requested output identifier**

`ORDER BY 1` sorts by the first selected expression, which is the aliased author identifier. The default SQL sort direction is ascending, so this produces increasing `id` values as required.

Using the positional form avoids any ambiguity about whether the engine permits the output alias in the order clause, though `ORDER BY id` would be an equivalent and often more explicit formulation in MySQL.

The order step occurs after duplicate elimination in the conceptual result. It therefore sorts only the distinct qualifying authors, not every source view row.

**Follow the logical query stages**

The solution can be understood as four small transformations:

1. `FROM Views` supplies every view-event row.
2. `WHERE author_id = viewer_id` retains only self-view events.
3. `SELECT DISTINCT author_id AS id` projects the person identifier and removes repetitions.
4. `ORDER BY 1` puts those unique identifiers in ascending order.

In the example, author seven viewing article two survives because both identifiers are seven. Author four's two identical self-view rows also survive initially, but `DISTINCT` reduces them to one identifier. Rows for authors whose viewers differ are rejected. Sorting the resulting set `{7, 4}` produces four followed by seven.

**Why the query is correct**

Every returned identifier came from a row satisfying `author_id = viewer_id`. By the schema's identity rule, that row proves the person authored and viewed the same article, so every returned author qualifies.

Conversely, suppose an author viewed at least one of their own articles. The table contains at least one corresponding row in which the author and viewer identifiers are equal. That row satisfies the filter, and its `author_id` enters the selected set. `DISTINCT` may merge it with other evidence for the same author but cannot remove the author's only result value. Thus every qualifying author is returned.

Duplicate elimination establishes exactly one row per author, the alias establishes the correct column name, and ordering establishes the required ascending presentation. Together, these properties match the full contract.

No join is needed because the author and viewer identifiers required for comparison are already present in each `Views` row. Joining to an author table or joining `Views` to itself would add work without providing new information.

## Complexity detail

Let `r` be the number of rows in `Views` and `a` be the number of distinct authors that pass the equality filter.

Evaluating `author_id = viewer_id` across the source takes `O(r)` logical row work. Duplicate elimination may use hashing or sorting. The final required order sorts at most `a` identifiers, taking `O(a log a)` time. This gives the manifest's combined bound `O(r + a log a)`.

Storing the distinct qualifying identifiers and sorting state can require `O(a)` auxiliary space. Physical database costs vary with indexes, execution plans, and whether duplicate elimination and ordering share a sort, but the stated bounds describe the result-size-sensitive logical approach.

The returned table itself contains `a` rows. If output storage is counted separately, it is also linear in `a`.

## Alternatives and edge cases

- **Use `GROUP BY author_id`:** Filtering self-view rows and grouping by author can also return one row per person. `DISTINCT` is more direct because no aggregate value is needed.
- **Use a self-join:** All necessary fields are already in one row. A join would create needless row combinations and make duplicate handling harder.
- **Select every matching row without `DISTINCT`:** Authors with repeated self-views or duplicate source rows would appear several times, violating the one-row-per-author result.
- **Compare `article_id` with `viewer_id`:** Those columns represent different kinds of identifiers. Self-view status is defined by equality between author and viewer.
- **Filter by date:** The problem imposes no date range. Every row is eligible evidence regardless of `view_date`.
- **Duplicate rows:** They do not change the answer because `DISTINCT` collapses their repeated author identifier.
- **Several own articles:** An author who self-views multiple articles still appears once.
- **Author also views other people's articles:** Non-self rows are ignored, while any self-view row is sufficient for qualification.
- **No self-views:** The filter leaves no rows, and the query returns an empty one-column result.
- **Ordering:** Ascending order is mandatory here, unlike SQL tasks that permit any order. `ORDER BY 1` supplies it explicitly.
- **Null considerations:** The stated schema does not introduce a special null rule. If null identifiers existed, SQL equality with null would not evaluate true, so such a row would not prove a known self-view.
