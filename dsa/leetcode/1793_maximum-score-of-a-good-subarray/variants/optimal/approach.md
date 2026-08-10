## General

**Fix which value acts as the minimum**

The score of a subarray is its minimum value multiplied by its length. For each index $i$, imagine that `nums[i] = v` is the minimum of the chosen subarray. To maximize the score for that fixed minimum, extend as far left and right as possible while every included value remains at least $v$.

The resulting candidate is useful only if its interval contains the required index $k$. A monotonic stack finds the relevant boundaries for every $i$ in linear time.

**Find the nearest strictly smaller value on the left**

The first scan moves from left to right. Stack `stk` stores indices whose values form a strictly increasing sequence after cleanup.

For current value `v = nums[i]`, the solution pops while `nums[stk[-1]] >= v`. Every popped index is unusable as a smaller boundary because its value is equal to or greater than $v$. After the popping:

- if the stack is nonempty, its top is the nearest index to the left whose value is strictly less than $v$, so it becomes `left[i]`;
- if the stack is empty, no smaller value exists to the left, and the sentinel `left[i] = -1` remains.

The current index is then pushed for future elements.

Thus every position from `left[i] + 1` through $i$ has value at least $v$, while including `left[i]`, when it exists, would introduce a smaller minimum.

**Find the nearest smaller-or-equal value on the right**

The second scan moves from right to left with a fresh stack. This time it pops while the top value is strictly greater than `v`, not greater than or equal.

After cleanup, the top is the nearest right index whose value is less than or equal to $v$. It becomes `right[i]`. If there is no such index, the sentinel `n` remains.

The usable candidate interval for $i$ is therefore

$$
[\texttt{left}[i]+1,\ \texttt{right}[i]-1],
$$

with length `right[i] - left[i] - 1`. Every value inside is at least $v$, so this interval's minimum is $v$.

**Why the left and right comparisons treat equality differently**

The asymmetric tie rule prevents equal values from blocking every copy of a plateau. On the left, equal values are popped, so a later equal element can inherit the earlier element's left reach. On the right, equal values remain, so an earlier copy stops just before the next equal copy.

For `[2, 2]`, the first 2 may receive a right boundary at the second 2 and represent only the first position. The second 2 pops the earlier equal value during the left scan, receives left boundary -1, and can represent both positions. At least one equal occurrence owns the full interval, while candidates are not all forced to duplicate it.

This convention is standard for handling duplicate minima. Using strict comparisons on both sides can make several equal indices represent overlapping maximal ranges; using non-strict comparisons on both sides can make each stop at another equal and miss the full plateau. One strict and one non-strict boundary gives complete coverage.

**Evaluate only intervals containing `k`**

For each index $i$, the candidate interval contains $k$ precisely when

`left[i] + 1 <= k <= right[i] - 1`.

When this holds, the solution computes

$$
\texttt{nums}[i]\cdot
(\texttt{right}[i]-\texttt{left}[i]-1)
$$

and maximizes `ans`.

All values are positive, so extending an interval without lowering its minimum can only improve or preserve the score. That is why the maximal boundary interval is the best candidate associated with $v$ and its chosen representative.

**Following the first example**

For `nums = [1,4,3,7,4,5]` and `k = 3`, value 3 at index 2 can extend from index 1 through index 5: index 0 contains 1, which is smaller, and the array ends on the right. The interval length is 5 and its score is `3 * 5 = 15`. It contains index 3, so the final pass considers it.

Other minima may produce shorter intervals or smaller products. Taking the maximum yields 15.

**Why some stack entry represents every optimum**

Take any optimal good subarray and let $v$ be its minimum. Choose the appropriate rightmost occurrence of $v$ within the equal-minimum chain represented by the asymmetric boundary convention. Its computed interval extends at least across the entire optimal subarray: no interior value is below $v$, and equal minima are assigned so that one occurrence crosses the plateau.

The computed interval also contains $k$ because the original subarray does. Since all `nums` values are positive, extending with values at least $v$ cannot lower the score; it keeps minimum $v$ and increases or preserves length. Therefore the candidate evaluated for that occurrence has score at least the optimum. No candidate can exceed the true optimum definition because every evaluated interval is itself a valid good subarray. The maximum is consequently exact.

## Complexity detail

Each index is pushed once and popped at most once in the left scan, so its total stack work is $O(n)$. The same amortized argument applies independently to the right scan. The final candidate loop is another $O(n)$ pass. Total time is $O(n)$, matching the manifest.

The exact protected solution allocates two length-$n$ boundary arrays and a stack that can hold $n$ indices. Its auxiliary space is $O(n)$, not the manifest's stated $O(1)$. The editorial's two-pointer greedy expansion can achieve $O(1)$ space, but that is a different implementation from this monotonic-stack source.

Sentinels -1 and $n$ avoid special formulas at array boundaries; they occupy entries in the existing arrays and do not change the bound.

## Alternatives and edge cases

- **Greedy two-pointer expansion from `k`:** Expand toward the larger adjacent value while tracking the current minimum. It achieves $O(n)$ time and $O(1)$ space, matching the manifest's space target, but it is not the protected implementation.
- **Binary-search boundary method:** Prefix minima and binary searches can solve the problem in $O(n\log n)$ time and $O(n)$ space.
- **Enumerate all good subarrays:** There can be $O(n^2)$ intervals containing $k$, and rescanning minima makes the approach even slower.
- **Range-minimum structure:** Fast minimum queries do not remove the quadratic number of candidate intervals by themselves.
- **Equal values:** The `>=` left pop and `>` right pop deliberately assign a plateau to a later equal occurrence.
- **`k = 0`:** A valid candidate must begin at the first position; the sentinel and containment check handle this directly.
- **`k = n - 1`:** Symmetrically, a candidate must reach the final position.
- **Single element:** Both sentinels remain, width is one, and the answer is `nums[0]`.
- **Strictly increasing array:** Left boundaries are nearby smaller values, while right boundaries often reach the end.
- **Strictly decreasing array:** Left boundaries often reach -1, while right boundaries are nearby smaller values.
- **All equal:** Tie handling ensures one occurrence represents the full array, which is the best good subarray for every valid $k$.
- **Positive-value guarantee:** It justifies expanding a fixed-minimum interval as far as possible; negative values would make greater length potentially harmful.
- **Containment check:** A large rectangle-like score is irrelevant if its interval does not include `k`.
- **Input preservation:** The method stores indices and boundaries without changing `nums`.
