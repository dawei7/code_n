## General
**Represent indirect friendship by components**

Maintain a disjoint-set union structure over the people. Its root for a person identifies that person's entire current friendship component. Path compression and union by size keep root queries amortized almost constant, and only accepted requests modify this structure.

**Test the only newly possible violation**

For a request `[u, v]`, first find component roots `u_root` and `v_root`. If they are equal, the request creates no new connectivity and is successful immediately. Otherwise, a hypothetical acceptance would merge exactly those two components. An existing restriction `[x, y]` becomes violated by that merge precisely when the current roots of `x` and `y` are `u_root` and `v_root` in either order.

Scan all restrictions for that cross-component pattern. If one appears, reject the request and leave the disjoint-set state untouched. If none appears, union the two request components and record success. The state was valid before the request, and no component other than these two changes, so this test excludes every and only possible new violation. Processing in input order therefore preserves all restrictions after every accepted request.

**Keep rejected requests nonpersistent**

The restriction scan reads the current roots but performs no speculative union. Consequently, rejection needs no rollback: only the final accepted branch changes a parent pointer. This also ensures that an unsuccessful request cannot influence a later answer.

## Complexity detail
Initialization costs $O(n)$. Each of the $Q$ requests performs constant-many disjoint-set operations and, unless its endpoints are already connected, scans up to $R$ restrictions with two finds per pair. The tight total bound is $O(n+Q(R+1)\alpha(n))$, which is $O(S^2\alpha(S))$ for $S=\max(n,R,Q)$. Parent and size arrays use $O(n)$ space, and the required result uses $O(Q)$.

## Alternatives and edge cases
- **Copy the disjoint set for each request:** Speculatively unioning on a full copy and then checking all restrictions is correct, but copying $O(n)$ state per request adds avoidable work and storage churn.
- **Rebuild connectivity for every restriction:** Replaying all accepted edges separately for each restriction can reach cubic time when requests and restrictions both scale.
- **Already connected endpoints:** The request is successful because it creates no new path, even if the same direct request appeared earlier.
- **Rejected request:** It adds no friendship and must not alter the outcome of future requests.
- **No restrictions:** Every request succeeds, including repetitions and requests within an existing component.
- **Restriction orientation:** `[x, y]` is symmetric, so both root orderings must be checked.
