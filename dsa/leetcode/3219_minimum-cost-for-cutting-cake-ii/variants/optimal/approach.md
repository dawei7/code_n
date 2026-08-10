## General

**Count how many physical cuts each boundary requires.** A horizontal boundary has one listed base cost, but after vertical cuts split the cake into `v` vertical strips, that boundary must be applied separately to all `v` affected pieces. Its current total contribution is base cost times `v`. A vertical boundary analogously costs its base value times the current number `h` of horizontal strips.

Every horizontal cut increases `h` by one and thereby makes all later vertical boundaries more expensive. Every vertical cut increases `v` and makes later horizontal boundaries more expensive. The goal is to place costly boundaries before the opposite multiplier grows.

**Sort each orientation descending.** The source mutates `horizontalCut` and `verticalCut` into nonincreasing order. Two pointers `i` and `j` identify the largest unprocessed cost in each orientation.

At each step:

- choose horizontal if no vertical cost remains, or its next cost is strictly larger;
- otherwise choose vertical.

A horizontal choice adds `horizontalCut[i] * v`, increments the horizontal piece count `h`, and advances `i`. A vertical choice adds `verticalCut[j] * h`, increments `v`, and advances `j`.

This is the merge phase of merge sort applied to two descending sequences, augmented with perpendicular multipliers.

**Why descending order is optimal.** Consider adjacent choices of different orientations with costs $a$ horizontal and $b$ vertical. Before them, let piece counts be $h$ and $v$.

Horizontal first costs

$$
av+b(h+1),
$$

while vertical first costs

$$
bh+a(v+1).
$$

The first ordering minus the second is $b-a$. If $a\ge b$, horizontal first is no more expensive. If $b\ge a$, vertical first is no more expensive. Thus the larger base cost can always be moved before the smaller perpendicular cost without worsening the schedule.

By repeatedly removing inversions in any schedule, there is an optimal schedule in global descending base-cost order. Same-orientation choices can be reordered freely because they do not change the multiplier applied to one another. The two sorted arrays and greedy merge produce exactly such a schedule.

When costs tie, either order has the same contribution. The exact code's strict comparison sends a tie to the vertical branch, which is safe.

**Why the multipliers represent the real cutting process.** Initially, the whole cake is one piece in each orientation, so `h=v=1`. After $x$ horizontal boundaries have been completed across all current vertical strips, the cake has $x+1$ horizontal bands. Any future vertical boundary must be cut once in every such band, hence multiplier `h`. The symmetric statement holds for `v`.

Although the implementation speaks of processing a boundary once, multiplying by the perpendicular piece count accounts for all separate physical operations along that line.

**Loop completeness and index safety.** There are $m-1$ horizontal and $n-1$ vertical entries. The loop continues while either pointer has work. Every iteration advances exactly one pointer, so it terminates after $m+n-2$ choices and processes every required boundary.

The condition tests whether the vertical list is exhausted before reading `verticalCut[j]`. Its second part tests the horizontal bound before reading `horizontalCut[i]`. Python's short-circuit rules prevent out-of-range access.

**Trace $m=3,n=2$.** Horizontal costs sort to `[3,1]` and vertical to `[5]`. Vertical five is processed first at multiplier one. It creates two vertical strips. Horizontal three and one are each then paid twice. Total is $5+6+2=13$.

The large Cake II limits make the greedy proof essential. A search over cut orders would face $(m+n-2)!$ interleavings in the worst case, while the exchange rule reduces the problem to sorting.

## Complexity detail

Sorting costs $O(m\log m+n\log n)$ time. The merge visits $m+n-2$ entries once, so it adds $O(m+n)$ time and sorting dominates.

Python sorts both caller-provided lists in place. Timsort may allocate $O(m+n)$ temporary memory in the worst case across the operations; the pointers and counters use constant space. Thus auxiliary space is $O(m+n)$ under the manifest's Python-specific convention.

With dimensions up to $10^5$ and costs up to $10^3$, the result can exceed 32-bit signed range. Python integer arithmetic grows as needed.

## Alternatives and edge cases

- **One globally sorted tagged array:** Combine horizontal and vertical costs with tags, sort descending, then update counts. It is correct but allocates an explicit $O(m+n)$ combined structure.
- **Frequency counting by cost:** Costs are bounded by $1000$. Count horizontal and vertical occurrences at each cost and scan costs downward, potentially reducing sorting to $O(m+n+1000)$ time. The exact source does not exploit this bound.
- **Priority queues:** Repeatedly pop the larger next cost from two max-heaps. This matches the greedy order but adds heap overhead when arrays can simply be sorted once.
- **Dynamic programming:** Dimension limits make state-based cut-order search infeasible; the exchange proof supplies the scalable structure.
- **Equal next costs:** Either orientation is optimal locally. Choosing vertical on ties does not affect the minimum total.
- **Only horizontal boundaries:** With one column, every horizontal cost has multiplier one.
- **Only vertical boundaries:** With one row, every vertical cost has multiplier one.
- **A $1\times1$ cake:** No cut arrays contain entries, and the answer is zero.
- **Repeated boundary costs:** Every occurrence represents a distinct line and must remain in the sorted streams.
- **Large expensive cut:** Processing it early avoids multiplying it by many perpendicular pieces.
- **Positive-cost guarantee:** All boundaries are required, and there is no negative-cost incentive that would alter exchange reasoning.
- **Input mutation:** The arrays are returned to the caller in descending order rather than their original order.
- **Short-circuit condition:** Reordering its terms carelessly can index an exhausted list.
- **Cake I versus II:** The algorithm is identical, but II's large limits make the $O(m\log m+n\log n)$ bound particularly important.
