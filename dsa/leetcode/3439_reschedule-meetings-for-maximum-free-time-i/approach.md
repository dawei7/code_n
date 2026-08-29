## General

**Represent the schedule by its free gaps.** With $n$ ordered non-overlapping meetings, there are $n+1$ free-time gaps:

- before the first meeting: `startTime[0]`;
- between meetings $i-1$ and $i$: `startTime[i] - endTime[i - 1]`;
- after the last meeting: `eventTime - endTime[-1]`.

The source stores these lengths in `nums`. Zero-length gaps are valid when meetings touch an event boundary or each other.

**Moving consecutive meetings merges adjacent gaps.** Suppose exactly $q$ consecutive meetings are rescheduled while preserving meeting order and durations. By packing those meetings against one side of the surrounding available region, their $q+1$ neighboring free gaps can be combined into one continuous free interval. Meeting durations do not become free; they are merely repositioned inside the same surrounding span. Therefore, the length that can be concentrated is the sum of those $q+1$ gap lengths.

Using fewer than $k$ moves merges at most $k$ gaps. Because every gap length is nonnegative, extending a group when possible cannot reduce its sum. Thus an optimum can be found among sums of $k+1$ consecutive gaps. At schedule boundaries, choosing the first or last group naturally represents packing meetings toward the event edge.

Conversely, a continuous free interval created by moving at most $k$ order-preserving meetings can cross only those moved meetings. They form one consecutive meeting block; an unmoved meeting inside would split the free interval. The interval can therefore combine no more than $k+1$ consecutive original gaps. This proves the gap-window formulation covers every possible optimum.

For the first example, the gaps are `[1, 1, 0]`: one unit before meeting $0$, one between the meetings, and none after the last. With $k=1$, the largest two-gap sum is $2$. Moving the first meeting right merges the first two gaps into free interval `[0,2]`.

For a fully occupied event whose meetings touch, every gap is zero. Every window sum is zero, correctly showing that rearranging durations cannot create free time that did not exist.

**Maintain a window of exactly \(k+1\) gaps.** `s` accumulates gap lengths as the loop advances. When `i >= k`, the current window contains indices `i-k` through `i`, exactly $k+1$ gaps. The source updates `ans` from `s` and then subtracts `nums[i-k]`, leaving the last $k$ gaps ready for the next iteration.

The update-before-subtraction order matters. Subtracting first would evaluate only $k$ gaps and model at most $k-1$ moved meetings.

When $k=n$, there are $n+1$ gaps and only one full window, evaluated at the final index. Its sum is all free time in the event; moving every meeting allows that free time to be placed contiguously while preserving order.

**Why no meeting-duration array is needed.** The total free time around a chosen block is already partitioned among the stored gaps. Rescheduling preserves every meeting duration, so only the distribution of those gap lengths changes. Summing gaps directly is equivalent to taking the outer span and subtracting meeting durations, but avoids extra prefix sums.
Before each evaluation at index $i$, `s` equals the sum of the $k+1$ gaps ending at $i$. This follows from adding the new gap and removing the old one only after the previous evaluation. The loop evaluates every possible length-$(k+1)$ consecutive gap window once. The structural argument shows each such sum is achievable and every achievable maximum is bounded by one of them. Therefore, their maximum is the answer.

The arrays `startTime` and `endTime` are read only. The derived gap list is independent of later rescheduling choices; it captures all freedom in the original schedule.

## Complexity detail

Let $n$ be the number of meetings. Building the $n+1$ gap list takes $O(n)$ time. The sliding-window loop visits each gap once and performs constant work, also $O(n)$. Total time is $O(n)$.

`nums` stores $n+1$ gap lengths, so auxiliary space is $O(n)$, matching the manifest. The sliding window itself uses only `s`, `ans`, and indices. A streaming construction could reduce auxiliary space, but the exact source materializes the gaps.

## Alternatives and edge cases

- **Meeting-duration prefix sums:** Enumerate each block of $k$ meetings, take its surrounding span, and subtract total duration. This is correct but uses more bookkeeping than summing gaps.
- **Try every rescheduled position:** Continuous start times create many possibilities. Gap conservation reduces them to discrete consecutive blocks.
- **Move nonconsecutive meetings:** They cannot help form one larger continuous free interval because an unmoved meeting between them remains an obstacle.
- **Use fewer than \(k\) meetings:** Nonnegative gaps mean a smaller merged-gap group is contained in some $k+1$ group with at least as large a sum, subject to available meetings.
- **Zero gaps:** They contribute normally and do not break the window reasoning.
- **Meetings at event boundaries:** The first or last gap is zero, correctly representing no free time outside the event.
- **\(k=1\):** The algorithm finds the greatest sum of two neighboring gaps, exactly the benefit of moving one meeting.
- **\(k=n\):** All $n+1$ gaps are summed once.
- **Preserved order:** The proof relies on moved meetings remaining in relative order; this distinguishes version I from the next problem.
- **Inclusive-looking meeting notation:** Only durations and differences matter; touching endpoints yield zero gaps and no double-counted time.
