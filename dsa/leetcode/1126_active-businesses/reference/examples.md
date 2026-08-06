## Examples

**Example 1**

- **Input:** `Events = [[1,"reviews",7],[3,"reviews",3],[1,"ads",11],[2,"ads",7],[3,"ads",6],[1,"page views",3],[2,"page views",12]]`

| business_id | event_type | occurrences |
|---:|---|---:|
| 1 | reviews | 7 |
| 3 | reviews | 3 |
| 1 | ads | 11 |
| 2 | ads | 7 |
| 3 | ads | 6 |
| 1 | page views | 3 |
| 2 | page views | 12 |

- **Output:** `[[1]]`

| business_id |
|---:|
| 1 |

- **Explanation:** The `reviews` average is $(7 + 3) / 2 = 5$, the `ads` average is $(11 + 7 + 6) / 3 = 8$, and the `page views` average is $(3 + 12) / 2 = 7.5$. Business `1` has `7` reviews, exceeding `5`, and `11` ads, exceeding `8`. It is therefore active because it is above average for two event types.
