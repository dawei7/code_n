## General

The object must support four different operations over shared history: append a new tweet, change a directed follow relationship, remove that relationship, and build a feed containing the ten newest eligible tweets. The exact solution separates these responsibilities across three mappings plus one global clock.

- `user_tweets[userId]` is a list of that user's tweet IDs in posting order, oldest first and newest last.
- `user_following[followerId]` is a set of users currently followed by `followerId`.
- `tweets[tweetId]` stores the global posting time of that tweet.
- `time` is incremented once per post, so later posts receive larger timestamps.

Tweet IDs are unique but do not encode chronological order. A tweet with ID `2` might be newer than one with ID `9000`. The separate monotonic timestamp is therefore necessary for a globally correct feed.

**Posting a tweet.**

`postTweet` first increments the global clock. It appends the tweet ID to the author's list and associates the ID with the new time. Appending keeps each user's list in chronological order without sorting. Since every tweet ID is guaranteed unique, assigning `self.tweets[tweetId]` cannot overwrite another tweet's timestamp under valid input.

The source retains every posted tweet. It does not trim a user's list to ten items, despite the manifest summary saying that only ten posts per user are retained. Older tweets can never enter a ten-item feed while the same user has ten newer eligible tweets, so trimming would be a valid optimization for this exact interface, but that optimization is not implemented here.

**Following and unfollowing are directed.**

`follow(followerId, followeeId)` adds the followee to the follower's set. A set naturally makes repeated follow calls idempotent: adding an existing member changes nothing. The relationship is one-way; following user `2` does not make user `2` follow back.

`unfollow` retrieves the follower's set, checks for the followee, and removes it only when present. An attempt to unfollow someone not currently followed is therefore a no-op. Access through `defaultdict(set)` also creates an empty set for a previously unseen follower, allowing both methods to work without explicit initialization branches.

**Selecting all eligible users for a feed.**

The feed includes followed users and the requesting user. `getNewsFeed` copies the current following set into a new set named `users`, then adds `userId`. The copy is important: adding the requesting user directly to the stored following set would silently create a self-follow relationship and alter later follow state. The contract says users cannot explicitly follow themselves, but their own tweets must still appear in their feed.

**Why only ten recent tweets per source need consideration.**

For each eligible user `u`, the expression `self.user_tweets[u][::-1][:10]` obtains up to that user's ten newest tweet IDs in newest-first order. No tweet older than a user's tenth-newest tweet can be among the global ten newest eligible tweets. There are already ten newer eligible tweets from that same user alone, so the older tweet has at least ten items ahead of it before any other users are considered.

This argument is independent for every source. Therefore the global answer is guaranteed to be among the union of at most ten candidates from each eligible user.

The exact slicing expression deserves careful attention. `[::-1]` first constructs a reversed copy of the entire per-user list, and only then `[:10]` copies its first ten entries. Semantically this obtains the right candidates. Operationally it performs work proportional to all tweets by that user, not merely ten. A direct slice such as `user_tweets[u][-10:]` followed by appropriate ordering would avoid that full reverse copy.

If an eligible user has never posted, `defaultdict(list)` supplies an empty list and contributes no candidates. This lookup may create a persistent empty list entry for that user.

**Combining and ranking candidates.**

The list comprehension creates one short list per eligible user. `sum(tweets, [])` then concatenates them into one flat candidate list. Although concise, repeatedly adding Python lists recopies earlier accumulated elements; this detail affects query complexity.

Finally, `nlargest(10, candidates, key=...)` returns at most ten tweet IDs with the greatest stored timestamps. Because the global clock strictly increases, timestamps are unique, so newest-to-oldest order is unambiguous. The key function looks up the posting time associated with each candidate tweet.

For the example, user `1` initially has tweet `5`, so their feed is `[5]`. After following user `2` and after user `2` posts tweet `6`, both authors are eligible. Tweet `6` has a larger timestamp than tweet `5`, so `nlargest` returns `[6, 5]`. After the unfollow, only user `1` and their own tweet remain eligible, restoring `[5]`.

**Why the resulting feed is correct.**

Every candidate belongs to either the requester or a currently followed user because candidate lists are built only for members of `users`. Thus no ineligible tweet can be returned.

