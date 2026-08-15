# Find Circular Gift Exchange Chains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3401 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-circular-gift-exchange-chains/) |

## Problem Description

### Goal

The `SecretSanta` table records directed gift exchanges between employees. Each row identifies the employee giving the gift, the employee receiving it, and the gift's value. A circular chain is a continuous loop in which every participating employee gives to exactly one other employee and receives from exactly one other employee.

Find each distinct chain statistic: the number of exchanges in the loop and the sum of their gift values. Assign `chain_id` values after sorting first by chain length and then by total gift value, both in descending order. The verified platform result represents equal `(chain_length, total_gift_value)` pairs once, even if separate employee loops share those same two statistics.

### Function Contract

**Inputs**

- `SecretSanta(giver_id, receiver_id, gift_value)`: One row per gift exchange. The pair `(giver_id, receiver_id)` is unique; `giver_id` identifies the giver, `receiver_id` identifies the recipient, and `gift_value` is the value transferred.

Let $e$ be the number of exchange rows. The valid input forms disjoint circular chains: each participating employee has one outgoing exchange and one incoming exchange.

**Return value**

- A table with columns `chain_id`, `chain_length`, and `total_gift_value`.
- Rows are ordered by `chain_length` descending and then `total_gift_value` descending. `chain_id` is the resulting one-based row number.

### Examples

#### Example 1

`SecretSanta`

| giver_id | receiver_id | gift_value |
|---:|---:|---:|
| 1 | 2 | 20 |
| 2 | 3 | 30 |
| 3 | 1 | 40 |
| 4 | 5 | 25 |
| 5 | 4 | 35 |

Output

| chain_id | chain_length | total_gift_value |
|---:|---:|---:|
| 1 | 3 | 90 |
| 2 | 2 | 60 |

Employees 1, 2, and 3 form a three-exchange loop worth 90 in total. Employees 4 and 5 form a two-exchange loop worth 60.
