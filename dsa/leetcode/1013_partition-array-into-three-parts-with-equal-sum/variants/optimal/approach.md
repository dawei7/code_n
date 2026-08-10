## General

**Derive the only possible part sum**

If three parts have equal sum `s`, the complete array sum must be `3s`. Therefore, the total must be divisible by three, and the target for every part is forced.

The line

`s, mod = divmod(sum(arr), 3)`

computes both quotient and remainder. If `mod` is nonzero, no integer target sum can satisfy the requirement, so the method returns false immediately.

Python's `divmod` also works for negative totals. When the total is exactly divisible by three, the remainder is zero and `s` is the exact signed target.

**Greedily cut whenever the running segment reaches the target**

Variable `t` is the sum of elements since the most recent greedy cut. For each value:

`t += x`.

Whenever `t == s`, the algorithm has found one nonempty consecutive segment of target sum. It increments `cnt` and resets `t = 0` so the next element begins a new candidate segment.

Resetting is essential. Without it, later comparisons would use a prefix sum from the start of the whole array rather than the sum of the current part.

**Why each counted segment is nonempty**

The target check happens only after one array element has been added. After a cut, `t` is reset, but `cnt` cannot increase again until a later loop iteration consumes at least one new element.

This remains true when `s = 0` and the next element is zero. A one-element zero part is nonempty and valid.

**Why finding at least three target segments is enough**

Suppose the scan finds three target-sum segments. Use the endpoints of the first and second segments as the two required cuts.

- The first part sums to `s`.
- The second part sums to `s`.
- Since the complete array sums to `3s`, everything after the second cut sums to `3s - 2s = s`.

The third greedy hit proves at least one element exists after the second cut, so the final part is nonempty.

The algorithm does not need to cut at the third hit or require exactly three hits. Once the first two cuts are known and some later target segment exists, the entire remaining suffix automatically has the target total.

**Why `cnt` may exceed three**

Negative values and a zero target can cause the running sum to hit `s` more than three times. Extra greedy segments do not invalidate the first two cuts; several later segments together still sum to the required remainder because the total was fixed at `3s`.

For `s = 0`, an array with many zero-sum chunks may produce a large `cnt`. Any first three demonstrate a legal three-part partition, so `cnt >= 3` is the right test.

**Trace the first example**

For

`[0,2,1,-6,6,-7,9,1,2,0,1]`,

the total is nine, so `s = 3`.

- Running sum reaches three after `0,2,1`. Count one and reset.
- The next segment `-6,6,-7,9,1` also sums to three. Count two and reset.
- The remaining `2,0,1` reaches three. Count three.

The method returns true.

**Why greedy early cuts do not destroy a possible solution**

With negative values, it may seem dangerous to cut at an early occurrence of the target. Suppose a valid partition exists, but the scan reaches sum `s` before the valid first cut and resets.

At the valid first cut, the elements since the greedy cut sum to zero, so a new greedy target may not occur there. However, by the valid second cut, the full prefix sums to `2s`. Subtracting the earlier greedy prefix sum `s` shows the segment since the greedy cut sums to `s`, so the greedy scan finds its second target no later than that boundary. The remaining total then supplies a third target by the end.

Thus an earlier valid target cut cannot reduce the eventual count below three when a valid three-part partition exists.

**The segment-sum invariant**

After processing each element, `cnt` is the number of nonempty target-sum segments greedily completed in the processed prefix, and `t` is the sum of the uncut suffix after the last such segment.

Adding the next value extends only that suffix. When it reaches `s`, counting and resetting creates one more valid consecutive segment and restores the invariant.

**Why the final Boolean is exact**

If `cnt >= 3`, the first two greedy cuts and the total-sum argument construct three nonempty equal-sum parts.

Conversely, if a valid partition exists, total divisibility holds, and the early-cut argument guarantees the greedy scan reaches the target at least three times. Therefore, returning `cnt >= 3` is both necessary and sufficient.

## Complexity detail

Let `N` be the array length.

Computing `sum(arr)` scans the array once, and the greedy loop scans it once more. Total time is `O(N)`.

Only `s`, `mod`, `cnt`, `t`, and the current value are stored, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Prefix-sum boundary search:** Find one prefix equal to `s` and a later prefix equal to `2s` while leaving an element for the suffix. It is also linear but needs careful boundary handling when `s = 0`.
- **Store all prefix sums:** It can search possible cuts but uses `O(N)` space unnecessarily.
- **Try every pair of cuts:** Direct enumeration costs `O(N^2)` or worse.
- **Total not divisible by three:** Impossible immediately, regardless of element arrangement.
- **Target zero:** At least three nonempty zero-sum greedy segments are required; repeated zero values are handled naturally.
- **Negative values:** The method does not assume running sums are monotone.
- **More than three target hits:** Still valid; use the first two cuts and the complete remaining suffix.
- **Exactly three elements:** Each element must equal the forced target, which the scan recognizes.
- **Nonempty requirement:** Counting a segment only after consuming an element and demanding a third hit ensures the suffix after the second cut is nonempty.
- **Input preservation:** The array is read twice but never modified.
