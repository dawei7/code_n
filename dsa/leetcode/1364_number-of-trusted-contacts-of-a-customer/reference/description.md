## Description

For each invoice, combine the invoice with its customer's identity and summarize that customer's contact list. The total contact count is the number of `Contacts` rows owned by the invoiced customer. A contact is additionally a trusted shop contact when its `contact_email` occurs as an `email` in `Customers`; the displayed contact name does not determine this status.

Report every invoice even when its customer has no contacts. In that case, both contact counts are zero. Customers with several invoices receive the same owner-level counts on each of their invoice rows.
