## General

**Interpret keys as directed edges**

Treat every room as a graph vertex. A key `j` found in room `i` creates a directed edge from `i` to `j`: once room `i` has been visited, that key makes room `j` reachable.

Room 0 is the only initially unlocked room, so the question becomes:

> Are all graph vertices reachable from vertex 0?

Depth-first search answers exactly that.

**The visited set represents rooms already unlocked and entered**

Set `vis` starts empty. Calling `dfs(0)` models entering the initially open room.

When `dfs(i)` is called, it first checks `if i in vis`. If so, that room and all keys reachable through it have already been processed, so the call returns.

Otherwise, it adds `i` to `vis` before following any key. Marking before recursion is essential. If room 0 contains a key to room 1 and room 1 contains a key back to room 0, the second call to room 0 sees it already marked and stops rather than recursing forever.

**Follow every key**

For each key `j` in `rooms[i]`, the function calls `dfs(j)`.

If `j` is new, the key unlocks a new reachable room, which is entered and explored. If it was already visited through another route, the early check makes the call constant work.

Taking keys is never harmful and has no capacity cost, so exploring every listed edge is the right action. A key can point to the current room, a previously visited room, or a future room; the same logic handles all cases.

**Why discovery order does not matter**

DFS follows one chain of keys as deeply as possible before returning. A breadth-first traversal would visit rooms in a different order, but both discover the same set of vertices reachable from room 0.

The question asks only whether all rooms can eventually be visited, not the order or minimum number of steps. Any complete reachability traversal is sufficient.

**Final comparison**

After DFS finishes, `len(vis)` is the number of rooms reachable from room 0. The expression

`len(vis) == len(rooms)`

returns true exactly when every room label from 0 through `n-1` was reached.

There is no need to inspect unvisited rooms' keys. Those keys are physically inaccessible because entering the room containing them would already require reachability.

**Trace the successful chain**

For `rooms = [[1],[2],[3],[]]`:

- enter room 0 and take key 1;
- enter room 1 and take key 2;
- enter room 2 and take key 3;
- enter room 3, which contains no key.

`vis` becomes `{0,1,2,3}`, whose size equals the number of rooms, so the result is true.

For `[[1,3],[3,0,1],[2],[0]]`, DFS from 0 can reach rooms 1 and 3. Their keys lead only among 0, 1, and 3. Room 2's only key is inside room 2 itself, so no reachable edge enters it. The visited size is three rather than four, and the result is false.

**Why the traversal is correct**

Every room added to `vis` is reachable: room 0 is initially accessible, and any later room is entered using a key from a previously reachable room.

Conversely, consider any room reachable through a sequence of keys starting from 0. DFS processes every key in every visited room, so by induction along that key sequence, it eventually calls DFS on and visits the room.

Thus, `vis` equals exactly the set of visitable rooms. Comparing its size with the total proves the returned Boolean.

## Complexity detail

Let `n` be the number of rooms and

$$
K=\sum_i |\texttt{rooms}[i]|
$$

be the total number of keys.

Each room is fully processed at most once because of `vis`. Across processed rooms, every key is examined once. Total time is `O(n+K)`.

The visited set stores at most `n` room numbers. Recursive call depth is at most `n` in a chain of rooms. Total auxiliary space is `O(n)`.

Repeated calls caused by keys to already visited rooms return immediately and do not repeat their adjacency-list scans.

## Alternatives and edge cases

- **Breadth-first search:** A queue-based traversal discovers the same reachable set and avoids recursion depth concerns.

- **Repeatedly scan for newly unlocked rooms:** It can require many passes. Graph traversal processes each room and key once.

- **No visited set:** Cycles such as room 0 keying room 1 and room 1 keying room 0 would recurse forever or repeat work.

- **Key to the same room:** The room is already marked before its keys are explored, so the self-call returns.

- **Duplicate paths to one room:** The first path explores it; later calls stop at the membership check.

- **Room with no keys:** DFS marks it visited and simply returns after an empty loop.

- **Key located inside its own locked room:** It provides no route into that room and cannot help unless some other reachable room also contains its key.

- **All room keys in room 0:** DFS reaches every listed room directly.

- **A disconnected subset of rooms:** No key path from 0 reaches it, so visited size remains smaller than `n`.

- **Distinct keys within a room:** Guaranteed by the contract, though the visited set would also tolerate duplicates.

- **Valid key range:** Every key is a room index, so no bounds validation is needed.

- **Recursion depth:** Up to 1000 rooms can form a chain near Python's default limit; iterative DFS or BFS is a robust equivalent.

- **Input immutability:** Key lists are iterated but never changed.
