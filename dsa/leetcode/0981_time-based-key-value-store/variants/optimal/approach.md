## General

**Store a separate chronological history for every key**

One key may receive many values over time, and a query does not necessarily ask for an exact stored timestamp. It asks for the value attached to the greatest stored timestamp that is less than or equal to the query timestamp. This is a predecessor search: among all eligible times, find the latest one.

The implementation organizes the data as

`self.ktv = defaultdict(list)`.

The dictionary maps each string key to its own list of `(timestamp, value)` pairs. Keeping separate histories matters because a timestamp recorded for one key must have no effect on queries for another key.

The problem guarantees that timestamps supplied to `set` are strictly increasing. In particular, timestamps appended to any one key also arrive in increasing order. Therefore,

`self.ktv[key].append((timestamp, value))`

keeps that key's list sorted by timestamp automatically. There is no insertion search, shifting, or later sorting. This guarantee is the reason a simple append is enough.

**Why sorted histories solve the query efficiently**

For a query at time `t`, a key's history has three conceptual regions:

- entries whose timestamp is less than or equal to `t`, which are eligible;
- possibly no eligible entries at all;
- entries whose timestamp is greater than `t`, which are too new.

Because the list is sorted, all eligible entries form one prefix. The required answer is the final pair in that prefix. Binary search can find the boundary immediately after the prefix without inspecting every older value.

The code uses

`i = bisect_right(tv, (timestamp, chr(127)))`.

To understand this precisely, remember that Python compares tuples lexicographically. It first compares their timestamps. Only when timestamps are equal does it compare the value strings.

Every pair with a smaller timestamp is less than the search tuple, and every pair with a larger timestamp is greater. For an equal timestamp, the stored value consists only of lowercase English letters and digits. Its characters have code points below `127`, so the stored value is less than the sentinel string `chr(127)`. Thus an existing pair at exactly the requested timestamp is placed on the eligible, left side of the insertion boundary.

As a result, `i` is exactly the number of stored entries whose timestamps are at most the requested timestamp. The predecessor, when it exists, is at index `i - 1`.

**Handle the two ways a query can have no answer**

If `key not in self.ktv`, the key has never been stored, so `get` immediately returns the empty string. This explicit membership check has an extra benefit with `defaultdict`: it avoids creating an empty list merely because somebody queried a missing key.

Even when the key exists, the query timestamp may precede its first stored timestamp. In that situation binary search returns `i = 0`. There is no index before the boundary, so the conditional expression returns `''`:

`return tv[i - 1][1] if i else ''`.

When `i > 0`, `tv[i - 1]` is the latest eligible pair, and index `1` extracts its value.

**Trace several boundary positions**

Suppose the history for `"foo"` is

`[(1, "bar"), (4, "bar2"), (9, "bar3")]`.

For `get("foo", 0)`, the insertion boundary is zero because every stored timestamp is too large. The result is `""`.

For `get("foo", 1)`, the sentinel makes the pair at timestamp one fall before the boundary, so `i = 1` and the method returns `"bar"`.

For `get("foo", 3)`, only timestamp one is eligible. The same index `i = 1` returns `"bar"`.

For `get("foo", 4)`, both timestamps one and four are eligible, so `i = 2` and `tv[1][1]` is `"bar2"`.

For a query later than every stored timestamp, `i` equals the list length and `i - 1` selects the final, most recent value.

**Why the answer is always the required value**

Appending preserves the invariant that each key's list is strictly increasing by timestamp. Consider a query boundary `i`. By the behavior of `bisect_right` with the sentinel tuple, every entry before `i` has timestamp at most the query timestamp, and every entry at or after `i` has timestamp greater than it.

If `i = 0`, no eligible call to `set` exists, so the empty string is required. Otherwise, the entry at `i - 1` is eligible and is later than every preceding eligible entry. No later list entry can qualify. Its value is therefore associated with the largest permitted previous timestamp, exactly matching the contract.

**Why the implementation does not need to compare values conceptually**

The desired ordering is entirely by timestamp. The value component appears in the binary-search key only because the stored list contains two-element tuples and Python uses full tuple ordering. The `chr(127)` sentinel is a mechanical way to position the search tuple after an equal-timestamp stored pair under the problem's character constraints. It does not assign any semantic order or priority to values.

## Complexity detail

Let `Q` be the total number of operations and let `K` be the number of stored entries for the particular key being queried.

A `set` operation performs one dictionary lookup and appends one tuple. Under the usual average-case hash-table and dynamic-array assumptions, this is amortized `O(1)` after the time needed to hash the key and retain the supplied strings.

A `get` operation performs an average-case `O(1)` dictionary lookup and binary-searches a list of length `K`, taking `O(\log K)` comparisons. Because `K <= Q`, a sequence of `Q` operations has the stated worst-case aggregate bound `O(Q \log Q)` when queries repeatedly search a history that may contain `O(Q)` entries.

Every `set` call stores one timestamp–value tuple, and dictionary/list overhead is linear in the number of stored records and distinct keys. The structural space usage is `O(Q)`; including string contents, it is proportional to the total size of all stored keys and values. A query uses `O(1)` auxiliary space.

## Alternatives and edge cases

- **Reverse linear scan:** Starting at the newest pair and scanning backward is simple and can be fast for queries near the latest timestamp, but one query can inspect all `K` entries instead of `O(\log K)`.
- **Ordered map per key:** A balanced search tree can find a predecessor and can support out-of-order insertions, but this problem's increasing timestamps make append-only arrays smaller and faster.
- **Two parallel arrays:** Store timestamps and values in separate lists and binary-search only the timestamp list. This avoids the sentinel detail but requires maintaining two synchronized structures.
- **Dictionary keyed by exact timestamp:** It makes exact-time lookup easy but does not efficiently find the greatest smaller timestamp, which is the central requirement.
- **Array indexed by timestamp:** Timestamps may reach `10^7` and keys may be numerous, so allocating every possible time slot would waste enormous space on unstored times.
- **Missing key:** The method returns `""` without accidentally inserting the key into the `defaultdict`.
- **Query before the first assignment:** Binary search returns zero, and the conditional avoids using Python's negative index `-1`, which would otherwise incorrectly return the newest value.
- **Exact timestamp:** The sentinel is greater than every legal stored value, so an exact match is included rather than skipped.
- **Query after the latest assignment:** The insertion index becomes `len(tv)`, making `i - 1` the final entry.
- **Repeated assignment timestamp:** The contract forbids it. The sentinel reasoning relies only on legal input, while strictly increasing timestamps also preserve an unambiguous chronological history.
- **Independent keys:** Each key owns a different list, so interleaved calls to `set` do not disturb the sorted order within any key.
- **Sentinel character assumption:** `chr(127)` is safe because legal values contain only lowercase English letters and digits. With unrestricted Unicode strings, a timestamp-only search or a custom key array would be more robust.
