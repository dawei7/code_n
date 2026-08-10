## General

**Use the complete polygon inequality**

For positive side lengths sorted as $a_1 \le a_2 \le \cdots \le a_k$, they can form a nondegenerate polygon exactly when the longest side is strictly smaller than the sum of all other sides:

$$
a_k < a_1+a_2+\cdots+a_{k-1}.
$$

The implementation sorts `nums` and builds prefix sums `s` with `s[0] = 0`. Thus `s[k]` is the sum of the first $k$ sorted values. For the prefix of length $k$, `nums[k - 1]` is its longest side and `s[k - 1]` is the sum of its other sides. The exact validity check is therefore

`s[k - 1] > nums[k - 1]`.

The loop begins at `k = 3` because a polygon needs at least three sides.

**Why only sorted prefixes need to be considered**

Suppose a candidate polygon’s longest chosen side is `nums[t]`. Every positive value before it that was not selected can be added as another side. Adding a positive side increases the perimeter and increases the sum on the “other sides” side of the inequality, while the longest side does not increase. Therefore, adding an omitted smaller or equal value cannot destroy validity and strictly improves the perimeter.

Consequently, for a fixed longest chosen side, the best candidate includes every sorted value through that side: it is a prefix. There is no reason to search arbitrary subsets. Any optimal polygon can be expanded into the complete prefix ending at its longest side, unless it already is that prefix.

This positive-value argument is essential. If zero or negative side lengths were allowed, adding every earlier number would not necessarily increase the perimeter or preserve the geometric meaning. The source constraints guarantee positive integers.

**Evaluate every possible longest side**

For each prefix length $k$ from three through $N$, the implementation tests the inequality. When it holds, `s[k]` is the perimeter of a valid polygon and is compared with `ans`.

The prefix length can alternate between invalid and valid as larger sides are considered. For example, a sudden very large value may exceed the sum accumulated before it. Additional later positive values might eventually make another prefix valid under a different longest side. Scanning all $k$ values is therefore the straightforward complete method.

`ans` begins at `-1`, the required result when no valid polygon exists. The code uses `max(ans, s[k])` rather than assuming the most recently seen valid prefix is always the answer. Since all values are positive, prefix sums do increase, so a later valid prefix has a larger perimeter, but the explicit maximum makes the intended optimization unambiguous.

For `nums = [1, 12, 1, 2, 5, 50, 3]`, sorting gives `[1, 1, 2, 3, 5, 12, 50]`. Prefixes through five satisfy the polygon condition when appropriate, and the length-five prefix has perimeter twelve because `1 + 1 + 2 + 3 > 5`. Adding side twelve fails because the preceding sum is exactly twelve, not strictly greater. Side fifty also fails. The best stored perimeter remains twelve.

**Why strict inequality matters**

If the longest side equals the sum of all other sides, the segments can flatten into a line but cannot form the required nondegenerate closed polygon. The solution uses `>` for the previous-side sum, not `>=`. In the three-side case this is the familiar strict triangle inequality.


Every time the loop stores `s[k]`, the sorted prefix has at least three positive sides and passes the necessary-and-sufficient longest-side condition, so the stored perimeter is achievable.

Conversely, take any achievable polygon formed from the input and let its longest selected value occur at sorted index $t$. Add every unselected value at an index at most $t$. Positivity preserves the inequality and increases or preserves the set’s perimeter, yielding the complete prefix through $t$. The loop examines that prefix and records its perimeter. Therefore, no feasible polygon can have a perimeter greater than all candidates considered by the loop. Taking their maximum returns the optimum, while leaving `ans = -1` correctly represents the absence of any candidate.

**Exact implementation behavior**

`nums.sort()` changes the input list in place. `accumulate(nums, initial=0)` is converted to a full list, providing constant-time access to every prefix sum but allocating $N+1$ integers. Python integers safely hold the possible perimeter beyond 32-bit range.

## Complexity detail

Let $N$ be the number of side lengths. Sorting costs $O(N\log N)$ time. Constructing the prefix sums and scanning all candidate prefix lengths each cost $O(N)$, so the total time is $O(N\log N)$.

The prefix-sum list uses $O(N)$ auxiliary space. Python’s sorting implementation may also require $O(N)$ temporary space in the worst case, so the overall auxiliary bound is $O(N)$. The scalar answer and loop index are constant-size.

## Alternatives and edge cases

- **Try every subset:** There are exponentially many subsets. Positivity proves that the best candidate for each longest side is its complete sorted prefix.
- **Running sum without a prefix list:** The editorial-style implementation can keep one scalar sum and achieve the same $O(N\log N)$ time with less explicit storage, but the exact solution materializes `s`.
- **Only test triples:** A valid polygon may need four or more smaller sides to outweigh a long side, so triangle-only logic misses answers such as the five-side optimum in the example.
- **Equality:** `sum(other sides) == longest` is degenerate and must be rejected; the comparison is strict.
- **Exactly three inputs:** The single prefix is tested as an ordinary triangle.
- **No valid prefix:** `ans` remains `-1`, matching the required failure value.
- **Duplicate lengths:** They are separate usable sides and all contribute to the prefix sum.
- **Large sums:** The perimeter can exceed 32-bit integer range; Python’s unbounded integers avoid overflow.
- **Input mutation:** The array remains sorted after the call.
