# Page Recommendations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1264 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/page-recommendations/) |

## Problem Description

### Goal

The `Friendship` table stores undirected friendships as two user identifiers, and `Likes` records which pages each user likes. A friendship involving user `1` may place that user in either friendship column.

Recommend every page liked by at least one friend of user `1` that user `1` has not already liked. Return each recommended page only once even when several friends like it. Pages liked only by nonfriends must not appear, and the result may be returned in any order.

### Function Contract

**Inputs**

- `Friendship(user1_id, user2_id)`: unique undirected friendship pairs.
- `Likes(user_id, page_id)`: unique user-page likes.
- Let $F$ and $L$ be the two table row counts, and let $R=F+L$.

**Return value**

- Return one column named `recommended_page` containing the distinct eligible page identifiers for user `1`.

### Examples

**Example 1**

If users `2`, `3`, `4`, and `6` are friends of user `1`, their liked pages are candidates regardless of which friendship column contains `1`. A page already liked by user `1` is excluded, while a page shared by users `2` and `3` appears once.

**Example 2**

When every page liked by a friend is also liked by user `1`, the result is empty.

**Example 3**

A page liked by a user with no friendship edge to user `1` is not recommended.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Normalize both friendship directions.** Build a `friends` common table expression containing `user2_id` from rows whose `user1_id` is `1`, unioned with `user1_id` from rows whose `user2_id` is `1`. `UNION` also protects against duplicate friend identifiers.

**Join friends to their liked pages.** Match `friends.friend_id` to `Likes.user_id`. This removes likes from unrelated users before page projection. Select distinct page identifiers because multiple friends may like the same candidate page.

**Exclude pages the target already likes.** Use `NOT EXISTS` against a second `Likes` alias constrained to `user_id = 1` and the same `page_id`. Unlike `NOT IN`, this remains safe under SQL null semantics, although the key columns are expected to be non-null. Alias the surviving identifier as `recommended_page`.

Every emitted page has a witnessing friend like and no matching self-like. Conversely, every page satisfying those two conditions joins through its friend's normalized identifier and survives the exclusion, proving completeness.

#### Complexity detail

With hash-based union, joining, anti-joining, and deduplication, the query processes the $R$ input rows in $O(R)$ logical time and uses $O(R)$ intermediate state. A physical engine may choose sort-based operations with an additional logarithmic factor.

#### Alternatives and edge cases

- **Correlated friendship checks:** Testing both friendship directions separately for every like is correct but may rescan `Friendship` and grow quadratically.
- **One friendship direction only:** It misses friends when user `1` appears in the other column.
- **`UNION ALL` without final `DISTINCT`:** Shared pages or repeated friend discovery can duplicate recommendations.
- **Inner join to user `1` likes:** It keeps already-liked pages rather than excluding them.
- **No friends:** No likes join through the friend set, so the result is empty.
- **Only self-liked friend pages:** The anti-join removes every candidate.

</details>
