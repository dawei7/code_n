## General

At any moment, only a suffix of the original array remains. The first value appended from that suffix is more important than every later value because comparison is lexicographic. The source therefore makes the largest possible next MEX, then removes the shortest prefix that achieves it so the remaining suffix retains as much useful information as possible.

**The largest possible next value is the MEX of the whole suffix**

Let $m$ be the MEX of all currently remaining elements. By definition:

- every value $0,1,\ldots,m-1$ occurs somewhere in the suffix;
- value $m$ does not occur anywhere in the suffix.

No prefix can have MEX greater than $m$, because every prefix also lacks $m$. A prefix has MEX exactly $m$ once it contains at least one copy of every value below $m$.

Therefore $m$ is the greatest achievable next result entry. Since lexicographic maximization prioritizes this entry over the complete future, any optimal strategy must choose a prefix whose MEX is $m$.

**Why the shortest qualifying prefix is optimal**

Among prefixes with MEX $m$, the source stops at the first one containing every required value $0$ through $m-1$.

Taking a longer prefix cannot improve the already fixed first result value because $m$ is absent from the entire suffix. It only discards extra elements that could help future segments.

Keeping those elements cannot lower the maximum MEX available to the next step: adding elements to a sequence's set of available values can only leave its MEX unchanged or increase it. If the next values tie, preserving a longer suffix similarly leaves at least as much freedom for later choices. This exchange can be repeated, so the earliest qualifying endpoint gives the lexicographically best tail among choices with the optimal first value.

The algorithm can therefore make this greedy choice independently at every suffix.

**Track the current suffix with `remaining`**

The MEX of an array of length $n$ is at most $n$. The source allocates counts for values zero through $n$ and ignores larger values, because no larger value can affect which integer in that range is first missing.

`remaining[v]` is the number of unconsumed occurrences of $v$. It is initialized from the full input and decremented whenever an element is removed.

The source finds the current suffix MEX by starting at zero and advancing while `remaining[mex] > 0`. This checks precisely which consecutive nonnegative values remain present.

**Build a positive-MEX segment**

Suppose the current `mex` is $m>0$. The segment must contain every value from zero through $m-1$ at least once.

The source stores:

- `segment_mex = mex`, because this is the result value being constructed;
- `unseen = segment_mex`, the number of required distinct values not yet encountered;
- `seen`, a set of required values already encountered in this segment.

It consumes elements from left to right. Every consumed value at most $n$ is removed from `remaining`. If the value is below `segment_mex` and is not already in `seen`, it satisfies one previously missing requirement, so it is inserted and `unseen` decreases.

Repeated copies do not decrease `unseen` again. Values at least $m$ do not matter to this segment's MEX, though they are still consumed and removed from the suffix counts.

The loop stops exactly when `unseen == 0`. At that point all values below $m$ are present, while $m$ is absent from the entire suffix, so the prefix MEX is exactly $m$. Because the scan stopped at the first such moment, this is the shortest qualifying prefix.

**Special case when the suffix MEX is zero**

If `mex == 0`, zero is absent from the entire remaining suffix. Consequently, every nonempty prefix has MEX zero, and every later segment will also have MEX zero.

All obtainable result arrays from this point consist entirely of zeroes. When their common prefix values are equal, the lexicographically larger array is the longer one. Choosing one input element per segment produces the maximum possible number of zero entries.

The source therefore consumes exactly one element, appends zero, and continues. This branch avoids creating an empty `seen` loop and implements the length tie-break correctly.

**Refresh the MEX after a segment**

After a positive-MEX segment is removed, the source recomputes `mex` from zero using the updated `remaining` counts. The next suffix can have a smaller MEX because the segment may have consumed the last copy of a required small value.

It cannot rely on the old MEX or only move the value upward. Resetting to zero is necessary, but it remains linear overall because each positive MEX $m$ required consuming at least $m$ distinct elements in its segment.

**Why the complete result is lexicographically maximal**

At each suffix, the source chooses the greatest possible first entry. No alternative with a smaller first entry can be lexicographically better, regardless of its tail.

Among alternatives with that same entry, the shortest qualifying prefix preserves the largest remaining suffix and cannot worsen the best future result. The zero case maximizes result length when all remaining entries must tie at zero.

Applying the same argument recursively after every removal establishes the complete greedy result.

## Complexity detail

Let $n$ be the input length. Initial frequency construction is $O(n)$. Every array element is consumed exactly once by either the zero branch or a segment-building loop.

Although MEX discovery restarts from zero after each positive segment, scanning up to MEX $m$ can be charged to the at least $m$ distinct required elements consumed by that segment. The sum of all such MEX values is at most $n$. Total time is therefore $O(n)$.

`remaining` uses $O(n)$ integers. A segment's `seen` set holds at most its MEX, and sets from different segments do not coexist. `result` can contain up to $n$ values. Additional space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Try every prefix recursively:** This explores exponentially many partitions. Lexicographic priority determines the next MEX greedily.
- **Choose the whole remaining suffix every time:** It obtains the maximum next MEX but may discard elements that could form valuable later entries. The shortest qualifying prefix gives an equal first value and a better available tail.
- **Stop after seeing each required value without deduplication:** Repeated copies of one value cannot substitute for another required value. The `seen` set makes `unseen` count distinct requirements.
- **Track values greater than `n`:** They cannot affect a MEX bounded by the array length and need no frequency slot.
- **Current MEX zero:** Zero is absent everywhere in the suffix, so consuming one element maximizes the number of tied zero outputs.
- **All values are positive:** The full-array MEX is zero and the answer contains one zero per input element.
- **Input contains every value from zero through `n - 1`:** The first MEX is $n$, the shortest qualifying prefix is the entire array, and the result has one entry.
- **Duplicate required values:** The segment ignores repeats for `unseen` but decrements every occurrence from `remaining`.
- **Last copy of a small value is consumed:** Recomputing from zero makes that value the next suffix MEX.
- **Values equal to `n`:** They are tracked because a length-$n$ array can have MEX $n$.
- **Values larger than `n`:** They are consumed normally but omitted from the count array.
- **Input is not mutated:** The source advances an index and maintains counts rather than deleting prefixes from `nums`.
