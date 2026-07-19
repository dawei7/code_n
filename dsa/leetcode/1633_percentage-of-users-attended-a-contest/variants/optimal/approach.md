## General
**Compute the denominator from all users.** The percentage denominator is the total row count of `Users`, not the number of users who appear in `Register`. A scalar subquery supplies that same total to every contest group, so users with no registrations still affect every percentage.

**Aggregate one numerator per contest.** Group `Register` by `contest_id`. Because `(contest_id, user_id)` is unique, `COUNT(*)` is exactly the number of distinct users registered for that contest; no additional `DISTINCT` is needed. Multiply by `100.0` before division to preserve a fractional result, then round to two decimal places.

**Apply the complete requested ordering.** Sort the computed percentage descending. Add `contest_id ASC` as the second key so ties are deterministic and match the contract.

Each registration contributes once to exactly one contest numerator, while the scalar count supplies the complete common denominator. Thus every computed ratio is the requested attendance share. Grouping emits exactly one row per registered contest, and the two ordering keys establish the mandated sequence.

## Complexity detail
Counting $u$ users and scanning $r$ registrations for hash aggregation take $O(u+r)$ time. Sorting the $c$ contest groups takes $O(c\log c)$ time, for $O(u+r+c\log c)$ overall. The aggregation state and output-ordering workspace use $O(c)$ space, apart from database-engine storage and the returned rows.

## Alternatives and edge cases
- **Join before counting:** Cross joining every registration with `Users` can reproduce the denominator but creates unnecessary intermediate rows and risks an incorrect numerator.
- **`COUNT(DISTINCT user_id)`:** This is correct but redundant under the composite primary-key guarantee and may require extra deduplication work.
- **Integer division:** Dividing integer counts before multiplying discards the fractional share; force decimal arithmetic first.
- Users absent from `Register` still belong in the denominator.
- A user registered in several contests contributes once to each corresponding group.
- Contest rows tied after two-decimal rounding are ordered by `contest_id`, not by their unrounded ratios.
- Only contests represented in `Register` appear in the result.
