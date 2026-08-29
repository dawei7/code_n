## General

There are $n+1$ division indexes, including positions before the first element and after the last. Recomputing left zeros and right ones separately for every division would repeat most work. Instead, the exact solution starts at division zero and updates the score when one element crosses from the right side to the left.

**Initialize the division before the array**

At index zero, the left part is empty, so `l0 = 0`. The right part is the entire binary array, and `sum(nums)` counts its ones, so `r1 = sum(nums)`.

The score is `l0 + r1 = r1`. The source initializes `mx = r1` and `ans = [0]`, meaning division zero is the best and only division examined so far.

Including this initial state before entering the loop is essential because index zero can be the unique answer, as in an all-ones array.

**Move one element across each boundary**

The loop `for i, x in enumerate(nums, 1)` processes values in original order while making `i` range from one through $n$. After processing `x = nums[i-1]`, the maintained counts describe division index `i`.

When `x == 0`, moving it to the left increases the number of left zeros by one. When `x == 1`, it contributes no left zero. The expression `x ^ 1` flips a binary bit, producing one for zero and zero for one. Thus `l0 += x ^ 1` performs exactly the correct update.

The element leaves the right side. If it is one, right ones decrease by one; if it is zero, they stay unchanged. Because `x` itself is zero or one, `r1 -= x` handles both cases.

The new score is `t = l0 + r1`.

**Keep every index tied for the maximum**

If `t == mx`, the current division ties the best score and `ans.append(i)` preserves it alongside earlier winners.

If `t > mx`, every previously stored division has a smaller score. The code sets `mx = t` and replaces the result with `ans = [i]`.

If `t < mx`, neither branch runs and the result remains unchanged.

This three-way behavior ensures that, after each iteration, `mx` is the greatest score among divisions zero through `i` and `ans` contains exactly all indexes in that processed prefix with score `mx`.

**Trace the score change directly**

Moving a zero from right to left increases the score by one: it was not counted as a right one and becomes a counted left zero. Moving a one decreases the score by one: it was counted on the right and becomes an uncounted left one.

So the division scores form a walk that starts at the total number of ones, moves up for each zero, and down for each one. The maintained `l0 + r1` computes the same walk using the two quantities named in the problem.

For `[0,0,1,0]`, index-zero score is one. Moving the first zero gives two, the second gives three, the one lowers it to two, and the final zero raises it to three. The maximum occurs at indexes two and four, both of which remain in `ans`.

**Why the invariant proves correctness**

Before the loop, counts and answer are correct for division zero. On each iteration, exactly one element changes sides, and the two constant-time updates produce the exact counts for the next division. The comparison logic then makes `ans` exactly the maximizers among all divisions seen so far.

After the final element crosses, index $n$ has been evaluated as well. Therefore every legal division index from zero through $n$ was considered once, and the returned list contains all and only global maximum-score indexes.

## Complexity detail

Let $n$ be the array length. `sum(nums)` performs one $O(n)$ scan. The loop performs a second $O(n)$ scan with constant work per element. Total time is $O(n)$.

The output list can contain up to $n+1$ indexes, so counting required output storage gives $O(n)$ space, matching the manifest. Excluding the output, the algorithm stores only `l0`, `r1`, `mx`, `i`, `x`, and `t`, which is $O(1)$ auxiliary space.

The input array is not modified.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Precompute left-zero and right-one counts for every boundary, then compare scores. This is linear time but uses $O(n)$ extra arrays unnecessarily.
- **Recount each division:** Counting both sides independently at all $n+1$ indexes takes $O(n^2)$ time.
- **Track score alone:** Start with total ones, add one for each zero, and subtract one for each one. This is equivalent and uses slightly fewer named counts, but the exact source keeps `l0` and `r1`.
- **All zeros:** Every move raises the score, so only division $n$ is returned.
- **All ones:** Every move lowers the score, so only division zero is returned.
- **One zero:** Scores are zero at division zero and one at division one, so the result is `[1]`.
- **One one:** Scores are one at division zero and zero at division one, so the result is `[0]`.
- **Ties separated by lower scores:** The equality branch appends a later index even if intermediate divisions were worse.
- **New maximum:** Replacing `ans` discards all indexes tied only for the old, now inferior maximum.
- **Division zero:** It is initialized explicitly because the loop begins with division one.
- **Division n:** `enumerate(..., 1)` reaches `i = n` after the last element moves left.
- **Binary guarantee:** `x ^ 1` behaves as a zero indicator only because `x` is guaranteed to be zero or one.
- **Any output order:** The source returns ascending indexes because it scans left to right, which is accepted even though sorting is not required.
- **Output-size bound:** In some alternating arrays, many divisions may tie, so result storage can genuinely be linear.
- **Input preservation:** Counts are updated separately; `nums` retains all original bits.
