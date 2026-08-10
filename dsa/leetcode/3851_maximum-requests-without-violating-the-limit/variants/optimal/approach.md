## General

**Separate users before optimizing**

A violation is defined for one user at a time. Keeping or dropping a request from user `u` cannot change whether user `v` violates the limit when `u\ne v`. Therefore the global maximum is the sum of the independent maxima for each user's timeline.

The source first builds `g`, a mapping from each user identifier to a list of that user's request times. It then processes every list separately. This decomposition is not merely convenient: if an optimal retained subset is chosen for each user, their union is globally valid, and no global solution can retain more than the sum of those per-user optima.

**Turn the interval rule into a condition on sorted times**

For one user, sort the request records by time. Equal times remain separate records and must all be considered. Suppose the retained times in nondecreasing order are

$$
a_0\le a_1\le\cdots.
$$

The user is valid exactly when no `k+1` retained requests fit into an inclusive interval of span `window`. Equivalently, whenever both endpoints exist,

$$
a_{i+k}-a_i>\texttt{window}.
$$

The inequality is strict. If the difference equals `window`, the inclusive interval `[a_i,a_i+\texttt{window}]` contains both endpoints and all `k-1` retained requests between them, for a total of `k+1`. Such a selection violates the rule.

Sorting makes it possible to decide requests chronologically. When considering a time `t`, only already-retained requests with `t-old\le window` can share an inclusive length-`window` interval with `t`. Any older request satisfying `t-old>window` is too far away to participate in a violation involving `t` or any later time.

**What the deque represents**

For each user's sorted list, `kept` stores the retained request times that are still active relative to the current time. Before deciding `t`, the loop removes values from the front while

`t - kept[0] > window`.

Because the times are sorted, the oldest values are at the front. Once one is more than `window` behind `t`, it will be even farther behind every future request, so discarding it from the deque is safe. It remains part of the total retained answer; it simply no longer matters for future window-capacity checks.

After eviction, every time in `kept` lies in `[t-window,t]`. If `len(kept) < k`, retaining `t` makes the active count at most `k`, so the source appends it. If `len(kept) == k`, appending `t` would place `k+1` retained requests in the inclusive interval `[t-window,t]`. The source instead drops the current request by decrementing `ans`.

The deque can never contain more than `k` elements. It contains only requests that the algorithm previously retained, not requests that were dropped. This distinction matters: a dropped record imposes no future restriction.

**Why keeping the earliest feasible requests is optimal**

The greedy method retains a request whenever doing so is currently legal and, when the active window is full, drops the new request rather than replacing an older retained one. The reason is that earlier retained times are at least as useful as later replacements for maximizing the number of records over the entire sorted timeline.

For a precise argument, number the requests selected by the greedy algorithm for one user as `g_1,g_2,\ldots`. The first `k` available records are always feasible, so they are the earliest possible first `k` selected records. For every later selected position `j`, feasibility is equivalent to

$$
g_j-g_{j-k}>\texttt{window}.
$$

The scan chooses `g_j` as the earliest remaining request time that satisfies that condition.

Now compare the greedy selections with any feasible selection `b_1,b_2,\ldots` from the same sorted records. Inductively assume the greedy's earlier selected records are no later than the corresponding records of the other selection. For `j>k`, feasibility of the other selection gives

$$
b_j-b_{j-k}>\texttt{window}.
$$

Since `g_{j-k}\le b_{j-k}`, `b_j` is also more than `window` after `g_{j-k}`. Thus by the time the scan reaches the record used as `b_j`, it is a feasible candidate for the greedy algorithm's `j`-th selection. The greedy chooses the earliest such candidate, so `g_j\le b_j`. This extends the componentwise-earliest property to every selected position.

If some feasible strategy could retain more requests than the greedy algorithm, its next selected record after all greedy selections would also have been feasible for the greedy scan by the same dominance reasoning. But the scan examined every record and did not select another one, a contradiction. Therefore the greedy count is maximum for that user.

Dropping the newest request when the active deque is full also follows intuitively from this dominance. Replacing an earlier active time with the current later time cannot allow an additional selection earlier in the already-processed prefix, and it shifts one selected position later. An earlier componentwise selection reaches its expiration threshold no later and never reduces future opportunities.

