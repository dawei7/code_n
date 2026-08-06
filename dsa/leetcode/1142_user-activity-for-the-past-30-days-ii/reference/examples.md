## Examples

**Example 1**

- **Input:** `Activity = [[1,1,"2019-07-20","open_session"],[1,1,"2019-07-20","scroll_down"],[1,1,"2019-07-20","end_session"],[2,4,"2019-07-20","open_session"],[2,4,"2019-07-21","send_message"],[2,4,"2019-07-21","end_session"],[3,2,"2019-07-21","open_session"],[3,2,"2019-07-21","send_message"],[3,2,"2019-07-21","end_session"],[3,5,"2019-07-21","open_session"],[3,5,"2019-07-21","scroll_down"],[3,5,"2019-07-21","end_session"],[4,3,"2019-06-25","open_session"],[4,3,"2019-06-25","end_session"]]`

| user_id | session_id | activity_date | activity_type |
|---:|---:|---|---|
| 1 | 1 | 2019-07-20 | open_session |
| 1 | 1 | 2019-07-20 | scroll_down |
| 1 | 1 | 2019-07-20 | end_session |
| 2 | 4 | 2019-07-20 | open_session |
| 2 | 4 | 2019-07-21 | send_message |
| 2 | 4 | 2019-07-21 | end_session |
| 3 | 2 | 2019-07-21 | open_session |
| 3 | 2 | 2019-07-21 | send_message |
| 3 | 2 | 2019-07-21 | end_session |
| 3 | 5 | 2019-07-21 | open_session |
| 3 | 5 | 2019-07-21 | scroll_down |
| 3 | 5 | 2019-07-21 | end_session |
| 4 | 3 | 2019-06-25 | open_session |
| 4 | 3 | 2019-06-25 | end_session |

- **Output:** `[[1.33]]`

| average_sessions_per_user |
|---:|
| 1.33 |

- **Explanation:** Within the 30-day period, users `1` and `2` each have one distinct session and user `3` has two. User `4` has no qualifying activity. The required average is therefore $(1 + 1 + 2) / 3 = 1.33$ after rounding.
