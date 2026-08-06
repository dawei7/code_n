## Examples

**Example 1**

- **Input:** `Customers = [[1,"Alice","alice@leetcode.com"],[2,"Bob","bob@leetcode.com"],[13,"John","john@leetcode.com"],[6,"Alex","alex@leetcode.com"]], Contacts = [[1,"Bob","bob@leetcode.com"],[1,"John","john@leetcode.com"],[1,"Jal","jal@leetcode.com"],[2,"Omar","omar@leetcode.com"],[2,"Meir","meir@leetcode.com"],[6,"Alice","alice@leetcode.com"]], Invoices = [[77,100,1],[88,200,1],[99,300,2],[66,400,2],[55,500,13],[44,60,6]]`

`Customers`:

| customer_id | customer_name | email |
|---:|---|---|
| 1 | Alice | alice@leetcode.com |
| 2 | Bob | bob@leetcode.com |
| 13 | John | john@leetcode.com |
| 6 | Alex | alex@leetcode.com |

`Contacts`:

| user_id | contact_name | contact_email |
|---:|---|---|
| 1 | Bob | bob@leetcode.com |
| 1 | John | john@leetcode.com |
| 1 | Jal | jal@leetcode.com |
| 2 | Omar | omar@leetcode.com |
| 2 | Meir | meir@leetcode.com |
| 6 | Alice | alice@leetcode.com |

`Invoices`:

| invoice_id | price | user_id |
|---:|---:|---:|
| 77 | 100 | 1 |
| 88 | 200 | 1 |
| 99 | 300 | 2 |
| 66 | 400 | 2 |
| 55 | 500 | 13 |
| 44 | 60 | 6 |

- **Output:** `[[44,"Alex",60,1,1],[55,"John",500,0,0],[66,"Bob",400,2,0],[77,"Alice",100,3,2],[88,"Alice",200,3,2],[99,"Bob",300,2,0]]`

| invoice_id | customer_name | price | contacts_cnt | trusted_contacts_cnt |
|---:|---|---:|---:|---:|
| 44 | Alex | 60 | 1 | 1 |
| 55 | John | 500 | 0 | 0 |
| 66 | Bob | 400 | 2 | 0 |
| 77 | Alice | 100 | 3 | 2 |
| 88 | Alice | 200 | 3 | 2 |
| 99 | Bob | 300 | 2 | 0 |

- **Explanation:** Alice has three contacts; Bob and John are trusted because their emails belong to shop customers, while Jal is external. Bob's two contacts are both external. Alex has one contact, Alice, whose email is registered, so that contact is trusted. John has no contact rows and therefore receives zero for both counts.