**How the total answer is accumulated**

The source initializes `ans` to the total number of input records. Every time a full active deque forces a request to be dropped, it subtracts one. Requests removed from the deque because they became old are not subtracted: they were validly retained and still count in the result. After all user groups have been processed, `ans` is exactly the number of records the per-user greedy selections retain.

For the inclusive-boundary example with times `[1,2]`, `k=1`, and `window=1`, the time `1` is retained. At time `2`, `2-1=1` is not greater than the window, so the old request remains active. The deque already has one record, and the source drops time `2`. This correctly recognizes that `[1,2]` contains both endpoints.

The exact source depends on `defaultdict` and `deque` from `collections`. The surrounding execution environment must make those names available.

## Complexity detail

Let `N` be the total number of request records, and let user `u` have `N_u` records. Grouping takes `O(N)` time. Sorting every user's list costs

$$
\sum_u O(N_u\log N_u)\le O(N\log N).
$$

During the chronological scans, every retained timestamp is appended to a deque once and removed from its front at most once. Every dropped timestamp receives one constant-time capacity check. The total deque work across all users is therefore `O(N)`. Sorting dominates, giving `O(N\log N)` overall time.

The grouping lists collectively hold `N` timestamps, so they use `O(N)` space. A user's deque holds at most `k` active retained timestamps, and no more than that user's list length; its storage is `O(\min(k,N_u))`. Since groups are processed one at a time, the maximum deque storage is `O(N)` and does not change the overall `O(N)` bound. Python's sorting also uses implementation-dependent temporary memory bounded by `O(N)` across the largest group. The source therefore matches the manifest's `O(N\log N)` time and `O(N)` space.

If all records already arrived grouped and sorted by user and time, the greedy scanning portion would be linear. The protected method accepts arbitrary input order, so its explicit per-user sorting is necessary and its worst-case comparison-sorting cost is unavoidable for this implementation.

## Alternatives and edge cases

- **Exhaustive subset search:** Trying every retained subset directly expresses the objective but needs `2^N` possibilities. Grouping, sorting, and exploiting the sliding-window structure reduce the problem to a greedy scan.
- **Dynamic programming over each timeline:** A DP could compute how many requests can be retained up to each index, but the fixed-capacity interval condition admits the stronger componentwise-earliest greedy rule, making a table unnecessary.
- **Replace the oldest active request:** When the deque is full, replacing its oldest time with the current later time does not improve the maximum cardinality. It moves a selected position later and can only delay, not advance, when that selected slot stops conflicting with future records.
- **Globally sort all records:** Sorting by `(user,time)` and resetting a deque when the user changes can achieve the same asymptotic bounds. The source instead groups first, which makes the independence between users explicit.
- **A heap instead of a deque:** A heap can remove minimum times, but sorted processing means active times already enter in nondecreasing order. A deque provides `O(1)` front eviction with less machinery.
- **Inclusive endpoint:** Evict only when `t-old>window`. Using `>=` would incorrectly treat two requests exactly `window` apart as unable to share an interval, even though both belong to `[old,old+window]`.
- **Duplicate timestamps:** Distinct records at the same time all lie in the same window. The deque stores duplicate values separately, so it retains at most `k` of them when no other active records consume capacity.
- **One user versus many users:** A busy user's drops never consume capacity for another user. Separate deques are logically required, whether implemented simultaneously or one group at a time.
- **`k` at least the size of a user group:** That user can retain every request. The deque never reaches capacity before all records are accepted, even if all times are identical.
- **Very small window:** The constraints make `window` positive, but the same rule would work for zero: only equal timestamps would coexist in a zero-span inclusive interval.
- **Old deque entries:** Removing an expired entry does not mean dropping the corresponding request from the answer. It was already accepted; removal only forgets it because it can no longer conflict with the present or future.
- **Arbitrary input order:** Running the deque logic without sorting would be invalid because an apparently expired request could be followed by an earlier timestamp. Per-user sorting establishes the chronological monotonicity on which every eviction relies.
