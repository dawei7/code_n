## General

**Duplicate identity is defined by email only.** Two customer rows may have different identifiers or names and still be duplicates for this task when their `email` values match. Conversely, rows with the same name are not duplicates if their email addresses differ. The `subset` argument tells pandas exactly which columns define equivalence.

The source returns:

`customers.drop_duplicates(subset=['email'])`.

Passing a one-element list selects `email` as the sole duplicate key. Other columns are carried along from whichever row survives; they do not participate in deciding whether two rows belong to the same group.

**Why the first occurrence survives.** pandas' default `keep` argument for `drop_duplicates` is `'first'`. The source does not spell it out, but that default is part of the exact behavior. pandas scans rows in their current order, marks an email as seen on its first occurrence, and removes later rows with the same key.

For email `john@example.com` in the example, Alice's row appears before Finn's. Alice's complete row is retained and Finn's complete row is dropped. The function does not merge their names, choose the smaller identifier, or sort before deduplication.

**Order and index behavior.** The surviving rows keep their original relative order. If original rows one, two, four, and six survive, they appear in that order. By default, `drop_duplicates` also preserves their original index labels. It does not close index gaps unless `ignore_index=True` is requested, and the source does not request it.

Index labels are not duplicate keys here. Even if two rows had the same index label, only the email subset determines whether they are considered duplicate records by this call.
Partition the rows into groups having equal email values. In each group, let the row occurring earliest in the DataFrame be its representative. `drop_duplicates` with this subset and default keep behavior returns exactly one representative per group: the earliest one. Therefore every distinct email appears exactly once, and the returned non-email fields come from the required first occurrence. That is precisely the requested table.

**Why selecting all columns in the output needs no extra code.** `drop_duplicates` removes rows but retains the DataFrame's complete column set. The output still contains `customer_id`, `name`, and `email` in the original order. A group-by aggregation could accidentally change column layout or require rules for the non-key fields; row deduplication already has the correct semantics.

**The result is not an in-place mutation.** The editorial shows an `inplace=True` variant, but the protected solution omits `inplace` and directly returns the method result. pandas' default is `False`, so `customers` is not structurally modified by this call. The returned DataFrame contains the surviving rows. This difference is operationally important when other code retains a reference to the original table.

**How detection is implemented conceptually.** pandas can maintain a hash-based set of email keys while scanning. A first key is accepted and recorded; a repeated key is rejected. Exact internals depend on dtype and pandas version, but this mental model explains the expected linear performance and stable first-occurrence behavior.

**Missing email values.** In ordinary pandas duplicate detection, repeated missing values in the selected key are treated as duplicates for this purpose, so the first missing-email row is retained and later missing-email rows are dropped. The problem examples use actual email strings, but it is useful to distinguish this from SQL, where null comparison rules differ.

The one-element list `['email']` and scalar `'email'` are both accepted subset forms. The source's list makes it obvious that subset conceptually supports one or more key columns.

## Complexity detail

Let $n$ be the number of customer rows. Hash-based duplicate detection examines one email per row, giving expected $O(n)$ time. Building the keep mask or hash state and producing the result can require $O(n)$ auxiliary or output storage in the worst case, especially when all emails are unique. These are the manifest's stated bounds.

Email hashing also depends on total string lengths at a lower level; standard table-complexity notation treats each stored email key operation as expected constant time. The input DataFrame is not copied merely for analysis in our code, but pandas creates a returned DataFrame representing retained rows.

## Alternatives and edge cases

- **Explicit `keep='first'`:** Adding the argument makes the default visible and produces the same result.
- **In-place deletion:** `inplace=True` modifies the caller's DataFrame and returns `None`; the exact source instead returns a new result.
- **Group by email:** Taking the first row of every group can work but may change ordering or index structure and is unnecessarily complex.
- **All emails unique:** Every row survives in original order.
- **All emails equal:** Only the first row survives.
- **Nonconsecutive index:** Surviving labels are preserved; call `reset_index(drop=True)` only if a new index is explicitly required.
- **Duplicate names but different emails:** Both rows survive because `name` is outside the subset.
- **Repeated missing emails:** pandas retains the first and treats later missing keys as duplicates for this operation.
