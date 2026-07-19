## General
**Track the run that is currently open**

Scan `s` from left to right while storing the current digit and the length of its unfinished segment. A matching next digit extends that segment. A different digit closes it: update the maximum belonging to the old digit, then start a new segment of length one for the new digit.

**Account for the final segment**

Transitions cause every completed segment except the last one to be recorded. After the loop, update the appropriate maximum once more using the remaining current length. Initial maxima of zero naturally implement the rule for a digit that never appears.

**Why the comparison is exact**

Every maximal segment is closed either by a digit change or by the end of the string, so each contributes its length exactly once to the maximum for its digit. Those two stored values are therefore precisely the longest one-segment and zero-segment lengths. Returning whether the former is greater implements the required strict comparison.

## Complexity detail
The scan examines each of the $N$ characters once and performs constant work per character, for $O(N)$ time. The current digit, current length, and two maxima occupy a fixed amount of storage, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Split on the opposite digit:** Taking maximum piece lengths from `s.split("0")` and `s.split("1")` is concise, but it allocates substring collections totaling $O(N)$ space.
- **Restart a scan at every position:** It can find the same maxima, but long uniform segments cause $O(N^2)$ repeated work.
- **Equal maxima:** Return `false` because the ones segment must be strictly longer.
- **Only ones:** The zero maximum remains zero, so every nonempty all-ones string returns `true`.
- **Only zeros:** The one maximum remains zero and cannot exceed the zero segment.
- **Alternating digits:** Both maxima are one when both digits appear, so the answer is `false`.
- **Final longest run:** It must be recorded after the loop because no later transition closes it.
