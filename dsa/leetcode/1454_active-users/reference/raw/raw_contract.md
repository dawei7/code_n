## Function Contract

**Inputs**

- `Accounts(id, name)`: account IDs and their associated user names;
- `Logins(id, login_date)`: login events, including possible duplicate events
  for one account on one date.

Let $A$ be the number of rows in `Accounts`, and let $L$ be the number of
distinct `(id, login_date)` pairs in `Logins`.

**Return value**

Return a relation with columns `id` and `name`. Include an account exactly once
when at least five of its distinct login dates form an unbroken sequence of
calendar days. Sort the rows by `id` ascending.
