# Number of Trusted Contacts of a Customer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1364 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/) |

## Problem Description

### Goal

The `Customers` table identifies registered customers and their email addresses. `Contacts` stores each customer's contact list by `user_id`; a contact is trusted when its `contact_email` also appears as an email in `Customers`. The contact's displayed name does not determine trust. `Invoices` associates invoice IDs and prices with customers.

For every invoice, report its ID, the invoiced customer's name, its price, that customer's total number of contacts, and how many of those contacts are trusted. Customers without contacts must receive zero for both counts. Return the rows in ascending `invoice_id` order.

### Function Contract

**Inputs**

- `Customers(customer_id, customer_name, email)`.
- `Contacts(user_id, contact_name, contact_email)`.
- `Invoices(invoice_id, price, user_id)`.
- Let $C$, $K$, and $I$ denote the numbers of customer, contact, and invoice rows, and let $N=C+K+I$.

**Return value**

- Columns `invoice_id`, `customer_name`, `price`, `contacts_cnt`, and `trusted_contacts_cnt`.
- One row per invoice, sorted by `invoice_id` ascending.

### Examples

**Example 1**

- Alice has two contacts, and Bob's registered email matches one of them.
- Alice's invoice reports `contacts_cnt = 2` and `trusted_contacts_cnt = 1`.

**Example 2**

- A customer with one external contact reports `1` total contact and `0` trusted contacts.

**Example 3**

- A customer with no contact rows still appears for every invoice, with both counts equal to `0`.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Classify contacts before joining invoices.** Start from `Contacts` and left join each `contact_email` to `Customers.email`. Group by the contact owner `user_id`. `COUNT(*)` gives the owner's total contacts, while a conditional sum counts rows whose joined customer ID is non-null.

**Preserve customers without contacts.** Join each invoice to its owning customer, then left join the aggregated counts. Missing aggregate rows mean that owner has no contacts, so apply `COALESCE(..., 0)` to both count columns.

The contact aggregation creates exactly one summary row per owner represented in `Contacts`, and the email join marks exactly the contacts whose addresses belong to registered customers. The final invoice join reuses the owner's summary for every invoice without multiplying contact rows. Ordering by `invoice_id` establishes the required presentation.

#### Complexity detail

Under the general comparison-based database model, joins, grouping, and final ordering take $O(N\log N)$ time; indexed or hash-based plans may be faster. The joined and grouped working state uses $O(N)$ space.

#### Alternatives and edge cases

- **Group after joining every invoice:** Join invoices directly to all contacts and trusted customers, then group by invoice. This is correct but repeats the same contact work for customers with several invoices.
- **Correlated counts:** Run separate contact subqueries for every invoice. Without usable indexes this repeatedly scans the tables and can grow quadratically or worse.
- **Inner join to summaries:** This incorrectly drops invoices belonging to customers with no contacts; the summary join must be left-sided.
- **External email:** A contact whose email is absent from `Customers` contributes to `contacts_cnt` but not `trusted_contacts_cnt`.
- **Matching name only:** Equal names do not establish trust; only `contact_email = Customers.email` matters.
- **Several invoices:** Every invoice appears separately with the same owner-level contact counts.
- **Zero contacts:** Convert both null aggregate values to numeric zero.

</details>
