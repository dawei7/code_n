## General

**Reuse the previous prefix total.** The running sum at position `i` equals every value from zero through `i`. After computing the sum through `i-1`, the next result needs only one addition: previous total plus `nums[i]`. Recalculating the entire prefix would repeat earlier work.

`accumulate(nums)` implements exactly this recurrence. It yields the first value unchanged, then repeatedly combines the prior accumulated total with the next input using addition. `list(...)` consumes that iterator and stores every yielded prefix total in the required output list.

For `[1,2,3,4]`, the iterator yields one, then three, then six, then ten. Each value includes the current input, so the definition is inclusive.

**The input remains unchanged.** The source builds a separate result. This matters if the caller needs the original numbers afterward. It also explains the manifest's linear space bound.

**Negative values require no special handling.** A running sum may rise, fall, or stay equal depending on the next number. The recurrence uses ordinary addition and does not assume monotonic totals.
After `accumulate` consumes the first `i+1` elements, its stored total equals their sum. The first yield establishes this for one element. Adding `nums[i]` to the correct preceding prefix establishes it for the next position. Induction proves every emitted element equals the required running sum.

Converting the iterator to a list preserves yield order, so output index `i` receives the sum through exactly input index `i`.

**Why the compact source is still an algorithm.** Although no explicit loop appears, `list` drives the accumulate iterator once per input element. The standard-library primitive does not precompute answers magically; it maintains one running total internally.

The nonempty constraint means there is always a first value. Even for a generalized empty input, `accumulate` would simply yield nothing and `list` would return an empty list.

**Follow the data flow one element at a time.** When the iterator receives the first number, that number is both the input prefix and its sum, so it can be emitted directly. For every later number, the iterator has two pieces of information: the total through the previous position and the untouched current input value. Adding them produces the next total, which replaces the iterator's stored state and is yielded to `list`.

This state replacement is safe because the next step never needs an older prefix separately. Every earlier input contribution is already compressed into the current total. That is the same dynamic-programming idea as retaining only the previous state when a transition depends on one predecessor.

**Distinguish output space from iterator state.** If the caller only wanted to consume running totals one at a time, returning `accumulate(nums)` would be lazy and use constant working memory. The contract requires a list, however, so `list` must retain every produced value simultaneously. The linear space is required by this returned representation, not by the recurrence itself.

**Why no overflow guard appears.** Python integers expand to hold larger exact values. With one thousand inputs whose magnitudes can reach one million, a prefix may exceed a narrow sixteen-bit or twenty-bit range, but Python still adds it exactly. In a fixed-width language, the chosen integer type would need to accommodate the largest possible absolute prefix total.

**A mixed-sign trace.** For `[3, -5, 4, -2]`, the outputs are three, negative two, two, and zero. The running total is allowed to cross zero several times. This demonstrates why the algorithm is about prefix aggregation, not a monotone growth property.

## Complexity detail

Let `N` be the input length. `accumulate` reads each element once and performs one addition after the first, while `list` appends each result once. Time is `O(N)`.

The returned list stores `N` integers, giving `O(N)` space. The iterator itself keeps only the source iterator and current total, which is `O(1)` working state beyond output.

Python integers may grow with the magnitude of prefix sums; conventional analysis treats arithmetic on the constrained values as constant-time. The input list is not copied separately.

Any method must produce `N` output values, so linear time is optimal.

## Alternatives and edge cases

- **Explicit output loop:** Maintain `total`, add each number, and append it. This is behaviorally identical and easier to customize.
- **Modify nums in place:** Add `nums[i-1]` into `nums[i]` from left to right. It uses constant auxiliary space but mutates input.
- **Recompute each prefix with sum:** It is clear but takes quadratic time across all positions.
- **Single element:** Its running sum is the element itself.
- **All zeros:** Every output remains zero.
- **Negative values:** Prefix totals may decrease, which is valid.
- **Mixed signs:** Cancellation is handled naturally.
- **Large magnitude:** Python integers avoid fixed-width overflow.
- **Input preservation:** The exact source returns a new list and leaves `nums` untouched.
- **Iterator laziness:** `accumulate` alone is lazy, but wrapping it in `list` materializes every result.
- **Inclusive prefix:** The current element always participates in its own output position.
- **Output length:** One value is yielded per input value.
- **Repeated values:** Every occurrence contributes at its own position; no frequency compression is appropriate.
- **Prefix total becomes zero:** Zero is emitted normally and remains the correct base for adding the next value.
- **Standard-library dependency:** The supported environment supplies `accumulate`; an explicit loop is the direct fallback when it is unavailable.
- **Materialization timing:** The function completes the full traversal before returning because `list` eagerly consumes the iterator.
