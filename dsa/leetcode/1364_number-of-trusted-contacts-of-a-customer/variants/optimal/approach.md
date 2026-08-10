## General

**What one output row represents**

The query starts from `Invoices` because the required result contains exactly one row for every invoice. An invoice supplies three important facts: its unique `invoice_id`, its `price`, and the `user_id` of the customer who owns it. The other two tables add information about that owner. `Customers` supplies the owner's name, while `Contacts` supplies zero or more people whom that owner trusts.

There are two related counts, and keeping their meanings separate is the central difficulty:

- `contacts_cnt` counts every contact row belonging to the invoice's customer.
- `trusted_contacts_cnt` counts only those contact rows whose `contact_email` also appears as an `email` in `Customers`.

A contact does not become trusted because its name resembles a customer's name. The test used by the exact solution is email equality.

**Why every join is a left join**

The first join is `Invoices AS t1 LEFT JOIN Customers AS t2 ON t1.user_id = t2.customer_id`. It attaches the invoice owner's customer record, allowing the query to select `t2.customer_name`. Starting with invoices and preserving the left side makes the intended ownership of the output clear: an invoice is the unit that must survive to the final result.

The second join is `LEFT JOIN Contacts AS t3 ON t1.user_id = t3.user_id`. For a customer with three contacts, the invoice row expands into three intermediate rows, one per contact. For a customer with no contacts, a left join still produces one intermediate row, but all columns from `t3` are `NULL`. An inner join would remove that invoice entirely, which would be wrong: its two counts should be zero.

The third join is `LEFT JOIN Customers AS t4 ON t3.contact_email = t4.email`. Here `t4` does not represent the invoice owner. It represents a possible shop customer whose email matches the current contact's email. A match fills `t4.email` with a non-`NULL` value. A non-customer contact remains in the intermediate result because this is also a left join, but its `t4.email` is `NULL`.

For Alice's invoice in the example, the contacts join produces rows for Bob, John, and Jal. The final join finds customer rows for Bob's and John's emails, but not for Jal's email. Those three rows therefore contain three non-`NULL` values of `t3.user_id` and two non-`NULL` values of `t4.email`.

**Why the two `COUNT` expressions give different answers**

SQL's `COUNT(column)` counts non-`NULL` values in that column; it does not count every intermediate row blindly. Consequently, `COUNT(t3.user_id)` counts contact rows. On the placeholder row created for an owner with no contacts, `t3.user_id` is `NULL`, so the count is zero rather than one.

Similarly, `COUNT(t4.email)` counts only contacts that found a matching customer email. An unmatched contact is preserved by the left join, but `t4.email` is `NULL` and contributes nothing. This use of nullability turns the same joined rows into both the total count and the filtered trusted count without a separate conditional expression.

**Why grouping by the invoice is necessary**

Joins deliberately expand one invoice into several intermediate rows. `GROUP BY invoice_id` collapses all rows belonging to the same invoice back into one output row and lets both `COUNT` functions summarize that group. Since `invoice_id` is unique in `Invoices`, the selected `price` and owner are functionally determined by the group. Two invoices for the same customer remain separate groups, so each invoice appears once and receives the same customer-level contact totals.

This also explains why grouping by `user_id` would be incorrect. It would merge all invoices belonging to one customer into a single row, losing distinct invoice IDs and prices.

Finally, `ORDER BY invoice_id` puts the completed rows in the required ascending order. SQL tables have no guaranteed presentation order without an explicit `ORDER BY`, even if the input happens to look sorted.

**Why the query is correct**

Consider any invoice. The first join associates it with its owner. The second join creates exactly one relevant joined row per contact of that owner, or a single null placeholder if no contact exists. Therefore, counting non-null `t3.user_id` values yields precisely the owner's number of contacts. For each genuine contact row, the final join supplies a non-null `t4.email` exactly when the contact email has a corresponding shop-customer email. Counting those values therefore yields the trusted subset. Grouping restores one row for this invoice, and ordering changes only presentation, not any value. Since this reasoning applies independently to every invoice preserved from `t1`, the complete result has the requested rows and counts.

## Complexity detail

Let $C$, $K$, and $I$ denote the numbers of rows in `Customers`, `Contacts`, and `Invoices`, and let $N=C+K+I$. The manifest states $O(N\log N)$ time and $O(N)$ space. This is a useful high-level bound for a conventional execution plan: the database can build indexes or hash tables for the equality joins and grouping, while the final ordering of up to $I$ result rows costs $O(I\log I)$. The sort is the part that naturally introduces the logarithmic factor.

Actual SQL runtime is chosen by the database optimizer and depends on indexes, statistics, join algorithms, and whether intermediate data fits in memory. With suitable indexes or hash joins, the joins and aggregation are linear in the input plus produced join rows. Without useful access paths, a database could choose slower nested-loop work. Complexity statements for declarative SQL therefore describe a reasonable execution model rather than a fixed instruction sequence controlled by the query text.

The $O(N)$ auxiliary-space bound accounts for join lookup structures, aggregation state, and sorting buffers in the standard model. The final output itself contains $I$ rows. One subtlety is that join cardinality matters: if an email in `Customers` matches several rows, the last join multiplies a contact row, increasing both work and counts. The intended identity model must make that lookup effectively unique for the exact query's counts to retain their stated meaning.

## Alternatives and edge cases

- **Pre-aggregate contacts first:** Group `Contacts` by `user_id`, compute total and trusted counts, and then join that compact result to `Invoices`. This can avoid repeating the same aggregation work for customers with many invoices, but it requires a longer query or a common table expression.
- **Conditional aggregation:** A query can use a condition inside `SUM` or `COUNT` to identify trusted contacts. This makes the predicate explicit, although the extra customer-email lookup is still required.
- **`EXISTS` for trust membership:** Testing whether a customer email exists avoids multiplying rows when `Customers.email` is not unique. The exact solution instead counts rows produced by its final join, so it relies on each contact email matching at most one relevant customer row.
- **No contacts:** The contact left join creates a null placeholder. Both counted columns are null, producing `0` and `0` while keeping the invoice.
- **Contact who is not a customer:** `t3.user_id` is present but `t4.email` is null. The row increases `contacts_cnt` only.
- **Contact who is a customer:** Both counted values are present. The row increases both totals exactly once under the intended unique-email lookup.
- **Several invoices for one customer:** Each invoice forms a separate `invoice_id` group. The contact counts repeat, but invoice IDs and prices remain distinct.
- **Duplicate customer emails:** The local schema explicitly makes `customer_id` unique but does not state the same property for `email`. If duplicate email rows are legal, the final join duplicates a contact and the exact `COUNT` expressions overcount; pre-deduplicating emails or using `EXISTS` is the robust remedy.
- **Missing owner row:** The first left join preserves such an invoice but returns a null customer name. Normal problem data is expected to associate invoices with customers; preserving the row is still safer than silently discarding it.
- **Ordering:** `GROUP BY` does not promise sorted output. `ORDER BY invoice_id` is essential, including when the sample input already appears nearly ordered.
