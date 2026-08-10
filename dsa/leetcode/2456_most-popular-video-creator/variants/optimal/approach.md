## General

**Maintain two independent facts for every creator**

The result needs a creator's total popularity and one representative video. These use different aggregations:

- Popularity is the sum of views across all the creator's videos.
- The representative is the video with the largest individual view count, breaking ties by the lexicographically smallest ID.

The dictionary `cnt` stores the first fact. The dictionary `d` stores an index into the original arrays for the second fact. Keeping an index rather than copying an ID and view count lets the code compare both associated fields through `views[d[c]]` and `ids[d[c]]`.

**Process aligned video records**

`zip(creators, ids, views)` groups the three values at each video position, and `enumerate` supplies that position as `k`. The arrays have equal length by contract, so no record is truncated.

For creator `c`, `cnt[c] += v` adds the current video's views to the creator's cumulative popularity. A `defaultdict(int)` starts an unseen total at zero.

The condition for replacing `d[c]` is:

`c not in d or views[d[c]] < v or (views[d[c]] == v and ids[d[c]] > i)`.

An unseen creator must record the first video. Otherwise the current video replaces the saved one when it has more views. On equal views, it replaces the saved video only if current ID `i` is lexicographically smaller.

The IDs do not need to be unique. Two distinct videos with the same ID are still counted separately in popularity, and if they tie for maximum views they lead to the same representative string.

**Find the global popularity maximum**

After the single pass, `cnt[c]` is complete for every creator and `d[c]` points to that creator's correct best video. Since at least one video exists, `max(cnt.values())` safely obtains the largest popularity `mx`.

The return comprehension iterates through creator totals and emits

`[c, ids[d[c]]]`

for every creator whose total equals `mx`. Dictionary iteration order is irrelevant because the answer may be returned in any order.

**Trace the first example**

For creators `["alice","bob","alice","chris"]`:

- Alice's first video records total 5 and representative `"one"` with 5 views.
- Bob records total 10 and representative `"two"`.
- Alice's second video raises her total to 10. It ties her first video's 5 views, but `"three"` is lexicographically larger than `"one"`, so the representative remains `"one"`.
- Chris finishes with total 4.

The maximum total is 10, so Alice and Bob are both returned with their saved IDs.

**Why the per-creator state is correct**

After processing any prefix of the videos, `cnt[c]` equals the sum of views for creator `c` in that prefix because every matching record adds its view count once.

For `d[c]`, the update compares the current saved candidate and new video under the exact ordering “larger views first, then lexicographically smaller ID.” Keeping the better of those two preserves the best video over the enlarged prefix. This induction begins with the creator's first video and holds through the complete scan.

At the end, filtering by the maximum total selects exactly all highest-popularity creators, and the saved index supplies exactly the required video for each one.

**Zero-view videos**

Views may be zero. A creator with several zero-view videos still gets a representative: the first occurrence enters through `c not in d`, and later equal-zero videos can replace it when their IDs are smaller. If every creator has total zero, every creator ties for highest popularity and is returned.

## Complexity detail

Let $n$ be the number of videos and $C$ the number of distinct creators. The main loop performs expected constant-time dictionary work per video, for expected $O(n)$ time. Finding `mx` and building the result each scan $C\le n$ entries, so total expected time remains $O(n)$.

The two dictionaries store one total and one index per creator, using $O(C)$ space, bounded by $O(n)$. The output can also contain $O(C)$ pairs. No per-creator video lists are stored.

String comparisons examine IDs of length at most five, so they are constant-time under the stated bounds. More generally, an ID length $L$ would add an $O(L)$ factor to tie comparisons.

## Alternatives and edge cases

- **Group all videos by creator:** Build lists and later compute totals and maxima. It is correct but stores every record again instead of one total and one best index.
- **Sort records:** Sorting by creator, views, and ID can organize the data but costs $O(n\log n)$ when hashing supports a one-pass solution.
- **Store a tuple per creator:** Keep total plus a best pair such as negative views and ID. This can be concise, but the source's saved index avoids duplicating strings.
- **Several creators tie:** Every total equal to `mx` is emitted; no arbitrary single winner is chosen.
- **Several videos tie for one creator:** The lexicographically smallest ID wins through the strict string comparison.
- **Duplicate IDs:** Videos remain distinct for summing views even when their ID strings match.
- **All views zero:** Every creator has maximum total zero and still has a correctly selected smallest-ID representative.
- **One video:** Its creator is the sole maximum and that video's ID is returned.
- **Output ordering:** No sort is required because the contract accepts any order.
- **Equal-length input guarantee:** It ensures `zip` processes every video record rather than stopping early.
