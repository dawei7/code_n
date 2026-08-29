## General

**This is a lazy window that remembers the best length implicitly.**

A standard sliding window repeatedly moves its left edge until the current window becomes valid again. The exact source uses a subtler variant: after adding each new character, it moves the left edge at most once. Its maintained window never becomes shorter. It either grows by one when the expansion is valid or stays at its previous length when the expansion is invalid.

Because the previous length was already achieved by some valid substring, an invalid expansion does not need to be repaired completely. The algorithm can keep a possibly invalid window of the same length and continue searching for the first valid window that is one character longer.

The variable `l` is the left edge of the maintained suffix of the processed input. The `Counter` `cnt` stores the frequency of each character in that maintained window, deleting keys whose frequency reaches zero. The number of keys, `len(cnt)`, is therefore the current number of distinct characters.

**Expand with every input character.**

The `for c in s` loop processes characters from left to right. Although it does not name a right index, after a character `c` is added, that character is the current right endpoint. The source increments `cnt[c]` to include it.

Suppose the maintained window previously had length $M$. Adding the new right endpoint temporarily creates a candidate of length $M+1$. There is only one substring of that length ending at this position: it begins at the current `l`.

If `len(cnt) <= k`, this candidate is valid. The source leaves `l` unchanged, so the maintained length grows from $M$ to $M+1$. Since no earlier valid substring was longer than $M$, this newly valid candidate establishes a new best length.

**On an invalid expansion, remove exactly one left character.**

If adding `c` makes `len(cnt) > k`, the length-$M+1$ candidate is invalid. The source removes `s[l]` once:

- decrement its frequency;
- delete its counter key if the frequency becomes zero;
- increment `l` by one.

Adding one character and removing one character leaves the maintained window length at $M$. That length was already known to be achievable by an earlier valid substring, so the global best does not decrease.

The current window is not required to become valid after this single removal. If the removed character still occurs elsewhere in the window, the distinct count can remain above `k`. That is intentional. The window's length still represents the historical optimum, and future one-for-one shifts may eventually discard enough old character types for the window to become valid again. Only then can a later expansion grow the best length.

**Why returning `len(s) - l` gives the answer.**

Let $M_r$ be the length of the longest valid substring found after processing through some right endpoint $r$. Maintain the invariant that the source's current window length equals $M_r$, even though the current window itself may be invalid.

Before any characters, both lengths are zero. Assume the invariant holds before processing the next character.

- If the length-$M_r+1$ expansion has at most `k` distinct characters, it is a valid substring longer than the old maximum. The source does not move `l`, so both the maintained length and the optimum become $M_r+1$.
- If that expansion has more than `k` distinct characters, it cannot establish a new maximum. There is only one length-$M_r+1$ substring ending at this new position, and it is invalid; no earlier substring had that length by definition of $M_r$. The source moves `l` once, restoring maintained length $M_r$, while the historical optimum remains $M_r$.

Therefore the invariant holds after every character. At the end, the right endpoint is `len(s) - 1`, so the maintained window length is

$$
\text{len}(s)-l.
$$

By the invariant, that length equals the global optimum. The method does not need an explicit `ans` variable.

**Why an already-invalid maintained window does not break the proof.**

Suppose the current length-$M$ window is invalid but an earlier valid window established the same length. Adding another character creates a length-$M+1$ window containing the invalid current window, so it is certainly invalid too. The `len(cnt) > k` condition fires, one character leaves, and the maintained length stays $M$.

If a later removal makes the current length-$M$ window valid again, that does not change the best—it merely finds another window of the known length. On the next iteration, the algorithm gets a genuine chance to extend this valid window to length $M+1$.

Thus validity is required only when growing the length, not while carrying the known best length forward.

**Walk through `eceba` with `k = 2`.**

Start with `l = 0` and an empty counter.

- Read `e`: the window `e` has one distinct character, so it grows to length one.
- Read `c`: `ec` has two distinct characters, so it grows to length two.
- Read `e`: `ece` still has two distinct characters, so it grows to length three. This is a valid best.
- Read `b`: the expanded `eceb` has three distinct characters. Remove one left `e` and increment `l` to one. The maintained window `ceb` still has three distinct characters, so it is invalid, but its length remains the known best of three.
- Read `a`: the temporary length-four suffix is invalid. Remove left character `c` and increment `l` to two. The maintained suffix `eba` still happens to be invalid for `k = 2`, but its length is three.

The source returns `5 - 2 = 3`, the length of the earlier valid substring `ece`. This trace demonstrates why interpreting the final counter as a valid answer window would be wrong; only its length encodes the best.

**Why counter updates stay accurate.**

The counter always describes exactly the maintained window from `l` through the current right endpoint. Every new right character is added. Whenever `l` advances, precisely the leaving character `s[l]` is decremented before the index changes. Deleting zero-frequency keys ensures `len(cnt)` counts actual distinct characters rather than historical keys.

Even when the window is invalid, its frequencies remain exact, so future additions and removals correctly detect when its distinct count falls back within the limit.

## Complexity detail

Let $n$ be `len(s)`. Each character is added to the counter once. At most one character is removed on each iteration, and `l` can advance at most $n$ times. With expected $O(1)$ hash-map updates, total expected time complexity is $O(n)$.

Unlike the standard eagerly shrinking window, the lazy window can retain more than $k+1$ distinct characters. For example, after first establishing a long run as the best for `k = 1`, successive new characters can enter while old repeated characters leave one occurrence at a time. The counter can therefore grow to $O(n)$ distinct keys in the worst case. The exact source's auxiliary space is $O(n)$, not the manifest's $O(k)$.

The manifest summary says the window shrinks “while” distinctness exceeds `k`, but the source uses a single `if`. A standard `while` version would keep the current window valid and use $O(k)$ counter space; this source deliberately uses the lazy invariant and has the larger worst-case storage bound.

## Alternatives and edge cases

- **Standard eager sliding window:** After adding each right character, repeatedly remove left characters while `len(cnt) > k`, then update an explicit maximum with the valid window length. It runs in $O(n)$ expected time and keeps at most $k+1$ temporary distinct keys, giving $O(k)$ space. This matches the manifest but not the exact source.

- **Track last occurrence positions:** Store each character's most recent index and evict the character with the smallest last index when distinctness exceeds `k`. With an ordered map or heap, this is more complex and may cost $O(n\log k)$ time.

- **Enumerate all substrings:** Checking distinct counts for every start and end is at least quadratic and cannot handle a string of length `50000` efficiently.

- **`k = 0`:** Every one-character expansion is invalid. The source immediately removes the same character, advances `l` on every iteration, and returns `n - n = 0`.

- **`k` at least the number of distinct characters:** No invalid expansion occurs, `l` remains zero, and the full string length is returned.

- **Repeated single character:** The counter has one key regardless of run length. For `k >= 1`, the maintained window grows across the entire string.

- **Deleting zero counts:** Without deleting a key when its count becomes zero, `len(cnt)` would overstate distinctness and prevent valid growth.

- **Final window may be invalid:** This is not a defect in the lazy proof. The returned length is a historical maximum encoded by the nondecreasing window size, not a claim that `s[l:]` is a valid witness.

- **Space discrepancy:** Because only one left character is removed per iteration, the counter is not bounded by `k`. Any explanation assigning $O(k)$ space to this exact code silently assumes a `while` loop that is not present.
