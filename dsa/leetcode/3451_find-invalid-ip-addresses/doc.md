# Find Invalid IP Addresses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3451 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-invalid-ip-addresses/) |

## Problem Description
### Goal
The `logs` table contains server-access records. Each row has a unique `log_id`, an IP-address string `ip`, and an HTTP `status_code`. The same IP string may occur in several log rows.

Classify an IP string as invalid when at least one of the following conditions holds: it contains a dot-separated octet whose numeric value is greater than $255$; an octet of more than one character begins with `0`; or the string contains fewer or more than four dot-separated octets. These are the task's complete invalidity conditions—an empty octet is not rejected by an additional syntax rule. Return one row per invalid IP with the number of log rows containing it. Sort first by that count in descending order and then by `ip` in descending order.

### Function Contract
**Inputs**

- `logs`: A table with columns `log_id` (`int`, unique key), `ip` (`varchar`), and `status_code` (`int`).

Let $r$ be the number of rows, let $S$ be the total number of characters across all `ip` values, and let $k$ be the number of distinct invalid IP strings.

**Return value**

Return columns `ip` and `invalid_count`, with one row for each distinct invalid IP. Order rows by `invalid_count` descending and then `ip` descending.

### Examples
**Example 1**

- Input: `logs = [(1, "192.168.1.1", 200), (2, "256.1.2.3", 404), (3, "192.168.001.1", 200), (4, "192.168.1.1", 200), (5, "192.168.1", 500), (6, "256.1.2.3", 404), (7, "192.168.001.1", 200)]`
- Output: `[("256.1.2.3", 2), ("192.168.001.1", 2), ("192.168.1", 1)]`

**Example 2**

- Input: `logs = [(1, "255.255.255.255", 200), (2, "255.255.255.256", 400)]`
- Output: `[("255.255.255.256", 1)]`

**Example 3**

- Input: `logs = [(1, "127.0.0.1", 200), (2, "192.168..1", 400)]`
- Output: `[]`
