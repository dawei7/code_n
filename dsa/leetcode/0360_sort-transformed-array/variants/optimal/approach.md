## General

Applying $f(x)=ax^2+bx+c$ to an ascending array does not necessarily preserve its order. When the graph bends upward, values near the parabola's vertex are small and values farther away are large. When it bends downward, the reverse is true. Sorting the transformed values from scratch would work, but it would ignore the useful fact that the original $x$ values are already ordered.

The exact solution keeps two pointers, `i` at the smallest remaining input and `j` at the largest. At every step it transforms both endpoints. The sign of $a$ tells whether one of those endpoint values is the largest or the smallest transformed value among all remaining inputs, so that value can be placed directly into its final output position.

**The helper evaluates the exact polynomial.**

The local function `f(x)` returns `a * x * x + b * x + c`. It avoids storing a separate transformed array. Each loop iteration evaluates only the currently exposed left and right endpoints.

The input contains integers and all coefficients are integers, so every transformed result is an integer. Duplicate input values or different inputs that produce equal outputs remain separate occurrences because the algorithm performs exactly one placement per input position.

**Why endpoints contain an extreme.**

Consider only the currently unprocessed values `nums[i]` through `nums[j]`. They occupy a closed interval of $x$ values, possibly with gaps and duplicates.

If $a>0$, the quadratic is convex: its graph opens upward. A convex function's maximum over a closed interval occurs at an endpoint. The minimum may be near the vertex in the interior, but the largest remaining transformed value must be either `f(nums[i])` or `f(nums[j])`.

If $a<0$, the quadratic is concave and opens downward. Its minimum over a closed interval occurs at an endpoint. The maximum may be internal, but the smallest remaining transformed value must be one of the two endpoint results.

If $a=0$, the function is linear, $f(x)=bx+c$. A linear function is monotone increasing, monotone decreasing, or constant, so both its minimum and maximum over the remaining interval occur at endpoints. The source groups this case with `a <= 0` and repeatedly selects the smaller endpoint value, which is valid for every sign of $b$.

These endpoint properties continue to hold after one pointer moves inward, because the remaining inputs still form an ordered subarray and therefore lie within a smaller closed interval.

**Upward parabola: fill the answer from the end.**

When `a > 0`, the method compares `y1 = f(nums[i])` and `y2 = f(nums[j])`. The larger one is the largest value still unplaced. It belongs at index `n - k - 1`, moving from the last output position toward the first as `k` increases.

If `y1 > y2`, the left endpoint supplies that maximum and `i` advances. Otherwise the right endpoint is used and `j` retreats. Equality may choose the right copy; either choice is safe because equal values are interchangeable in sorted order and both occurrences will eventually be placed.

Filling from the back is essential. The first extremes found for an upward parabola are large, not small. Writing them from left to right would produce descending order.

**Downward parabola or line: fill from the beginning.**

When `a <= 0`, one endpoint supplies the smallest remaining transformed value. The source writes it at `ans[k]`, so output positions are filled from left to right.

If `y1 > y2`, the right endpoint value `y2` is smaller, so it is written and `j` moves left. Otherwise `y1` is no larger, so the left value is written and `i` moves right. Again, ties can be resolved either way.

For a downward parabola, the endpoints begin near the low outer arms and movement proceeds toward the high vertex. For a linear function, the comparisons effectively detect whether transformed order follows the input or is reversed.

**A trace for an upward parabola.**

Use `nums = [-4,-2,2,4]` and $f(x)=x^2+3x+5$. Endpoint transformations initially are `9` and `33`, so `33` goes in the last output slot and the right pointer moves. Next, `f(-4)=9` and `f(2)=15`, so `15` takes the next slot from the right. The remaining endpoint values are `9` and `3`; `9` is placed, followed by `3`. The output becomes `[3,9,15,33]` without a sorting pass.

**A trace for a downward parabola.**

With $f(x)=-x^2+3x+5$ on the same inputs, endpoint values are `-23` and `1`. The smaller `-23` goes at output index zero. After moving the left pointer, endpoint results are `-5` and `1`, so `-5` follows. Continuing produces `[-23,-5,1,7]` in ascending order.

**Why the final array is sorted and complete.**

For `a > 0`, before each iteration the unfilled prefix of `ans` is reserved for the unprocessed values. The algorithm identifies the maximum of those values and writes it into the rightmost remaining slot. This preserves the invariant that the filled suffix is sorted and contains the correct largest results.

For `a <= 0`, it identifies the minimum and writes it into the leftmost remaining slot. The filled prefix is therefore sorted and contains the correct smallest results.

Exactly one pointer moves on every iteration, so exactly one input occurrence is consumed. The loop runs exactly $n$ times, including the final iteration when both pointers identify the same remaining position. Thus every transformed occurrence is written once, no value is lost, and the output is ascending.

## Complexity detail

Let $n$ be the length of `nums`. The loop has exactly $n$ iterations. Each iteration performs two constant-time polynomial evaluations, one comparison, one output assignment, and one pointer update. Total running time is $O(n)$, satisfying the follow-up.

The preallocated `ans` list contains $n$ integers and therefore uses $O(n)$ space, matching the manifest when required output storage is counted. Apart from the output, the two pointers, loop index, endpoint values, and helper invocation use $O(1)$ auxiliary space.

The method does not mutate `nums`. It also avoids a separate $O(n)$ transformed-values list followed by comparison sorting. In fixed-width languages, one should choose a numeric type wide enough for $ax^2+bx+c$; Python integers grow automatically, and the published bounds are small in any case.

## Alternatives and edge cases

- **Transform then sort:** Map every input through `f` and sort the results. This is simple and correct but costs $O(n\log n)$ time, missing the linear follow-up.

- **Find the vertex and merge outward:** Locate $-b/(2a)$, split inputs around it, and merge transformed monotone runs. This can also run in $O(n)$ but requires more careful boundary and sign handling than endpoint extremes.

- **`a = 0`, positive `b`:** The transformation is increasing, so the left endpoint is repeatedly selected and the output follows input order.

- **`a = 0`, negative `b`:** The transformation is decreasing, so the right endpoint is repeatedly selected, reversing the relevant input order into ascending transformed order.

- **`a = 0`, `b = 0`:** Every transformed value equals `c`. Endpoint ties choose the left copy, and the result contains `n` identical values.

- **Vertex outside the input range:** The quadratic is monotone across all supplied values. Endpoint selection still works; no explicit vertex test is needed.

- **Duplicate inputs:** Each position is consumed independently, so duplicate transformed results appear with the correct multiplicity.

- **Different inputs with equal outputs:** Symmetric points around the vertex can transform equally. Tie handling chooses either endpoint first and preserves both copies.

- **One input element:** Both pointers reference it. One transformed value is written, one pointer moves, and the result has length one.

- **Why the sign test is `a > 0`:** Only an upward-opening quadratic requires taking maxima and filling backward. The `else` branch correctly covers downward quadratics and every linear special case.

- **No floating-point vertex calculation:** The source relies only on integer evaluations and comparisons, avoiding rounding concerns near $-b/(2a)$.
