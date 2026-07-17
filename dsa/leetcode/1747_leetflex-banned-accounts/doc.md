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

### Required Complexity

- **Time:** $O(R^2)$
- **Space:** $O(B)$

<details>
<summary>Approach</summary>

#### General

**Give the session table two roles**

Self-join `LogInfo` so one alias represents the first session and the other represents a possible conflicting session. Match only rows with equal `account_id` and unequal `ip_address`.

**Use the complete interval-overlap condition**

Two closed intervals `[login1, logout1]` and `[login2, logout2]` overlap exactly when neither finishes before the other begins:

$$
\texttt{login1} \le \texttt{logout2}
\quad\land\quad
\texttt{login2} \le \texttt{logout1}.
$$

This covers partial overlap, containment, equal starts, and a shared endpoint. Requiring both inequalities avoids treating separated sessions as simultaneous.

**Collapse multiple conflicts to one account**

An account may have several conflicting session pairs, and the symmetric join can see each pair in both directions. Select `DISTINCT account_id` and order it for deterministic local output; only membership is semantically required.

#### Complexity detail

Without a specialized interval index, the self-join can compare $O(R^2)$ session pairs in the worst case. Deduplication stores at most one state for each of the $B$ banned accounts, using $O(B)$ result or hash space. Database indexes on `account_id` can reduce comparisons between unrelated accounts but do not change the all-one-account worst case.

#### Alternatives and edge cases

- **Correlated existence check:** `EXISTS` can stop after one conflict per account, but still has a quadratic worst case without suitable indexing.
- **Application-side sweep line:** Sorting events by account and time can detect active distinct IPs in $O(R\log R)$ time, but moves the task outside the required SQL query and needs careful endpoint ordering.
- **Same IP address:** Overlap alone is insufficient; the two addresses must differ.
- **Different accounts:** Their sessions never conflict with each other.
- **Contained interval:** A session fully inside another is an overlap.
- **Shared endpoint:** Closed session intervals that meet at one timestamp count as simultaneous.
- **Several violations:** Return the account only once.
- **Sequential reuse:** A later session beginning after the earlier logout is allowed.

</details>
