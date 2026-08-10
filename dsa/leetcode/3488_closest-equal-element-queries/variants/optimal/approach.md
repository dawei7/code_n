## General

**Unroll the circle into two consecutive copies.** Circular distance is awkward only because moving past index $n-1$ returns to zero. The protected source conceptually forms an array of length `m = 2 * n` where unfolded position $i$ contains

`nums[i % n]`.

Now a wrap-around move in the original circle becomes an ordinary forward or backward distance between occurrences in adjacent copies.

Array `d` has one entry per unfolded position and starts at sentinel `2n`. It will store the nearest same-value distance discovered from either direction.

**Find the nearest equal occurrence to the left.** Dictionary `left` maps a value to its most recently seen unfolded index. Scanning `i = 0..2n-1`, if current value `x` already appears in the dictionary, `i - left[x]` is the distance to its nearest previous occurrence. No older occurrence can be closer because the dictionary retains the greatest prior index.

The code minimizes `d[i]` with that distance, then sets `left[x] = i` so later positions see the current occurrence as their nearest left neighbor.

**Find the nearest equal occurrence to the right.** The reverse scan uses dictionary `right` analogously. At unfolded index `i`, a stored `right[x]` is the smallest already visited index greater than `i`, so `right[x] - i` is the nearest distance to the right. Minimizing `d[i]` combines the nearest left and right choices.

For any fixed occurrence on a line, the nearest same value must be its immediate equal neighbor on either side in occurrence order. Farther equal positions cannot beat those two, which is why retaining only one dictionary position per direction is sufficient.

**Combine the two copies of each original index.** Original index $i$ appears at unfolded positions $i$ and $i+n$. The assignment

`d[i] = min(d[i], d[i + n])`

uses whichever copy has the better visible neighbor configuration. Together, the forward and backward scans over both copies include equal occurrences reached across either circular boundary.

Suppose value three occurs at original indices one and five in an array of length seven. Their direct gap is four, while the wrap-around gap is $7-4=3$. In the doubled sequence, one copy of index five lies three positions before the next copy of index one, so one directional scan records distance three. The final minimum returns the circular answer.

**Distinguish a real neighbor from the index's duplicate copy.** Even a value occurring only once in `nums` appears twice in the doubled sequence, at positions $i$ and $i+n$. Their distance is exactly $n$. That is not another original index and must not count.

If a value has a genuinely different occurrence, one of the two circular directions reaches it in fewer than $n$ steps. Therefore, the final result converts any `d[i] >= n` to $-1$. This correctly rejects the artificial duplicate-only match while preserving every real nearest distance.

For a one-element array, the only unfolded match is one full cycle away, so every query returns $-1$.

**Answer queries by constant-time lookup.** After preprocessing all indices, the source returns one value per query:

`-1 if d[i] >= n else d[i]`.

Queries need not be sorted or unique. Repeated queries simply reuse the same precomputed distance, and neither input array is changed.

**Why preprocessing is correct.** The two-copy line contains, around each original occurrence, representatives of the first equal occurrence encountered clockwise and counterclockwise whenever one exists. The forward and backward dictionaries compute exactly the closest equal neighbors on that line. Taking both copies covers wrap-around at either end, and the full-cycle test removes the occurrence paired only with itself. Thus `d[i]` is exactly the minimum circular distance to a different equal-valued index, or correctly signals none.

## Complexity detail

Both unfolded scans visit $2n$ positions and perform expected constant-time dictionary operations. Combining copies visits $n$ positions, and producing answers visits $q$ queries. Total expected time is $O(n+q)$.

`d` has length $2n$. The two dictionaries each store at most one index per distinct value, no more than $n$. Auxiliary space is $O(n)$. These bounds match the manifest.

The code computes the doubled sequence lazily with modulo rather than allocating a second values array, so the only doubled storage is the distance array.

## Alternatives and edge cases

- **Store occurrence lists and binary-search each query:** This gives $O(n+q\log n)$ time; preprocessing every index removes the query logarithm.
- **Scan outward for every query:** Repeated searches can cost $O(nq)$.
- **Check only ordinary index difference:** Circular distance must use the smaller of direct and wrap-around routes.
- **Use only one unfolded copy:** Positions near its ends may not see their wrap-around neighbor on the missing side.
- **Value occurring once:** Its two unfolded copies are distance $n$, which the source converts to $-1$.
- **Value occurring twice:** The answer at either occurrence is the smaller of their direct gap and $n$ minus that gap.
- **Adjacent equal values:** Their minimum distance is one.
- **All values equal:** Every index has an equal neighbor one step away when $n>1$.
- **One-element array:** The artificial full-cycle copy is not another index, so the answer is $-1$.
- **Repeated query indices:** Preprocessing makes each lookup independent and constant time.
- **Unordered queries:** The returned list follows query order because it iterates `queries` directly.
- **Input preservation:** Unlike an editorial variant that overwrites queries, the protected source returns a fresh list.
