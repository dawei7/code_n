## General

**Separate active content from reusable identifiers**

Keep a hash table from every active `videoId` to a record containing the video
string and its view, like, and dislike counters. Direct lookup then handles
watching, reactions, and queries without searching through other videos.
Deleting the table entry removes both the content and all statistics, which is
important because a later upload that reuses the same identifier must begin
with three zero counters.

Identifiers that have never been assigned form a simple increasing sequence,
tracked by `next_id`. Deleted identifiers are different: any of them may be
smaller than `next_id`, so store them in a min-heap. An upload takes the heap
minimum when one exists; otherwise it takes `next_id` and advances that
counter. Thus the returned identifier is always the smallest available one.
A removal pushes an identifier only when its video actually exists, preventing
duplicate heap entries after repeated removal requests.

**Apply each operation's state change exactly once**

A successful `watch` first finds the record, increments its view counter, and
uses a slice ending at `endMinute + 1`. Python slicing automatically stops at
the string boundary, matching the required clamp. Missing watches return
`"-1"` before changing state. Likes and dislikes similarly update only an
existing record, while both statistic queries return their distinct missing
sentinels.

The hash table always contains exactly the active identifiers, and the heap
contains exactly the previously assigned identifiers that are currently free.
These sets are disjoint. Consequently, choosing the heap minimum or
`next_id` preserves the smallest-available rule after every upload and removal,
while record-local updates preserve independent statistics for every active
video.

## Complexity detail

Let $Q$, $U$, and $C$ have the meanings defined in the function contract.
Every heap insertion or removal costs $O(\log Q)$; hash-table operations take
expected $O(1)$ time, and returned substrings take time proportional to their
length. The complete sequence therefore takes $O(Q\log Q+C)$ time. Active
video strings use at most $O(U)$ space, while records and reusable identifiers
use $O(Q)$, for $O(U+Q)$ auxiliary state including stored input content.

## Alternatives and edge cases

- **Scan upward for every upload:** Testing identifiers from `0` until a gap is found is correct but can take $O(Q)$ per upload and $O(Q^2)$ over a sequence.
- **Ordered set of deleted identifiers:** A balanced search tree also supports minimum extraction and insertion in $O(\log Q)$ time, but Python's standard library provides a min-heap directly.
- **Only a monotone counter:** This cannot reuse a deleted smaller identifier and violates the assignment rule.
- **Repeated removal:** Removing an already missing identifier must not add the same identifier to the heap twice.
- **Identifier reuse:** A newly uploaded video receives fresh zeroed views, likes, and dislikes even when its identifier belonged to a removed video.
- **Watch beyond the end:** Return through the final character and count exactly one view.
- **Missing identifiers:** `watch`, `getLikesAndDislikes`, and `getViews` use different sentinels; reactions and removal do nothing.
- **Independent counters:** Watching changes only views, while likes and dislikes affect only their respective counters.
