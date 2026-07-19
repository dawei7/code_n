## General
**Treat emails as identity vertices**

Create one disjoint-set element for every distinct email. Names are output labels, not evidence of identity: two records with the same name remain separate unless their email components connect.

**Union each account around one representative email**

Within a record, union every email with its first email. This connects the entire record with only a linear number of union operations. Path compression and union by size keep later representative searches nearly constant time.

**Collect emails by final representative**

After all unions, find the representative of every email and append that email to its component. Sort each component's emails, prepend the associated name, and emit the merged record. The outer list needs no semantic order, though the local implementation sorts it for deterministic display.

**Why shared-email chains merge correctly**

Every union joins emails known to belong to one account. If two accounts share an email, their union operations touch the same disjoint-set element and combine their components; repeating this argument joins any transitive chain. Conversely, disjoint-set components can merge only through an account containing emails from both sides, so unrelated records are never combined.

## Complexity detail
Let `E` count all email occurrences and `U` the distinct emails. Disjoint-set work takes $O(E \alpha(U))$ time. Sorting the component email lists costs at most $O(U \log U)$, which gives the stated $O(E \log E)$ bound. Parent, size, name, and grouped-email maps use $O(E)$ space.

## Alternatives and edge cases
- **Email graph plus DFS or BFS:** connect every account's first email to its others and traverse connected components; it has comparable asymptotic cost.
- **Pairwise account intersection:** compare every pair of email sets before traversing account components; it is correct but can take $O(A^2)$ set comparisons.
- **Repeated set merging:** continually search for overlapping groups and combine them; careless rescanning can also become quadratic.
- Identical names do not merge records without a shared email.
- One shared email can connect records transitively even when the endpoint records share no email directly.
- Duplicate occurrences of an email must appear only once in the merged output.
- Emails inside every output record are sorted, while the order of the records is unrestricted.
