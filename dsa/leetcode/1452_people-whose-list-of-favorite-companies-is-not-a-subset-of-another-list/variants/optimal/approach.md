## General
**Represent each list by membership, not order**

Convert every favorite-company list to a hash set. A set captures the exact
meaning of the input: company presence matters, but list position does not.
It also supports expected constant-time membership and a direct subset test,
instead of repeatedly scanning strings in an ordinary list.

**Compare each person with every possible containing list**

Process people in increasing index order. For person $i$, inspect every other
set. A strictly smaller set cannot contain the current set and may be skipped.
Because the contract guarantees all lists are distinct, an equal-cardinality
set cannot be a subset either: two finite sets of equal size can have a subset
relationship only when they are equal. It is therefore enough to test
`current.issubset(candidate)` only when the candidate is larger.

If any such test succeeds, person $i$ is excluded and no more comparisons are
needed for that person. If none succeeds, append $i$ to the answer. Appending
during the left-to-right scan automatically produces increasing indices.

**Why every returned index and every exclusion is correct**

An index is excluded only after a set operation proves that all of its
companies occur in another person's larger set, which is exactly the
disqualifying condition. Conversely, the algorithm considers every other set
that could possibly contain the current one. Smaller and equal-sized distinct
sets are mathematically incapable of containing it; every larger set receives
an explicit subset test. If all those tests fail, no other person's list is a
superset, so the index must qualify.

Thus each omitted index has a valid containing witness and each returned index
has none. The scan order establishes the required output order without a
separate sort.

## Complexity detail
Constructing the $P$ sets stores and reads at most $PC$ company entries. There
are at most $P(P-1)$ ordered person comparisons, and a hash-set subset test
examines at most $C$ elements, giving $O(P^2C)$ expected time. Early exits and
size filters improve many inputs but do not change the worst-case bound.

The sets retain $O(PC)$ company references. The output contains at most $P$
indices and is covered by that bound; the comparison loop uses constant
additional scalar state.

## Alternatives and edge cases
- **List membership checks:** For each candidate pair, test every company with
  `company in other_list`. Each membership scan can cost $O(C)$, producing
  $O(P^2C^2)$ worst-case time.
- **Sort each company list and use two pointers:** A linear merge can test one
  subset relation after preprocessing. It avoids hash assumptions but requires
  sorting and more comparison code.
- **Global company bitsets:** Map names to bit positions and use bitwise subset
  tests. This can be fast when the vocabulary is compact, but Python integers
  or explicit bitsets require extra indexing machinery.
- **One person:** With no other list available, index `0` always qualifies.
- **Disjoint lists:** Every index qualifies because each list contains a
  company absent from every other candidate.
- **Transitive containment:** A list contained in any other list is excluded;
  it does not matter whether that larger list is itself contained elsewhere.
- **Equal cardinality:** Distinct equal-sized sets cannot contain one another,
  though their company order may differ.
- **Input order inside a list:** Reordering companies does not alter subset
  relationships.
- **Result order:** Append indices during the increasing scan rather than
  returning them in set-size order.
