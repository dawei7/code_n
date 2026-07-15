# People Whose List of Favorite Companies Is Not a Subset of Another List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1452 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) |

## Problem Description
### Goal

`favoriteCompanies[i]` lists the favorite companies of person $i$, where
people are indexed from zero. A person should be excluded when every company
in that person's list also appears in some other person's list—that is, when
their list is a subset of another list.

Return the indices of exactly those people whose favorite-company list is not
a subset of any other person's list. The indices must appear in increasing
order. Company order inside an input list has no semantic meaning.

### Function Contract
**Inputs**

- `favoriteCompanies`: a list containing $P$ favorite-company lists, with
  $1 \le P \le 100$.
- Each person's list contains between $1$ and $500$ distinct company names.
- Every company name contains between $1$ and $20$ lowercase English letters.
- All favorite-company lists are distinct as sets, even if their input orders
  differ.

Let $C$ be the maximum number of companies in one person's list.

**Return value**

Return the qualifying person indices in increasing order. Index $i$ qualifies
exactly when there is no $j\ne i$ for which every company in
`favoriteCompanies[i]` belongs to `favoriteCompanies[j]`.

### Examples
**Example 1**

- Input: `favoriteCompanies = [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]`
- Output: `[0, 1, 4]`
- Explanation: Lists at indices `2` and `3` are contained in larger lists;
  the other three are not contained in any person's list.

**Example 2**

- Input: `favoriteCompanies = [["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]`
- Output: `[0, 1]`

**Example 3**

- Input: `favoriteCompanies = [["leetcode"], ["google"], ["facebook"], ["amazon"]]`
- Output: `[0, 1, 2, 3]`
- Explanation: The four distinct singleton sets are mutually disjoint, so none
  is a subset of another.

### Required Complexity
- **Time:** $O(P^2C)$
- **Space:** $O(PC)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Constructing the $P$ sets stores and reads at most $PC$ company entries. There
are at most $P(P-1)$ ordered person comparisons, and a hash-set subset test
examines at most $C$ elements, giving $O(P^2C)$ expected time. Early exits and
size filters improve many inputs but do not change the worst-case bound.

The sets retain $O(PC)$ company references. The output contains at most $P$
indices and is covered by that bound; the comparison loop uses constant
additional scalar state.

#### Alternatives and edge cases

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

</details>
