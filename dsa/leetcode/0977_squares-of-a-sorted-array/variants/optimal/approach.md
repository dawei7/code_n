## General

**The largest square must come from an end**

The input is non-decreasing, but squaring destroys ordinary order around zero. Large negative values can produce large positive squares.

Within a sorted interval `nums[i:j+1]`, the value with greatest absolute magnitude must be at one of the two ends:

- left endpoint may be the most negative;
- right endpoint may be the most positive.

Therefore, the largest remaining square is always `nums[i]^2` or `nums[j]^2`.

**Two pointers**

Pointer `i` starts at zero and `j` at the final index.

Each iteration computes:

- `a = nums[i] * nums[i]`;
- `b = nums[j] * nums[j]`.

The larger square is appended to `ans`, and only the pointer that supplied it moves inward.

If squares are equal, the `else` branch chooses the right value. Either choice is correct because both output values are identical.

**Why output is built backward**

The algorithm repeatedly selects the largest remaining square. Thus `ans` is non-increasing.

The required answer is non-decreasing, so the final expression `ans[::-1]` reverses it.

One could instead preallocate an array and fill it from right to left. The exact code uses append plus one final reversal.

**Trace**

For `[-4, -1, 0, 3, 10]`:

- Compare sixteen and one hundred; append one hundred and move right.
- Compare sixteen and nine; append sixteen and move left.
- Compare one and nine; append nine and move right.
- Compare one and zero; append one and move left.
- Append zero.

Intermediate list is `[100, 16, 9, 1, 0]`. Reversing gives `[0, 1, 9, 16, 100]`.

**Why interior values cannot have a larger square**

Every interior value lies numerically between the endpoints.

If the interval crosses zero, absolute value is maximized at one endpoint. If all values are nonnegative, the right endpoint has maximum magnitude. If all are nonpositive, the left endpoint has maximum magnitude.

These cases prove the endpoint selection for every iteration.

**Maintained invariant**

Before each iteration, indices outside `[i, j]` have already contributed their squares to `ans` in descending order.

The remaining interval still inherits sorted order from the input. Choosing its largest endpoint square preserves descending output, then shrinking the interval preserves the invariant.

When pointers cross, every input element has contributed exactly once.

**Why multiplication is used rather than exponentiation**

`nums[i] * nums[i]` directly computes the square for integers. Negative signs disappear naturally.

The operation is exact in Python and bounded safely under the constraints.


At each step, the endpoint argument proves the algorithm selects the largest square not yet emitted. Appending it creates the correct next element of descending sorted order.

Induction gives a fully descending list containing every square once. Reversal produces the required non-decreasing result.

**Why consuming one endpoint preserves every other candidate**

After choosing the larger endpoint square, the unchosen endpoint stays in the interval. Its square will be compared again against the newly exposed opposite endpoint.

No value is discarded without being emitted, and no value is emitted twice. Pointer movement supplies a one-to-one correspondence between input elements and output squares.

**Comparison with merging two sorted sequences**

Negative values, when read from most negative toward zero, have decreasing square magnitude. Nonnegative values, when read from zero upward, have increasing square magnitude.

One solution could find the sign boundary and merge two square sequences. The two-end method is the same ordering insight viewed from the largest values downward and avoids locating the boundary explicitly.

**Why the final reverse is linear**

Slice `ans[::-1]` visits every output entry once and creates a reversed list. It does not resort values or perform comparisons.

Thus it preserves the linear target even though it allocates another output-sized list temporarily.

**Bounds and arithmetic**

Each input magnitude is at most ten thousand, so each square is at most one hundred million. Python integers represent it exactly.

The algorithm relies only on multiplication and comparison, with no floating-point precision concerns.

The loop condition `i <= j` is also important. When both pointers reach the same final element, that element has not yet been emitted, so the loop must process it once. Afterward one pointer crosses the other, proving that every input position contributed exactly one square and that no position was duplicated.

## Complexity detail

Let `N` be input length.

Each iteration moves exactly one pointer, so there are `N` iterations. Reversing `N` outputs is also linear. Total time is `O(N)`.

The output and reversed copy use `O(N)` space. Apart from returned storage, pointers and square variables use `O(1)`.

## Alternatives and edge cases

- **Square then sort:** Correct but costs `O(N log N)`.
- **Fill result from the end:** Avoids the final reversed copy while keeping linear time.
- **All nonnegative:** Right pointer supplies values in reverse order.
- **All nonpositive:** Left pointer usually supplies the largest magnitudes.
- **Array crossing zero:** Both endpoints must be compared.
- **Equal squares:** Either endpoint may be consumed first.
- **Single element:** It is appended and reversal changes nothing.
- **Zero:** Its square is zero and naturally appears near the final descending position.
- **Duplicate values:** Each occurrence contributes one square.
- **Input preservation:** The method reads but does not mutate `nums`.
