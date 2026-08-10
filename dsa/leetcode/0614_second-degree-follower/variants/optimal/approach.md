## General

**Read each relationship in the correct direction.** A row `(followee, follower)` means that the user in `follower` follows the user in `followee`. A second-degree user must play both roles somewhere in the table: the user follows at least one other person, and at least one person follows that user. The query finds such users by joining two copies of `Follow`.

Call the two aliases `f1` and `f2`. In an `f1` row, `f1.follower` is a person who follows somebody. In an `f2` row, `f2.followee` is a person who is followed by somebody. The condition

`f1.follower = f2.followee`

therefore matches exactly when the same user satisfies both halves of the definition. The shared value is the second-degree user.

**What one joined row means.** The CTE names the shared user `follower`:

`f1.follower AS follower`

It also selects `f2.follower AS followee`. That second alias is slightly misleading: `f2.follower` is actually one of the people who directly follows the shared user. A clearer temporary name might have been `direct_follower`, but the final logic is still correct. Each CTE row can be read as:

> the user in the first output column follows somebody, and the user in the second output column follows that first user.

Suppose the table contains `Alice <- Bob`, `Bob <- Cena`, and `Bob <- Donald`, where each arrow points from follower to followee. The `f1` row saying Bob follows Alice can join both `f2` rows in which Bob is the followee. The CTE consequently contains `(Bob, Cena)` and `(Bob, Donald)`.

**Why the CTE automatically filters the users.** A person who follows nobody never appears in `f1.follower`, so that person cannot enter the join. A person with no followers never appears in `f2.followee`, so that person also cannot enter the join. There is no separate `WHERE` clause because an inner join already requires evidence for both roles.

The query then groups by the shared user and computes `COUNT(DISTINCT followee)`. Despite the temporary name, this counts distinct direct followers of that user. The primary key `(followee, follower)` already prevents duplicate copies of one relationship, so `COUNT(*)` would count the same thing only if the join did not repeat those relationships. `DISTINCT` ensures that one follower name contributes only once after the join.

**Why every reported count is correct.** Consider a user `u` that appears in the final result. The CTE has at least one row for `u`, which could only be created from an `f1` row where `u` is a follower and an `f2` row where `u` is a followee. Thus `u` follows someone and is followed by someone, so `u` is genuinely second degree. Every distinct `f2.follower` joined to `u` is a direct follower of `u`, and the count includes it once.

Conversely, suppose `u` is a second-degree user. Because `u` follows at least one person, there is at least one `f1` row with `f1.follower = u`. Because someone follows `u`, there is at least one `f2` row with `f2.followee = u`. Those rows satisfy the join condition, so `u` enters the CTE. In fact, every direct follower of `u` has an `f2` row that joins with the `f1` evidence. Grouping collects those rows, and the distinct count is exactly the number of direct followers.

**Why multiple outgoing relationships do not inflate the answer.** If a second-degree user follows several people, there are several qualifying `f1` rows. Each one joins every incoming `f2` row, creating repeated copies of the same direct follower in the CTE. This is why `COUNT(DISTINCT ...)` is important for this exact join shape. For example, if `u` follows three users and has two followers, the join produces six rows, but the distinct count correctly returns two.

Finally, `ORDER BY 1` orders by the first selected expression, `follower`. This satisfies the required alphabetical ordering. An explicit `ORDER BY follower` would be easier to maintain, but the ordinal is valid for this two-column projection.

## Complexity detail

Let $R$ be the number of rows in `Follow`. The two aliases each refer to the same $R$-row relation. With an index, hash table, or sort on the join key, finding matching users is commonly bounded by $O(R\log R)$ for a sort-based plan or expected $O(R)$ for a hash-based plan. Grouping, distinct counting, and the final ordering can each require sorting or hashing. The manifest therefore gives the conservative time bound $O(R\log R)$ and auxiliary space bound $O(R)$.

There is a crucial output-multiplicity detail. If a user follows many people and also has many followers, the raw join emits the product of those two counts. Summed across users, that intermediate result can be $O(R^2)$ in a highly concentrated worst case. Thus the literal join's logical worst-case work can be quadratic even though indexed database plans and typical data may behave much better. A semijoin-style eligibility test followed by a separate follower count can avoid that multiplication.

The CTE may be materialized or inlined depending on the database optimizer. If materialized, it needs space proportional to its joined row count. If inlined, the engine may pipeline rows into the grouping operation. The manifest's $O(R)$ space describes ordinary indexed, hashed, or sorted processing, but it is not a promise that every physical plan materializes no larger intermediate.

## Alternatives and edge cases

- **Count incoming relationships, then filter with `EXISTS`:** Group rows by `followee` to count each user's followers, and retain a group only when an `EXISTS` subquery finds that user in the `follower` column. This directly separates counting from eligibility and avoids multiplying incoming and outgoing degrees.
- **Intersection of role sets:** Build the set of users appearing as `follower`, intersect it with users appearing as `followee`, and join that set to incoming counts. This mirrors the definition very clearly but may require more CTEs.
- **`COUNT(*)` instead of `COUNT(DISTINCT ...)`:** It is unsafe with the current two-way join because every outgoing relationship repeats all incoming relationships. It becomes safe only after the eligibility check is restructured so each incoming row appears once.
- **User follows many accounts:** The distinct count prevents those outgoing rows from inflating the number of people who follow the user.
- **User is followed by many accounts:** Every distinct incoming follower is preserved and counted exactly once.
- **User only follows others:** Such a user has no matching `f2.followee` row and is excluded.
- **User is only followed by others:** Such a user has no matching `f1.follower` row and is excluded.
- **Self-follow relationships:** The schema promises that none exist. If they did, one self-edge alone would satisfy both roles, which may or may not match the intended social definition.
- **Duplicate relationships:** The composite primary key excludes them. `DISTINCT` nevertheless protects the count from duplicates created by the join's multiple outgoing matches.
- **Alias naming:** The CTE column named `followee` actually stores a direct follower. Reading it by its source expression, `f2.follower`, prevents a direction mistake during review.
