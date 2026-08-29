## General

**Split the pattern into three fixed pieces.** With exactly two stars,

$$
p=A*B*C.
$$

A matching substring must contain an occurrence of $A$, followed without overlap by an occurrence of $B$, followed without overlap by an occurrence of $C$. The stars consume any intervening characters, including none. Any fixed piece may be empty.

The source first finds every start position of each fixed piece in `s`.

**Use KMP to find occurrences in linear time.** For a non-empty `word`, `occurrences` builds the standard prefix-function array. `prefix[i]` is the length of the longest proper prefix of `word` that is also a suffix ending at $i$.

While scanning `s`, `matched` records how many pattern characters currently match. On mismatch, prefix links skip to the next viable border instead of restarting from scratch. When `matched == len(word)`, a full occurrence ends at the current source index, so its start is recorded. Resetting with the prefix link allows overlapping occurrences.

If `word` is empty, it occurs at every boundary position $0$ through `len(s)`. Returning all these boundaries is essential for patterns such as `"**"` and `"*abc*"`.

All occurrence lists are sorted because KMP discovers starts from left to right.

**Choose the tightest first occurrence for each middle occurrence.** Fix `middle_start`. An $A$ occurrence is compatible when

`first_start + len(first) <= middle_start`.

The pointer `first_index` advances past every compatible start. Then `first_starts[first_index - 1]` is the latest compatible $A$ start. Among choices ending before the same middle occurrence, the latest start minimizes total substring length, so earlier compatible occurrences can never be better for this middle.

If no first occurrence is compatible, this middle occurrence is skipped.

**Choose the earliest last occurrence after the middle.** The end of $B$ is

`after_middle = middle_start + len(middle)`.

`last_index` advances until `last_starts[last_index] >= after_middle`. This is the earliest non-overlapping $C$ occurrence, so it minimizes the matching substring's end for the fixed middle.

If no such last occurrence remains, later middle starts cannot help because they end even farther right. The source safely breaks.

The resulting candidate begins at the latest compatible $A$ start and ends after the earliest compatible $C$ occurrence. Its length is `end - start`.

**Why the two pointers never move backward.** Middle starts are considered in increasing order. As the middle moves right, the set of compatible $A$ starts only grows, so `first_index` can advance monotonically. The required start for $C$ also never moves left, so `last_index` is monotone. This avoids a binary search or fresh scan for every middle occurrence.

For pattern `"**"`, all three pieces are empty and every boundary is an occurrence. At middle boundary zero, the latest compatible first and earliest compatible last are both zero, producing length zero as required.

For `"*adlogi*"`, empty outer pieces can start and end exactly at the fixed middle occurrence's boundaries, yielding length six.
Any match has some chosen $B$ occurrence. For that same middle, replacing its $A$ occurrence with the latest compatible one cannot increase the start span, and replacing $C$ with the earliest compatible one cannot increase the end. Thus the source finds the shortest match using that middle. Considering every $B$ occurrence and taking the minimum finds the global shortest match.

If no candidate updates the sentinel `len(s) + 1`, no ordered non-overlapping triple exists and the method returns `-1`.

The latest-compatible-first choice and earliest-compatible-last choice are independent once the middle occurrence is fixed: moving the first start right cannot invalidate its already-checked end-before-middle relation, and moving the last start left cannot overlap the fixed middle because the pointer stops at `after_middle`. This independence is what permits two simple monotone pointers instead of a three-way dynamic program.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert p\rvert$. Building KMP data and scanning for all three pieces costs $O(n+m)$ total; three source scans are a constant factor. Occurrence lists can each contain $O(n)$ starts.

The middle loop and both monotone pointers advance at most $O(n)$ times. Total time is $O(n+m)$ and auxiliary space is $O(n+m)$ for prefix arrays, split pieces, and occurrence lists, matching the manifest.

## Alternatives and edge cases

- **Try every substring:** There are $O(n^2)$ candidates before pattern checking.
- **Repeated `str.find` calls:** They can be concise but worst-case behavior and overlapping-occurrence management are less explicit than KMP.
- **Binary search occurrence lists:** It gives $O(n\log n)$ combination time; monotone pointers exploit ordered middle starts for linear time.
- **Empty fixed piece:** It occurs at all $n+1$ boundaries, not only character positions.
- **Overlapping fixed pieces:** They are not allowed to overlap in one match; end/start inequalities enforce sequence order.
- **Stars matching empty:** Equality at boundaries is accepted, allowing adjacent fixed pieces.
- **Overlapping occurrences within one list:** KMP prefix fallback records them all.
- **No last occurrence:** Breaking is safe because later middle endings only move right.
- **Pattern `"**"`:** The empty substring is found with length zero.
- **No match:** The untouched sentinel maps to `-1`.
