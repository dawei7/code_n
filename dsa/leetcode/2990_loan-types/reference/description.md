## Description

The `Loans` table contains uniquely identified loans, the user who holds each
loan, and its `loan_type`.

Return every distinct `user_id` having at least one loan whose type is exactly
`"Mortgage"` and at least one whose type is exactly `"Refinance"`. Extra loan
types and repeated loans of either required type do not alter this condition.
Sort qualifying user IDs in ascending order.
