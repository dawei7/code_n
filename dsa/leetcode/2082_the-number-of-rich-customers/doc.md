# The Number of Rich Customers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2082 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-rich-customers/) |

## Problem Description

### Goal

The `Store` table records individual bills. Each row has a unique bill identifier, the customer responsible for that bill, and its integer amount. A customer is considered rich when at least one of their bills has an amount strictly greater than 500.

Report how many distinct customers satisfy that condition. Multiple qualifying bills from the same customer must contribute only once, an amount equal to 500 does not qualify, and the result must be a single row with column name `rich_count`.

### Function Contract

**Inputs**

- `Store(bill_id, customer_id, amount)`: a relation of $B$ bills where `bill_id` is unique; each row associates one amount with one customer.
- Let $C$ be the number of distinct customers who have at least one qualifying bill.

**Return value**

- Return one row and one column named `rich_count`, containing $C$.

### Examples

**Example 1**

- Input: `Store = [[6,1,549],[8,1,834],[4,2,394],[11,3,657],[13,3,257]]`
- Output: `[[2]]`
- Explanation: Customers 1 and 3 each have a bill above 500; customer 1 still counts only once despite having two.

**Example 2**

- Input: `Store = [[1,7,500],[2,8,501]]`
- Output: `[[1]]`
- Explanation: The threshold is strict, so only customer 8 qualifies.

**Example 3**

- Input: `Store = [[1,4,100],[2,4,900],[3,5,300]]`
- Output: `[[1]]`
- Explanation: One qualifying bill is enough to make customer 4 rich.
