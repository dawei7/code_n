## General

**What the data structure must remember**

The router supports three operations that ask for three different views of the same live packets:

- `addPacket` must recognize an exact duplicate quickly and may need to evict the oldest packet.
- `forwardPacket` must remove the oldest live packet, so packets need a global FIFO order.
- `getCount` must count one destination's live timestamps inside an inclusive interval.

Trying to satisfy all three operations with one list would be expensive. A list preserves FIFO order, but duplicate detection and range counting would require scans. The protected solution therefore stores the same logical information in several coordinated structures:

- `q` is a `deque` of full `(source, destination, timestamp)` tuples in arrival order.
- `vis` is a set of encoded packet keys used for duplicate detection.
- `d[destination]` is an append-only list containing every successfully added timestamp for that destination.
- `idx[destination]` is the index of the first timestamp in that destination list that is still live.

The most important design choice is that old timestamps are not physically deleted from `d`. Deleting the first item of a Python list would shift every later item and cost linear time. Instead, `idx` moves to the right when a packet is forwarded or evicted. Thus, the live timestamps for destination `d` are exactly the suffix

`self.d[d][self.idx[d]:]`.

This is lazy deletion: expired history remains in memory, but one integer marks the boundary between expired and live entries.

**Why each destination list is sorted**

Calls to `addPacket` arrive in non-decreasing timestamp order. Every accepted packet is appended to its destination's list in that same global order. Taking only the packets for one destination cannot reverse their order, so each `d[destination]` list is also non-decreasing.

Forwarding is FIFO across the whole router. Therefore, for any particular destination, packets leave in the same order in which their timestamps were appended. Incrementing `idx[destination]` always expires the first live entry of that destination. The remaining suffix stays sorted, which is exactly what makes binary search possible.

Without the non-decreasing timestamp guarantee, this implementation would not be correct: appending would no longer produce sorted histories, and `bisect_left` could return meaningless boundaries.

**Adding a packet**

The helper `f(a, b, c)` converts the three fields into one integer:

`a << 46 | b << 29 | c`.

`addPacket` first computes that key. If the key is already in `vis`, the source treats the packet as a duplicate and returns `False` without changing any structure.

Otherwise, it inserts the key into `vis`. If `q` already contains `memoryLimit` packets, it calls `forwardPacket`. That removes exactly the FIFO front packet and frees one slot. The new tuple is then appended to `q`, and its timestamp is appended to the appropriate destination history.

Notice that eviction happens only for a packet that passed the duplicate test. A rejected duplicate does not evict anything. Also, the new key is inserted just before an old packet is evicted; this ordering is safe only if distinct packets have distinct encoded keys.

**Forwarding or evicting the oldest packet**

If `q` is empty, `forwardPacket` returns `[]`. Otherwise, `popleft()` supplies the oldest live tuple in constant time. The method removes that packet's key from `vis` so that the same triple may be accepted again later, increments the corresponding destination's live-start index, and returns the three fields as a list.

The method is shared by explicit forwarding and automatic capacity eviction. That is valuable because both events have exactly the same bookkeeping requirements. There is only one path that removes a live packet, so `q`, `vis`, and `idx` are less likely to disagree.

**Counting a destination in an inclusive time range**

For `getCount(destination, startTime, endTime)`, let `ls` be the destination's complete timestamp history and `k = idx[destination]` be its first live position. The source performs:

- `bisect_left(ls, startTime, k)` to find the first live timestamp greater than or equal to `startTime`;
- `bisect_left(ls, endTime + 1, k)` to find the first live timestamp strictly greater than `endTime`.

Their difference is the number of live timestamps in the inclusive range. Passing `k` as the lower search boundary is essential: expired timestamps before `k` must not be counted. Searching for `endTime + 1` is equivalent to using an upper-bound search for `endTime` because timestamps are integers.

For example, suppose one destination's history is `[90, 95, 105, 110]` and its first two packets have left the router. Then `idx` is `2`, so only `[105, 110]` is live. For the range `[100, 110]`, the lower boundary is position `2` and the boundary after the range is position `4`, giving `4 - 2 = 2`. The expired values never enter the result even though they remain in the list.

**Why the coordinated structures are logically correct**

Ignoring the encoding issue described below, the following relationship is maintained after every operation: `q` contains every live packet exactly once in FIFO order; `vis` contains exactly the keys of those packets; and each destination suffix beginning at `idx` contains exactly the timestamps of its live packets in arrival order.

The relationship is initially true because every structure is empty. A successful add places the same new packet into all relevant views, evicting one old packet first if necessary. A duplicate changes nothing. A forward removes the same oldest packet from the queue and set and advances exactly its destination boundary. By induction, all views continue to represent the same live collection. Consequently, queue removal obeys FIFO and the binary-search difference counts precisely the desired live packets.

