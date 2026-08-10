## General

**A valid substring is determined by character occurrence ranges**

If a substring contains character `c`, it must include every occurrence of `c`. The source first records `first[c]` and `last[c]` for each lowercase letter.

Any minimal valid substring must begin at the first occurrence of some character. Starting later would omit that character's earlier occurrence, while starting earlier without necessity would only increase length. The outer loop therefore considers an index only when `first[label] == left`.

The two arrays have fixed length 26. Missing letters keep sentinel first position `len(s)` and last position minus one.

**Expanding one candidate to closure**

For a candidate starting at `left`, the initial right boundary is the last occurrence of its starting character. The algorithm scans from left through the current right boundary.

Whenever it encounters character `inner`, a valid interval containing that position must also contain every occurrence of `inner`. Two checks follow:

- If `first[inner] < left`, this candidate is impossible. It already contains `inner` but starts after an earlier occurrence, and moving left would mean it is not the minimal candidate for this outer start. The loop breaks.
- Otherwise, `right = max(right, last[inner])` extends the interval far enough to include the character's final occurrence.

Extending right may expose new characters, whose last occurrences may extend it again. The while loop continues until the scan passes the final closed boundary.

Python's `while ... else` executes the `else` block only when the loop ends normally, not when `break` rejects the candidate. Thus only fully closed valid intervals reach selection.

**Why a successful closure is valid and minimal**

When the scan completes, every character appearing between `left` and `right` has its first occurrence no earlier than `left` and last occurrence no later than the final `right`. Therefore, all occurrences of every contained character lie inside the interval.

The starting character requires both endpoints initially, and every later boundary extension is forced by a contained character. No shorter right endpoint can make the substring valid for this start. It is the minimal valid interval beginning at `left`.

**Greedily selecting intervals**

Successful candidates are encountered in increasing left-boundary order. `selected_end` is the right boundary of the most recently selected substring.

If `left > selected_end`, the new interval is disjoint from all selected intervals, so the code appends it.

If `left <= selected_end`, it overlaps the most recent selected interval. Because that prior interval is valid and contains the character whose first occurrence is `left`, it must also contain all occurrences needed by the new candidate. Consequently, the new minimal interval is nested within the previous one and ends no later. The source replaces `answer[-1]` with the new substring and updates `selected_end`.

**Why replacement preserves maximum count**

Replacing one overlapping interval with another keeps the number of chosen substrings unchanged. The new interval ends no later, so it leaves at least as much room for every future interval. It cannot reduce the maximum number achievable after this point.

Among solutions with the same count, the nested replacement also shortens or preserves the current substring, improving total length. Repeating this rule gives the unique minimum-total-length solution among all maximum-count selections.

This is analogous to interval scheduling by earliest finishing time, with the extra closure step generating the only meaningful valid candidates.

**Why earlier selected intervals remain safe**

Only the most recent selected interval can overlap a new candidate because selected intervals are ordered and disjoint. If the new left is beyond `selected_end`, it is beyond all of them. If not, nesting applies to the last one. Replacing that last interval cannot reach backward into the preceding selected interval because its left boundary is later than the replaced interval's left.

The returned strings may be in any order, and the source naturally returns them in left-to-right order.

## Complexity detail

The initial occurrence scan is $O(n)$. There are at most 26 candidate starts, one per lowercase letter. Each closure scan can traverse up to $n$ characters, so a direct bound is $O(26n)=O(n)$ because the alphabet size is fixed.

The first and last arrays use $O(26)=O(1)$ auxiliary space. The answer and substring slices contain output characters. Excluding required output, index state is constant. In Python, slicing creates string objects; stored output is $O(n)$ total because selected intervals do not overlap, and temporary replaced candidates can also occupy $O(n)$ space at a moment.

These qualifications explain the manifest's $O(n)$ time and $O(1)$ algorithmic auxiliary-space shorthand.

## Alternatives and edge cases

- **Generate intervals then sort by end:** Build every valid minimal character interval and run standard earliest-finish interval scheduling. It is equivalent but uses an explicit candidate list.
- **Dynamic programming over positions:** It can optimize count and total length but is more state than the fixed-alphabet greedy structure needs.
- **One repeated character:** Its only minimal valid substring spans all occurrences.
- **Unique character:** Its candidate can be the one-character substring, maximizing count and minimizing length.
- **Invalid candidate start:** Encountering a character whose first occurrence lies earlier forces rejection rather than leftward expansion.
- **Nested valid intervals:** The later, smaller interval replaces the previous selection to improve length without reducing count.
- **Disjoint valid intervals:** Each is appended, increasing the count.
- **Adjacent intervals:** They are nonoverlapping because the next left is greater than the previous end.
- **Substring copying:** Python slices allocate new strings even though the index algorithm uses constant fixed state.
- **Lowercase alphabet:** The constant 26 factor is essential to the linear-time bound.
