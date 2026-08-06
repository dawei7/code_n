## Events Table

| Column Name | Type |
|---|---|
| `business_id` | int |
| `event_type` | varchar |
| `occurrences` | int |

The pair `(business_id, event_type)` is the composite primary key, so a business has at most one row for a given event type. Each row records how many times that event occurred at that business.
