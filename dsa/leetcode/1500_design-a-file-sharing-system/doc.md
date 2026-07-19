# Design a File Sharing System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1500 |
| Difficulty | Medium |
| Topics | Hash Table, Design, Sorting, Heap (Priority Queue), Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-file-sharing-system/) |

## Problem Description
### Goal

A very large file is divided into $m$ chunks whose identifiers run from $1$ through $m$. Users may enter and leave a sharing system while owning different subsets of those chunks. Every joining user must receive the smallest positive user ID that is not currently assigned; an ID becomes available for reuse after its user leaves.

A user may request one chunk. The system must report, in ascending user-ID order, every current user who owns that chunk. A nonempty result means the transfer succeeds, so the requester also owns the chunk from that point onward. An empty result means no transfer occurs. Implement construction, joining, leaving, and requesting while keeping both user IDs and chunk ownership consistent through the entire operation stream.

### Function Contract
**Platform interface**

- `FileSharing(m)` initializes a file with chunk IDs in $[1,m]$, where $1 \le m \le 10^5$.
- `join(ownedChunks)` registers a new user who initially owns the distinct chunk IDs in `ownedChunks`, assigns the smallest unused positive user ID, and returns it. The list length is at most $\min(100,m)$ and may be zero.
- `leave(userID)` removes that active user and all of their ownership relationships, makes `userID` reusable, and returns nothing.
- `request(userID, chunkID)` returns the sorted IDs of all current owners of `chunkID`. If that list is nonempty, `userID` gains the chunk after the owner list is determined.

Every `userID` passed to `leave` or `request` identifies an active user, every chunk ID lies in $[1,m]$, and at most $10^4$ method calls are made.

**App-local adapter**

Let $q$ be the number of entries in `operations`, $U$ the greatest number of simultaneously active users, $H$ the number of current user-chunk ownership relationships, $k$ the number of chunks supplied to `join` or removed by `leave`, and $p$ the number of owners returned by a `request`.

- `m`: the number of chunks in the file.
- `operations`: an ordered array of `[name, arguments]` entries using `"join"`, `"leave"`, or `"request"`.
- Return one result per operation: the assigned ID for `join`, `null` for `leave`, and the sorted owner list for `request`.

### Examples
**Example 1**

- Input: `m = 4, operations = [["join",[[1,2]]],["join",[[2,3]]],["join",[[4]]],["request",[1,3]],["request",[2,2]],["leave",[1]],["request",[2,1]],["leave",[2]],["join",[[]]]]`
- Output: `[1,2,3,[2],[1,2],null,[],null,1]`
- Explanation: User 1 obtains chunk 3 from user 2. After user 1 leaves, nobody owns chunk 1. IDs 1 and 2 are both free before the final join, so the smaller ID 1 is reused.

**Example 2**

- Input: `m = 3, operations = [["join",[[]]],["join",[[1]]],["request",[1,1]],["request",[1,1]]]`
- Output: `[1,2,[2],[1,2]]`
- Explanation: The first request reports only the preexisting owner and then gives chunk 1 to user 1. The second request therefore includes both users.

**Example 3**

- Input: `m = 2, operations = [["join",[[1,2]]],["join",[[2]]],["leave",[1]],["request",[2,1]],["join",[[1]]],["request",[2,1]]]`
- Output: `[1,2,null,[],1,[1]]`
- Explanation: Leaving removes every chunk formerly supplied by user 1. Rejoining under the reused ID restores only the chunks explicitly supplied to that new user.
