## General
**Start from the canonical friend pairs**

Join each `Friendship` row to the listening facts of its first user and then to the facts of its second user. Require the two listening rows to have the same `song_id` and `day`. This prevents nonfriends from ever becoming candidates and retains the stored `user1_id < user2_id` orientation automatically.

**Measure distinct overlap within each day**

Group matching rows by both friend IDs and by `day`. A group represents the songs that one friend pair shared on one particular date. Keep it only when `COUNT(DISTINCT song_id)` is at least three.

The distinct count is necessary because either user's repeated log rows can multiply join matches. Keeping the date in the group is equally necessary because activity from separate dates cannot be accumulated.

**Collapse repeated qualification**

A friendship may satisfy the rule on several days. Applying `DISTINCT` to the projected friend IDs reduces those daily groups to one output row. Every emitted row therefore corresponds to an input friendship with a qualifying day, and every qualifying friendship produces such a group, so the result is exact.

## Complexity detail
The shared-song join has at most $O(L^2)$ logical row combinations in the worst case, while scanning or indexing the friend relation contributes $O(F)$. Grouping and deduplication remain within $O(L^2)$ intermediate space. Thus the worst-case bounds are $O(L^2+F)$ time and $O(L^2)$ space.

This bound matches the possible output and input scale. With $U$ users, three common songs on one day, and every user pair present in `Friendship`, $L=3U$ and $F=\Theta(U^2)$. Every friendship must be returned, so merely reading and emitting the required relation takes $\Omega(L^2+F)$ work for that family.

## Alternatives and edge cases
- **Self-join all listeners before checking friendship:** This creates nonfriend candidate pairs unnecessarily; driving from `Friendship` restricts work to the required relation.
- **Group only by friend IDs:** This incorrectly combines common songs heard on different days.
- **Use `COUNT(*)`:** Duplicate listening rows and their join cross-products can falsely reach the threshold.
- **Exactly three distinct songs:** The friendship qualifies because the threshold is inclusive.
- **Multiple qualifying days:** Return the canonical friendship only once.
- **Similar nonfriends:** Exclude the pair even when its listening overlap is otherwise sufficient.
- **Empty listening activity:** No friendship qualifies.