**Material correctness defect in the protected source**

The particular bit packing in `f` is not injective under the documented constraints. A timestamp can require 30 bits because it may reach `10^9`, but the destination is shifted by only 29 bits. Bit 29 is therefore shared by `destination` and `timestamp`. Likewise, an 18-bit destination shifted by 29 can reach bit 46, which is also the first bit allocated to `source`.

Because the fields are combined with bitwise OR, an already-set overlapping bit hides the corresponding bit from the other field. For example, with the same positive source and destination `1`, timestamps `1` and `536870913` differ only by bit 29. The destination already sets bit 29, so both triples produce the same encoded key. If the earlier packet is still live, the later, genuinely distinct packet is incorrectly rejected as a duplicate.

Thus, the data-structure strategy is sound, but the exact protected implementation is not fully correct for the stated domain. A collision-free tuple key, or non-overlapping shifts with enough bits for every field, is required for complete correctness. This document describes the source as it exists and does not silently claim that its packed-key invariant holds.

## Complexity detail

Let `q` be the total number of method calls, `a` the number of successfully added packets, `m` the memory limit, and `h_d` the total number of accepted packets ever recorded for a queried destination `d`.

The constructor initializes a constant number of containers, so it takes `O(1)` time.

An `addPacket` performs expected `O(1)` set work, at most one constant-time deque removal, one deque append, and one list append. Its expected time is therefore `O(1)`. A `forwardPacket` also takes expected `O(1)` time: `popleft`, set removal, dictionary access, and an index increment are all constant-time expected operations.

`getCount` performs two binary searches over a destination history, taking `O(\log h_d)` time. Because `h_d \le a \le q`, this is `O(\log q)`. Across an arbitrary sequence of `q` operations, the conservative bound is `O(q \log q)`, matching the manifest. If most calls are adds or forwards, the actual work can be closer to linear.

The live queue and duplicate set contain at most `m` entries. However, destination histories are append-only and are never compacted, so they can retain all `a` accepted timestamps even when the memory limit is small. The destination dictionaries can also acquire entries through count queries. Total auxiliary space is therefore `O(q)` in the worst case, not merely `O(m)`. The integer bounds make the packed-key arithmetic constant-size, although its collision behavior remains the correctness issue described above.

## Alternatives and edge cases

- **Use packet tuples directly in the set:** Storing `(source, destination, timestamp)` avoids all bit-width reasoning and is collision-free at the logical level. Python tuple hashing still gives expected constant-time lookup and is the simplest repair for the protected source's genuine encoding defect.
- **Use collision-free bit fields:** Packing can work if each field receives enough non-overlapping bits. The shifts must be derived from the actual maximum values, and the proof must include boundary values rather than assuming that 29 bits hold `10^9`.
- **Physically delete destination timestamps:** Removing the front of an ordinary list costs linear time because later elements shift. A deque supports front deletion but does not support binary search, so the append-only list plus live-start index is the useful combination here.
- **Balanced ordered multiset per destination:** This supports insertion, deletion, and range counts, but Python's standard library has no direct order-statistics multiset. It adds complexity that the non-decreasing timestamp guarantee lets the source avoid.
- **Linear scan for `getCount`:** Scanning only live packets is easy but can cost `O(m)` per query and `O(qm)` over many calls. Binary search is the reason historical timestamps are kept in sorted per-destination lists.
- **Duplicate packet:** A true duplicate must return `False` and must not cause an eviction. The source has this control flow, subject to false duplicates created by encoded-key collisions.
- **Packet re-added after forwarding:** Once a packet leaves, its key is removed from `vis`, so the exact triple may legally be added again. Its timestamp is appended to history; the non-decreasing call guarantee ensures that this remains sorted.
- **Automatic eviction:** Adding a new non-duplicate to a full router forwards exactly one oldest packet before appending the new one, keeping the live size at `memoryLimit`.
- **Empty forwarding:** `forwardPacket` returns an empty list and changes no index or set when no packet is live.
- **Unknown destination:** Because `d` and `idx` are default dictionaries, querying an unseen destination obtains an empty history and zero boundary, so both searches return zero and the count is zero.
- **Repeated timestamps:** Lists may contain equal timestamps from different sources. `bisect_left(startTime)` and `bisect_left(endTime + 1)` include every equal value in the requested inclusive range.
- **Expired timestamps still stored:** Binary search must begin at `idx[destination]`. Omitting that lower bound would count packets that have already been forwarded or evicted.
- **Integer upper endpoint:** Searching for `endTime + 1` is safe in Python because integers do not overflow. In a fixed-width language, an upper-bound operation for `endTime` may be safer.
