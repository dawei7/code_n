## General

A median depends on the middle of the sorted data, but the stream keeps adding values. Sorting the entire collection after every insertion would repeatedly redo work. The central insight is that a median query does not need the complete sorted order: it needs only the largest value in the lower half and the smallest value in the upper half.

The source maintains exactly those two boundaries with two heaps:

- `maxq` represents the lower half. Python provides a min-heap, so this heap stores each lower value with its sign negated. Its root `maxq[0]` is the smallest negative value, which corresponds to the largest original lower-half value `-maxq[0]`.
- `minq` is a normal min-heap containing the upper half. Its root `minq[0]` is the smallest upper-half value.

The names describe the boundary operation each logical heap must support: a maximum from the lower half and a minimum from the upper half. The negation in `maxq` is an implementation technique, not a change to the numbers in the stream.

**The two invariants**

After every call to `addNum`, the data structure maintains two properties.

First, the heaps form an ordered partition:

$$
\text{every lower-half value} \le \text{every upper-half value}.
$$

Second, their sizes are balanced so that `minq`, the upper half, either has the same number of elements as `maxq` or has exactly one more:

$$
\lvert\texttt{minq}\rvert = \lvert\texttt{maxq}\rvert
$$

or

$$
\lvert\texttt{minq}\rvert = \lvert\texttt{maxq}\rvert + 1.
$$

Giving the extra element to `minq` is a design choice. A symmetric implementation could give it to the lower heap, but the insertion and query formulas would then need to follow that opposite convention consistently.

Together, these invariants expose the median at the two roots. If the total count is even, the two heaps have equal sizes, and the sorted middle pair consists of the largest lower value and the smallest upper value. If the total count is odd, `minq` has one extra value, and its smallest element is the single middle value.

**Routing a new number to the proper side**

The compact line

`heappush(self.minq, -heappushpop(self.maxq, -num))`

does several carefully ordered operations.

Conceptually, treat `num` as a candidate for the lower half. Because `maxq` stores negated values, the code pushes `-num` into it. It then immediately pops the smallest stored negative value. The smallest negative represents the largest original value among the old lower half plus the new candidate. Negating that popped value converts it back to its original sign, and the outer `heappush` inserts it into `minq`.

In plain language: temporarily place the new value with the lower values, remove the largest value from that candidate group, and send that largest value to the upper heap.

This operation restores the ordering invariant regardless of how small or large `num` is:

- If `num` is very large, it becomes the largest candidate and moves directly to `minq`; the old lower half stays unchanged.
- If `num` belongs in the lower half, some previous lower-half maximum is displaced into `minq`, leaving `num` among the lower values.
- If `num` equals boundary values, either copy may cross the boundary. Since equal values satisfy the non-strict ordering relation, the partition remains valid.

After this routing step, every value left in `maxq` is no larger than every value in `minq`. However, `minq` has just received one element and may now exceed `maxq` by two elements.

**Restoring the size invariant**

The condition `len(self.minq) - len(self.maxq) > 1` detects the only possible size violation. If it holds, the source removes `heappop(self.minq)`, the smallest upper-half value, negates it, and pushes it into `maxq`.

Moving the smallest upper value down is exactly the safe rebalance. It is no larger than the values remaining in `minq`, and it is at least as large as the existing lower values because the ordering invariant already held. Thus, it becomes the new boundary maximum of the lower half without mixing the two ordered groups.

No opposite rebalance is required. The first routing line always sends one candidate to `minq`, and the previous valid size relation ensures `maxq` cannot become larger than `minq` afterward.

**Tracing the example stream**

Consider insertions 1, 2, and 3. The table shows original values, even though `maxq` stores its values negated internally.

| Operation | Logical lower half | Upper half | Median |
| --- | --- | --- | --- |
| add 1 | empty | 1 | 1 |
| add 2 | 1 | 2 | $(1+2)/2=1.5$ |
| add 3 | 1 | 2, 3 | 2 |

When 1 arrives, the push-pop operation routes it into `minq`. The upper heap has one element and the lower heap is empty, which is the valid odd-count arrangement.

When 2 arrives, it is routed into `minq`, temporarily giving the upper heap two elements. The size difference is two, so the smallest upper value, 1, moves into the lower heap. Both halves then contain one value.

When 3 arrives, it remains in the upper half. That half now has one extra value, so no rebalance is needed. Its minimum, 2, is the middle of the sorted values `[1, 2, 3]`.

The same logic also handles an out-of-order insertion. If 0 arrives next, it first enters the lower candidates. Their largest value crosses into the upper half, then the smallest upper value moves down if balancing requires it. No full sorting pass is needed.

**Reading the median**

When the heap sizes are equal, the number of stored values is even. The lower middle value is `-self.maxq[0]`, and the upper middle value is `self.minq[0]`. Their mean is

