## Function Contract

**Inputs**

`Spending(user_id, spend_date, platform, amount)` contains $R$ purchase rows at the unique user-date-platform grain. The only platform values are `desktop` and `mobile`.

**Return value**

- Return exactly `spend_date`, `platform`, `total_amount`, and `total_users`.
- For every represented date, return one row for each of `desktop`, `mobile`, and `both`.
- Classify a user separately on each date. A user with both platform rows contributes the sum of both amounts and one user to `both`, not to either single-platform category.
- Use `0` for both measures when a date-category pair has no users.
- Result row order is unrestricted.
