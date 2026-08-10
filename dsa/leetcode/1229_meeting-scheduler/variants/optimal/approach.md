## General

**Sort both calendars, then compare one pair at a time**

The input slots for each person do not overlap one another, but they are not guaranteed to arrive in chronological order. The solution first calls `sort()` on both lists. Python’s list comparison orders each two-element slot by its start and then by its end, so the calendars become chronological.

Two pointers `i` and `j` identify the current slot from each person. For those two slots, their common interval begins at the later start and ends at the earlier end:

`start = max(slots1[i][0], slots2[j][0])`

`end = min(slots1[i][1], slots2[j][1])`

If `end - start >= duration`, the intersection contains enough elapsed time. Beginning at `start` is the earliest meeting inside this particular overlap, so the method returns `[start, start + duration]`.

The use of `end - start` follows the contract’s elapsed-time semantics. Although the description calls endpoints inclusive, a duration-eight meeting starting at 60 ends at 68, as shown by the examples.

**Why the pointer with the earlier ending can be discarded**

If the current overlap is too short, at least one current slot must be abandoned. Suppose `slots1[i]` ends before `slots2[j]`. Keeping `slots1[i]` while moving to a later slot of person two cannot help. Because person two’s own slots are sorted and nonintersecting, the next person-two slot starts after the current person-two slot ends, which is already after `slots1[i]` ends. Thus `slots1[i]` cannot overlap any future person-two slot at all.

The code increments `i` in this case. Symmetrically, if person two’s slot ends earlier, it increments `j`.

When the end times are equal, the `else` branch advances `j`. Discarding either slot is safe: both become unavailable at the same time, and neither can form a better future overlap while paired with a later slot from the other calendar.

**Why the first returned meeting is globally earliest**

Sorting places slots in increasing start order. At every unsuccessful comparison, the algorithm discards only a slot that cannot participate in any feasible overlap with the other pointer’s current or future slots. Therefore, it never skips a possible meeting.

The current intersection’s `start` is the earliest time compatible with both current slots. If it is long enough, no later pointer pair can produce an earlier feasible start: any earlier candidate involving discarded slots was already shown impossible, and remaining slots begin no earlier in their own calendars. Returning immediately is consequently correct.

**Walking through the first example**

Person one has `[10,50]` first and person two has `[0,15]` first. Their intersection runs from 10 to 15, only five time units, so it cannot host duration eight. Person two’s slot ends earlier, so `j` advances.

The next person-two slot is `[60,70]`. It does not overlap `[10,50]`, and person one’s slot ends earlier, so `i` advances. Now `[60,120]` and `[60,70]` intersect from 60 through 70, a length of ten. The earliest duration-eight interval is `[60,68]`, which is returned.

For duration 12, that overlap is too short. The person-two pointer reaches the end, proving that no further pair exists, and the method returns an empty list.


Before each loop iteration, every pair involving a slot before `i` in the first calendar or before `j` in the second has been ruled out as a source of a feasible meeting earlier than any remaining candidate.

The overlap calculation tests the current pair completely. If it works, its earliest subinterval is the globally earliest feasible answer by the invariant. If it fails, advancing the earlier-ending slot is safe by the nonoverlap argument and extends the ruled-out region while preserving the invariant. If either pointer reaches its list’s end, every possible cross-person pair has been tested or safely eliminated, so no meeting exists.

**The source mutates its inputs**

`slots1.sort()` and `slots2.sort()` reorder the supplied lists in place. The slot objects themselves are not changed, but callers will observe chronological list order after the method returns. This is normal for the exact implementation and saves creating explicit sorted copies.

The problem asks only for one earliest interval, so the scan stops as soon as it finds one. It does not enumerate all overlaps.

## Complexity detail

Let \(n=\lvert\texttt{slots1}\rvert\) and \(m=\lvert\texttt{slots2}\rvert\). Sorting costs \(O(n\log n+m\log m)\). Each loop iteration advances at least one pointer, so the scan costs \(O(n+m)\). Sorting dominates, giving total time \(O(n\log n+m\log m)\).

Python’s Timsort may allocate \(O(n+m)\) temporary space across the two in-place sorts in the worst case. The pointer scan itself uses \(O(1)\) auxiliary space. The returned two-element list is constant-sized output.

## Alternatives and edge cases

- **Already sorted calendars:** The scan alone would be \(O(n+m)\). The exact source sorts unconditionally because chronological order is not guaranteed.
- **Heap over both calendars:** A heap can process slots by start time, but it stores \(O(n+m)\) entries and has a comparable or worse logarithmic cost.
- **All-pairs comparison:** Checking every slot from one person against every slot from the other costs \(O(nm)\) and ignores the nonoverlap structure.
- **Touching endpoints:** If `end - start` is zero, there is no positive-duration meeting even if both slots contain that endpoint.
- **Overlap exactly equals duration:** The `>=` test accepts it and returns the entire intersection from `start`.
- **Equal ending times:** The exact code advances person two’s pointer. Either pointer is safe to discard because both current slots expire together.
- **One calendar exhausts:** No future cross-calendar pair remains, so returning `[]` is correct.
- **Very large timestamps:** Only comparisons, addition, and subtraction are used; Python integers avoid overflow.
- **In-place sorting:** Callers needing original order should pass copies or use `sorted`. The current source intentionally mutates both input lists.
- **Nonoverlap guarantee within one person:** The pointer-discard proof depends on it. Overlapping same-person slots would need merging first or a different argument.
