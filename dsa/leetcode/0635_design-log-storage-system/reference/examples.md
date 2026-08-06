## Examples

**Example 1**

- **Input:** `["LogSystem", "put", "put", "put", "retrieve", "retrieve"] [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]`
- **Output:** `[null, null, null, null, [3,2,1], [2,1]]`
- **Explanation:** After constructing the system, store the three listed logs. The `Year` query covers all of 2016 and 2017 at year precision, so IDs `3`, `2`, and `1` all qualify. The `Hour` query covers the hour buckets from January 1, 2016 at `01:XX:XX` through January 1, 2017 at `23:XX:XX`, so IDs `2` and `1` qualify. ID `3` is excluded from that second result because its `00:00:00` timestamp precedes the starting hour bucket.
