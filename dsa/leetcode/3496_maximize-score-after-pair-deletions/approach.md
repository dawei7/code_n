## General

**The score is everything removed, so focus on what remains.** Every operation adds the values of the two removed elements. No element is removed twice, and operations stop when the array has at most two elements. Therefore,

$$
\text{score}
=
\sum\texttt{nums}
-
\text{sum of the final remaining elements}.
$$

The total array sum is fixed. Maximizing the score is equivalent to minimizing the sum of a remainder that can actually be left by the allowed end deletions.

**The parity of the original length determines final size.** Each operation removes exactly two elements, so length parity never changes.

- If $n$ is odd, repeated operations stop with one element.
- If $n$ is even, they stop with two elements.

For $n=1$ or $n=2$, the process performs no operation, and the same remainder formulas return score zero.

**The remaining elements always form one contiguous interval.** Removing the first two shortens the interval from the left. Removing the last two shortens it from the right. Removing the first and last shortens both ends. None of these operations removes an interior element while keeping elements on both sides. Starting from the whole array, the live elements therefore remain a contiguous subarray after every step.

This structural fact determines which final remainders are reachable.

**For odd length, any single element can remain.** Choose target index $t$. There are $t$ elements to its left and $n-1-t$ to its right, and their total is even.

If both side counts are even, repeatedly remove two from each side as needed. If both are odd, first remove one element from each end with the first-and-last operation; both remaining side counts become even. Thus every target element can be isolated.

The cheapest reachable one-element remainder is therefore `min(nums)`, and the source returns

`sum(nums) - min(nums)`.

Negative values are handled naturally. Leaving a very negative element makes the removed total larger than the original total sum, which is valid because the score excludes that negative remainder.

For `[2,4,1]`, leaving the minimum value one means removing the first two elements for score six.

**For even length, the final two elements must be adjacent.** Since the live array is always contiguous, a final interval of length two is an adjacent pair from the original array.

Conversely, every adjacent pair can be left. For pair indices $t,t+1$, there are $t$ elements on the left and $n-t-2$ on the right. Their total is even. As in the odd case, remove pairs from individual sides when both counts are even, or remove one from each end once when both are odd, then finish with same-side pair removals.

Thus reachable final sums are exactly `nums[t] + nums[t+1]` for adjacent pairs. Python's `pairwise(nums)` enumerates them lazily, and the source subtracts their minimum from the total.

For `[5,-1,4,2]`, adjacent sums are $4,3,6$. Leaving pair `[-1,4]` with sum three removes the first and last values for score $7$, which is optimal.

**Why arbitrary nonadjacent pairs cannot remain.** A first-and-last deletion removes endpoints rather than joining separated interior elements. At every moment all live indices are consecutive, so when only two survive they must have been neighbors originally. Treating any two values as a possible remainder would overestimate the score.

**Why the formula is fully correct.** The score/remainder identity shows the best sequence leaves a minimum-sum reachable remainder. Parity fixes whether that remainder has one or two elements. The reachability arguments prove that the odd case permits exactly every singleton and the even case permits exactly every adjacent pair. The source selects the minimum in that complete set and subtracts it from the fixed total, so its result is the maximum achievable score.

No dynamic programming over operation sequences is required because different sequences leading to the same final interval remove the same complement and earn the same total.

## Complexity detail

`sum(nums)` scans all $n$ elements. For odd length, `min(nums)` performs another linear scan. For even length, `pairwise` yields $n-1$ adjacent pairs and the generator computes each sum once before `min` chooses the smallest. Total time is $O(n)$.

The total, current minimum, and pairwise iterator use $O(1)$ auxiliary space. `pairwise` is lazy and does not construct a list of pairs. These bounds match the manifest.

The total score may be negative if every forced removal has negative sum. The method maximizes correctly without assuming positivity.

## Alternatives and edge cases

- **Interval dynamic programming:** It can model all operations but costs at least quadratic time when final-remainder reachability gives a linear formula.
- **Greedily remove the largest current pair:** A locally large removal may force an unfavorable final remainder; optimizing the remainder globally is simpler.
- **Leave any two elements for even \(n\):** Only adjacent original elements can form the final contiguous interval.
- **Odd length:** Exactly one element remains because removing two preserves odd parity.
- **Even length:** Exactly two remain, including the initial $n=2$ case.
- **One element:** No operation runs; total minus that same minimum returns zero.
- **Two elements:** The only adjacent-pair sum equals the total, so the score is zero.
- **Negative minimum singleton:** Leaving it can increase the score above the whole-array sum, which is mathematically valid.
- **Negative adjacent pair:** The best score may similarly exceed the original sum by leaving that negative pair.
- **All equal values:** Every reachable remainder has the same sum, so every complete sequence ties.
- **Lazy `pairwise`:** It enumerates consecutive values only and keeps constant memory.
- **Reachability parity:** Side counts around a target singleton or pair have the same parity, enabling either same-side removals or one initial cross-end removal.
