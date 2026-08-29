## General

**Fitting is monotone across sorted font sizes**

The available `fonts` are strictly increasing. The interface guarantees that character width and font height never decrease as font size increases.

Therefore, if a particular font does not fit, no larger font can fit. If a font fits, every smaller available font also fits. The predicate has the form:

`True, True, ..., True, False, ..., False`.

This monotonicity allows binary search for the last fitting font.

**What `check(size)` verifies**

The text is displayed on one line, so a font fits only if both height and total width are within the screen.

The helper first calls `fontInfo.getHeight(size)`. If it exceeds `h`, it returns false immediately without asking for character widths. This avoids unnecessary interface calls for a font already too tall.

Otherwise, it calculates:

`sum(fontInfo.getWidth(size, c) for c in text)`

and compares the total with `w`. Every character occurrence contributes separately, as required by the interface contract. Equal characters cause repeated API calls in this exact implementation.

Width and height comparisons are inclusive: exactly matching `w` or `h` fits.

**Upper-mid binary search**

The search begins with `left = 0` and `right = len(fonts) - 1`. It does not assume the smallest font fits; `ans = -1` is assigned but not used later.

While `left < right`, the midpoint is:

`mid = (left + right + 1) >> 1`.

Adding one chooses the upper middle. If `fonts[mid]` fits, `left = mid` keeps that font and every possible larger answer. Because the midpoint is above `left` when two candidates remain, the interval makes progress.

If it does not fit, monotonicity excludes it and every larger index, so `right = mid - 1`.

When the indices meet, they identify the largest candidate not ruled out by the monotone search.

**Why the final check is required**

If at least one font fits, the converged index is the largest fitting one. However, the search started without testing whether any font fits. When all fonts fail, the interval still converges to index zero.

The return expression checks `fonts[left]` once more:

`fonts[left] if check(fonts[left]) else -1`.

This distinguishes “smallest is the answer” from “nothing fits.” The local variable `ans` is unused and has no effect on behavior.

**Why the search cannot skip a valid larger font**

When a midpoint fits, every smaller index also fits, so discarding the left half below it cannot remove the maximum. When it fails, every larger size has width and height at least as large, so discarding the right half cannot remove a fitting answer.

The invariant is that, if a fitting font exists, the largest fitting index remains within `[left,right]`. Convergence and the final check produce exactly that font.

**Interface calls and repeated characters**

The source treats `FontInfo` as a black box and calls only its documented methods. It does not implement or infer font metrics.

Although text contains only lowercase letters, the implementation does not count character frequencies. For text with many repeated letters, it calls `getWidth` once per occurrence during each successful height probe. The interface guarantees repeated calls with equal arguments return equal values, so frequency compression would be possible but is not used.

**Edge examples**

With one available font, the loop does not run. The final check returns that font if it fits or negative one otherwise.

If height fails, width is never evaluated for that probe. If height fits but width exceeds the screen, the font fails. Both dimensions must pass.

## Complexity detail

Let $L$ be text length and $F$ the number of available fonts.

Binary search performs $O(\log F)$ probes, plus one final probe. A probe uses one height call and, when height passes, up to $L$ width calls and additions. The exact worst-case time is therefore $O(L\log F)$.

The generator passed to `sum` is lazy, and the binary search stores only scalar indices. Exact auxiliary space is $O(1)$ apart from interface internals.

These bounds differ from the manifest’s $O(L+\sigma\log F)$ time and $O(\sigma)$ space, which describe preprocessing character frequencies for alphabet size $\sigma$. The checked-in source does not build that frequency map and rescans every character at each probe.

## Alternatives and edge cases

- **Character-frequency compression:** Count each distinct character once, then calculate width as frequency times one API width. This yields $O(L+\sigma\log F)$ time and $O(\sigma)$ space.
- **Linear scan from largest font downward:** It may find an answer quickly but takes $O(FL)$ worst-case time.
- **Binary search without a final check:** It would incorrectly return the smallest font when no font fits.
- **Lower midpoint with `left = mid`:** This can stall when two indices remain. The source uses upper midpoint to guarantee progress.
- **Height too large:** The helper returns immediately and makes no width calls.
- **Width exactly `w`:** It fits because the comparison is `<= w`.
- **Height exactly `h`:** It fits the height condition.
- **One available font:** The final check alone decides it.
- **No fitting font:** Search converges to zero and returns `-1` after the final failed check.
- **All fonts fit:** Every probe moves left upward until the largest index is returned.
- **Repeated letters:** The exact source repeats width calls; frequency preprocessing would reduce them.
- **Single-line requirement:** Widths are summed; no wrapping or line-height multiplication is performed.
- **Monotonic API guarantee:** Binary search correctness relies on both dimensions being non-decreasing with font size.
- **Unused `ans` variable:** It is initialized but never read; the converged index and final check determine the return.
