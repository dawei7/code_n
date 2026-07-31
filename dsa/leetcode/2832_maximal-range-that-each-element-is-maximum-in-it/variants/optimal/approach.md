## General

Fix an index `i`. A range containing `i` can keep `nums[i]` as its maximum while it expands across neighboring values smaller than `nums[i]`. Expansion must stop immediately before the nearest greater value on either side. Since all values are distinct, equality never complicates the boundary.

Let $L_i$ be the index of the nearest value greater than `nums[i]` to the left, or $-1$ if none exists. Let $R_i$ be the corresponding index to the right, or $n$ if none exists. Every value strictly between these blockers is smaller than `nums[i]`, so the maximal valid range is

$$
[L_i+1,\ R_i-1]
$$

and its length is $R_i-L_i-1$.

**Nearest greater value on the left**

Scan from left to right while maintaining indices whose values decrease from the bottom of a stack to its top. Before processing `nums[i]`, pop every smaller top value: it cannot block `nums[i]`, and the current larger value will be a nearer blocker for future elements. The remaining top, if present, is $L_i$.

Store the left-hand contribution `i - L_i`, which counts indices from $L_i+1$ through `i`.

**Nearest greater value on the right**

Clear the stack and perform the symmetric scan from right to left. After removing smaller values, the remaining top is $R_i$ when it exists. Add `R_i - i - 1`, the number of valid indices strictly to the right of `i`. The sum is exactly $R_i-L_i-1$.

**Why the stack top is the nearest blocker**

Indices enter in scan order. Popped indices have smaller values and therefore cannot bound the current element. Any earlier greater index below the top is farther away than the surviving top. Thus the top is simultaneously greater and nearest. Each computed interval contains no greater value, so it is valid; extending it by one position would cross a nearest greater blocker whenever one exists, proving maximality.

## Complexity detail

Let $n$ be the length of `nums`. Each index is pushed once and popped at most once in each directional pass. Both passes therefore take $O(n)$ time. The answer and stack require $O(n)$ space.

The benchmark uses $n$ as `size` and strictly increasing inputs. A direct expansion from every index must rescan its entire prefix, while the monotonic stack still processes every index only a constant number of times.

## Alternatives and edge cases

- **Single pass with a sentinel:** Append a conceptual value larger than every input and finalize an index when it is popped. This can compute both blockers in one pass but requires more delicate span bookkeeping.
- **Segment tree plus searches:** Range-maximum queries combined with binary searches can locate both blockers in $O(n \log n)$ total time and use $O(n)$ space.
- **Direct expansion:** Walk left and right from every index until reaching a greater value. It is correct but takes $O(n^2)$ time on monotone arrays.
- **Single element:** With no blockers, the sole answer is $1$.
- **Global maximum:** The largest value has no greater blocker and therefore owns the full array length.
- **Increasing input:** Every element owns the prefix ending at its index.
- **Decreasing input:** Every element owns the suffix beginning at its index.
- **Distinctness:** Strict comparisons are sufficient because equal values cannot occur.
