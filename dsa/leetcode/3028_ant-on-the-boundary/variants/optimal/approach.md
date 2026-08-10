## General

**Represent position with a signed prefix sum.** Put the boundary at coordinate zero. The ant begins at zero. A positive value moves it right, which increases its coordinate; a negative value moves it left, which decreases its coordinate by the corresponding magnitude. Therefore, after completing movement $i$, its position is

$$
S_i=\sum_{j=0}^{i}\texttt{nums}[j].
$$

The ant has returned to the boundary after that movement exactly when $S_i=0$. The problem is consequently asking for the number of zero-valued prefix sums.

The exact source captures this transformation directly:

`return sum(s == 0 for s in accumulate(nums))`

`accumulate(nums)` yields the prefix sums one at a time. The generator compares each yielded sum with zero. In Python, `True` contributes 1 and `False` contributes 0 to `sum`, so the final integer is the number of completed moves whose endpoint is the boundary.

**Why crossings during a movement do not count.** A value represents one complete movement of possibly several units. If the ant begins at coordinate 2 and receives movement $-5$, its continuous path crosses coordinate zero but ends at $-3$. The reference explicitly says to check only after all units of that movement have been completed. The prefix sum after the move is $-3$, not zero, so the generator adds nothing. This is precisely the required behavior.

If the problem instead counted every physical crossing, one would compare signs and magnitudes between consecutive positions. That is a different task. Here only exact zero endpoints matter.

**Why each zero prefix is one return.** Every item in `nums` corresponds to one observation time: immediately after the movement finishes. If the prefix is zero, the ant is on the boundary at that observation and contributes one. The next input is nonzero, so the ant leaves the boundary during the next move; if a later prefix is again zero, that is another distinct return and is counted separately.

The initial position is not counted. `accumulate(nums)` begins with `nums[0]`, not with an initial zero. Thus the generator tests only states after at least one move, exactly matching “returns” rather than “starts.”

**A loop-invariant explanation.** After `accumulate` has yielded the first $i+1$ values, the latest yielded value equals the ant's position after moves 0 through $i$. This is true initially because the first position is `nums[0]`. Each subsequent accumulated value adds the next signed movement, matching the coordinate update. The Boolean generator contributes one exactly for zero coordinates. Therefore, after processing any prefix of movements, `sum` has counted exactly the boundary returns within that prefix. At exhaustion, it has the requested total.

**Trace both returning and crossing.** For `nums = [2, 3, -5]`, the yielded positions are 2, 5, and 0. Their zero tests are false, false, and true, so the result is one.

For `nums = [3, 2, -3, -4]`, positions are 3, 5, 2, and $-2$. The last move crosses zero on its way from 2 to $-2$, but no yielded position equals zero. The answer is zero.

For `nums = [1, -1, 2, -2]`, positions are 1, 0, 2, 0. Two different completed moves end on the boundary, so the answer is two.

**Why signs already encode direction.** There is no need for separate branches for left and right. Adding a negative integer is subtraction of its magnitude; adding a positive integer is movement to the right. A single accumulated sum exactly matches both rules and makes the implementation less error-prone.

**Streaming behavior.** `itertools.accumulate` does not precompute a list of all positions. It maintains the current total and yields it. The generator expression likewise creates one Boolean at a time for `sum`. The algorithm therefore derives the answer without retaining the path history.

## Complexity detail

Let $N$ be the number of movements. `accumulate` visits each number once, and each yielded prefix is compared with zero once. Total time is $O(N)$.

The iterator stores only its running sum. The generator expression stores the current value, and `sum` stores its running count. No prefix array is built, so auxiliary space is $O(1)$. The input list is not modified.

Although a prefix sum can grow with $N$ and the movement magnitudes, the stated constraints keep it bounded. Standard analysis treats integer addition and comparison as constant-time operations here. The output is one integer and is not counted as auxiliary storage.

## Alternatives and edge cases

- **Explicit running-sum loop:** Initialize `position = answer = 0`, add each movement, and increment when position is zero. This is equivalent in time and space and may be easier for beginners to debug; the exact source expresses the same loop through iterators.
- **Build a prefix-sum list:** Counting zeros afterward works but wastes $O(N)$ memory because past positions are never needed.
- **Count sign changes:** This incorrectly counts movements that cross the boundary without ending there, which the statement explicitly excludes.
- **Count zero values in `nums`:** Individual movements are guaranteed nonzero, and a return depends on the cumulative position rather than one movement's size.
- **Initial boundary position:** It is not a return and is not included because no initial zero is emitted.
- **First movement returns:** A nonzero first movement cannot end at zero from the initial zero, consistent with the constraints.
- **Multiple returns:** Every later zero prefix contributes independently; the method does not stop after the first.
- **Crossing without landing:** A change from positive to negative position, or vice versa, adds zero unless the new prefix itself is exactly zero.
- **Move away after a return:** The following nonzero movement creates a nonzero prefix, and a subsequent zero is properly counted as another return.
- **All movements in one direction:** Every prefix has the same nonzero sign, so the result is zero.
- **Lazy memory use:** Neither `accumulate` nor the Boolean generator materializes all intermediate values, which is why the exact source truly uses constant auxiliary space.
