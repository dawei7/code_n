## General

**Each index asks for one range sum.** For index $i$, the required subarray ends at $i$ and begins at

$$
\textit{start}_i
=
\max(0,i-\texttt{nums}[i]).
$$

Computing that subarray by looping over its elements would repeat work because neighboring requests overlap heavily. Prefix sums turn every requested range into one subtraction.

The source constructs

`s = list(accumulate(nums, initial=0))`.

The initial zero shifts the prefix array so that

$$
\texttt{s}[t]
=
\sum_{j=0}^{t-1}\texttt{nums}[j].
$$

Thus `s[0] = 0`, `s[1] = nums[0]`, and `s[n]` is the sum of the whole input.

For any inclusive range `nums[left ... right]`, subtract the prefix before `left` from the prefix after `right`:

$$
\sum_{j=\textit{left}}^{\textit{right}}\texttt{nums}[j]
=
\texttt{s}[\textit{right}+1]-\texttt{s}[\textit{left}].
$$

At the current `i` with value `x`, the source substitutes `right = i` and `left = max(0, i - x)`:

`s[i + 1] - s[max(0, i - x)]`.

The generator evaluates this expression once for every `(i, x)` from `enumerate(nums)`. The outer `sum` adds all defined subarray sums into the answer.

**Be precise about the subarray length.** When `i - nums[i] >= 0`, the range begins `nums[i]` positions before $i$ and includes both endpoints. Its length is therefore `nums[i] + 1`, not `nums[i]`. If that start would be negative, `max(0, ...)` clamps it to the beginning and the subarray contains all elements from index zero through $i$.

For `nums = [2,3,1]`:

- $i=0$, $x=2$, so start is zero and the sum is `s[1] - s[0] = 2`;
- $i=1$, $x=3$, so start is again zero and the sum is `s[2] - s[0] = 5`;
- $i=2$, $x=1$, so start is one and the sum is `s[3] - s[1] = 4`.

Their total is $11$.

For the second example, the final value $2$ at index $3$ gives start $1$, selecting indices $1,2,3$. The formula uses `s[4] - s[1]` and obtains $4$ without revisiting those elements individually during prefix construction.

**Why every contribution is exact.** The prefix invariant follows by construction: `accumulate` successively adds each next input value, and the initial zero represents an empty prefix. Subtracting two prefixes cancels every element before `start` and leaves exactly indices `start` through $i$. The clamped expression is identical to the statement's definition. Summing these exact per-index quantities returns the requested total, with each element counted as many times as the independently defined subarrays include it.

The approach does not modify `nums`. `accumulate` reads its values and the `list` call creates a separate prefix array.

All input values are positive under the constraints. Positivity is not needed for the prefix subtraction itself, but it ensures `i - x <= i`, so the defined start never lies after the ending index. The clamp handles starts before zero.

**The expression is compact but contains two lazy/eager layers.** `accumulate` is an iterator, but wrapping it in `list` eagerly stores all $n+1$ prefix values for later random access. The range-sum generator passed to `sum` is lazy and holds only the current index and value. Random access into `s` is what makes each later query constant time.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Constructing the prefix list visits each element once, taking $O(n)$ time. The generator then performs one constant-time start calculation and prefix subtraction for each index, taking another $O(n)$. Total time is $O(n)$.

The prefix list contains $n+1$ integers, so auxiliary space is $O(n)$. The generator and accumulation result use constant additional state beyond that list. These bounds match the manifest.

## Alternatives and edge cases

- **Nested summation:** Summing `nums[start:i+1]` separately for every index can take $O(n^2)$ time when many starts clamp to zero.
- **Slice plus `sum`:** This also allocates temporary slices and repeats additions; prefix differences avoid both.
- **Running total only:** A single total of the entire prefix cannot answer arbitrary earlier start points because each `nums[i]` chooses a different start. The complete prefix array provides random access.
- **Start clamped to zero:** When `nums[i] > i`, the range simply includes the entire prefix through $i$.
- **Value equal to zero:** Although excluded by the stated constraints, the formula would select only `nums[i]` because start would equal $i$.
- **First index:** `max(0, 0 - nums[0])` is zero, and the first contribution is always `nums[0]`.
- **Inclusive endpoint:** Using `s[i]` rather than `s[i+1]` would omit the current element. The shifted prefix convention prevents that off-by-one error.
- **Length interpretation:** An unclamped range contains `nums[i] + 1` elements because it includes the current index and that many positions before it.
- **Large total:** An element may contribute to many subarray sums. Python integers grow as necessary and avoid fixed-width overflow.
- **Input preservation:** The source allocates `s` but never sorts, slices, or changes `nums` itself.
