## General

**Always take the largest currently available reward**

Each operation adds the chosen current value to the score, then replaces only that value by its smaller successor

$$
\left\lceil\frac v3\right\rceil.
$$

At any moment, the best immediate reward is the largest array value. A max-priority queue supports repeatedly finding it and reinserting its successor.

Python's standard heap is a min-heap, so the method stores negative values. The smallest negative number corresponds to the largest original value.

**Build the heap**

List `h=[-v for v in nums]` negates every input. `heapify(h)` rearranges it into heap order in linear time.

The original `nums` list is not modified. All evolving operation values live in `h`.

**Perform exactly `k` operations**

On every iteration:

1. `heappop(h)` removes the smallest negative entry;
2. negating it recovers largest current positive value `v`;
3. add `v` to `ans`;
4. compute $\lceil v/3\rceil$;
5. negate and push the successor back.

The heap size stays equal to `len(nums)`, representing one current value for every original index.

The loop runs exactly `k` times as required, even after values become one. Since $\lceil1/3\rceil=1$, choosing a one simply earns another one and reinserts it.

**Why the greedy choice is optimal**

Think of every original index as a reward chain:

$$
v,\ \left\lceil\frac v3\right\rceil,\
\left\lceil\frac{\lceil v/3\rceil}{3}\right\rceil,\ldots
$$

Taking one reward unlocks the next reward in that same chain. Each chain is nonincreasing.

Suppose a proposed optimal schedule chooses smaller available reward `y` while larger reward `x>=y` is available. Swap the order so `x` is taken first. This gains at least as much now. Taking `x` unlocks a successor no larger than `x`, while `y` remains available for a later step. Reordering the two choices cannot reduce the total of the selected rewards; if later decisions differ, the priority-queue schedule always retains the largest available option.

Applying this exchange at every first disagreement transforms an optimal schedule into the greedy schedule without decreasing its score. Therefore, repeatedly choosing the current maximum is optimal.

**Trace the second sample**

For `[1,10,3,3,3]` and `k=3`:

- pop 10, score becomes 10, and reinsert $\lceil10/3\rceil=4$;
- pop 4, score becomes 14, and reinsert $\lceil4/3\rceil=2$;
- the largest current value is 3, so pop it and finish with score 17.

The heap automatically compares newly produced successors with untouched elements.

**Ceiling calculation in the exact source**

The implementation uses `ceil(v/3)`. With `v<=10^9`, Python floating-point division represents the relevant quotient precisely enough for this conversion.

An integer-only equivalent is

`(v+2)//3`,

which avoids floating point and is generally preferable when bounds are larger.

**Why a sorted array alone is inconvenient**

After selecting the maximum, its replacement may belong anywhere among the remaining values. Re-sorting or inserting into a sorted list every time would cost linear or logarithmic work with more complex data movement.

A heap maintains only enough order to retrieve the maximum, which is exactly the needed operation.

**Negative values reverse heap priority**

For positive rewards $x>y$, their stored keys satisfy $-x<-y$. A min-heap removes the numerically smallest key, so it removes $-x$ first and recovers reward $x$. Reinserting the negated successor preserves the same ordering rule for every future operation.

There is no conflict with the score accumulator: only heap keys are negated. `ans` always receives the restored positive `v`.


Before each iteration, heap entries are the current values of all indices after earlier operations. Popping the most negative entry selects their maximum. Reinserting the transformed value creates exactly the state described by the chosen operation.

The greedy exchange argument proves this selected index can begin some optimal remaining schedule. Induction over `k` iterations proves the accumulated `ans` is globally maximum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Creating and heapifying `h` costs $O(n)$ time. Each of `k` iterations performs one pop and one push on a heap of size `n`, costing $O(\log n)$.

Total time is $O(n+k\log n)$.

The heap stores `n` integers, so auxiliary space is $O(n)$. The score can exceed 32-bit range, and fixed-width languages should use 64-bit arithmetic.

## Alternatives and edge cases

- **Repeated linear maximum search:** It costs $O(kn)$ and is too slow.
- **Balanced ordered multiset:** It supports maximum removal and reinsertion in $O(\log n)$ but is more machinery.
- **Integer ceiling formula:** `(v+2)//3` is exact without floating point.
- **`k=1`:** Take the original maximum once.
- **Single array element:** Repeatedly follow its ceiling-divided chain.
- **Values equal one:** They remain one under the operation.
- **Duplicate maxima:** Choosing any equal occurrence gives the same immediate and successor values.
- **Exactly `k`:** Do not stop when rewards become small.
- **Input preservation:** Only the negative heap is mutated.
- **Large score:** Use a sufficiently wide accumulator.
