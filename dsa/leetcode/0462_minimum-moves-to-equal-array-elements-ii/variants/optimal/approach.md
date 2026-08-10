## General

If every value must become a common target `k`, changing `nums[i]` to `k` costs exactly `abs(nums[i] - k)` moves: each move closes the distance by one. For a chosen target, the total cost is therefore

$$
F(k)=\sum_{i=0}^{n-1}\lvert\texttt{nums}[i]-k\rvert.
$$

The question is not how to simulate the moves, but which target minimizes this sum of absolute distances. The minimizing target is a median, not the arithmetic mean. The exact solution sorts the array, selects its middle element, and sums every distance from that element.

**Why the median minimizes absolute distance**

Imagine moving a proposed target `k` one unit to the right. Every input value to the left of `k` becomes one unit farther away, increasing the total cost by one for each such value. Every input value to the right becomes one unit closer, decreasing the cost by one for each such value.

If more values lie to the right than to the left, moving right decreases the total cost. If more lie to the left, moving right increases it. A minimum is reached where neither side has a numerical majority—that is exactly the median region.

After sorting, a median has at most half the values below it and at most half above it. Moving away from that region causes distances on the larger side to increase at least as fast as distances on the smaller side decrease. No target outside the median region can improve the sum.

**A pairing view of the same fact**

Sort values as

$$
a_0\le a_1\le\cdots\le a_{n-1}.
$$

Pair the smallest with the largest, the second smallest with the second largest, and so on. For any target `k` lying between a pair's endpoints,

$$
\lvert a_i-k\rvert+\lvert a_{n-1-i}-k\rvert=a_{n-1-i}-a_i.
$$

This contribution is already as small as possible; moving `k` outside the pair's interval makes the sum larger. A median lies inside every nested outer-pair interval, so it simultaneously minimizes every pair's combined contribution. If `n` is odd, the unpaired center value is itself the median and contributes zero.

**How the exact median index is selected**

After `nums.sort()`, the code computes

`k = nums[len(nums) >> 1]`.

Shifting a nonnegative integer right by one bit is integer division by two, so `len(nums) >> 1` equals `len(nums) // 2`.

For odd `n`, this is the unique middle index. For even `n`, it selects the upper of the two central values. Every target between the lower and upper medians minimizes the absolute-distance sum, so choosing the upper median is fully optimal. The target is allowed to be any integer; selecting an existing array value is convenient and sufficient.

**Why the distance sum equals the number of moves**

For a value `v < k`, exactly `k - v` increments are necessary and sufficient. For `v > k`, exactly `v - k` decrements are necessary and sufficient. Absolute value combines both cases. Each permitted move changes one element by one, so it can reduce that element's remaining distance by at most one. Consequently, no strategy can use fewer than the sum of distances, and independently moving each value toward `k` achieves exactly that sum.

For `[1,2,3]`, the median is `2`. The costs are `1`, `0`, and `1`, totaling two.

For `[1,10,2,9]`, sorting gives `[1,2,9,10]`. The exact code chooses upper median `9`. Distances are `8 + 7 + 0 + 1 = 16`. Choosing any integer from `2` through `9`, including the lower median `2`, also gives 16; a target outside that interval costs more.

**Why the mean would solve a different problem**

The arithmetic mean minimizes the sum of squared distances, where large deviations receive extra weight. Here each unit of distance costs exactly one move, so the objective uses absolute values. An outlier can pull the mean far away from most values, but it cannot pull the median past half the data. That robustness matches the move-count objective.

## Complexity detail

Let $n$ be the number of elements. Python sorting takes $O(n\log n)$ time. Selecting the middle element is $O(1)$. The generator inside `sum` then visits all $n$ values and performs constant-time arithmetic under the standard fixed-width model, adding $O(n)$ time. Sorting dominates, so total time is $O(n\log n)$.

The array is sorted in place, so its original order is mutated. Python's Timsort can use $O(n)$ temporary storage in the worst case, which matches the manifest's $O(n)$ space bound. The distance generator is lazy and does not allocate a separate list; apart from sorting workspace, only the target and running sum are needed.

Python integers avoid intermediate overflow. In fixed-width languages, distance and total accumulation should use a wide type even though the final answer is guaranteed to fit in 32 bits.

## Alternatives and edge cases

- **Quickselect the median:** Expected $O(n)$ time finds the middle order statistic without fully sorting, followed by an $O(n)$ distance scan. It mutates the array and has quadratic worst-case time with naive pivots.
- **Deterministic median of medians:** Guarantees $O(n)$ worst-case selection but is considerably more complex and usually unnecessary for these bounds.
- **Try every possible target:** The numerical range can span billions, making range enumeration infeasible.
- **Use the arithmetic mean:** It minimizes squared error, not the sum of unit moves, and can be suboptimal here.
- **Odd length:** The middle sorted value is the unique median region and is optimal.
- **Even length:** Any target between the two central values is optimal; the exact code chooses the upper one.
- **One element:** It is its own median, its distance is zero, and no moves are needed.
- **All values equal:** Every absolute difference is zero.
- **Negative values:** Sorting and absolute differences work across zero without special handling.
- **Duplicate medians:** Repeated central values simply make the optimal target explicit and do not affect the proof.
- **Input mutation:** Callers needing the original order must sort a copy rather than reuse this exact in-place implementation.
