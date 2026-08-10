## General

Every jump has equal cost one, so breadth-first search finds the minimum number of jumps. The challenge is representing teleport destinations without repeatedly scanning the whole array.

The source globally precomputes distinct prime factors, groups indices by those factors, and clears a teleport group after its first expansion.

**Prime-factor preprocessing**

`factors[x]` lists every distinct prime divisor of `x` for values through `10^6`.

The global sieve visits `i` from 2 upward. An empty `factors[i]` means no smaller prime divided `i`, so `i` is prime. It then appends `i` to every multiple `j`.

Consequently:

- a prime `p` has `factors[p]=[p]`;
- a composite has its distinct prime divisors;
- 1 has an empty list.

This table is built once when the module loads.

**Map each prime to divisible indices**

For each array value `x` and each `p in factors[x]`, index `i` is appended to `g[p]`.

Thus `g[p]` contains exactly all indices whose values are divisible by prime `p`.

When the BFS reaches an index whose value itself is prime `p`, looking up `g[nums[i]]` produces precisely its legal teleport destinations.

If `nums[i]` is composite, `g[nums[i]]` is normally an empty newly created list because keys populated during construction are primes only. This correctly yields no teleportation: the rule requires the current value itself to be prime.

**BFS state**

`q` contains all indices at the current distance `ans` from index 0. `vis` prevents revisiting indices, and index 0 is marked before the search begins.

For every current index:

- if it is `n-1`, the current BFS level is the minimum distance and is returned;
- its legal teleport list is retrieved;
- adjacent indices are temporarily appended to the same list;
- every unvisited destination is marked and placed in `nq`.

After the whole level, `q=nq` and `ans` increments.

**Why appending adjacent indices is safe**

The source reuses local variable `idx`, which references `g[nums[i]]`. It appends `i+1` unconditionally and `i-1` when valid.

The target check occurs first, so any processed non-target index has `i+1<n`. The left boundary is guarded by `if i`.

These appended entries are valid one-step neighbors. They are considered alongside teleports, then the list is cleared.

For prime current values, this temporarily mutates the shared teleport group before clearing it. That does not create invalid reachability because only the two legal adjacent destinations were added.

**Why each teleport group is expanded once**

Suppose prime group `g[p]` is expanded for the first time at BFS distance `d`. Every index divisible by `p` is reachable in one more jump and is immediately marked or was reached earlier.

If another index with value exactly `p` is processed later, expanding the same group cannot discover a shorter path: all its destinations already received distance at most `d+1`.

Clearing the list prevents repeated scans while preserving every shortest route.

For composite value keys, clearing only removes the temporary adjacent entries from an otherwise empty defaultdict list.

**Why BFS returns a minimum**

The queue advances level by level. All destinations generated from distance `d` have distance `d+1`. Marking on enqueue ensures the first discovered distance for an index is retained.

Therefore, the first level containing `n-1` is its shortest jump distance.

**Following `[1,2,4,6]`**

Level 0 contains index 0. Its value 1 gives no teleport group, but adjacent index 1 is enqueued.

At level 1, value 2 is prime. `g[2]` contains indices 1, 2, and 3 because their values are divisible by 2. Index 3 is enqueued.

At level 2, index 3 is the destination, so the answer is 2.

**Termination**

Adjacent moves alone connect every array index in a line. Even if no teleport is usable, BFS can progress from 0 through 1, 2, and so on. Thus the queue cannot permanently become empty before reaching `n-1`, making the infinite `while 1` loop safe under valid input.

**Environment dependencies**

The exact file uses `defaultdict` and `List` without shown imports. Standalone execution must import them from `collections` and `typing`.

## Complexity detail

Let `M=10^6` and `n=len(nums)`.

Global factor preprocessing performs one append per prime-multiple relation, totaling `O(M\log\log M)` time and space by the sum of reciprocal primes.

Building `g` processes every distinct prime factor of every array value. A value at most `M` has `O(\log M)` distinct factors as a loose bound, so this is `O(n\log M)` time and stored index entries.

Each index is enqueued at most once. Each prime group is scanned and cleared at most once, so BFS also totals `O(n\log M)` over stored group entries plus adjacent work.

Combined time is `O(M\log\log M+n\log M)`. Space is the global factor table plus `g`, visited state, and queues; the manifest summarizes this as `O(n+M)`, though the factor-entry volume is more precisely `O(M\log\log M)`.

## Alternatives and edge cases

- **Test primality during BFS and scan nums:** Scanning all destinations per reached prime can become quadratic.
- **Reverse BFS:** The editorial describes factor-based reverse edges; forward BFS in the exact source is equally shortest-path correct.
- **Do not clear groups:** Correctness remains, but the same large list may be scanned many times.
- **One-element array:** Index 0 is already the destination, so answer is zero.
- **Value 1:** It has no prime teleport and only adjacent moves apply.
- **Composite current value:** It cannot initiate teleportation even though its index belongs to groups of its prime factors.
- **Prime current value:** It reaches every index whose value is divisible by that prime.
- **Teleport to self:** The group includes the current index, but `vis` skips it.
- **Repeated prime values:** The first reached occurrence expands the group; later occurrences need no repeat.
- **No teleportation:** Adjacent steps guarantee answer `n-1`.
- **Right boundary:** The destination is returned before `i+1` is appended.
- **Missing imports:** Standalone use must supply `defaultdict` and `List`.
- **Input preservation:** The source mutates only group lists, not `nums`.
