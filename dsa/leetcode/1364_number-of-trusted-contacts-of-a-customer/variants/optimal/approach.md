## General

**Reduce registered emails to membership keys.** Trust depends only on whether a contact email exists in `Customers`, not on how many customer rows carry it. The `customer_emails` CTE therefore selects distinct addresses before any contact join. Each contact can then match at most one membership row, preventing duplicate registered addresses from multiplying either contact count.

**Aggregate each owner's contacts once.** Left join `Contacts` to the distinct email set and group by `user_id`. `COUNT(*)` counts every contact row, while `COUNT(trusted.email)` counts only rows whose address exists in the shop-customer set. This produces one reusable summary per customer who has contacts.

**Attach summaries without losing invoices.** Join every invoice to its owning customer for the requested name, then left join the owner summary. A missing summary means the customer has no contacts, so both nullable counts become zero through `COALESCE`. Reusing one summary avoids repeating contact work when a customer has several invoices, and the final `ORDER BY` establishes the required ascending invoice order.

The distinct email set gives each contact exactly one yes-or-no trust marker. Aggregation therefore computes both owner-level counts correctly. The final joins create one output row per invoice with its owner's summary, including the zero-contact case, which proves all five output columns and their cardinality.

## Complexity detail

Let $C$, $K$, and $I$ be the numbers of customers, contacts, and invoices, with $N=C+K+I$. In the general comparison-based model, deduplication, joins, grouping, and final ordering take $O(N\log N)$ time. Hash-based plans may have expected linear work before the required output sort. The distinct email set, owner summaries, and join state use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Raw customer-email join:** Joining contacts directly to `Customers` is shorter, but duplicate registered emails can multiply one contact and inflate both counts; reduce to distinct membership keys first.
- **Correlated `EXISTS`:** Testing email existence once per contact preserves correct membership semantics, but without a usable email index it can repeatedly scan `Customers`.
- **Group after joining every invoice:** This can be correct with careful distinct-email handling, but repeats the same contact work for customers with several invoices.
- **Inner join to owner summaries:** This drops invoices for customers with no contacts; the summary join must remain left-sided.
- **External contact:** The row contributes to `contacts_cnt` but not to `trusted_contacts_cnt`.
- **Contact-name match:** Names are irrelevant to trust; only `contact_email` membership matters.
- **Self email:** A contact address equal to the owner's registered email is trusted because that address exists in `Customers`.
- **Several invoices:** Each invoice remains a separate ordered row and reuses the same owner-level counts.
- **No owner contacts:** Both counts must be numeric zero rather than null.
