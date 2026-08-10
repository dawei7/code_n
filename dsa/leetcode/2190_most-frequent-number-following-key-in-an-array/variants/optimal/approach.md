## General

Only adjacent positions matter. For every occurrence of `key` that is not the final array element, the value immediately after it contributes one vote to that follower value.

The exact solution walks all adjacent pairs once, maintains a frequency counter for qualifying second values, and updates the best follower as soon as its count becomes the largest seen.

**Generate adjacent pairs directly**

`pairwise(nums)` yields

`(nums[0], nums[1])`, `(nums[1], nums[2])`, and so on through the final adjacent pair.

Each yielded pair is assigned to `a, b`. Here `a` represents `nums[i]` and `b` represents `nums[i + 1]` for one index `i`.

This avoids manual index arithmetic while covering exactly the allowed range from zero through `len(nums) - 2`. The last array element appears as a follower but never as the first component of a nonexistent pair beyond the array.

**Filter on the key position**

The code enters its counting block only when `a == key`. In that case, `b` is precisely a target that immediately follows an occurrence of `key`, so `cnt[b]` increases by one.

If `a` is not the key, the adjacent value `b` is irrelevant for this problem and no counter changes.

Notice that `b` may itself equal `key`. Consecutive copies of the key are valid: in `[2,2,2]`, the second two follows the first, and the third follows the second, so target two receives two votes.

**Maintain the best count online**

`mx` stores the greatest follower frequency observed so far, and `ans` stores the follower that achieved it.

After incrementing `cnt[b]`, the code compares it with `mx`. If it is strictly larger, both `mx` and `ans` are updated. If it merely ties the current maximum, the stored answer remains unchanged.

The contract guarantees that the final maximum target is unique. Temporary ties during the scan therefore do not create ambiguity in the returned result. The eventual unique winner must at some point raise its count above every competitor and trigger an update.

**Why updating only the changed target is enough**

One loop iteration changes only `cnt[b]`. Every other follower's frequency remains exactly what it was, so none of them can newly exceed `mx` at this moment.

It is sufficient to compare the updated `b` with the existing maximum rather than rescan the entire Counter after every pair. This keeps the pass linear.

**Why every qualifying occurrence contributes once**

For any index `i` in the problem's range, `pairwise` yields exactly one pair whose first element is `nums[i]` and second is `nums[i + 1]`. If the first equals `key`, the corresponding target counter increases once.

No other generated pair represents that same index `i`, so the occurrence is not double-counted. If the first does not equal `key`, the occurrence should not contribute and is skipped.

After the scan, `cnt[target]` therefore equals the definition's number of indices for every follower that ever occurs after the key.

**Why `ans` ends at the unique maximum**

Initially no follower has been seen, and `mx = 0`. The first qualifying follower reaches count one, exceeds zero, and becomes `ans`.

Whenever a follower establishes a new strictly greatest observed frequency, the update records it. At the end, let $w$ be the unique target with maximum final count. When $w$ reaches that final count, it is strictly above every other target's final count and hence above every count observed for them. The conditional must set `ans = w`. No later target can surpass it, so the returned value is $w$.

For `[1,100,200,1,100]` with key one, the adjacent pairs beginning with one are `(1,100)` twice. Counter entry 100 reaches two and remains the unique maximum.

**Understand the initial zero answer**

`ans` begins at zero even though input values are positive. Under valid test generation, at least one counted follower exists and replaces it. A key occurrence at the final position alone cannot define the promised unique target maximum; the problem's answer guarantee rules out a case with no qualifying follower.

## Complexity detail

Let $n$ be the array length. `pairwise` produces $n-1$ adjacent pairs, and each iteration performs expected constant-time Counter operations. Total time is $O(n)$.

The counter stores one entry per distinct value that follows `key`. Given the fixed value range one through 1000, this is at most 1000 entries and is $O(1)$ with respect to $n$, matching the manifest. If values were unbounded, the more general auxiliary-space bound would be $O(u)$ for $u$ distinct followers.

`pairwise` is lazy and keeps only iterator state rather than materializing all pairs.

## Alternatives and edge cases

- **Count then call `most_common`:** First build all follower counts, then select the maximum. It is correct but performs a separate pass over distinct targets.
- **Fixed frequency array:** Values are at most 1000, so a 1001-entry list can replace the Counter and make the constant-space interpretation explicit.
- **Manual index loop:** Iterate `i` through `range(len(nums) - 1)` and inspect `nums[i + 1]`. It has identical behavior.
- **Consecutive keys:** The key itself is a valid target when one key immediately follows another.
- **Key at the final index:** That occurrence creates no pair because nothing follows it.
- **Several key occurrences:** Each immediate follower occurrence contributes independently, even when positions share the same target value.
- **Temporary tie:** Strict comparison keeps the earlier leader, but the guaranteed unique final maximum eventually overtakes all others.
- **Unique final winner:** No explicit tie-breaking rule is needed.
- **Minimum array length two:** There is one adjacent pair, which is counted if its first value is the key.
- **Values unrelated to key:** Followers after non-key values never enter the Counter.
- **Lazy adjacency:** `pairwise` avoids an $O(n)$ list of tuples.
- **Input preservation:** The array and key are only read.
- **Fixed-domain space:** The Counter is logically bounded by 1000 possible positive values under the contract.
