# Accounts Merge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 721 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/accounts-merge/) |

## Problem Description
### Goal
Each account record begins with a person's name followed by one or more email addresses. Two records definitely belong to the same person when they share at least one email, and that connection is transitive through any chain of overlapping records. Equal names alone do not prove that accounts belong to the same person.

Merge every connected group into one record containing the person's name followed by all distinct emails in lexicographic order. Records for different people may be returned in any order. All accounts belonging to one person use the same name, but different people may share that name.

### Function Contract
**Inputs**

- `accounts`: records whose first string is a name and whose remaining strings are that record's email addresses

**Return value**

- One record per connected person, containing the name followed by all distinct emails in sorted order; merged records themselves may appear in any order

### Examples
**Example 1**

- Input: `accounts = [["John","a@mail.com","b@mail.com"],["John","b@mail.com","c@mail.com"]]`
- Output: `[["John","a@mail.com","b@mail.com","c@mail.com"]]`

**Example 2**

- Input: `accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`
- Output: `[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`

**Example 3**

- Input: `accounts = [["Alex","x@mail.com"],["Alex","y@mail.com"]]`
- Output: `[["Alex","x@mail.com"],["Alex","y@mail.com"]]`

### Required Complexity

- **Time:** $O(E \log E)$
- **Space:** $O(E)$

<details>
<summary>Approach</summary>

#### General

**Treat emails as identity vertices**

Create one disjoint-set element for every distinct email. Names are output labels, not evidence of identity: two records with the same name remain separate unless their email components connect.

**Union each account around one representative email**

Within a record, union every email with its first email. This connects the entire record with only a linear number of union operations. Path compression and union by size keep later representative searches nearly constant time.

**Collect emails by final representative**

After all unions, find the representative of every email and append that email to its component. Sort each component's emails, prepend the associated name, and emit the merged record. The outer list needs no semantic order, though the local implementation sorts it for deterministic display.

**Why shared-email chains merge correctly**

Every union joins emails known to belong to one account. If two accounts share an email, their union operations touch the same disjoint-set element and combine their components; repeating this argument joins any transitive chain. Conversely, disjoint-set components can merge only through an account containing emails from both sides, so unrelated records are never combined.

#### Complexity detail

Let `E` count all email occurrences and `U` the distinct emails. Disjoint-set work takes $O(E \alpha(U))$ time. Sorting the component email lists costs at most $O(U \log U)$, which gives the stated $O(E \log E)$ bound. Parent, size, name, and grouped-email maps use $O(E)$ space.

#### Alternatives and edge cases

- **Email graph plus DFS or BFS:** connect every account's first email to its others and traverse connected components; it has comparable asymptotic cost.
- **Pairwise account intersection:** compare every pair of email sets before traversing account components; it is correct but can take $O(A^2)$ set comparisons.
- **Repeated set merging:** continually search for overlapping groups and combine them; careless rescanning can also become quadratic.
- Identical names do not merge records without a shared email.
- One shared email can connect records transitively even when the endpoint records share no email directly.
- Duplicate occurrences of an email must appear only once in the merged output.
- Emails inside every output record are sorted, while the order of the records is unrestricted.

</details>
