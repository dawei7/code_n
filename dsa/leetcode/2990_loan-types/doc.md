# Loan Types

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2990 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/loan-types/) |

## Problem Description
### Goal
The `Loans` table contains uniquely identified loans, the user who holds each
loan, and its `loan_type`.

Return every distinct `user_id` having at least one loan whose type is exactly
`"Mortgage"` and at least one whose type is exactly `"Refinance"`. Extra loan
types and repeated loans of either required type do not alter this condition.
Sort qualifying user IDs in ascending order.

### Function Contract
**Inputs**

- `Loans(loan_id, user_id, loan_type)`: uniquely identified user loans

Let $R$ be the number of loan rows.

**Return value**

Return distinct qualifying user IDs ordered ascending.

### Examples
**Example 1**

- Input: User `102` has both target types; the other users have only one.
- Output: `[(102)]`

**Example 2**

- Input: A user has several Mortgage loans but no Refinance loan.
- Output: No row for that user.

**Example 3**

- Input: Several users each have both types.
- Output: Every such user once, in ascending order.
