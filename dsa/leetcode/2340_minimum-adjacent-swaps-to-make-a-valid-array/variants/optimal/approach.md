## General

**Choose the occurrences that are already closest to their required ends**

Only one occurrence of the global minimum must reach index zero, and only one occurrence of the global maximum must reach index `n - 1`. When a value occurs several times, the best minimum candidate is its leftmost occurrence because it needs the fewest leftward adjacent swaps. The best maximum candidate is its rightmost occurrence because it needs the fewest rightward swaps.

The scan stores these indices as `i` and `j`:

- `i` becomes the index of the leftmost minimum;
- `j` becomes the index of the rightmost maximum.

Both start at zero, then every element is compared with the value at the currently selected index.

**Why the minimum comparison keeps the leftmost copy**

When `v < nums[i]`, the scan has found a genuinely smaller value and updates `i = k`. When values are equal, the code contains the additional condition `k < i`.

Because `k` advances from left to right, a later equal occurrence normally cannot have `k < i`, so the first occurrence of the current minimum remains selected. The explicit tie condition states the intended rule even though the traversal order already enforces it.

Moving this selected minimum to index zero costs exactly `i` adjacent swaps: it must cross each of the `i` elements before it once.

**Why the maximum comparison keeps the rightmost copy**

The condition `v >= nums[j]` updates `j` for both a larger value and an equal maximum. Consequently, every later occurrence of the current maximum replaces the earlier one. The extra equal-and-later clause is redundant after `>=`, but it reinforces the rightmost intention.

Moving the selected maximum from index `j` to the final index costs `n - 1 - j` swaps before accounting for interaction with the minimum move.

**Add the two endpoint distances**

If `i < j`, the selected minimum already lies left of the selected maximum. Moving the minimum left affects only elements before it, and moving the maximum right affects only elements after it. Their routes do not cross, so the costs simply add:

`i + (n - 1 - j)`.

If `i > j`, the maximum lies before the minimum. To place them at opposite ends, their routes cross once. The adjacent swap in which the selected minimum passes the selected maximum simultaneously moves the minimum one step left and the maximum one step right.

Adding their independent distances counts that shared swap twice. Subtracting one corrects the overlap:

`i + (n - 1 - j) - 1`.

The expression `(i > j)` is a Python Boolean, numerically one when crossing occurs and zero otherwise.

**Why the selected copies minimize the answer**

Choosing any later minimum would add at least one to its leftward distance. Choosing any earlier maximum would add at least one to its rightward distance. A different pair can change the crossing adjustment by at most one, but the extreme choices already achieve the minimum endpoint distances and correctly receive that adjustment when needed.

More directly, adjacent swaps preserve relative order except for the pair being swapped. A chosen minimum must cross every element before it, and a chosen maximum must cross every element after it. Those crossings are unavoidable. The only crossing shared by both obligations is between the two selected elements when the maximum begins to the left of the minimum. The formula counts every unavoidable crossing exactly once and describes an achievable sequence, so it is optimal.

**Handle the one-element overlap**

If `i == j`, the same position is both the selected minimum and maximum. Under valid data, this is unavoidable for a one-element array; the array is already valid. The method returns zero explicitly.

When every element of a longer array is equal, the scan chooses `i = 0` and `j = n - 1`, so the general formula also returns zero. Any equal endpoint values already satisfy both requirements.

**No swaps need to be simulated**

The algorithm calculates how many adjacent crossings are necessary but does not mutate the array. The endpoints alone determine the minimum count; constructing each intermediate state would add work without changing the answer.

## Complexity detail

Let `n` be the array length. The single loop examines each element once and performs constant-time comparisons and assignments, so running time is `O(n)`.

Only indices `i`, `j`, `k` and the current value are stored, giving `O(1)` auxiliary space. The input list is never reordered or modified.

The answer is at most on the order of `2n` and fits easily in ordinary integer ranges; Python integers remove overflow concerns.

## Alternatives and edge cases

- **Use built-in minimum and maximum plus index searches:** Find the minimum and maximum values, then locate the first minimum and last maximum. This is correct but makes several linear passes instead of one.
- **Simulate adjacent swaps:** Moving the chosen elements step by step takes `O(n)` operations and mutates data merely to obtain a count that endpoint distances already provide.
- **Choose the rightmost minimum:** It requires at least as many swaps to reach the left edge and can be strictly worse.
- **Choose the leftmost maximum:** It requires at least as many swaps to reach the right edge and can be strictly worse.
- **Forget the crossing correction:** When `i > j`, one swap advances both selected elements toward their endpoints, so the raw sum overcounts by one.
- **Subtract for `i < j`:** Their routes do not cross in that order, so subtracting would undercount.
- **One element:** It is simultaneously smallest, largest, leftmost, and rightmost; zero swaps are needed.
- **All values equal:** The first and last elements already provide valid endpoint occurrences, so the result is zero.
- **Minimum already first:** Its distance contribution is zero.
- **Maximum already last:** Its distance contribution is zero.
- **Maximum immediately before minimum:** Their single mutual swap is exactly the shared crossing represented by the subtraction.
- **Multiple minima and maxima:** The scan's tie behavior selects the endpoint-nearest copies.
- **Minimum equals maximum:** This means all values are equal, handled naturally.
- **Input preservation:** The method only reads `nums` and returns a count.
