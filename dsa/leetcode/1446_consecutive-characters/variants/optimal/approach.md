## General

**A valid substring is one run of equal characters.** The power of the string is not about how often a character appears in total. It is about the longest contiguous block in which every character is the same. For example, two occurrences of `a` separated by another letter cannot be combined. The string can therefore be viewed as consecutive runs, and the task is to find the maximum run length.

The solution keeps two integers:

- `t` is the length of the equal-character run that ends at the current position.
- `ans` is the largest run length seen anywhere so far.

Both begin at one because the input is guaranteed to be nonempty. Even a one-character string has power one, and before any adjacent pair is examined, the first character already forms a run of length one.

**Use adjacent pairs to detect whether a run continues.** `pairwise(s)` lazily yields `(s[0], s[1])`, then `(s[1], s[2])`, and so on. Each loop iteration names the earlier character `a` and the next character `b`. There are only two cases.

If `a == b`, the new character continues the same run that ended at `a`. The run ending at `b` is one character longer, so the code executes `t += 1`. This extended run might be the longest so far, so it updates `ans = max(ans, t)`.

If `a != b`, the old run ends before `b`. The character `b` begins a new run whose current length is exactly one, so the code resets `t = 1`. There is no need to update `ans` in this branch because `ans` was initialized to one and can never be smaller than the new run length.

The iterator avoids manual indexing. It supplies exactly the comparison needed for every character after the first: compare that character with its immediate predecessor. It does not build a list of all pairs; Python's pairwise iterator advances through the string lazily.

**Understand the invariant after every pair.** After processing pair `(s[p - 1], s[p])`, `t` equals the length of the maximal same-character substring ending at position `p`. Meanwhile, `ans` equals the maximum run length among all positions from zero through `p`.

If the pair is equal, extending the previous run by one establishes the new `t`. Taking the maximum preserves the best earlier run or replaces it with the longer current run. If the pair differs, only `s[p]` belongs to the run ending at `p`, so resetting to one is correct, and the best completed run remains in `ans`. This proves that the invariant is maintained.

When all pairs have been processed, every possible run has ended at some visited position. Consequently, `ans` is the maximum length of any same-character substring, which is exactly the string's power.

**Trace a string with several changes.** Consider `s = "abbcccaa"`. Initially `t = 1` and `ans = 1` for the first `a`. The pair `a, b` differs, so `t` remains one for the new `b` run. The next pair `b, b` matches, changing `t` to two and `ans` to two.

The transition `b, c` resets `t` to one. The next two matching `c` pairs grow it to two and then three, and `ans` becomes three. The transition `c, a` resets the current run, and the final `a, a` pair grows `t` to two. The final answer remains three because the earlier `ccc` run was longer than the ending `aa` run.

This trace also shows why a frequency table is insufficient. The string contains several `a` characters in separate locations, but only adjacent occurrences belong to one candidate substring. The algorithm deliberately forgets an old run's current length at a character change while preserving only the global maximum.

**Why every maximal run is measured exactly.** Take any maximal run occupying positions `l` through `r`. At position `l`, either it is the first character or the preceding character differs, so `t` is one. Every adjacent pair within positions `l` through `r` is equal, causing one increment for each additional character. By the time position `r` is processed, `t` equals `r - l + 1`, the run's full length, and `ans` is updated with it. The next differing pair resets `t` but cannot erase `ans`.

Every value of `t` also represents a real contiguous run because it grows only across equal adjacent pairs and resets immediately across a difference. Thus `ans` can never overstate the answer. Since every maximal run reaches its exact length in `t`, `ans` cannot understate it either.

**Why initialization at one matters.** Starting `t` or `ans` at zero would require special handling for the first character or an update on every iteration. With the nonempty constraint, one is the correct base result. It also handles a single-character input: `pairwise` yields no pairs, the loop does not run, and the function returns one.

The code assumes `pairwise` is available from the supported Python environment. Its semantics are a rolling adjacent iterator. If it were replaced by precomputing `list(pairwise(s))`, the comparisons would be the same but the unnecessary list would consume linear memory.

## Complexity detail

Let `n` be the length of `s`. A nonempty string has exactly `n - 1` adjacent pairs. The loop processes each pair once, doing one character comparison and a constant number of integer operations. Total running time is `O(n)`.

The variables `ans`, `t`, `a`, and `b` occupy constant storage. `pairwise(s)` is lazy and retains only enough iterator state to provide consecutive elements, so it does not copy the string or store all pairs. Auxiliary space is `O(1)`, matching the manifest.

The input string itself is not counted as auxiliary memory because it is supplied by the caller. The returned integer is constant-size under the usual word-RAM model and is at most `n`.

Reading every character is asymptotically necessary. An unseen suffix could extend the final run or contain an even longer new run, so no algorithm can determine the exact answer for arbitrary input without inspecting the string in the worst case. The linear-time scan is therefore optimal.

## Alternatives and edge cases

- **Manual index loop:** Iterate `i` from one through `n - 1` and compare `s[i]` with `s[i - 1]`. This has identical time and space bounds and may be preferable where `pairwise` is unavailable.
- **Track the previous character explicitly:** Loop over characters, store `previous`, and update a count. This is the editorial's equivalent formulation and handles the first character with either a sentinel or a special initialization.
- **Group consecutive characters:** `itertools.groupby` can form each run lazily, after which the maximum group length is measured. It is expressive, but counting each group usually introduces more iterator machinery than the two-counter scan.
- **Frequency map:** Counting total occurrences per character is incorrect because equal letters separated by other characters do not form one substring.
- **Generate every substring:** Testing all substrings repeats work and needs at least quadratic candidates. A run is fully determined by adjacent equality, so one pass is sufficient.
- **Sort the characters:** Sorting destroys original adjacency, which is the defining property of a substring. It would answer a different frequency question.
- **One-character string:** There are no adjacent pairs. The initial value one is returned, which is the only nonempty substring's length.
- **All characters equal:** Every pair matches, `t` grows from one to `n`, and `ans` finishes at `n`.
- **All neighboring characters different:** Every iteration resets `t` to one. The power is one.
- **Longest run at the beginning:** `ans` records that run before later differences reset `t`, so it is not lost.
- **Longest run at the end:** The equal-pair branch updates `ans` immediately on each extension, so no special end-of-loop flush is needed.
- **Several equally long runs:** Taking `max` keeps their common length. The task asks only for the length, not a location or character.
- **Lowercase-only guarantee:** The algorithm would also work for other comparable characters, but it needs no case normalization because the input is already restricted.
- **Substring versus subsequence:** Only adjacent positions count. The pair scan enforces contiguity automatically and never skips intervening characters.
- **Empty string outside the contract:** Initialization to one would be wrong for an empty input. The stated lower bound of one makes this case impossible; a generalized function would need a separate empty check.
- **Lazy iterator requirement:** Calling `pairwise` directly keeps space constant. Materializing all pairs would change auxiliary space to `O(n)` without improving the result.
