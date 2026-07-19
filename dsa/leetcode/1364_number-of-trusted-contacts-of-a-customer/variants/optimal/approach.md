## General
**Classify contacts before joining invoices.** Start from `Contacts` and left join each `contact_email` to `Customers.email`. Group by the contact owner `user_id`. `COUNT(*)` gives the owner's total contacts, while a conditional sum counts rows whose joined customer ID is non-null.

**Preserve customers without contacts.** Join each invoice to its owning customer, then left join the aggregated counts. Missing aggregate rows mean that owner has no contacts, so apply `COALESCE(..., 0)` to both count columns.

The contact aggregation creates exactly one summary row per owner represented in `Contacts`, and the email join marks exactly the contacts whose addresses belong to registered customers. The final invoice join reuses the owner's summary for every invoice without multiplying contact rows. Ordering by `invoice_id` establishes the required presentation.

## Complexity detail
Under the general comparison-based database model, joins, grouping, and final ordering take $O(N\log N)$ time; indexed or hash-based plans may be faster. The joined and grouped working state uses $O(N)$ space.

## Alternatives and edge cases
- **Group after joining every invoice:** Join invoices directly to all contacts and trusted customers, then group by invoice. This is correct but repeats the same contact work for customers with several invoices.
- **Correlated counts:** Run separate contact subqueries for every invoice. Without usable indexes this repeatedly scans the tables and can grow quadratically or worse.
- **Inner join to summaries:** This incorrectly drops invoices belonging to customers with no contacts; the summary join must be left-sided.
- **External email:** A contact whose email is absent from `Customers` contributes to `contacts_cnt` but not `trusted_contacts_cnt`.
- **Matching name only:** Equal names do not establish trust; only `contact_email = Customers.email` matters.
- **Several invoices:** Every invoice appears separately with the same owner-level contact counts.
- **Zero contacts:** Convert both null aggregate values to numeric zero.
