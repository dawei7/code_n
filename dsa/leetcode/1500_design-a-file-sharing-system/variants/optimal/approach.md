## General
**Track ownership in both directions**

Maintain `user_chunks`, mapping every active user ID to the set of chunks that user owns, and `chunk_users`, mapping every currently available chunk to the set of active users who own it. The first direction makes leaving proportional to the departing user's holdings; the second answers a request without scanning unrelated users. Whenever ownership changes, update both sets so the maps describe the same relationships.

Sparse maps matter because $m$ may be much larger than the number of chunks currently held. There is no need to allocate a container for every possible chunk. When the last owner of a chunk leaves, its empty reverse-map entry can be removed.

**Assign the smallest reusable ID**

Keep a min-heap `available_ids` containing IDs released by `leave`, plus `next_id`, the smallest ID never assigned before. A joining user receives the heap minimum when one exists; otherwise they receive `next_id` and that counter advances. Every ID below `next_id` is either active or present exactly once in the heap, so these two cases always choose the smallest unused positive integer.

After choosing the ID, convert `ownedChunks` to a set, store it in `user_chunks`, and add the user to each corresponding `chunk_users` set. Source guarantees make the input IDs distinct, but using a set also keeps later ownership tests and insertions constant-time on average.

**Transfer a requested chunk only when it exists**

Read the current owner set for `chunkID` and sort it to form the required return value. This snapshot is taken before changing the requester's ownership. If it is empty, return it immediately and leave both maps unchanged.

If at least one owner exists, insert the requester into the chunk's owner set and insert the chunk into the requester's holdings. Set insertion is idempotent, so a requester who already owns the chunk remains represented once, while the returned snapshot already includes that user as required. The two-map invariant is therefore preserved after both new and repeated requests.

**Remove every trace of a departing user**

On `leave`, remove the user's chunk set from `user_chunks`. For each held chunk, delete the user from the corresponding owner set and remove the chunk entry if no owners remain. Finally push the released user ID into the min-heap. Since valid operations never leave the same active account twice, no duplicate reusable ID enters the heap.

Construction establishes empty, mutually consistent maps and no available IDs. Each operation above either adds or removes the same ownership pair in both directions, while join and leave partition all previously assigned IDs between active users and the reuse heap. Those invariants prove that requests report exactly the current owners and joins always choose the required ID.

## Complexity detail
Heap insertion or removal costs $O(\log U)$, and touching $k$ initial or departing ownership relationships costs $O(k)$ expected time. Thus `join` and `leave` each take $O(k + \log U)$ time. A request reads and sorts $p$ owners in $O(p \log p)$ time, then performs expected $O(1)$ set updates. These per-operation bounds are summarized by the notation-only required bound; across an operation stream, sum the relevant $k$ and $p \log p$ terms.

The active-user map, reusable-ID heap, and two views of each ownership relationship require $O(U + H)$ auxiliary space. Empty chunks consume no storage, and returned owner lists occupy $O(p)$ output space.

## Alternatives and edge cases
- **Linear search for a free ID:** Test `1, 2, 3, ...` against an active-user set on every join. It is correct but repeated reuse of a high ID can make the operation stream quadratic.
- **Monotone IDs without reuse:** Always incrementing a counter is simpler, but violates the rule that the smallest released ID must be assigned first.
- **Only user-to-chunk sets:** Leaving is efficient, but each request must scan all active users to discover owners of one chunk.
- **Only chunk-to-user sets:** Requests are direct, but leaving must scan every represented chunk because the departing user's holdings are unknown.
- **Store owners in a continuously sorted list:** Requests avoid sorting, but joins, leaves, and successful transfers require linear insertion or deletion. Hash sets keep updates expected constant-time and sort only the output that must already contain $p$ IDs.
- **Empty initial holdings:** `join([])` still creates a user and assigns the smallest available ID; it simply adds no ownership pairs.
- **Unavailable requested chunk:** Return `[]` and do not give the requester that chunk. Empty reverse-map entries are equivalent to absent entries.
- **Requester already owns the chunk:** The returned sorted list includes the requester, and idempotent set insertion creates no duplicate relationship.
- **Leave after successful requests:** Remove both the chunks supplied at join time and every chunk acquired later, because all are stored in the same per-user set.
- **Several released IDs:** The heap, rather than release order, ensures the next join reuses the numerically smallest one.
