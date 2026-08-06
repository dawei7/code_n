## Examples

**Example 1**

- **Input:** `FriendRequest = [[1,2,"2016/06/01"],[1,3,"2016/06/01"],[1,4,"2016/06/01"],[2,3,"2016/06/02"],[3,4,"2016/06/09"]], RequestAccepted = [[1,2,"2016/06/03"],[1,3,"2016/06/08"],[2,3,"2016/06/08"],[3,4,"2016/06/09"],[3,4,"2016/06/10"]]`

FriendRequest:

| sender_id | send_to_id | request_date |
|---:|---:|---|
| 1 | 2 | 2016/06/01 |
| 1 | 3 | 2016/06/01 |
| 1 | 4 | 2016/06/01 |
| 2 | 3 | 2016/06/02 |
| 3 | 4 | 2016/06/09 |

RequestAccepted:

| requester_id | accepter_id | accept_date |
|---:|---:|---|
| 1 | 2 | 2016/06/03 |
| 1 | 3 | 2016/06/08 |
| 2 | 3 | 2016/06/08 |
| 3 | 4 | 2016/06/09 |
| 3 | 4 | 2016/06/10 |

- **Output:** `[[0.8]]`

| accept_rate |
|---:|
| 0.8 |

- **Explanation:** The acceptance table contains four unique directed pairs because the two rows for `(3,4)` count once. The request table contains five unique pairs, so the overall rate is $4/5 = 0.80$.
