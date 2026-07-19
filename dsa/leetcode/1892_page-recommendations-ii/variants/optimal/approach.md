## General
**Normalize the undirected graph**

Create a common table expression containing `(user_id, friend_id)` in both directions for every stored friendship. Using `UNION` also protects the logical relation from duplicate directed pairs. Every later step can then reason from the target user to one friend without orientation-specific conditions.

**Generate and filter candidate pages**

Join each directed friendship to `Likes` on `friend_id`. This produces one candidate row for every friend who likes a page; an inner join is important because a friend with no likes contributes no recommendation. Left-join the target user's own likes on both `user_id` and `page_id`, then keep only candidates with no matching own-like row.

**Aggregate friend support**

Group the remaining candidates by target `user_id` and `page_id`. Each source row corresponds to one distinct friend-page like, so `COUNT(*)` is exactly the number of friends supporting that recommendation. Grouping emits each recommendation once.

Every output page has a supporting friend and lacks an own-like match. Conversely, any page satisfying those conditions appears through at least one directed friendship and survives the anti-join, so it is grouped and returned with the exact support count.

## Complexity detail
Expanding friendships and indexing or hashing the two base relations uses $O(F+L)$ work and storage. The friend-to-like join produces $C$ candidate rows. In a general sort-based plan, deduplication and grouping cost $O((F+L+C)\log C)$ time; hash-based plans can approach linear expected work. Intermediate friendships, join state, candidates, and groups occupy $O(F+L+C)$ space.

## Alternatives and edge cases
- **One-direction friendship join:** It misses recommendations whenever the target user appears in `user2_id`.
- **Left-join friends to likes:** It can create a spurious recommendation with a null `page_id`; use an inner join for candidate likes.
- **Correlated friend count:** Recounting supporters for every candidate user-page pair is correct but can repeatedly scan the same friendship and like rows.
- **Already-liked page:** Exclude it even if many friends like it.
- **Several supporting friends:** Return one row and count every distinct friend once.
- **One friend liking several pages:** Each not-yet-liked page becomes its own recommendation.
- **Friend with no likes:** That friendship contributes no result row.
- **Isolated liker:** A user with likes but no friendship cannot generate or receive a recommendation.
