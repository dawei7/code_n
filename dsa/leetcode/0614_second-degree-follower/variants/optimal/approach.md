## General
**Identify users who follow someone**

The `follower` column names users who follow at least one account. Select its distinct values into an `active_followers` relation so each eligible user appears only once, even if that user follows several accounts.

**Count who follows each eligible user**

Join `Follow` to `active_followers` where `Follow.followee` equals the eligible user. Every joined relationship is one direct follower of that user. Group by `followee` and count the rows.

**Why this is exactly the second degree**

A grouped user necessarily appears as a followee, so at least one person follows them, and the join proves that the same user appears as a follower elsewhere. Conversely, any user with both roles appears once in `active_followers` and all rows naming that user as `followee` join to it. The count therefore includes every direct follower exactly once without multiplication from the accounts the user follows.

## Complexity detail
For `R` relationships, distinct extraction, joining, grouping, and ordering take $O(R \log R)$ time in the general comparison-based database model and $O(R)$ execution space. Hash aggregation and suitable indexes can make the main passes near-linear.

## Alternatives and edge cases
- **Grouped `IN` subquery:** group by `followee` and retain groups whose user occurs in `SELECT follower FROM Follow`; engines commonly materialize the subquery once, making this concise and efficient.
- **Direct self-join:** join `Follow.followee` to another row's `follower`; a user who follows several accounts multiplies direct-follower rows, so the count must use `DISTINCT` or a deduplicated role relation.
- **Correlated membership count:** rescanning all relationships for every row is correct but can take $O(R^2)$ time.
- A user who only follows others is not returned because nobody follows them.
- A user who is only followed is not returned because they follow nobody.
- Cycles are valid and can make every participant a second-degree follower.
- Following several users must not multiply the reported number of direct followers.
