## General
The candidate separates the task into identifying the survivor of every email group and deleting everything else. The survivor set is computed once by grouping on `email` and taking `MIN(id)` from each group. The outer `DELETE` then removes every row whose `id` is not in that set.

For `(1,a), (2,b), (3,a), (4,a)`, grouping produces keeper ids `1` and `2`. Rows 3 and 4 are outside that set and are deleted, while rows 1 and 2 remain. A group with one row contributes that row's id, so already-unique emails are unchanged.

Every retained id is the minimum id of its email group and is therefore the required representative. Conversely, every nonminimum row is absent from the keeper set and is deleted. Because `id` is a non-null primary key and each email is non-null, the subquery cannot introduce a `NULL` that would make `NOT IN` indeterminate. Thus exactly one row, with the smallest original id, remains for every email.

The final `SELECT` is only the app-local observation adapter: LeetCode observes the table after mutation, whereas the local SQLite runner needs a result set to compare. The immutable Accepted MySQL source uses a joined delete with the same survivor rule; the candidate is intentionally staged separately and is not submission evidence.

## Complexity detail
The grouping scan builds the minimum-id survivor set in $O(n \log n)$ logical work under SQLite's sort-based grouping plan. Testing membership and deleting the other rows requires another linear scan. The temporary grouping structure and survivor set use $O(n)$ space in the worst case. Exact physical costs remain database- and index-dependent.

## Alternatives and edge cases
- **Correlated `EXISTS`:** Deleting a row when a smaller same-email row exists mirrors the native predicate, but without an email index SQLite can repeat a growing search for every row and take quadratic time.
- **Joined delete:** The immutable Accepted MySQL source names duplicate and keeper aliases directly, but SQLite does not support MySQL's multi-table `DELETE` syntax.
- **Window ranking:** `ROW_NUMBER() OVER (PARTITION BY email ORDER BY id)` labels every non-survivor clearly, but deleting through the ranked result requires dialect-specific CTE support.
- **Minimum-id rule:** Deleting an arbitrary member of each duplicate group violates the contract even if one row per email remains.
- **Already-distinct data:** Every id appears in the survivor set, so the candidate deletes nothing.
- **Large duplicate groups:** One minimum id is retained regardless of group size or physical row order.
- **Null semantics:** The schema guarantees non-null primary keys and emails, which makes `NOT IN` safe here.
