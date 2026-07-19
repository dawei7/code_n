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
