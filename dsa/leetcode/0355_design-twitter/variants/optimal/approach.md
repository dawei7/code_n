## General
**Retain only history that can still reach a feed**

Assign every posted tweet a strictly increasing timestamp and keep each user's ten newest `(timestamp, tweet_id)` pairs. Older tweets from that same user can never enter any ten-item feed because ten newer tweets from the user already outrank them.

Following relationships are hash sets. Posting, following, and unfollowing are therefore expected constant-time operations. A user is always included as a feed source whether or not the user follows themself.

**Merge independently sorted tweet streams**

To build a feed, consider the querying user and every followee as independently sorted tweet streams. Put the newest tweet from each non-empty stream into a max-heap, represented with negative timestamps. Repeatedly remove the globally newest tweet, add its ID to the feed, and insert the next older tweet from the same user's stream. Stop after ten results or when the heap is empty.

**Why the heap emits global timestamp order**

The heap always contains the newest not-yet-emitted tweet from each source that still has one. Therefore its root is the newest remaining tweet across all sources. After that tweet is emitted, exposing only the next tweet from its own stream restores the invariant. Induction proves that the output is globally newest-first, and stopping at ten gives exactly the required prefix.

## Complexity detail
Posting and relationship changes take expected $O(1)$ time. For `F` feed sources, heap construction is $O(F)$ and at most ten pop/push steps cost $O(10 \log F)$. Each user stores at most ten tweets; with `U` users and `E` follow edges, space is $O(U + E)$ up to the fixed factor ten.

## Alternatives and edge cases
- **Scan all tweet history:** makes feed queries increasingly expensive as the service accumulates posts.
- **Gather every retained candidate then select ten:** is another approach linear in the number of followed sources, but materializes all candidates before selection.
- **Materialize each user's feed:** makes reads cheap but requires costly fan-out updates whenever a followed account posts.
- Following an already-followed user and unfollowing a missing relationship are idempotent.
- Self-following must not duplicate the user's own tweets.
- A user with no available tweets receives an empty feed.
- Globally unique timestamps determine order even when tweet IDs repeat.
