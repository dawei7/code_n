## General
**Normalize both friendship directions.** Build a `friends` common table expression containing `user2_id` from rows whose `user1_id` is `1`, unioned with `user1_id` from rows whose `user2_id` is `1`. `UNION` also protects against duplicate friend identifiers.

**Join friends to their liked pages.** Match `friends.friend_id` to `Likes.user_id`. This removes likes from unrelated users before page projection. Select distinct page identifiers because multiple friends may like the same candidate page.

**Exclude pages the target already likes.** Use `NOT EXISTS` against a second `Likes` alias constrained to `user_id = 1` and the same `page_id`. Unlike `NOT IN`, this remains safe under SQL null semantics, although the key columns are expected to be non-null. Alias the surviving identifier as `recommended_page`.

Every emitted page has a witnessing friend like and no matching self-like. Conversely, every page satisfying those two conditions joins through its friend's normalized identifier and survives the exclusion, proving completeness.

## Complexity detail
With hash-based union, joining, anti-joining, and deduplication, the query processes the $R$ input rows in $O(R)$ logical time and uses $O(R)$ intermediate state. A physical engine may choose sort-based operations with an additional logarithmic factor.

## Alternatives and edge cases
- **Correlated friendship checks:** Testing both friendship directions separately for every like is correct but may rescan `Friendship` and grow quadratically.
- **One friendship direction only:** It misses friends when user `1` appears in the other column.
- **`UNION ALL` without final `DISTINCT`:** Shared pages or repeated friend discovery can duplicate recommendations.
- **Inner join to user `1` likes:** It keeps already-liked pages rather than excluding them.
- **No friends:** No likes join through the friend set, so the result is empty.
- **Only self-liked friend pages:** The anti-join removes every candidate.
