## Description

Table: `Customers`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
| email         | varchar |
+---------------+---------+
customer_id is the column of unique values for this table.
Each row of this table contains the name and the email of a customer of an online shop.
```

Table: `Contacts`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | id      |
| contact_name  | varchar |
| contact_email | varchar |
+---------------+---------+
(user_id, contact_email) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the name and email of one contact of customer with user_id.
This table contains information about people each customer trust. The contact may or may not exist in the Customers table.
```

Table: `Invoices`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| invoice_id   | int     |
| price        | int     |
| user_id      | int     |
+--------------+---------+
invoice_id is the column of unique values for this table.
Each row of this table indicates that user_id has an invoice with invoice_id and a price.
```

Write a solution to find the following for each $\text{invoice}_{id}$:

- $\text{customer}_{name}$: The name of the customer the invoice is related to.

- `price`: The price of the invoice.

- $\text{contacts}_{cnt}$: The number of contacts related to the customer.

- `trusted_contacts_cnt`: The number of contacts related to the customer and at the same time they are customers to the shop. (i.e their email exists in the `Customers` table.)

Return the result table **ordered** by $\text{invoice}_{id}$.

The result format is in the following example.
### Function Contract

**Input**

- `Customers`: the shop-customer table described above.
- `Contacts`: each customer's trusted-person list described above.
- `Invoices`: the customer invoices described above.

Let $C$, $K$, and $I$ be the respective row counts, and let $N=C+K+I$.

**Return value**

Return one row for every invoice with these columns:

- $\text{invoice}_{id}$: the invoice's unique ID.
- $\text{customer}_{name}$: the name of the customer related to that invoice.
- `price`: the invoice price.
- $\text{contacts}_{cnt}$: the number of contacts belonging to that customer.
- `trusted_contacts_cnt`: the number of those contacts whose email occurs in `Customers.email`.

Sort the result by $\text{invoice}_{id}$ in ascending order. An email's existence determines trust; neither a matching name nor the number of customer rows carrying that email changes the number of contact rows.

### Examples

#### Example 1

```
**Input:**
Customers table:
+-------------+---------------+--------------------+
| customer_id | customer_name | email              |
+-------------+---------------+--------------------+
| 1           | Alice         | alice@leetcode.com |
| 2           | Bob           | bob@leetcode.com   |
| 13          | John          | john@leetcode.com  |
| 6           | Alex          | alex@leetcode.com  |
+-------------+---------------+--------------------+
Contacts table:
+-------------+--------------+--------------------+
| user_id     | contact_name | contact_email      |
+-------------+--------------+--------------------+
| 1           | Bob          | bob@leetcode.com   |
| 1           | John         | john@leetcode.com  |
| 1           | Jal          | jal@leetcode.com   |
| 2           | Omar         | omar@leetcode.com  |
| 2           | Meir         | meir@leetcode.com  |
| 6           | Alice        | alice@leetcode.com |
+-------------+--------------+--------------------+
Invoices table:
+------------+-------+---------+
| invoice_id | price | user_id |
+------------+-------+---------+
| 77         | 100   | 1       |
| 88         | 200   | 1       |
| 99         | 300   | 2       |
| 66         | 400   | 2       |
| 55         | 500   | 13      |
| 44         | 60    | 6       |
+------------+-------+---------+
**Output:**
+------------+---------------+-------+--------------+----------------------+
| invoice_id | customer_name | price | contacts_cnt | trusted_contacts_cnt |
+------------+---------------+-------+--------------+----------------------+
| 44         | Alex          | 60    | 1            | 1                    |
| 55         | John          | 500   | 0            | 0                    |
| 66         | Bob           | 400   | 2            | 0                    |
| 77         | Alice         | 100   | 3            | 2                    |
| 88         | Alice         | 200   | 3            | 2                    |
| 99         | Bob           | 300   | 2            | 0                    |
+------------+---------------+-------+--------------+----------------------+
**Explanation:**
Alice has three contacts, two of them are trusted contacts (Bob and John).
Bob has two contacts, none of them is a trusted contact.
Alex has one contact and it is a trusted contact (Alice).
John doesn't have any contacts.
```