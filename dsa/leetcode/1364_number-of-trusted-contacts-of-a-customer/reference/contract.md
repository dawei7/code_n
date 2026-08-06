## Function Contract

**Input**

- `Customers`: the shop-customer table described above.
- `Contacts`: each customer's trusted-person list described above.
- `Invoices`: the customer invoices described above.

Let $C$, $K$, and $I$ be the respective row counts, and let $N=C+K+I$.

**Return value**

Return one row for every invoice with these columns:

- `invoice_id`: the invoice's unique ID.
- `customer_name`: the name of the customer related to that invoice.
- `price`: the invoice price.
- `contacts_cnt`: the number of contacts belonging to that customer.
- `trusted_contacts_cnt`: the number of those contacts whose email occurs in `Customers.email`.

Sort the result by `invoice_id` in ascending order. An email's existence determines trust; neither a matching name nor the number of customer rows carrying that email changes the number of contact rows.
