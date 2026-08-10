## General

**Translate the building process into suffixes of the final string**

Characters are prepended one at a time. If the final string has length `n`, the intermediate string of length `i` is exactly the suffix of `s` containing its last `i` characters.

For example, when `s = "abaca"`, the built strings are `"a"`, `"ca"`, `"aca"`, `"baca"`, and `"abaca"`. These begin at final-string indices four, three, two, one, and zero.

Therefore, summing scores of all built strings is the same as summing, for every suffix `s[index:]`, the length of its longest common prefix with the full string `s`.

Computing each comparison independently can repeat the same character checks and take quadratic time for a repetitive string. The Z-algorithm computes all of these longest-common-prefix lengths together in linear time.

**Meaning of the Z array**

For every index `index > 0`, `z[index]` is the largest length such that

`s[0:z[index]] == s[index:index + z[index]]`.

That is exactly the score of the suffix beginning at `index`. The code leaves `z[0] = 0` by convention. The suffix at index zero is the full string, whose score is `length`, so the return expression adds that value separately:

`length + sum(z)`.

The mapping between built strings and suffixes is one-to-one, merely visited in the reverse length order. Addition is independent of order, so this sum equals the requested total.

**Keep the rightmost known prefix-matching interval**

The variables `left` and `right` describe an inclusive interval `[left, right]`, often called a Z-box. The substring `s[left:right + 1]` is known to equal the prefix `s[0:right - left + 1]`. Among intervals discovered so far, the algorithm keeps one extending farthest to the right.

Initially both values are zero. The main loop begins at index one because index zero's full-string score is handled separately.

When `index > right`, the new position lies outside the known box. There is no reusable information, so `z[index]` remains its initialized zero and the while loop begins comparing `s[0]` with `s[index]`.

When `index <= right`, the position lies inside the box. Because the box substring copies the prefix, the pattern beginning at `index` initially behaves like the pattern beginning at prefix-relative position `index - left`. The code initializes

`z[index] = min(right - index + 1, z[index - left])`.

The first quantity is how many characters remain inside the known box. The second is the already computed prefix match length at the mirrored prefix-relative position. Their minimum is guaranteed to match without performing new character comparisons.

**Why the minimum is the safe reusable amount**

If `z[index - left]` ends before the right edge of the current box, that entire known match can be copied and it already stops at a mismatch represented within the box. If it reaches or extends beyond the box edge, only `right - index + 1` characters are guaranteed, because existing information says nothing about the next character after `right`.

Taking the minimum handles both situations without claiming an unverified match outside the known interval. It can underestimate only at the boundary, and the following while loop extends from exactly that point.

**Extend beyond what is known**

The loop

`while index + z[index] < length and s[z[index]] == s[index + z[index]]`

compares the next prefix character with the next suffix character. Each successful comparison increments `z[index]`. It stops at the string boundary or at the first mismatch, leaving the exact longest common prefix length.

The bounds check appears first, so both string accesses are valid. The comparison uses `s[z[index]]` because a Z value of `t` means the first `t` prefix characters already match and position `t` is the next one to test.

After extension, the matching interval for this index ends at `index + z[index] - 1`. If that endpoint is farther right than the current `right`, the code replaces the box with

`left = index` and `right = index + z[index] - 1`.

If `z[index] = 0`, the endpoint is `index - 1` and normally does not extend the current right boundary. A zero-length match needs no useful box.

**Why every Z value is exact**

Outside a box, comparison begins at offset zero and continues until the first mismatch or boundary, directly measuring the exact prefix match.

Inside a box, the copied minimum is guaranteed to match because the box equals the prefix and the referenced Z value describes matching prefix structure. If the copied match ends strictly before the box boundary due to a known mismatch, it is already exact. If it reaches the boundary, the while loop tests every additional character needed to determine whether the match extends. In either situation, the final value cannot be too small and stops before it could become too large.

