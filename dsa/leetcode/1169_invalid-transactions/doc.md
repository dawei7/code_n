# Invalid Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1169 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [invalid-transactions](https://leetcode.com/problems/invalid-transactions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/invalid-transactions/).

### Goal
Return every transaction string that is invalid because its amount is too high or because the same person has another transaction in a different city within 60 minutes.

### Function Contract
**Inputs**

- `transactions`: strings formatted as `"name,time,amount,city"`.

**Return value**

All invalid transaction strings. Order is not important.

### Examples
**Example 1**

- Input: `transactions = ["alice,20,800,mtv","alice,50,100,beijing"]`
- Output: `["alice,20,800,mtv","alice,50,100,beijing"]`

**Example 2**

- Input: `transactions = ["alice,20,1200,mtv","bob,50,100,beijing"]`
- Output: `["alice,20,1200,mtv"]`

**Example 3**

- Input: `transactions = ["alice,20,100,mtv","alice,80,100,mtv"]`
- Output: `[]`

---

## Solution
### Approach
Parsing, grouping, and pairwise window checks.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` in the straightforward grouping approach.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(transactions):
    parsed = []
    by_name = defaultdict(list)
    for index, transaction in enumerate(transactions):
        name, time, amount, city = transaction.split(",")
        entry = (index, name, int(time), int(amount), city)
        parsed.append(entry)
        by_name[name].append(entry)

    invalid = set()
    for index, name, time, amount, city in parsed:
        if amount > 1000:
            invalid.add(index)
        for other_index, _, other_time, _, other_city in by_name[name]:
            if city != other_city and abs(time - other_time) <= 60:
                invalid.add(index)
                invalid.add(other_index)

    return [transactions[i] for i in range(len(transactions)) if i in invalid]
```
</details>
