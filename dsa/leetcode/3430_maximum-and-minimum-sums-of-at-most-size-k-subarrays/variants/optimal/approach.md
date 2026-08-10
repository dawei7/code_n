## General

**Group all eligible subarrays by their ending index.** When processing `end_idx`, the source needs the sum of maxima and the sum of minima over every subarray ending there with length at most $k$. If those two sums are known, adding them to the global answer counts every eligible subarray exactly once, at its unique right endpoint.

The earliest allowed start is

`start_idx = max(0, end_idx - k + 1)`.

Two monotonic deques compress extreme values for all such starting positions:

- `max_stack` groups starts whose subarray currently has the same maximum;
- `min_stack` groups starts whose subarray currently has the same minimum.

An entry is `[idx, num, shares]`. `shares` is the number of active starting positions whose extreme is `num`. `subarrays_max_sum` is the sum of all maximum values across active starts; `subarrays_min_sum` is the analogous minimum sum.

**Remove the start that just became too old.** Once `start_idx` advances above zero, exactly one formerly active start falls outside the length limit. The deque front contains the group owning the oldest start. Decreasing its `shares` by one and subtracting its `num` from the running extreme sum removes that one subarray contribution.

If the front entry's `idx` lies before the new `start_idx`, its represented extreme element has left the allowed window and its remaining share count is exhausted, so the entry is popped. The same operation is performed independently for maxima and minima.

This front update happens before adding the current element because the stored shares still describe subarrays ending at the previous index. It narrows their starts to exactly those that may be extended into length-at-most-$k$ subarrays ending now.

**Extend all starts with a new maximum candidate.** The singleton subarray containing only `num` creates one new share and contributes `num` to `subarrays_max_sum`.

For existing groups, if a previous maximum is less than or equal to `num`, extending those subarrays makes `num` their new maximum. The source pops each such back entry, transfers its `prev_shares` into `max_shares`, and adjusts the running sum by

`(num - prev_num) * prev_shares`.

That expression replaces `prev_num` by `num` for every transferred starting position. Once the back value is greater than `num`, earlier groups also have greater maxima and remain unchanged. Appending `[end_idx, num, max_shares]` records all starts now owned by the new value.

The minimum deque is symmetric. A previous minimum greater than or equal to `num` becomes `num` after extension, so its shares transfer and the sum changes by

`(num - prev_num) * prev_shares`.

This quantity may be negative, correctly reducing the sum of minima.

**Understand a small maximum example.** Suppose active subarrays ending at the previous position have maxima $3$ for one start and $1$ for one later start. Appending $2$ leaves the first maximum at $3$, changes the second from $1$ to $2$, and creates singleton maximum $2$. The maximum sum changes from $4$ to $3+2+2=7$. The max deque pops the $1$ group, transfers its share to the new $2$ entry, and adds exactly $(2-1)\cdot1$ after first adding the singleton $2$.

**Tie handling keeps the deques compact.** Maximum entries are popped with `<=` and minimum entries with `>=`. Equal extremes are assigned to the newer index. Their numeric contribution does not change, but merging equal groups avoids redundant entries and makes later front expiration unambiguous.

After both insertions, `subarrays_max_sum + subarrays_min_sum` is exactly the requested contribution of every eligible subarray ending at `end_idx`. The source adds it to `subarrays_max_min_sum`.

**Why the invariants prove correctness.** Each active start belongs to exactly one share group in each deque. Back merging applies the mathematical rule

$$
\max(\textit{old maximum},x)
$$

or

$$
\min(\textit{old minimum},x)
$$

to every extended subarray, while the singleton creates the new start. Front eviction removes exactly the start whose length would exceed $k$. Thus the running sums are correct for the current endpoint. Summing them over all endpoints counts precisely all non-empty subarrays of length at most $k$.

## Complexity detail

Every index is appended once to each deque. An entry can be popped from the back once during extreme merging or from the front once when it expires. Share decrements occur once per endpoint after the window reaches length $k$. All deque-end operations and arithmetic are constant time, so total time is $O(n)$ despite the inner `while` loops.

At most $k$ active starting positions are represented, so each deque actually needs $O(k)$ entries; the manifest's $O(n)$ space is a valid looser bound because $k\le n$. The running sums and indices use $O(1)$ additional space.

## Alternatives and edge cases

- **Enumerate all bounded subarrays:** There can be $O(nk)$ of them, and scanning each for extrema is even slower. Share groups aggregate their contributions.
- **One monotonic deque per single window:** Standard sliding-window extrema find only the maximum or minimum of a fixed-length window, not the sum of extrema over every suffix ending at a point. Shares are the extra ingredient.
- **Contribution boundaries per element:** Previous/next greater and smaller boundaries can also count bounded-length subarrays, but the at-most-$k$ cap makes the combinatorics more involved.
- **\(k=1\):** Only singleton subarrays remain. Each element contributes itself as both maximum and minimum, so the result is twice the array sum.
- **\(k=n\):** No start is evicted, and the method sums extremes over all subarrays.
- **Equal elements:** Non-strict pop comparisons merge equal groups. Every subarray still receives the correct equal extreme once.
- **Negative values:** Maximum and minimum sums may be negative. The arithmetic uses actual values and requires no nonnegative assumption.
- **Front share decrement:** Only one oldest start expires per new endpoint, so decrementing exactly one share is correct.
- **Back-pop amortization:** A single new extreme may pop many entries, but each entry can be popped only once over the entire traversal.
- **No modulo:** The task requests the exact integer sum. Python integers prevent overflow for the stated bounds.
