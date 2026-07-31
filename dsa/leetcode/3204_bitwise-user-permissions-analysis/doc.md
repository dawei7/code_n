# Bitwise User Permissions Analysis

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3204 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-user-permissions-analysis/) |

## Problem Description

### Goal

The `user_permissions` table stores one integer permission mask for each user. Every bit position represents a distinct access level or feature: a set bit means that the user possesses the corresponding permission.

Produce one result row with two combined masks. `common_perms` must contain exactly the bits set for every user, so it is the bitwise AND of all values in `permissions`. `any_perms` must contain every bit set for at least one user, so it is the bitwise OR of those values.

The result may be returned in any order.

### Function Contract

**Inputs**

The `user_permissions` table contains:

- `user_id`: An integer that uniquely identifies a row.
- `permissions`: The user's permissions encoded as an integer bit mask.

Let $r$ be the number of rows in `user_permissions`.

**Return value**

- A one-row table with integer columns `common_perms` and `any_perms`.

### Examples

**Example 1**

Input table `user_permissions`:

| user_id | permissions |
|---:|---:|
| 1 | 5 |
| 2 | 12 |
| 3 | 7 |
| 4 | 3 |

Output:

| common_perms | any_perms |
|---:|---:|
| 0 | 15 |

The AND of the four masks is `5 & 12 & 7 & 3 = 0`, while their OR is `5 | 12 | 7 | 3 = 15`.
