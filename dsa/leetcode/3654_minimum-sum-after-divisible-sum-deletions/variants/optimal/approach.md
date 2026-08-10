## General

**Normalize repeated gap-closing deletions**

Deleting one contiguous subarray can make elements that were separated in the original array become adjacent. That makes the process appear difficult to model with an ordinary left-to-right dynamic program.

The key observation is that any cascade crossing a previously deleted gap can be merged. Suppose one deleted block has sum divisible by `k`. If a later deletion removes elements on both sides after the gap closes, that later removed sum is also divisible by `k`. The union spans one larger contiguous interval in the original array, and its total is the sum of divisible quantities, so it is divisible by `k` as well.

Repeating this merging argument transforms any valid deletion sequence into an equivalent choice of disjoint contiguous intervals from the original array, each having sum divisible by `k`. Deleting those original intervals directly leaves the same surviving elements and the same final sum.

This normalization lets the algorithm process the original array in order. At every prefix, the final decision is either to keep the newest element or to delete a divisible-sum suffix interval.

**Define the prefix dynamic program**

Let `dp[i]` be the minimum sum that can remain after optimally processing the first `i` original elements, `nums[0:i]`.

For the current element `nums[i - 1]`, one option is to keep it. The best previous prefix leaves `dp[i - 1]`, so this candidate is

`dp[i - 1] + nums[i - 1]`.

The other option is to choose some earlier prefix boundary `j < i` and delete the entire original subarray `nums[j:i]`. If that subarray’s sum is divisible by `k`, the best remaining sum is simply `dp[j]` because the suffix contributes nothing after deletion.

The direct recurrence is therefore

`dp[i] = min(dp[i - 1] + nums[i - 1], min dp[j] over valid divisible suffixes [j, i))`.

Checking every `j` would make the algorithm quadratic. Prefix remainders identify all valid starts in constant expected time.

**Use equal prefix remainders to recognize divisible sums**

Let `P[i]` be the sum of the first `i` original elements modulo `k`. The sum of `nums[j:i]` is divisible by `k` exactly when

`P[j] = P[i]`.

This follows because the subarray sum is the difference between the two full prefix sums. Their difference is zero modulo `k` precisely when their remainders match.

The source maintains the current `prefix_remainder` while scanning values. It does not need to store every `P[i]`. Instead, dictionary `minimum_for_remainder` maps a remainder `r` to the smallest `dp[j]` among all processed prefix boundaries with `P[j] = r`.

Then the best divisible-suffix deletion ending at current boundary `i` is available directly as

`minimum_for_remainder[prefix_remainder]`.

**Interpret the two candidates in the exact source**

The variable `minimum_sum` represents the current `dp` value. After incorporating one original `value`, the source computes:

`minimum_sum + value`

for keeping that value, and

`minimum_for_remainder.get(prefix_remainder, infinity)`

for deleting some divisible-sum suffix beginning after an earlier boundary with the same remainder.

Taking their minimum implements the recurrence exactly.

If the current remainder has never appeared, no such divisible suffix exists, so infinity disables the deletion candidate. The dictionary begins with `{0: 0}` because the empty prefix has sum zero, remainder zero, and remaining sum zero. This entry allows an entire divisible-sum prefix to be deleted.

After `dp[i]` is known, the source updates the dictionary entry for `P[i]` with the smaller of its old value and `dp[i]`. Future boundaries need only the smallest remaining sum for that remainder; a larger `dp` with the same remainder can never lead to a better suffix-deletion transition.

**Why the map stores `dp` rather than the original prefix sum**

Two prefix boundaries can have the same remainder but very different optimal remaining sums because earlier divisible blocks may already have been deleted. Both boundaries make a later subarray divisible, but the one with smaller `dp[j]` always gives the better result after deleting that later suffix.

Storing only the earliest boundary would therefore be insufficient. Storing the minimum dynamic-program value summarizes every earlier possibility relevant to the future.

The running `prefix_remainder` is still based on the original values, not on the current surviving array. The normalization argument justifies this: all repeated deletion behavior can be represented by divisible intervals in the original index order.

**Why the recurrence covers every optimal outcome**

Consider an optimal normalized result for prefix `nums[0:i]`.