Thus, every `z[index]` equals the score of suffix `s[index:]`. Adding all those values and the full-string score at index zero produces exactly the sum of scores.

**Why the scan remains linear**

The nested while loop can look quadratic, but comparisons within an existing Z-box are obtained by copying earlier results rather than repeated character checks. A successful while-loop comparison that goes beyond the current `right` advances the right boundary. That boundary moves only from left to right and can advance at most `n - 1` positions overall.

Some iterations can perform one final failing comparison, contributing at most one such comparison per index. Reused work inside boxes plus globally bounded right-edge extensions keeps total character comparisons proportional to `n`.

**Trace a repetitive pattern**

For `s = "babab"`, the suffix at index two is `"bab"` and matches the first three characters, so `z[2] = 3`. The suffix at index four is `"b"`, so `z[4] = 1`. Suffixes at indices one and three start with `a` rather than the prefix's `b` and have Z value zero. Adding the full-string score five gives `5 + 3 + 1 = 9`.

The algorithm computes these values without separately restarting a full prefix comparison for every suffix.

## Complexity detail

Let `n = len(s)`. The main index loop executes `n - 1` times. Z-box reuse avoids rechecking known characters, the inclusive `right` boundary advances at most `n` times, and there is at most constant additional failed-comparison work per index. The Z-array construction therefore takes `O(n)` time.

Computing `sum(z)` performs another `O(n)` pass. Sequential linear passes combine to `O(n)` total time.

The length-`n` Z array uses `O(n)` space. All other values—`length`, `left`, `right`, and `index`—use `O(1)` space. The returned result is a single integer, so total auxiliary space is `O(n)`.

The sum can be as large as `1 + 2 + \cdots + n = n(n + 1)/2` for a string containing one repeated character. Python integers safely hold it; a fixed-width implementation should use a 64-bit type.

## Alternatives and edge cases

- **Compare every suffix directly:** For each starting index, scan from the beginning until a mismatch. This is easy to derive but takes `O(n^2)` time on strings such as `"aaaaa..."`.
- **Rolling hash with binary search:** Hashes can test substring equality and binary search each suffix's LCP in `O(\log n)` expected time, giving `O(n \log n)` overall and introducing collision concerns unless carefully verified.
- **Suffix array or suffix tree:** These structures can support rich suffix queries but are substantially more machinery than the all-prefix LCP values computed directly by the Z-algorithm.
- **Prefix-function array:** KMP's prefix function captures borders of prefixes, while this task asks how every suffix matches the global prefix. Transformations are possible, but the Z-array matches the required quantity directly.
- **Single-character string:** The loop is empty, `sum(z)` is zero, and returning `length` gives the sole score one.
- **No later character matches the first:** Every `z[index]` for `index > 0` is zero, so the total is only `n`, the score of the full string.
- **All characters equal:** Suffix at index `i` matches for `n - i` characters. The result reaches the triangular-number maximum, and box reuse prevents quadratic comparisons.
- **Overlapping matches:** Z-boxes are designed for overlap. The reference `z[index - left]` safely reuses a prefix-relative result even when the current suffix lies inside a previous match.
- **Match reaches the end:** The bounds condition stops before either index passes `length - 1`, and the recorded Z value equals the remaining suffix length.
- **Zero-length match:** The while loop fails immediately, `z[index]` remains zero, and no useful box extension occurs.
- **Inclusive right boundary:** Remaining known characters are counted by `right - index + 1`. Omitting the `+ 1` would undercount positions inside the box.
- **Full string's score:** `z[0]` is left at zero by convention, so `length` must be added explicitly. Returning only `sum(z)` would omit `s_n`.
- **Prepending interpretation:** The intermediate strings are suffixes, not prefixes, of the final string. Confusing the direction would compute the wrong family of comparisons.
- **Input preservation:** Strings are immutable and `s` is never changed; all computed match lengths live in `z`.
