## General

**Turn undirected friendships into directed adjacency rows.** Each `Friends` row stores a pair once, but either user must be searchable as the starting user. CTE `T` contains the original orientation and the reversed orientation through `UNION ALL`:

`(user_id1,user_id2)` and `(user_id2,user_id1)`.

Thus every row in `T` can be read as “the first user has the second user as a neighbor.”

`UNION ALL` is appropriate because the two directions are semantically distinct adjacency entries. It avoids the duplicate-elimination work of `UNION`.

**Generate user pairs that share a neighbor.** Aliases `t1` and `t2` join on

`t1.user_id2 = t2.user_id2`.

Their second columns are the same neighbor $z$. The selected first columns are two users $u$ and $v$ that both connect to $z$. The subquery therefore produces every ordered pair $(u,v)$ having at least one mutual friend.

It also produces self-pairs $(u,u)$ when an adjacency row joins with itself, but those do not match ordinary friendship rows between two different users and cause no harm.

**Exclude original friendships found in that set.** The outer query begins from `Friends`, so it considers only pairs who are actually friends. Tuple predicate

`(user_id1, user_id2) NOT IN (subquery)`

keeps a friendship only when its ordered pair never appeared among users sharing a neighbor.

Because `T` contains both directions, a mutual friend generates both $(u,v)$ and $(v,u)$. The stored orientation of the original row is therefore covered regardless of which user has the smaller identifier.

**Why direct friendship is not mistaken for a mutual friend.** For users $u$ and $v$ connected directly, directed rows are $(u,v)$ and $(v,u)$. Their neighbor columns are $v$ and $u$, which differ when users are distinct. They do not join merely because they are friends with each other. A third user $z$ is needed to produce outgoing rows $(u,z)$ and $(v,z)$ with equal second columns.

**A small trace.** If friendships include $(1,2)$, $(1,5)$, and $(2,5)$, CTE `T` contains $(1,5)$ and $(2,5)$. Their join produces pair $(1,2)$, causing the original friendship to be excluded.

For isolated friendship $(6,7)$ with no third adjacent user, no common-neighbor join produces $(6,7)$, so it remains.
If the query excludes a friendship, the subquery contains its endpoint pair, which means two directed adjacency rows share some neighbor; that neighbor is a mutual friend. If a friendship has a mutual friend, those two adjacency rows exist in `T` and join, so the pair enters the subquery and is excluded. Therefore retained pairs are exactly friendships with no mutual friend.

**Null sensitivity.** Tuple `NOT IN` can behave unexpectedly when its subquery contains nulls because SQL uses three-valued logic. Here both columns come from primary-key friendship identifiers, which are non-null under MySQL primary-key rules, so the issue does not arise under the schema.

**Required ordering.** `ORDER BY 1, 2` sorts the retained stored pairs by `user_id1` and then `user_id2` ascending.

## Complexity detail

Let $M$ be the number of friendship rows and $d_z$ the degree of user $z$. CTE `T` has $2M$ rows. The common-neighbor self-join emits

$$
\sum_z d_z^2
$$

ordered endpoint pairs in the worst case, which can be $O(Md)$ using maximum degree $d$ and quadratic for a star-like dense neighborhood output.

Final anti-membership and sorting of retained friendships add database-dependent lookup and $O(M\log M)$ ordering work. Materializing directed edges costs $O(M)$ space; the join result may be much larger unless optimized as an anti-join.

## Alternatives and edge cases

- **`NOT EXISTS` correlated anti-join:** It avoids tuple `NOT IN` null semantics and can stop at the first mutual friend, often giving the optimizer a clearer anti-join.
- **Store normalized undirected edges:** Normalization helps uniqueness but still requires checking adjacency from both endpoints; the bidirectional CTE makes that explicit.
- **One mutual friend:** A single shared neighbor is enough to exclude the friendship.
- **Several mutual friends:** The subquery may emit the endpoint pair repeatedly, but membership remains true and the outer friendship is excluded once.
- **No mutual friend:** The pair never appears in the subquery and survives.
- **Direct friendship only:** The endpoints are not treated as their own mutual neighbor.
- **Self-pairs in subquery:** They are harmless because valid friendships connect two users.
- **Duplicate friendship rows:** The composite primary key prevents them.
- **NULL identifiers:** Primary-key non-null guarantees are important for `NOT IN` correctness.
- **Output orientation:** The query preserves the orientation stored in `Friends` and sorts those columns as requested.
- **Why `UNION ALL` does not create false mutual friends:** The two orientations represent genuine adjacency. A common-neighbor match still requires identical neighbor identifiers, so merely duplicating direction does not invent a third connection.
- **High-degree user:** A popular mutual friend creates many endpoint combinations in the self-join, explaining why runtime depends on degree distribution rather than only the number of original friendship rows.
