## Examples

**Example 1**

- Input: `Person = [[1,"Wang","Allen"],[2,"Alice","Bob"]], Address = [[1,2,"New York City","New York"],[2,3,"Leetcode","California"]]`

Person:

| personId | lastName | firstName |
|---:|---|---|
| 1 | Wang | Allen |
| 2 | Alice | Bob |

Address:

| addressId | personId | city | state |
|---:|---:|---|---|
| 1 | 2 | New York City | New York |
| 2 | 3 | Leetcode | California |

- Output: `[["Allen","Wang",null,null],["Bob","Alice","New York City","New York"]]`

| firstName | lastName | city | state |
|---|---|---|---|
| Allen | Wang | null | null |
| Bob | Alice | New York City | New York |

- Explanation: Person `1` has no address row, so Allen Wang's city and state are null. Address row `1` belongs to person `2`, so Bob Alice receives the New York City address. The address for person `3` creates no output row because no matching person exists.