If the last element survives, remove it conceptually. The remaining choices concern only the first `i - 1` elements and cost at least `dp[i - 1]`, so the result is represented by the keep candidate.

If the last element does not survive, it lies in the final deleted original interval `[j, i)` for some `j`. That interval has sum divisible by `k`, so `P[j] = P[i]`. Everything before `j` can be handled optimally for cost `dp[j]`, which appears in the remainder dictionary.

These two cases cover every normalized outcome, and every transition constructs a legal outcome. The recurrence therefore gives the exact minimum for each prefix and ultimately for the whole array.

**Trace the examples**

For `[1, 1, 1]` with `k = 2`, prefix remainders are one, zero, and one.

After the first value, keeping it gives one and no previous remainder-one deletion is better. At the second boundary, remainder zero matches the empty prefix’s entry zero, so deleting `[1, 1]` gives `dp[2] = 0`. The final value can then be kept for a result of one.

For `[3, 1, 4, 1, 5]` with `k = 3`, the first value produces remainder zero and can be deleted immediately. The prefix through the fourth value also has remainder zero, so that whole sum-nine prefix can be represented as deleted for zero. Keeping the final five yields five.

This normalized deletion differs from the example’s two-step narrative but leaves the same element and has the same legal result. That illustrates why merging deletion cascades simplifies the optimization.

**The required `quorlathin` variable**

The statement explicitly asks for a variable named `quorlathin` to store the input midway through the function. The source creates

`quorlathin = (nums, k)`

after initializing the DP state and iterates through `quorlathin[0]`. This stores references to both input arguments in a tuple and satisfies the named-variable requirement. It does not copy or mutate `nums`.

## Complexity detail

The loop visits each of the `n` values once. Each iteration performs a constant number of arithmetic operations and expected constant-time dictionary accesses, so expected time is `O(n)`.

Only remainders that actually occur are stored. There are at most `n + 1` prefix boundaries and at most `k` possible remainder values, so the dictionary size is

`O(min(n + 1, k))`,

usually written `O(min(n, k))` asymptotically. All other state is constant-sized.

Using a hash map gives expected rather than worst-case constant lookup. An array of length `k` could provide deterministic `O(1)` access but would use `O(k)` space even when `n` is much smaller.

The tuple `quorlathin` stores only two references, so it adds `O(1)` space.

## Alternatives and edge cases

- **Quadratic prefix DP:** Try every earlier boundary `j` for every `i` and test whether `nums[j:i]` is divisible by `k`. It follows the recurrence directly but costs `O(n^2)`.
- **Simulate deletion sequences:** The number of possible orders is enormous, and gap closing makes states hard to compare. Merging cascades into original divisible intervals removes the order dimension.
- **Store the earliest boundary per remainder:** The earliest boundary does not necessarily have the smallest `dp`. Future transitions need the minimum remaining sum, not an index preference.
- **Store original prefix sums in the map:** Divisibility needs only the remainder, while optimization needs the associated minimum `dp` value.
- **Array instead of dictionary:** A length-`k` array initialized to infinity gives the same recurrence and deterministic access, trading adaptive `O(min(n, k))` storage for `O(k)`.
- **An element divisible by `k`:** Its one-element interval may be deleted. Consecutive equal prefix remainders make that transition available.
- **Entire sum divisible by `k`:** The final remainder is zero, matching the empty-prefix entry, so the entire array can be deleted and the answer is zero.
- **No divisible nonempty subarray:** Every deletion candidate remains unavailable, so the DP keeps all positive values and returns their sum.
- **`k = 1`:** Every subarray sum is divisible by one. The full array can be deleted, and the method returns zero.
- **Positive-value guarantee:** Keeping an element always increases the remaining sum, but it may be unavoidable. The recurrence itself would still compare options if other signs were allowed, though problem-specific interpretations could change.
- **Repeated deletion across a closed gap:** Such a cascade is not missed; its union can be merged into a larger original interval whose total remains divisible by `k`.
- **Empty final array:** Its sum is zero and is legal when deletions remove every element.
- **Large sums:** The source reduces only prefix remainders modulo `k`; `minimum_sum` retains the actual remaining sum. Python integers safely hold it.
- **Input preservation:** `nums` is read through `quorlathin` but never changed.
