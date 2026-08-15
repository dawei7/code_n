# Drop Duplicate Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2882 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/drop-duplicate-rows/) |

## Problem Description

### Goal

A customer DataFrame contains the columns `customer_id`, `name`, and `email`. Some rows may use an email address that already appeared in an earlier row, so those rows are duplicates with respect to `email` even when their identifiers or names differ.

Remove every later occurrence of an email address and retain only the first row carrying that email. Return all three original columns, preserve the order of the retained customers, and do not treat matching names or other fields as duplicates when their email addresses differ.

### Function Contract

**Inputs**

- `customers`: A pandas DataFrame with integer column `customer_id` and object columns `name` and `email`.

Let $n$ be the number of customer rows.

**Return value**

Return a DataFrame containing the first row for each distinct `email`, with columns `customer_id`, `name`, and `email` in their original order.

### Examples

#### Example 1

- **Input:** `customers = [{"customer_id": 1, "name": "Ella", "email": "emily@example.com"}, {"customer_id": 2, "name": "David", "email": "michael@example.com"}, {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"}, {"customer_id": 4, "name": "Alice", "email": "john@example.com"}, {"customer_id": 5, "name": "Finn", "email": "john@example.com"}, {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}]`
- **Output:** `[{"customer_id": 1, "name": "Ella", "email": "emily@example.com"}, {"customer_id": 2, "name": "David", "email": "michael@example.com"}, {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"}, {"customer_id": 4, "name": "Alice", "email": "john@example.com"}, {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}]`

#### Example 2

- **Input:** `customers = [{"customer_id": 10, "name": "Mia", "email": "mia@example.com"}, {"customer_id": 11, "name": "Noah", "email": "noah@example.com"}]`
- **Output:** `[{"customer_id": 10, "name": "Mia", "email": "mia@example.com"}, {"customer_id": 11, "name": "Noah", "email": "noah@example.com"}]`

#### Example 3

- **Input:** `customers = [{"customer_id": 20, "name": "Ada", "email": "team@example.com"}, {"customer_id": 21, "name": "Bo", "email": "team@example.com"}, {"customer_id": 22, "name": "Cy", "email": "team@example.com"}]`
- **Output:** `[{"customer_id": 20, "name": "Ada", "email": "team@example.com"}]`
