## General

**Separate jump destination computation from reachability**

For each index, an odd jump has one deterministic destination and an even jump has another, or no legal destination.

The solution first computes these destinations using an ordered map, then uses memoized DFS to determine which starts reach the final index.

Table `g[i][1]` stores odd-jump destination. `g[i][0]` stores even-jump destination.

**Process indices from right to left**

A jump must go to a larger index. When processing `i` from right to left, `SortedDict sd` contains exactly values at future indices.

Its keys are array values in sorted order, and each key maps to the smallest future index having that value.

**Odd-jump destination**

Odd jumps need the smallest future value greater than or equal to `arr[i]`.

`sd.bisect_left(arr[i])` finds the first key meeting that lower bound. If it exists, the corresponding mapped index becomes `g[i][1]`; otherwise destination is minus one.

**Even-jump destination**

Even jumps need the largest future value less than or equal to `arr[i]`.

`sd.bisect_right(arr[i]) - 1` finds the last key meeting that upper bound. If its position is nonnegative, its mapped index becomes `g[i][0]`; otherwise minus one.

**Why duplicate values choose the smallest index**

After destinations are queried, code assigns `sd[arr[i]] = i`.

Scanning right to left means each new index for a repeated value is smaller than the previously stored future index. Overwriting therefore keeps the smallest index among positions available to any still-earlier source.

This exactly enforces the tie rule.

**Memoized reachability**

`dfs(i, k)` asks whether index `i` can reach the end when next jump type is `k`, where one means odd and zero even.

At final index, return true because zero further jumps are allowed.

If `g[i][k] == -1`, required next jump does not exist, so return false.

Otherwise, jump to that destination and toggle parity with `k ^ 1`.

Caching avoids recomputing the same index-parity state from multiple starts.

**Why start parity is odd**

Every starting sequence begins with jump number one, which is odd. The answer sums `dfs(i, 1)` for all indices.

The final index returns true immediately and is always a good start.

**Trace concept**

For duplicate future values, ordered-map lookup selects their shared value according to odd/even rule, and stored map value supplies the smallest eligible index.

After this preprocessing, DFS no longer compares array values. It follows fixed directed edges whose parity alternates.


The ordered-map searches implement the exact extremal value conditions. Right-to-left overwrite implements the exact smallest-index tie condition. Thus `g` contains every required legal destination.

DFS follows precisely the unique jump sequence from each state. Its base and missing-edge cases match reachability. Induction along strictly increasing indices proves each Boolean result.

Summing odd-start states therefore counts exactly good indices.

**Why there are no cycles**

Every destination index is greater than its source. Recursive paths move strictly right and must end at the final index or a missing jump.

This acyclic structure guarantees termination independently of caching.

**Keys and values have separate roles**

Each ordered-map key is an array value used for the smallest-greater or largest-smaller search. Its associated map value is the actual index destination.

This implements both rule levels: optimize destination value first, then use smallest index among ties.

**Why insertion follows querying**

Index `i` cannot jump to itself because destinations must be larger. Both searches occur before inserting `arr[i]`.

Afterward, insertion makes `i` available to every earlier index, for which it is a legal forward destination.

**How caching shares suffix work**

Different starts can converge on the same index with the same next parity. Their remaining jump sequence is identical.

Caching one Boolean per `(index, parity)` prevents repeated traversal and limits reachability computation to at most `2N` states.

## Complexity detail

Let `N` be array length.

Each index performs constant many `SortedDict` searches and one update, each `O(log N)`, so preprocessing is `O(N log N)`.

There are at most `2N` DFS states, each constant work after preprocessing, adding `O(N)` time. Total is `O(N log N)`.

Destination table, ordered map, cache, and recursion use `O(N)` space. A path may have `O(N)` recursive depth.

## Alternatives and edge cases

- **Monotonic-stack preprocessing:** Sort indices by values in two orders to compute next destinations in `O(N log N)` without a tree map.
- **Scan all future indices:** Direct but `O(N^2)`.
- **Iterative DP right to left:** Once destinations are known, compute odd/even reachability without recursion.
- **Final index:** Always good with zero jumps.
- **No legal odd jump:** A nonfinal start is immediately bad.
- **Equal target values:** Smallest future index must win.
- **Alternating parity:** Toggle with `k ^ 1` after every jump.
- **Repeated values:** Map overwrite during reverse scan enforces tie-breaking.
- **Strictly increasing indices:** Prevent cycles.
- **Deep path:** Recursive implementation may approach Python's recursion limit.
