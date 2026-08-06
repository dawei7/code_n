## Examples

**Example 1**

- **Input:** Users Moustafa, Jonathan, Winston, and Luis, with transfers of 400 from Moustafa to Winston, 500 from Winston to Jonathan, and 200 from Jonathan to Moustafa.
- **Output:**
  | user_id | user_name | credit | credit_limit_breached |
  | --- | --- | --- | --- |
  | 1 | Moustafa | -100 | Yes |
  | 2 | Jonathan | 500 | No |
  | 3 | Winston | 9900 | No |
  | 4 | Luis | 800 | No |
- **Explanation:** Luis remains unchanged; only Moustafa finishes below zero and receives `"Yes"`.

**Example 2**

- **Input:** A user with credit zero and no transactions.
- **Output:**
  | user_id | user_name | credit | credit_limit_breached |
  | --- | --- | --- | --- |
  | 1 | Alice | 0 | No |
- **Explanation:** The breach test is strictly less than zero.

**Example 3**

- **Input:** One user pays 75 and receives 20 from separate users.
- **Output:**
  | user_id | user_name | credit | credit_limit_breached |
  | --- | --- | --- | --- |
  | 1 | Bob | 945 | No |
- **Explanation:** Incoming and outgoing amounts contribute with opposite signs.
