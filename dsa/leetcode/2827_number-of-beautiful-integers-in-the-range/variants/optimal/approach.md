## General

**Count up to a bound and subtract.** Iterating over every integer is too slow when the interval reaches $10^9$. The method defines an implicit prefix-count function $F(B)$ through digit dynamic programming: count decimal representations no greater than $B$ whose even- and odd-digit counts balance and whose numeric value is divisible by `k`.

The inclusive answer is `F(high) - F(low - 1)`. The source evaluates one cached recursive function with `s = str(high)`, clears the cache, changes `s` to `str(low - 1)`, and evaluates it again.

**Build a number one decimal position at a time.** State `dfs(pos, mod, diff, lead, limit)` records everything the remaining suffix needs to know.

- `pos` is the next position in bound string `s`.
- `mod` is the remainder modulo `k` of the significant digits chosen so far.
- `diff` encodes odd-digit count minus even-digit count with an offset of ten.
- `lead` is true while all chosen digits are only leading-zero padding.
- `limit` is true while the chosen prefix equals the bound prefix exactly.

The actual parity difference is `diff - 10`. Starting at ten represents zero difference while avoiding negative state values.

**Respect the upper bound.** If `limit` is true, the current digit may be at most `int(s[pos])`. Otherwise, it may be any digit through nine. The next tight flag is `limit and i == up`. When already loose, it stays false; when tight, it remains true only after choosing the bound digit.

**Do not count leading-zero padding as decimal digits.** If candidate digit `i` is zero while `lead` is true, the code advances without changing `mod` or `diff`. This represents a shorter integer padded on the left to the bound's length.

Once the number has started, zero is a genuine even digit. It follows the ordinary branch, subtracting one from `diff` and updating the remainder. This distinction is essential: the number ten has one odd digit and one even digit, while its invisible left padding must not add even digits.

**Update the parity balance.** For a significant digit, `nxt = diff + 1` when the digit is odd and `diff - 1` when it is even. At the end, `diff == 10` means equal counts.

Equal counts also imply an even number of significant digits. The DP does not need to check length parity separately because a zero final difference cannot arise from an odd number of plus-or-minus-one contributions.

**Update divisibility incrementally.** Appending digit `i` to a decimal prefix with remainder `mod` produces new remainder

`(mod * 10 + i) % k`.

Only the remainder is needed; storing the potentially large full prefix would create many more states. At completion, `mod == 0` exactly means divisibility by `k`.

**The base case and the all-leading-zero representation.** When every position has been processed, the source returns whether `mod == 0 and diff == 10`. It does not check `lead`. Therefore, the padding-only path representing zero is counted by every prefix call, even though the problem asks about positive integers.

This does not corrupt the range answer because `low > 0`. Both $F(\texttt{high})$ and $F(\texttt{low}-1)$ include the same one zero representation, including when `low - 1 = 0`, so subtraction cancels it exactly. A standalone prefix-count helper intended to report only positive beautiful integers would add `not lead` to the base case.

**Why caching is valid within one bound.** Future choices depend only on the five state components. Distinct digit prefixes with the same position, remainder, parity difference, leading status, and tightness have identical valid suffix counts. `@cache` evaluates that subproblem once.

The cache must be cleared before changing `s` because `s` is closed over and is not included in the key. Reusing high-bound states for the low-bound string would be incorrect.
Every integer from zero through $B$ has one length-equal padded digit sequence. The tight transitions admit it exactly when it is at most $B$. The remainder transition tracks its value modulo `k`, and the offset difference tracks only its significant even and odd digits. Thus accepted paths correspond exactly to beautiful positive integers plus the one zero sentinel. Subtracting the two prefix counts removes the sentinel and all values below `low`, leaving precisely the desired interval.

## Complexity detail

Let $D$ be the number of digits in the bound. `pos` has $D$ values, `mod` has `k` values, and `diff` can vary over $O(D)$ balances. `lead` and `limit` each have two values. Therefore, there are $O(D^2k)$ states.

Each state tries at most ten digits, a fixed decimal constant, so one prefix count takes $O(D^2k)$ time. Two prefix counts have the same asymptotic bound.

The cache stores $O(D^2k)$ integer results. Recursion depth is $O(D)$ and is dominated by the cache. Clearing between bounds prevents both tables from being retained together. Auxiliary space is $O(D^2k)$.

With $D\le10$ and $k\le20$, the state space is small. Counts fit comfortably in Python integers, which also avoid fixed-width overflow.

## Alternatives and edge cases

- **Bottom-up digit DP:** Fill equivalent remainder and balance states iteratively for each position. This avoids recursion and cache clearing but requires explicit handling of tight and leading dimensions.
- **Enumerate multiples of `k`:** Testing every multiple in the interval can still require up to $10^9/k$ candidates and is too slow for small `k`.
- **Odd digit length:** Equal even and odd counts are impossible, and the balance state rejects such completed numbers naturally.
- **Leading zeros:** They are padding and must not be counted as even digits; the dedicated branch preserves `diff`.
- **Significant zero:** Once `lead` is false, zero is an even digit and changes both balance and numeric remainder.
- **Number zero:** The exact prefix DP counts it as a sentinel, but prefix subtraction cancels it because `low` is positive.
- **`k = 1`:** Every number has remainder zero, so only parity balance constrains acceptance.
- **Single-point range:** Subtraction returns one exactly when that number is beautiful.
- **Lower bound one:** The second bound is zero; its one sentinel count cancels the high call's sentinel.
- **Cache clearing:** It is mandatory because the bound string is not part of the cache key.
- **Offset ten:** The maximum digit length is ten, so differences stay within a small nonnegative range around the offset.
