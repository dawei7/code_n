## General

**Use one fixed-size sliding window.** Every candidate substring has the same length `k`. Two consecutive candidates overlap in `k - 1` positions: moving one step right removes exactly one character from the left and adds exactly one character on the right. Recounting all `k` characters for every position would ignore that overlap.

The set `vowels` contains the five lowercase English vowels. Membership testing answers in expected constant time whether one character contributes one to the window count. Because the input contains lowercase letters, there is no need to normalize case.

**Count the first complete window once.** `s[:k]` is the substring from index zero through `k - 1`. The generator `c in vowels for c in s[:k]` yields one Boolean per character. Python sums `True` as one and `False` as zero, so the result is the number of vowels in the first length-`k` window.

That value initializes both `cnt` and `ans`. `cnt` tracks the current window, while `ans` remembers the greatest count seen in any complete window so far. Initializing from a real full window avoids special cases later.

**Update only the two changing characters.** The loop variable `i` is the index of the character entering on the right. It starts at `k` because indices zero through `k - 1` already belong to the initial window.

Before an iteration, `cnt` describes substring `s[i-k..i-1]`. Sliding right changes the window to `s[i-k+1..i]`. Character `s[i]` enters, and character `s[i - k]` leaves. The update
`int(s[i] in vowels) - int(s[i-k] in vowels)`
adds the entering contribution and subtracts the leaving contribution.

There are four intuitive cases. If both characters are vowels, one vowel replaces another and the count stays unchanged. If neither is a vowel, it also stays unchanged. If only the entering character is a vowel, the count rises by one. If only the leaving character is a vowel, it falls by one. The arithmetic expression handles all four without branches.

After updating `cnt`, `ans = max(ans, cnt)` records the new complete window. The update must occur before this maximum because `cnt` initially describes the previous position.

**Trace the important example.** For `s = "abciiidef"` and `k = 3`, the first window `abc` contains one vowel, so both counters start at one. Sliding to `bci` removes `a` and adds `i`; both are vowels, so the count remains one. Sliding to `cii` removes `b` and adds `i`, increasing it to two. Sliding to `iii` removes `c` and adds `i`, increasing it to three. `ans` becomes three, the greatest possible value for a window of length three.

Later windows may reduce the current count, but `ans` keeps the best earlier value. This separation is essential: `cnt` must change with the active window, while the answer must never decrease.

**The window invariant.** Before each maximum update in the loop, `cnt` equals the number of vowels in the length-`k` substring ending at `i`. Initially, the direct sum establishes the invariant for the first window. Removing the old left contribution and adding the new right contribution transforms the exact count for one window into the exact count for the next.

At every point, `ans` is the maximum count among all windows processed so far. Initializing it with the first window establishes that statement, and taking a maximum after each slide preserves it. The loop reaches every possible start position exactly once, so the final `ans` is the requested maximum.

**Why all candidate substrings are covered.** A string of length `n` has `n - k + 1` substrings of length `k`, beginning at indices zero through `n - k`. The initialization covers start zero. Loop index `i = k` produces start one, and the final index `n - 1` produces start `n - k`. No candidate is skipped or repeated.

**Be precise about the initial Python slice.** The manifest says `O(1)` space, and the sliding-window state itself is constant. However, the exact expression `s[:k]` creates a new Python string of length `k` before the generator consumes it. The exact source therefore has `O(k)` transient auxiliary space. Iterating over indices zero through `k - 1` would avoid that allocation and achieve the advertised constant-space bound.

## Complexity detail

Let `n` be `len(s)`. Counting the initial `k` characters takes `O(k)` time. The loop performs `n - k` iterations with constant-time set membership and arithmetic. Total time is `O(k + n - k) = O(n)`.

The vowel set always has five entries, and the counters use constant space. The created substring `s[:k]` occupies `O(k)` characters temporarily, so the exact implementation's auxiliary space is `O(k)`. After initialization, the ongoing sliding window uses `O(1)` state.

If the first count were computed with an index-based generator over the original string, no window substring would be copied and auxiliary space would be `O(1)`, matching the manifest.

The algorithm is time-optimal in the worst case because every character can affect some candidate window and must be inspected.

## Alternatives and edge cases

- **Index the first window:** Sum `s[i] in vowels` for indices from zero to `k - 1`. This preserves `O(n)` time and achieves true `O(1)` auxiliary space by avoiding `s[:k]`.
- **Recount every substring:** It is simple but costs `O(nk)` time because overlapping characters are counted repeatedly.
- **Prefix sums of vowel indicators:** Build a length-`n + 1` prefix array and query each window in constant time. It runs in `O(n)` time but uses `O(n)` extra space, more than sliding state needs.
- **Two explicit if statements:** Add one when the entering character is a vowel and subtract one when the leaving character is a vowel. This is equivalent to the compact integer-difference expression.
- **k equals one:** Each window is one character, so the answer is one if any vowel exists and zero otherwise.
- **k equals n:** The initial window is the whole string, the sliding loop is empty, and its count is returned.
- **All vowels:** Every complete window contains `k` vowels, which is the maximum possible answer.
- **No vowels:** Both counters remain zero throughout.
- **Entering and leaving are both vowels:** Their contributions cancel and `cnt` stays unchanged.
- **Entering and leaving are both consonants:** The count also stays unchanged.
- **Maximum in the first window:** `ans` is initialized before sliding, so that maximum is preserved.
- **Maximum in the last window:** The final loop iteration updates `ans` after forming it.
- **Lowercase guarantee:** The vowel set intentionally contains lowercase letters only. Case conversion is unnecessary.
- **Output upper bound:** A window has exactly `k` characters, so `ans` can never exceed `k`.
- **Slice accounting:** Although the slice is short-lived, peak auxiliary memory includes it. Report `O(k)` for this exact source and `O(1)` for an index-based initialization.
