# Minimum Money Required Before Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2412 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-money-required-before-transactions](https://leetcode.com/problems/minimum-money-required-before-transactions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-money-required-before-transactions/).

### Goal
Determine the minimum initial capital required to complete a series of transactions regardless of the order in which they are performed. Each transaction consists of a cost (money spent) and a cashback (money returned). If you have enough money to cover the cost, you perform the transaction and your balance decreases by the cost and then increases by the cashback.

### Function Contract
**Inputs**

- `transactions`: A list of lists, where each inner list `[cost, cashback]` represents a transaction.

**Return value**

- An integer representing the minimum initial money required to complete all transactions.

### Examples
**Example 1**

- Input: `transactions = [[2,1],[5,0],[4,2]]`
- Output: `10`

**Example 2**

- Input: `transactions = [[3,0],[0,3]]`
- Output: `3`

**Example 3**

- Input: `transactions = [[0,0]]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a **Greedy strategy**. We categorize transactions into two groups: those where `cost > cashback` (net loss) and those where `cost <= cashback` (net gain or break-even).
1. For net loss transactions, we sort them by `cashback` in descending order to minimize the peak money required.
2. For net gain transactions, we perform them as early as possible to increase our balance.
3. The total initial money is the sum of all net losses plus the maximum "bottleneck" encountered during the sequence.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting of transactions, where `N` is the number of transactions.
- **Space Complexity**: `O(1)` (excluding input storage), as we only use a few variables to track the running balance and the maximum requirement.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(transactions: List[List[int]]) -> int:
    """
    Calculates the minimum initial money required to complete all transactions.
    """
    total_loss = sum(max(0, cost - cashback) for cost, cashback in transactions)
    answer = 0

    for cost, cashback in transactions:
        if cost > cashback:
            answer = max(answer, total_loss + cashback)
        else:
            answer = max(answer, total_loss + cost)

    return answer
```
</details>
