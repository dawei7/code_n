## General

**The state maintained by the object**

The class must remember active users across many method calls. The stored implementation keeps four fields:

- `cur` is the largest fresh user ID issued so far.
- `chunks` stores the valid upper chunk ID `m`.
- `reused` is a min-heap of IDs belonging to users who have left.
- `user_chunks` maps each active user ID to a set of chunks currently owned by that user.

The sets make membership tests and adding a newly received chunk efficient on average. The heap makes the smallest reusable ID available at its root.

There is deliberately no map from a chunk to its owners. A request discovers owners by scanning all active users. This keeps joining and leaving structurally simple but makes requests depend on the active-user count.

**Assigning the smallest available ID**

When `join` is called, every reusable ID came from an earlier active user and is therefore at most `cur`. If `reused` is nonempty, `heappop` returns its smallest element. That value is smaller than the next never-issued ID `cur + 1`, so it is the globally smallest available positive ID.

If no departed ID is available, all IDs from one through `cur` are active. The method increments `cur` and assigns that next consecutive integer.

It then converts `ownedChunks` to a set and stores it at `user_chunks[userID]`. The contract says the initial list contains unique chunk IDs, but using a set also establishes the representation needed for later membership and insertion.

`cur` does not decrease when a high-numbered user leaves. It represents the frontier of IDs ever issued, not the number of active users. Reuse is handled exclusively by the heap.

**Removing a user**

`leave(userID)` pushes the ID into `reused` and removes its mapping with `self.user_chunks.pop(userID)`. Once the mapping disappears, future requests cannot find any chunk through that user.

The contract guarantees that the user is active and every leave matches a join. Therefore, the same ID is not pushed twice without being popped by another join, and `pop` is not asked to remove a missing key. Those guarantees preserve the one-copy-per-free-ID heap invariant.

The user's set is discarded as a whole. Because ownership is stored only by user, the method does not need to visit every chunk to update a reverse index.

**Processing a request exactly as written**

The method first rejects a `chunkID` below one or above `self.chunks`. Valid problem calls do not require this guard, but it makes the source robust to out-of-range chunk requests.

It initializes an empty result and loops through every `userID, chunk-set` pair in `user_chunks`. If the requested chunk belongs to a set, that user's ID is appended.

After the scan, there are two cases:

- If `res` is empty, nobody can supply the chunk. The requester does not receive it, and the empty list is returned.
- If `res` is nonempty, the request succeeds. The code adds `chunkID` to the requester's ownership set, then returns `sorted(res)`.

The addition happens after collecting owners. Therefore, a requester who did not own the chunk before the call is not retroactively included in the returned provider list. A requester who already owned it is found during the scan and does appear. Set insertion is idempotent, so adding an already owned chunk causes no duplication.

**Why the object remains correct**

After every operation, the keys of `user_chunks` are exactly the active user IDs, and each mapped set is exactly that user's currently owned chunks. A join creates one active entry with the provided ownership. A leave deletes exactly one active entry. A successful request adds exactly the requested chunk to the active requester; a failed request changes nothing.

The heap contains exactly freed IDs not currently assigned. Joining removes its minimum when possible, and leaving adds the newly freed active ID. Since never-issued IDs begin at `cur+1` and all heap IDs are smaller, the join rule always returns the smallest free positive integer.

During a request, scanning every active mapping finds every and only current owner. Sorting those discovered IDs establishes the required ascending return order.

## Complexity detail

Let $U$ be the number of active users, $F$ the number of reusable IDs, $k$ the number of initially owned chunks in one join, $p$ the number of current owners of a requested chunk, and $H$ the total number of active user-chunk ownership entries.

`join` takes $O(k)$ expected time to build the ownership set plus $O(\log F)$ time when popping a reused ID. With no reusable ID, allocation is constant time. `leave` performs a heap push in $O(\log F)$ time and removes one dictionary entry. In Python, reclaiming the removed set may also take time proportional to that user's stored chunks as references are released.

`request` scans all $U$ active users, with expected constant-time set membership per user, then sorts $p$ owner IDs. Its time is $O(U + p \log p)$ expected, plus constant expected insertion on success. The manifest's `O(k + \log U + p \log p)` shorthand does not explicitly expose this mandatory $U$-user scan; the exact method has distinct costs by operation.

Active ownership storage is $O(U+H)$. The reuse heap can contain up to the number of issued but currently inactive IDs, so a fully explicit bound also includes $F$: $O(U+H+F)$. The temporary request result uses $O(p)$ space.

## Alternatives and edge cases

- **Chunk-to-owners reverse index:** Maintain an ordered owner set for each chunk. Requests become proportional to owner count, but join, leave, and successful request must update both directions consistently.
- **Unordered reverse sets plus sorting:** Owner lookup is direct, and sorting still costs $O(p \log p)$ when returning a request.
- **Scanning for a free ID:** Testing IDs from one upward on every join can be slow after frequent churn. The min-heap returns the smallest reusable ID efficiently.
- **User joins with no chunks:** An empty set is stored, and the user can acquire chunks through later successful requests.
- **No owner for a requested chunk:** The method returns an empty list and does not grant the chunk.
- **Requester already owns the chunk:** The requester appears among current owners, and adding the chunk again leaves the set unchanged.
- **Departed owner:** Removing the user's entire map entry ensures none of that user's chunks are offered afterward.
- **Frequent join and leave:** Heap size can grow with inactive reusable IDs, so space is not described solely by active-user count.
- **Out-of-range chunk:** The source returns an empty list even though valid calls are guaranteed by the contract.
- **Sorted output:** Dictionary iteration order is irrelevant because `sorted` establishes ascending IDs.
