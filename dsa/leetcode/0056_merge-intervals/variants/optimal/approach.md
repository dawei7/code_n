## General

**Sorting turns a global overlap problem into a neighbor decision**

Before sorting, an interval may overlap another interval anywhere in the input, so it is difficult to know when a merged group is complete. `intervals.sort()` orders the pairs lexicographically: primarily by start and, for equal starts, by end.

After sorting, interval starts never decrease. Once the next start lies strictly beyond the current merged end, no later interval can reach backward and overlap the current group because every later start is at least as large. That makes it safe to finalize one merged interval and begin another.

**Keep one active merged interval**

`st` and `ed` represent the union of the current connected chain of overlapping intervals. They are initialized from the first sorted pair. The input is guaranteed non-empty, so `intervals[0]` is valid.

For each later `[s, e]`, there are two cases:

- If `ed < s`, a genuine gap separates the active interval from the new one. The active `[st, ed]` is appended to the answer, and `[s, e]` becomes the next active interval.
- Otherwise, `s <= ed`, so the closed intervals overlap or touch. Their union begins at `st` and ends at `max(ed, e)`, so only `ed` needs updating.

The start remains `st` during a merge because sorting guarantees `s >= st`. A new interval may be completely contained inside the active one; taking the maximum keeps `ed` unchanged in that case.

**Why touching endpoints merge**

These are closed intervals. `[1,4]` contains endpoint 4, and `[4,5]` also contains endpoint 4. Their intersection is not empty, so their union is the single interval `[1,5]`.

That is why the gap test is `ed < s`, not `ed <= s`. Equality belongs to the merge case.

**The scan invariant**

Before processing each new sorted interval, `ans` contains finalized, mutually non-overlapping intervals covering all earlier groups except the active group. `[st, ed]` covers exactly the union of that final not-yet-appended overlapping chain. Every interval in `ans` ends before `st`.

If `s <= ed`, the new interval intersects the active union. Extending `ed` to the larger endpoint preserves a single interval covering the same union plus the new input. If `s > ed`, sorting proves neither this nor any later interval can overlap the active group, so appending it is final and starting at `[s,e]` restores the invariant.

After the loop, one active interval remains. The final `ans.append([st, ed])` is necessary because only a later gap triggers an append inside the loop. Omitting it would always lose the last merged group.

**A step-by-step example**

For `[[1,3],[2,6],[8,10],[15,18]]`, the active interval starts as `[1,3]`. Start 2 is not beyond end 3, so the end extends to 6. Start 8 is beyond 6, so `[1,6]` is finalized and `[8,10]` becomes active. Start 15 creates another gap. After the loop, `[15,18]` is appended, producing the expected three groups.

**Why no overlap is missed**

Suppose the algorithm finalizes `[st, ed]` because the next start is `s > ed`. Every unprocessed interval starts at or after `s`, so all begin after `ed`; none can overlap the finalized interval. Conversely, whenever `s <= ed`, the new closed interval intersects the active one, so merging is required. These two exhaustive cases establish both completeness and non-overlap of the returned cover.

**Mutation and copying behavior**

`intervals.sort()` rearranges the caller's outer list. The method then copies endpoint integers into `st` and `ed` and constructs fresh two-element lists when appending to `ans`. It does not modify the original inner interval lists.

The loop uses `intervals[1:]`, which creates a new list of references to all intervals except the first. This is an $O(n)$ temporary allocation. The manifest already allows $O(n)$ space, but the slice is still part of the exact implementation and would be avoidable with index-based iteration.

## Complexity detail

Sorting $n$ intervals costs $O(n \log n)$. The suffix slice and scan each cost $O(n)$, and every scan step does constant work. Overall time is $O(n \log n)$, matching the manifest.

The returned answer may contain $n$ fresh intervals when none overlap, requiring $O(n)$ output space. Independently, `intervals[1:]` allocates $O(n)$ references, and Python sorting may use proportional temporary workspace. The exact auxiliary/storage bound is therefore $O(n)$, consistent with the manifest.

## Alternatives and edge cases

- **Append the first interval and merge into the result tail:** This removes separate `st`/`ed` state, but mutating the tail may alias input interval objects unless copies are made.
- **Sweep-line events:** Sort starts and ends as events to reconstruct covered components. It is more machinery than needed when whole intervals can be sorted directly.
- **Graph connected components:** Treat overlaps as edges and combine components. Building pairwise edges can cost $O(n^2)$ and ignores the order structure.
- **Already disjoint intervals:** Every new start creates a gap, so each interval is copied into the answer separately.
- **Nested intervals:** A contained end does not shrink `ed`; `max` preserves the outer interval.
- **Equal starts:** Lexicographic sorting places smaller ends first, but repeated merges still produce the maximum end correctly.
- **Touching endpoints:** Equality merges because intervals are closed.
- **Single interval:** The loop is empty, and the final append returns a fresh copy of that interval.
- **Empty list outside the contract:** Accessing the first interval would fail; the documented constraint guarantees at least one.
- **Caller-visible ordering:** The outer input list is sorted in place, even though its inner pairs are not modified.
