## General

**Represent the undirected relation explicitly.** Each stored friendship has
two usable directions. Build an adjacency CTE containing `(user_id1,
user_id2)` and its reversal, naming the columns `user_id` and `friend_id`.
This makes neighbor lookup uniform even when a user appears in different
source columns across rows.

**Materialize the pairs that share a neighbor.** Self-join the adjacency CTE on
`friend_id`. Two different `user_id` values in a joined row are connected to
the same third user, so normalize their order and deduplicate them into a set
of mutual-friend pairs. Join each original friendship to that set by its
normalized endpoints and retain only rows for which the join finds no match.

Project the original pair rather than the expanded adjacency rows, then apply
the required two-column ordering. The bidirectional expansion includes every
neighbor, so absence from the materialized pair set is equivalent to having no
mutual friend.

## Complexity detail

Let $m$ be the number of friendships and $d$ the maximum user degree. The
adjacency CTE has $2m$ rows. With indexed or hash-assisted neighbor lookup,
testing all original pairs takes $O(md)$ work in the worst case; ordering up
to $m$ retained pairs adds $O(m\log m)$. The expanded adjacency and working
indexes use $O(m)$ space. Actual database plans may choose different join
strategies, so package benchmarks measure the scaling of the authored query.

## Alternatives and edge cases

- **Assume one endpoint column identifies the user:** This misses friendships when the same user appears in the opposite column of another row.
- **Count two-hop paths with an inner join:** This finds pairs that do have mutual friends; an anti-existence condition is needed for the requested complement.
- **Repeated orientation-specific joins:** Enumerating all four endpoint-column combinations is correct but longer and easier to make incomplete than normalizing adjacency once.
- A single isolated edge qualifies because neither endpoint has another neighbor.
- Every edge in a triangle is excluded by the third vertex.
- A path or four-cycle can contain several edges while still giving adjacent endpoints no common neighbor.
- Return the stored orientation and sort by `user_id1`, then `user_id2`; do not emit reversed duplicates.