$$
\frac{\texttt{minq[0]}+(-\texttt{maxq[0]})}{2},
$$

which the source writes as `(self.minq[0] - self.maxq[0]) / 2`.

When the sizes differ, the maintained invariant guarantees that `minq` has exactly one extra element. Its root is then the one value with equally many elements on either side, so `findMedian` returns `self.minq[0]`.

The contract guarantees at least one insertion before a median query. Therefore, the odd-size branch always has a valid upper root, and the equal-size branch used for a real query has two nonempty heaps.

**Why the maintained roots are sufficient**

Assume both invariants hold after an insertion. For an even number $2k$ of values, the lower heap contains the $k$ smallest values and the upper heap contains the $k$ largest values. Their boundary roots are positions $k-1$ and $k$ in zero-based sorted order, precisely the two values whose average defines the median.

For an odd number $2k+1$ of values, the lower heap contains $k$ values and the upper heap contains $k+1$. Because every lower value is no greater than every upper value, the smallest upper value has $k$ values before it and $k$ values after it. It is precisely the median.

The insertion procedure preserves ordering and then restores the permitted size difference, as described above. Since the empty constructor trivially satisfies both invariants, they hold after every insertion. The returned root or root average is therefore correct after every stream prefix.

## Complexity detail

Suppose $k$ values have already been inserted. Heap insertion, removal, and combined push-pop each take $O(\log k)$ time in the worst case. `addNum` performs one `heappushpop`, one push into `minq`, and, when needed, one pop and one push for rebalancing. The number of heap operations per insertion is constant, so a single insertion costs $O(\log k)$ time.

`findMedian` reads one or two heap roots and performs at most one subtraction and one division. Heap roots are directly indexed, so a median query costs $O(1)$ time.

Across $n$ total insertions, the insertion work sums to $O(n\log n)$. This is the manifest's aggregate time bound. Median queries do not change that bound; even if one query follows every insertion, their total additional work is only $O(n)$.

Every inserted value is stored exactly once in one of the two heaps. Together the heaps therefore contain $n$ elements and use $O(n)$ space. Apart from those stored values, the object uses only constant additional fields and temporary values. Python's negated integers in `maxq` are the lower-half representation, not duplicate copies in a second data structure.

## Alternatives and edge cases

- **Sort on every median query:** Appending is cheap, but each query can cost $O(n\log n)$. It repeats ordering work and is poor when medians are requested frequently.
- **Keep one sorted list:** Binary search finds an insertion index in $O(\log n)$ time, but inserting into a Python list can shift $O(n)$ elements. Median lookup is then $O(1)$, with slower updates than the two-heap method.
- **Balanced search tree with order statistics:** Such a tree can support logarithmic insertion and median selection, but Python has no built-in order-statistic tree, and implementing one is substantially more complex.
- **Frequency buckets for values in `[0, 100]`:** Under the first follow-up's narrow value range, store 101 counts and scan the buckets for the middle rank. Updates become $O(1)$ and queries take $O(101)$, which is constant with respect to stream length.
- **Buckets plus outlier structures:** If 99 percent of values lie in `[0, 100]`, counts can cover the dense range while separate ordered structures track values below 0 and above 100. Rank counts determine whether the median lies in the dense range or an outlier side, but the bookkeeping is more specialized.
- **Reservoir sampling:** It can estimate a median with bounded storage, but the contract requires an exact answer within numerical tolerance, not a statistical approximation.
- **Putting the extra element in the wrong heap:** This source gives the extra value to `minq`. If `maxq` had the extra element, returning `minq[0]` for odd sizes would be wrong.
- **Forgetting negation:** `maxq[0]` is a stored negative number. The logical lower maximum is `-maxq[0]`, which explains the subtraction in the even-size formula.
- **Negative stream values:** Negation still reverses their ordering correctly. For example, original values `-5` and `-2` are represented as 5 and 2 in the lower max-heap mechanism; Python's min-heap root still corresponds to the largest original lower value after the sign conversion.
- **Duplicate values:** Equal elements may reside on either side of the partition. The invariant uses `<=`, so duplicates do not affect correctness or require unique keys.
- **One inserted value:** It resides in `minq`, which has one extra element. `findMedian` returns that value directly.
- **Two inserted values:** The heaps have equal sizes. Their roots are the lower and upper values, and the formula returns their arithmetic mean.
- **Odd number of values:** `minq` has exactly one extra element, making its root the unique median.
- **Even number of values:** Both heaps have equal sizes, so the mean of their boundary roots is required even when that result is fractional.
- **Large positive and negative bounds:** The inputs lie between $-10^5$ and $10^5$. Their sum and negation are safe in Python integers, and `/ 2` produces a floating-point result as the return contract expects.
- **Query before insertion:** The source does not guard against empty roots because the problem explicitly guarantees at least one stored element before `findMedian` is called.
