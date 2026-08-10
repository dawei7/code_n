## General

**Area depends on the shorter endpoint and the distance**

For a pair of line indices `i < j`, the width is `j - i`. Horizontal water can rise only to the shorter line, so the pair stores

$$
(j-i)\min(\texttt{height[i]},\texttt{height[j]}).
$$

The method starts with the outside pair, which has maximum possible width:

```python
max_area, i, j = 0, 0, len(height) - 1
```

Each iteration records that pair's area, then removes one endpoint whose remaining pair possibilities are provably dominated.

**The shorter endpoint is the only side worth replacing**

Suppose `height[i] < height[j]`. The current pair is limited by `height[i]`. If `j` moves inward while `i` stays fixed, width decreases and the limiting height can never exceed `height[i]`, regardless of how tall the new right line is. Every such area is smaller than the current one.

Formally, for every `k` with `i < k < j`:

$$
\begin{aligned}
A(i,k)
&= (k-i)\min(\texttt{height[i]},\texttt{height[k]}) \\
&\le (k-i)\texttt{height[i]} \\
&< (j-i)\texttt{height[i]} \\
&= A(i,j).
\end{aligned}
$$

The method has already compared `A(i,j)` with `max_area`. Therefore no unseen pair using endpoint `i` can improve the answer, and `i += 1` safely discards all of them at once.

If the right line is shorter, the symmetric proof shows that every unseen pair retaining `j` is dominated, so `j -= 1` is safe.

**Tie handling in this exact implementation**

The branch is

```python
if height[i] < height[j]:
    i += 1
else:
    j -= 1
```

Equal heights go to the `else` branch. This is safe because the current pair uses that shared height and the largest width available to either endpoint within the active interval. Retaining the right endpoint while moving the left inward cannot beat it, and retaining the left while moving the right inward cannot beat it. The code chooses to discard the right endpoint; discarding the left or both would also be logically safe after the current area is recorded.

**Why area is measured before pointer movement**

The line

```python
max_area = max(max_area, min(height[i], height[j]) * (j - i))
```

must precede elimination. The proof says future pairs with the shorter endpoint cannot beat the **current pair**. If that current value were never placed into `max_area`, discarding the endpoint could throw away the best numerical result without saving it.

After recording, the proof licenses removal. This measure-then-eliminate order repeats until `i == j`, when no two distinct lines remain.

**Walk through the decisive early moves**

For `[1,8,6,2,5,4,8,3,7]`:

1. Pair `(0, 8)` has area `min(1, 7) * 8 = 8`. The left height is shorter, so index `0` is discarded.
2. Pair `(1, 8)` has area `min(8, 7) * 7 = 49`. The right height is shorter, so index `8` is discarded only after `49` is saved.
3. Pairs `(1, 7)` and `(1, 6)` produce `18` and `40`. They cannot exceed the saved `49`.

This shows the width/height tradeoff. The two height-`8` lines are not optimal because their width is only `5`; height `7` at a farther index gives the larger product.

**The surviving interval always contains every unresolved possibility**

At the start, all pairs lie between `i = 0` and `j = n - 1`. On each iteration, the method proves that all unresolved pairs containing one endpoint are no better than an area already considered. Removing that endpoint deletes only resolved, dominated candidates.

By induction, any pair that could still improve `max_area` has both endpoints inside the new interval. When the pointers meet, no candidate pair remains unresolved. The saved maximum is therefore the global optimum.

## Complexity detail

Let $n = \lvert\texttt{height}\rvert$.

- **Time complexity: $O(n)$.** Exactly one pointer moves inward per iteration. `i` can increase at most `n - 1` times, and `j` can decrease at most `n - 1` times, but their combined movement before meeting is only `n - 1`. Each iteration performs constant work.
- **Space complexity: $O(1)$.** `max_area`, `i`, and `j` are the only persistent local state. No additional structure grows with the input.

The fixed-width geometry is evaluated directly from the original array; no preprocessing phase changes these bounds.

## Alternatives and edge cases

- **Optimal variant implementation:** It is the same two-pointer algorithm with variables named `l`, `r`, `t`, and `ans`. Both variants use the same strict comparison and move the right pointer on ties.
- **All-pairs enumeration:** Straightforward and useful for deriving the area formula, but $O(n^2)$ pairs are infeasible at the maximum input size.
- **Choose the tallest two lines:** This ignores their distance. A slightly shorter line far away can create a larger container.
- **Move the taller side first:** The shorter retained side still caps height while width shrinks, so this cannot reveal an improvement involving that shorter endpoint.
- **Move both endpoints every time:** On unequal heights, the taller endpoint has not been proved disposable; moving it too can skip the optimum.
- **Equal heights:** The code moves `j`; either endpoint could be safely removed after evaluation.
- **Two-element input:** The single iteration calculates the only possible container.
- **Zero at one endpoint:** Current area is zero and the zero-height limiting endpoint is discarded.
- **All zeros:** Every area is zero, and the initialized maximum remains correct.
- **All equal heights:** The outermost pair is optimal because every later pair has the same height limit and smaller width.
- **Large width versus large height:** The algorithm does not assume one always wins. It evaluates each nondominated tradeoff encountered by safe eliminations.
- **Horizontal-water rule:** `min` is mandatory. Using `max` or an average would allow water above the shorter wall and violate the container model.
- **Input preservation:** Pointer movement changes only indices, not line heights or order.
