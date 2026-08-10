## General

**Reachability is determined by a remainder class**

Seeding the machine with value `v` destroys targets

$$
v,\ v+\texttt{space},\ v+2\cdot\texttt{space},\ldots
$$

Every such number has the same remainder `v % space`. Conversely, two targets with the same remainder differ by an integer multiple of `space`.

There is one directional detail: the multiplier `c` must be non-negative, so a seed can reach same-remainder targets that are at least the seed, but not smaller ones.

For any remainder group, choosing its minimum target as the seed destroys every target in that group. Every other group member equals that minimum plus a non-negative multiple of `space`. No seed can destroy targets from a different remainder group.

Therefore the maximum number destroyable is the size of the largest remainder group, and the best seed for a group is its smallest value.

**Count every remainder**

The expression

`Counter(v % space for v in nums)`

builds a frequency map from remainder to number of targets in that class. Duplicate target values count separately because `nums` represents targets, and seeding their value destroys every occurrence.

The second loop considers every original value `v`. It retrieves its group size as `t = cnt[v % space]`.

The state `mx` is the largest group frequency seen among candidates so far, and `ans` is the smallest target value seen with that frequency. Both begin at zero. Since all target values and frequencies are positive, the first iteration necessarily updates them.

**Apply the primary and secondary ordering**

The condition

`t > mx or (t == mx and v < ans)`

first prefers a larger destroyed-target count. On a tie, it prefers the smaller seed value required by the statement.

Although `t` is the entire remainder-group size even when the current `v` is not that group's minimum and could not destroy smaller group members, the final selection remains correct. For every group, the loop eventually visits its minimum value. That minimum has the same count `t` and replaces any larger value from the group through the tie rule.

After the complete scan, `ans` is thus the minimum member of one of the maximum-frequency remainder groups, and it truly destroys all `mx` targets in that group.

**Trace the first example**

For `nums=[3,7,8,1,1,5]` and `space=2`:

- Odd targets 3, 7, 1, 1, and 5 share remainder 1, giving frequency 5.
- Target 8 has remainder 0, giving frequency 1.

The maximum class is the odd group. Its smallest target is 1, and seeding 1 reaches 1, 3, 5, 7, and all later odd positions on the number line. Both occurrences of target 1 are destroyed, so the count is five.

For `[1,3,5,2,4,6]` with space 2, both remainder groups have size three. Their minimum candidate seeds are 1 and 2, so the global tie-break returns 1.

When `space` exceeds every difference, most remainders can be unique. If every group size is one, the second rule returns the minimum value in all of `nums`.


Any seed `v` can destroy only targets congruent to it modulo `space`, so its destruction count is no greater than the size of that remainder group and hence no greater than the maximum counter frequency.

For a maximum-frequency group, let `m` be its minimum target. Every group member is `m+c*space` for some non-negative integer `c`, so seed `m` destroys the entire group and attains that upper bound.

The scan selects the smallest minimum among all groups attaining the bound because every member is visited and equal frequencies are resolved by smaller value. The returned seed is therefore both maximally destructive and minimal among such seeds.

## Complexity detail

Let $n$ be the number of targets. Counter construction visits every value once and takes expected $O(n)$ time. The selection loop is another $O(n)$ expected-time pass with hash lookups, so total expected time is $O(n)$.

There can be at most one stored count per distinct remainder, bounded by both $n$ and `space`. Counter space is $O(\min(n,\texttt{space}))$. The remaining scalar state is $O(1)$.

The input array is not sorted or modified. Modulo and integer comparisons are constant-time for the bounded values under the standard model.

## Alternatives and edge cases

- **Sort by remainder then value:** Sorting can group congruent targets and reveal each group's minimum, but costs $O(n\log n)$ time when hashing gives expected linear time.
- **Array of remainder counts:** If `space` is small, a length-`space` array avoids hashing. With space up to $10^9$, allocating it can be impossible.
- **Count by exact value:** Exact duplicates alone are insufficient because distinct values separated by multiples of `space` are mutually reachable from their group minimum.
- **Duplicate minimum targets:** They all count as separate destroyed targets, and the same seed value remains valid.
- **Several largest remainder groups:** The scan returns the smallest target among their minima.
- **Seed larger than its group minimum:** It cannot reach smaller same-remainder targets, which is why the tie rule must eventually select the minimum group member.
- **`space=1`:** Every target shares remainder zero; the minimum target destroys all of them.
- **Space larger than target range:** Remainder groups often contain one value, so the smallest target wins.
- **Unsorted input:** Counter frequencies and the explicit numeric tie-break do not depend on encounter order.
- **Positive targets:** Initial `ans=0` is safe because the first positive candidate always replaces it through `t>mx`.
