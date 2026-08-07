## Function Contract

**Platform interface**

- `FileSharing(m)` initializes a file with chunk IDs in $[1, m]$, where $1 \le m \le 10^5$.
- `join(ownedChunks)` registers a new user owning initial chunk IDs in `ownedChunks`, assigns and returns the smallest available positive user ID.
- `leave(userID)` removes active `userID` and all of their owned chunks, making `userID` available for reuse.
- `request(userID, chunkID)` returns a sorted list of current user IDs owning `chunkID`. If non-empty, `userID` is added to the owners of `chunkID`.

**Return value**

- `join`: integer assigned user ID.
- `leave`: None (`null`).
- `request`: list of integer user IDs sorted in ascending order.
