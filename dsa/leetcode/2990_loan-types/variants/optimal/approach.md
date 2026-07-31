## General

**Reduce each user to target-category presence.** Group rows by `user_id`.
Inside each group, retain only the two required loan type names through a
conditional expression and count their distinct values. A count of two means
both `Mortgage` and `Refinance` occur at least once; duplicates cannot inflate
the result beyond two and unrelated types become null and are ignored.

Filter to groups with count two, then order their user IDs ascending. Every
surviving group contains both required types, and any user containing both
contributes the two distinct names, so the condition is necessary and
sufficient.

## Complexity detail

Let $R$ be the number of loan rows. Grouping and ordered output take
$O(R\log R)$ time in the general comparison-based model, with up to $O(R)$
grouping state.

## Alternatives and edge cases

- **Conditional Boolean aggregates:** Requiring both `MAX(loan_type = ...)` flags is equivalent.
- **Target-type self-join:** Joining Mortgage rows to Refinance rows by user is correct but duplicate-heavy users can create quadratic intermediate results.
- **Duplicate loan types:** Multiple Mortgage rows still establish only one required category.
- **Unrelated types:** AutoLoan, Inschool, and other names neither help nor disqualify a user.
- **Only one target type:** At least one occurrence of each is mandatory.
- **Distinct output:** Grouping produces each qualifying user exactly once before ascending sorting.
