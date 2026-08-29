## General

**A boundary may have to be cut more than once.** There are $m-1$ horizontal boundary lines and $n-1$ vertical boundary lines. Once vertical cuts divide the cake into several vertical pieces, applying one horizontal boundary across the original width requires a separate cut in every vertical piece. If there are currently `v` vertical pieces, choosing horizontal boundary cost $a$ adds $a\cdot v$.

Symmetrically, when there are `h` horizontal pieces, a vertical boundary of cost $b$ adds $b\cdot h$.

The order matters because each cut increases the multiplier for every future perpendicular cut.

**Do expensive cuts before they acquire large multipliers.** The greedy rule processes boundary costs from largest to smallest across both orientations. The source first sorts each list descending, then merges the two sorted streams.

Variables `h` and `v` begin at one because the uncut cake is one horizontal piece and one vertical piece. Taking a horizontal cut costs `horizontalCut[i] * v` and increments `h`. Taking a vertical cut costs `verticalCut[j] * h` and increments `v`.

**Prove the local ordering rule by exchange.** Consider one horizontal cost $a$ and one vertical cost $b$ that are adjacent in some proposed schedule, with current piece counts $h,v$.

Doing horizontal then vertical costs

$$
av+b(h+1).
$$

Doing vertical then horizontal costs

$$
bh+a(v+1).
$$

Subtracting gives

$$
[av+b(h+1)]-[bh+a(v+1)]=b-a.
$$

If $a>b$, horizontal-first is cheaper. If $b>a$, vertical-first is cheaper. If equal, both orders cost the same. Therefore any schedule containing a smaller cost immediately before a larger perpendicular cost can be swapped without increasing total cost. Repeated exchanges transform an optimal schedule into global nonincreasing cost order.

Cuts of the same orientation do not change each other's multiplier, so their internal order does not affect cost. Sorting both lists descending and always taking the larger front value realizes a valid globally descending merge.

**Read the exact tie and exhaustion logic.** The condition selects horizontal when the vertical stream is exhausted, or when a horizontal cost remains and is strictly larger than the next vertical cost. Otherwise it selects vertical.

On equal costs, the source takes vertical. The exchange equation shows either order has identical cost, so strict `>` is safe.

Short-circuit evaluation matters: when `j == n - 1`, Python does not evaluate `verticalCut[j]`, which would be out of bounds. Likewise, the second comparison verifies `i < m - 1` before reading the horizontal entry.

**Why every required boundary is processed.** The horizontal array has exactly $m-1$ entries and the vertical array $n-1$. Index `i` increases after every horizontal selection, and `j` after every vertical selection. The loop ends only when both streams are exhausted. Every original boundary cost is therefore used once as a boundary choice, while its multiplier accounts for the number of physical cake pieces along which that boundary must be applied.

**Trace the first example.** For $m=3,n=2$, descending costs are horizontal `[3,1]` and vertical `[5]`. Initially $h=v=1$. Cost five is largest, so cut vertically for $5\cdot1=5$ and set $v=2$. Then horizontal cost three is applied across two vertical pieces for six, and horizontal cost one costs another two. Total is $5+6+2=13$.

For the $2\times2$ example with costs seven and four, horizontal seven is paid once, creating two horizontal pieces. Vertical four is then paid twice, for total $7+8=15$.

## Complexity detail

Sorting $m-1$ horizontal costs takes $O(m\log m)$ time and sorting $n-1$ vertical costs takes $O(n\log n)$. The merge loop performs exactly $m+n-2$ selections, adding $O(m+n)$ time. Total time is $O(m\log m+n\log n)$.

Both lists are sorted in place. Python's Timsort can use $O(m+n)$ temporary auxiliary memory across the two sorts in the worst case. The merge variables use $O(1)$ space. Thus the Python-specific auxiliary bound is $O(m+n)$ as stated in the manifest.

The source mutates both input arrays by reordering them descending. The cost total is safely represented by Python integers.

## Alternatives and edge cases

- **Dynamic programming over cut subsets:** For Cake I's tiny $m,n\le20$, richer DP is conceivable, but it ignores the exchange property and scales poorly compared with sorting.
- **Min-cost-first greedy:** Incorrect. Cheap early cuts increase the multiplier paid by later expensive perpendicular cuts.
- **One combined tagged list:** Store every cost with its orientation, sort globally descending, and update piece counts. This is equivalent but allocates an additional combined array.
- **Equal horizontal and vertical costs:** Either can go first; the source chooses vertical and remains optimal.
- **One row:** `horizontalCut` is empty, `h=1` throughout, and each vertical boundary is paid once.
- **One column:** The symmetric horizontal-only case is handled by stream exhaustion.
- **Both dimensions one:** Both arrays are empty, the loop never runs, and cost is zero.
- **Repeated costs:** Sorting retains all boundary occurrences; each boundary is still processed once.
- **Positive costs:** The exchange argument works cleanly, and no required cut should be omitted.
- **Piece counts, not completed cuts:** After $x$ horizontal boundaries have been processed, `h=x+1` horizontal pieces exist.
- **Short-circuit safety:** Exhausted-array checks must precede indexed comparisons.
- **Input mutation:** Both cost arrays are permanently sorted descending.
- **Constraint difference from Cake II:** This source and proof already scale beyond the small Cake I limits; the greedy rule does not rely on $m,n\le20$.
