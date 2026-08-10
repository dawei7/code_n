## General

**Orient the problem so the first sum is smaller**

The exact solution computes `s1 = sum(nums1)` and `s2 = sum(nums2)`. If they are already equal, zero operations are required.

The remaining logic assumes `s1 < s2`. When `s1 > s2`, the method calls itself with the arrays swapped. On that second call, the smaller-sum array is first, so no further swap occurs.

This normalization lets every useful operation be described as reducing one positive gap:

`d = s2 - s1`.

**Compute how much each element can close the gap**

For an element `v` in the lower-sum `nums1`, increasing it as far as six can raise that sum by at most:

`6 - v`.

For an element `v` in the higher-sum `nums2`, decreasing it as far as one can lower that sum by at most:

`v - 1`.

Either change closes the same gap. The source concatenates all these maximum improvements into `arr`.

Each capacity lies from zero through five. Capacity zero represents an element already at the unhelpful extreme: a six in the low array cannot increase, and a one in the high array cannot decrease.

**Why one maximum capacity per element is enough**

One operation may change an element directly to any value from one through six. There is never a reason to spend two operations gradually changing the same element; the final desired value could have been assigned in the first operation.

Thus each array position contributes at most one useful action whose greatest gap reduction is its capacity. If the final operation needs less than full capacity, that element can be changed by only the remaining amount because any intermediate value in the allowed range is permitted.

**Take the largest improvements first**

The exact source sorts `arr` in descending order. It subtracts capacities from `d` one by one and returns the one-based iteration number as soon as `d <= 0`.

For any fixed number $k$ of operations, choosing the $k$ largest capacities gives the greatest possible total gap reduction. If those $k$ capacities cannot cover `d`, no other set of $k$ elements can.

Therefore the first prefix length whose cumulative capacity reaches the gap is the minimum operation count.

This is a standard greedy exchange argument: if a chosen set contains a smaller capacity while an unchosen larger capacity exists, swapping them cannot reduce the total improvement.

**Why overshooting causes no problem**

The loop subtracts each element's maximum capacity and may make `d` negative. That does not mean the actual array sums must cross.

On the final selected element, use only the remaining positive gap rather than its full capacity. Because capacity is the maximum adjustable amount and values can change to any integer between one and six, every smaller nonnegative adjustment up to that capacity is achievable.

Hence cumulative maximum capacity at least `d` is sufficient for exact equality.

**Detect impossibility naturally**

If all capacities are consumed and `d` is still positive, even changing every useful element to its extreme cannot close the original sum difference. The method then returns minus one.

This covers length-based impossible cases such as seven ones versus one six. The low array cannot decrease and the high array cannot increase under the normalized direction; the total useful capacity is too small.

No separate feasibility formula is needed because the capacity scan calculates the exact available improvement.

**Trace the greedy reasoning**

Suppose the gap is ten and available capacities begin five, five, four. One operation can close at most five, so one is insufficient. The first two capacities total ten, so two operations suffice and are minimal.

Choosing a capacity four before an available five could not reduce the operation count. Sorting ensures the most powerful changes are always considered first.

**Why the returned count is correct**

Every capacity describes the maximum gap reduction achievable with one operation on a distinct element. The descending prefix of length $k$ has at least as much total capacity as any other $k$ operations.

If the loop first reaches `d <= 0` at operation $k$, those $k$ elements can close the gap exactly, while no set of fewer elements has enough capacity. If it never reaches zero, no collection of allowed changes can equalize the sums. Thus the returned $k$ or minus one is correct.

## Complexity detail

Let $N=\lvert\texttt{nums1}\rvert+\lvert\texttt{nums2}\rvert$. Computing sums and building capacities takes $O(N)$ time. The exact source then calls `sorted(arr, reverse=True)`, which takes $O(N\log N)$ time, followed by an $O(N)$ scan. A one-time recursive swap repeats linear sum work but does not change the bound. Exact time is $O(N\log N)$.

This does not match the manifest's $O(n+m)$ target. Because capacities are only zero through five, a six-bucket frequency count could process them in linear time, but the current `solution.py` uses comparison sorting.

`arr` stores $N$ capacities, and `sorted` creates a second list while `arr` remains live. Peak auxiliary space is $O(N)$, not the manifest's $O(1)$. The recursion depth is at most two calls.

## Alternatives and edge cases

- **Six gain buckets:** Count capacities zero through five and consume from five downward, achieving $O(n+m)$ time and $O(1)$ auxiliary space under the fixed value domain.
- **Max heap:** Repeatedly take the largest gain, but heap construction and pops are more expensive than six counters.
- **Change arbitrary elements:** Without prioritizing capacity, extra operations may be used unnecessarily.
- **Already equal sums:** The early return gives zero before building capacities.
- **First sum larger:** One recursive swap normalizes the direction.
- **Capacity zero:** Such an action cannot help and will appear only after all positive gains in descending order.
- **Final capacity larger than gap:** Use only the needed partial value change.
- **Insufficient total capacity:** The loop ends and returns minus one.
- **One-element arrays:** The same capacity rules determine reachability and count.
- **Different lengths:** Length affects total capacity but needs no separate algorithm.
- **Values at one:** They have increase capacity five in the low array and decrease capacity zero in the high array.
- **Values at six:** They have increase capacity zero in the low array and decrease capacity five in the high array.
- **Negative gap avoided:** Swapping ensures `d` begins positive in the main greedy path.
- **One operation per position:** Direct assignment to any allowed value makes repeated edits to one element unnecessary.
- **Input preservation:** Capacities are derived into a new list; neither input array is modified.
