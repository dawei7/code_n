## General
**Separate searchable starts from original positions**

Create `(start, original_index)` pairs and sort them by start. The original interval order remains untouched, while the sorted starts form the monotone search space needed for every query.

**Find the lower bound of each end**

For an interval ending at `end`, binary-search for the first sorted start that is at least `end`. If the insertion position is inside the array, its paired original index is the answer; if it equals `n`, no right interval exists.

**Why the lower bound is exactly the requested interval**

Every sorted position before the lower bound has a start smaller than the current end and is invalid. The lower-bound position, when present, is valid and no later position can have a smaller start. Unique starts make its original index unambiguous.

## Complexity detail
Sorting the `n` indexed starts costs $O(n \log n)$. Each of `n` binary searches costs $O(\log n)$, so total time remains $O(n \log n)$. The sorted pairs, start array, and output use $O(n)$ space.

## Alternatives and edge cases
- **Two sorted sweeps:** sort starts and ends separately, then advance a start pointer to answer every end in $O(n \log n)$ total time.
- **Scan every interval for every query:** directly tracks the smallest valid start but takes $O(n^2)$ time.
- **One interval:** it usually has no right interval because its end exceeds its own start.
- **Negative coordinates:** ordering and lower bounds work unchanged.
- **Exact endpoint match:** a start equal to the current end is valid.
- **No qualifying start:** return `-1` for that position.
