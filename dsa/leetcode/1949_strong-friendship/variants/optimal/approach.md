## General

**Make the undirected graph explicit**

Each `Friendship` row stores one undirected edge only in the canonical order `user1_id < user2_id`. To find neighbors uniformly from either endpoint, CTE `t` creates two directed rows per friendship: the original direction and the reversed direction through `UNION ALL`.

Because the primary key prevents duplicate original edges and the endpoints have strict order, these directed rows are distinct. In `t`, a row `(x, y)` can be read as “$y$ is a friend of $x$.”

**Start from an existing friendship**

Alias `t1` is the friendship being evaluated. This matters because the output asks which existing friendships are strong, not every arbitrary user pair with common neighbors.

Although `t` contains both orientations, the predicate `t1.user1_id < t1.user2_id` retains only the canonical orientation. The result therefore cannot contain both $(x,y)$ and $(y,x)$.

**Join both endpoints to the same neighbor**

`t2` is joined with `t1.user2_id = t2.user1_id`. For candidate pair $(x,y)$, each matching `t2` row exposes one friend `t2.user2_id` of $y$.

`t3` is joined with `t1.user1_id = t3.user1_id`, exposing friends `t3.user2_id` of $x$.

The WHERE equality `t3.user2_id = t2.user2_id` requires those exposed neighbor IDs to be the same. Each surviving joined row therefore represents one user $z$ who is a friend of both $x$ and $y$.

Grouping by the candidate endpoints and computing `COUNT(1)` gives the number of common friends. `HAVING COUNT(1) >= 3` retains exactly strong friendships and exposes the count under alias `common_friend`.

**Why common friends are counted once**

For a fixed user, `t` has at most one outgoing row to a particular neighbor because `Friendship` has a unique edge per unordered pair. Therefore a common friend $z$ supplies exactly one matching `t2` row and one matching `t3` row, producing exactly one joined combination for candidate $(x,y)$. No `DISTINCT` is needed inside the count.

The endpoints themselves do not become false common friends. There are no self-friendship rows, so $x$ is not listed as its own neighbor and neither is $y$.

**Why the query is correct**

Every returned group begins with a real friendship from `t1` in canonical order. Each counted row identifies a distinct common neighbor, and the HAVING threshold proves there are at least three, so every returned friendship is strong.

Conversely, take any strong friendship $(x,y)$ with $x<y$. The original directed row appears in `t1`. For every common friend $z$, the symmetrized CTE contains $y\to z$ and $x\to z$, so the joins generate one row. At least three such rows make the group pass HAVING. Thus every strong friendship is returned.

No ordering clause appears because any result order is allowed.

**Follow one witness row concretely**

For candidate friendship $(1,2)$ and common friend $6$, `t1` supplies directed edge `(1,2)`. The first join finds `t2 = (2,6)`, while the second finds `t3 = (1,6)`. Their neighbor fields both equal six, so one row survives. A user who is connected to only endpoint one can supply `t3` but no matching `t2` and contributes nothing. This row-level view explains why the count is intersection size rather than the sum or union of neighbor lists.

The candidate edge itself does not generate a witness with neighbor one or two. Producing neighbor one from endpoint one would require self-edge `(1,1)`, and producing neighbor two from endpoint two would require `(2,2)`. Neither exists in the friendship model. The direct friendship establishes eligibility through `t1` but is not counted as a common friend.

## Complexity detail

Let $E$ be the number of original friendships and let $W$ be the number of joined common-neighbor witness rows generated before grouping.

Building the conceptual directed CTE has $2E$ rows and costs $O(E)$. With suitable indexes or hash structures, producing witness rows is proportional to the join output, and grouping may require $O(W\log W)$ time or expected $O(W)$ hashing. The manifest summarizes time as $O(E+W\log W)$ and space as $O(E+W)$.

As with all declarative SQL, the actual plan is optimizer-dependent. High-degree users can make $W$ much larger than $E$ because one common-neighbor relationship participates in many candidate pairs.

## Alternatives and edge cases

- **Normalize with a separate adjacency table:** Materialize both directions once and index by user. This can simplify repeated graph queries but is unnecessary for a single statement.
- **Correlated common-neighbor count:** Count intersection per friendship with subqueries. It is readable but may repeat neighbor scans.
- **Omit symmetrization:** Then friendships stored with a user in the second column would be missed when looking up that user's neighbors.
- **Use `UNION` instead of `UNION ALL`:** Duplicate elimination is unnecessary because the schema and endpoint order already make the two directed sets disjoint.
- **Exactly three common friends:** The inclusive `>= 3` threshold accepts the friendship.
- **Two common friends:** The group exists but fails HAVING.
- **No common friend:** No witness row reaches grouping, so the friendship is absent.
- **High-degree users:** They can create many join combinations; join-output size is the important workload measure.
- **Canonical endpoint order:** The final inequality removes the reversed copy and satisfies `user1_id < user2_id`.
- **Only actual friendships:** Driving the query from `t1` prevents reporting nonfriends who happen to share neighbors.
- **Candidate endpoints:** Neither endpoint is counted as a common friend because the directed adjacency CTE contains no self-edges.
- **Any output order:** No `ORDER BY` is required.
