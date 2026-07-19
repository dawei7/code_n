# Leetflex Banned Accounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1747 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/leetflex-banned-accounts/) |

## Problem Description

### Goal

The `LogInfo` table records account sessions. Each row gives an account identifier, the IP address used, and the session's login and logout timestamps. The combination `(account_id, ip_address, login)` uniquely identifies a row.

An account must be banned when it has two sessions from different IP addresses that overlap in time, meaning the account is simultaneously logged in from both addresses. Return every banned `account_id` once. Sessions from the same address do not create a violation, and nonoverlapping sessions from different addresses are allowed.

### Function Contract

**Inputs**

- `LogInfo(account_id, ip_address, login, logout)`: session rows with a unique `(account_id, ip_address, login)` key.

Let $R$ be the number of session rows and $B$ the number of banned accounts.

**Return value**

- Return a one-column table named `account_id`.
- Include each account exactly once when at least one pair of its sessions uses different IP addresses and has overlapping closed time intervals.

### Examples

**Example 1**

- Input: account `1` has overlapping sessions from `10.0.0.1` and `10.0.0.2`.
- Output: `(1)`
- Explanation: The same account is active from two different addresses at a common time.

**Example 2**

- Input: account `2` uses two different addresses, but its first session ends before the second begins.
- Output: no row for account `2`.
- Explanation: Sequential use of different addresses is not simultaneous access.

**Example 3**

- Input: account `3` has overlapping sessions from the same address.
- Output: no row for account `3`.
- Explanation: A violation requires distinct IP addresses as well as temporal overlap.