Suppose an eligible tweet is not included among its author's ten newest. At least ten newer tweets from that author are eligible, so the omitted tweet cannot be in the global top ten. Consequently, candidate pruning cannot remove a required answer. `nlargest` selects exactly the ten greatest global timestamps from the remaining complete candidate pool and orders them descending, so every returned item is one of the ten most recent eligible tweets and every required top-ten tweet is returned.

Follow changes need not modify stored tweets. A feed query consults the current relationship set, so following exposes an author's existing retained history immediately, while unfollowing excludes that author immediately. This behavior follows naturally from query-time filtering.

**The manifest describes a more efficient algorithm than the source.**

The manifest says the structure retains ten posts per user and heap-merges the newest entries from feed sources in $O(F+10\log F)$ time. The exact solution retains all posts, extracts candidates with full-list reversals, concatenates lists using repeated addition, and calls `nlargest` over a flat candidate list. It does not perform a $k$-way heap merge of chronological streams. Its real persistent space and feed-query cost are therefore larger than the manifest claims.

## Complexity detail

Let $P$ be the total number of posted tweets, $E$ the number of live follow edges, and $U$ the number of user keys represented in the mappings. For one feed query, let $F$ be the number of eligible sources including the requester, let $P_F$ be the total number of historical tweets stored by those sources, and let $P_{\max}$ be the largest tweet-list length among them.

`postTweet` uses one increment, one amortized constant-time list append, and one expected constant-time hash assignment, so it takes amortized expected $O(1)$ time. `follow` and `unfollow` use expected $O(1)$ set operations.

During a feed query, copying the follow set costs $O(F)$. Reversing each full tweet list costs total $O(P_F)$ time. Each retained slice has at most ten elements. Concatenating $F$ short lists with `sum(..., [])` can copy the growing partial result once per list, costing $O(10F^2)=O(F^2)$ in the worst case. There are at most $10F$ flat candidates. `nlargest(10, ...)` takes $O(10F\log 10)=O(F)$ time because the requested result size is the constant ten. The exact overall query bound is therefore

$$
O(P_F+F^2),
$$

not the manifest's heap-merge bound.

Persistent tweet lists and the timestamp map each represent all $P$ tweets, while following sets represent $E$ edges; mapping keys and empty defaults contribute up to $O(U)$. Persistent storage is $O(P+E+U)$, not merely $O(U+E)$. During a query, the full reverse of one source list may temporarily contain $P_{\max}$ references, while the per-source slices and flattened candidates contain $O(F)$ elements because ten is constant. Peak query workspace is therefore $O(P_{\max}+F)$, excluding the returned list of at most ten IDs.

## Alternatives and edge cases

- **Heap-merge per-user streams:** Keep each user's tweets in chronological order, push the newest tweet from every eligible source into a max-heap, and after popping one push that same user's next older tweet. This returns ten items in $O(F+10\log F)$ time and matches the manifest's merge summary.

- **Retain only ten tweets per user:** Because feeds never return more than ten items and current follow relationships apply to history uniformly, older per-user tweets can be discarded. This reduces tweet-list storage to $O(10U)$, though timestamps for discarded tweets should also be removed if nothing else needs them.

- **Improve the exact candidate extraction:** Use `self.user_tweets[u][-10:]` to copy only ten tail items and flatten with `itertools.chain` or a comprehension. This avoids full reversals and quadratic list concatenation while preserving the same candidate-pruning proof.

- **Sort all eligible history:** Gathering every eligible tweet then sorting by timestamp is correct but costs $O(P_F\log P_F)$ time per feed and ignores the fixed output size of ten.

- **Requester follows nobody:** The temporary user set still includes the requester, so their own recent tweets appear. If they have no tweets, the result is `[]`.

- **Repeated follow:** Set insertion is idempotent, so it does not duplicate a source or duplicate its tweets in the feed.

- **Unfollow a missing relationship:** The membership guard makes the operation a no-op and avoids a removal error.

- **More than ten tweets from one author:** Only that author's ten newest can matter to any ten-item feed; older ones are semantically irrelevant to the query even though this source still stores and reverses them.

- **Tweet ID order:** IDs must never be used as timestamps. The global counter, not numerical tweet ID, determines recency.

- **Self-follow:** The contract prevents explicit self-follow calls. Own tweets are added through the temporary query set, so no stored self-edge is needed.

- **Default entries created by reads:** Querying a previously unseen user creates empty following and tweet containers through `defaultdict`. This is harmless but means read operations can increase the mapping-key count.
