WITH customer_emails AS (
    SELECT DISTINCT email
    FROM Customers
),
contact_counts AS (
    SELECT c.user_id,
           COUNT(*) AS contacts_cnt,
           COUNT(trusted.email) AS trusted_contacts_cnt
    FROM Contacts AS c
    LEFT JOIN customer_emails AS trusted
      ON trusted.email = c.contact_email
    GROUP BY c.user_id
)
SELECT i.invoice_id,
       customer.customer_name,
       i.price,
       COALESCE(counts.contacts_cnt, 0) AS contacts_cnt,
       COALESCE(counts.trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM Invoices AS i
JOIN Customers AS customer
  ON customer.customer_id = i.user_id
LEFT JOIN contact_counts AS counts
  ON counts.user_id = i.user_id
ORDER BY i.invoice_id;
