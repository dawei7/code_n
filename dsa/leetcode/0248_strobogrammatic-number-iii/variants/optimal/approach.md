## General

The range endpoints may contain up to fifteen digits, so iterating through every integer from `low` to `high` and testing each one would be far too expensive. Strobogrammatic numbers are sparse and highly structured. The exact solution generates only strings that are unchanged by a 180-degree rotation, then counts the generated values that lie inside the inclusive numeric interval.

Rotation reverses positions and transforms digits. The legal mirrored pairs are

```text
00, 11, 69, 88, 96
```

The pair `69` means that a left `6` becomes a right `9`; `96` represents the reverse orientation. A center digit in an odd-length number stays at the same position, so it can only be `0`, `1`, or `8`.

**Only relevant digit lengths are generated**

Let `a = len(low)` and `b = len(high)`. Any integer in the interval has between `a` and `b` digits because the endpoints contain no leading zeros. The outer loop therefore calls the generator for every length `n` in `range(a, b + 1)` and no other length.

This digit-length filtering is already powerful. Every generated number of a length strictly between `a` and `b` must lie between the endpoints numerically. Only candidates having the same length as a boundary can potentially fall outside. The source nevertheless applies one uniform inclusive check to every candidate, keeping the logic simple and safe.

**Generate a length from its center**

The nested helper `dfs(u)` generates strobogrammatic strings of the current remaining length `u`.

- If `u == 0`, it returns `['']`. The empty string is the neutral center used to build even-length strings.
- If `u == 1`, it returns `['0', '1', '8']`, the only legal fixed centers for odd-length strings.
- Otherwise, it obtains every inner string from `dfs(u - 2)` and surrounds it with rotation-compatible pairs.

For each inner string `v`, four pairs are always allowed: `11`, `88`, `69`, and `96`. The pair `00` is appended only when `u != n`, meaning the current layer is internal rather than the full requested number.

**Why zero depends on recursion depth**

A multi-digit integer cannot begin with zero, but zeros are perfectly valid inside it. For example, `1001` is a valid four-digit strobogrammatic number and requires the inner string `00`. On the other hand, `0110` is not a four-digit integer representation under the contract.

The outer loop variable `n` is captured by the helper. During `dfs(n)`, only the outermost call has `u == n`, so only that call suppresses `00`. Recursive calls have smaller `u` and may create zero-wrapped inner strings. Python closures use the current loop value of `n` when the helper runs, so each length receives the appropriate outer-length comparison.

For `n = 2`, recursion reaches the empty center. The outer layer creates `11`, `88`, `69`, and `96`, but not `00`. For `n = 4`, the internal length-two layer includes `00`; the outer layer can then turn it into `1001`, `8008`, `6009`, or `9006`.

**Filtering against the inclusive bounds**

The source first converts `low` and `high` from decimal strings to Python integers. Each generated string `s` is also converted with `int(s)`, then tested with

$$
\text{low}\le \operatorname{value}(s)\le\text{high}.
$$

Both inequalities are inclusive, so a strobogrammatic endpoint is counted. Python integers have arbitrary precision, making conversion safe even for fifteen-digit inputs.

For `low = "50"` and `high = "100"`, both endpoint lengths are two and three, so the solution generates lengths two and three. Among the two-digit results, `69`, `88`, and `96` pass the range check; `11` is too small. Every valid three-digit result is greater than `100`, including `101`, so none passes. The count is `3`.

For `low = high = "0"`, only length one is generated. The candidates are `0`, `1`, and `8`, and the inclusive check accepts only `0`, producing count `1`.

**Why generation is sound and complete**

The base strings are strobogrammatic. If an inner string remains identical after rotation, wrapping it in one legal pair also remains identical: rotation swaps the endpoints and transforms each into its partner while preserving the valid interior. Excluding an outer `00` ensures every generated string is also a valid representation of its requested length. Therefore, every generated candidate is a valid strobogrammatic number.

Conversely, take any strobogrammatic number of length `n`. Its outer digits must be one of the five legal pairs, and after removing them, the remaining substring must itself be strobogrammatic. Repeating this removal reaches the empty center for even length or one of `0`, `1`, and `8` for odd length. The recursion constructs that exact chain of pairs. The number cannot begin with zero, so its outermost choice is among the four pairs generated at `u == n`. Thus no valid length-`n` candidate is missed.

The outer loop covers every possible length in the numeric interval, and the final numeric condition retains exactly those candidates within the boundaries. Together these facts prove that `ans` counts every and only strobogrammatic number in `[low, high]`.

## Complexity detail

Let $d=\text{len(high)}$, the maximum generated length. A length with $h=\lfloor n/2\rfloor$ mirrored pairs has four choices for the outer pair, five choices for each inner pair, and three center choices when odd. Its count is therefore $\Theta(5^{n/2})$ up to parity-dependent constants.

Summing candidates over all lengths from `a` through `b` is dominated geometrically by the largest lengths, so the total number generated is $O(5^{d/2})$. Constructing and converting each length-$O(d)$ string costs $O(d)$, giving total time $O(d\cdot5^{d/2})$.

The exact source materializes lists in `dfs`; it does not stream one candidate through an in-place buffer. At the largest length, storing $\Theta(5^{d/2})$ strings of length $d$ requires $O(d\cdot5^{d/2})$ space. The recursion stack alone is $O(d)$, but it does not dominate the generated lists. Therefore, the manifest's $O(d)$ space would describe a backtracking generator that counts candidates one at a time, not this protected list-returning implementation.

Only one target length's generated list is needed by the loop at a time, so lists from completed outer iterations can be reclaimed. Peak memory is governed by the largest active generation rather than the sum across all lengths.

## Alternatives and edge cases

- **In-place backtracking with a character buffer:** Fill mirrored positions and check a completed candidate immediately instead of returning a list. This preserves the $O(d\cdot5^{d/2})$ time but can reduce auxiliary working space to $O(d)$ excluding recursion and the count, matching the manifest's space claim.
- **Lexicographic boundary comparison:** For equal-length canonical decimal strings, compare directly with `low` and `high` rather than converting to integers. This is useful in languages without arbitrary-precision integers; the exact Python source safely uses `int`.
- **Test every integer in the range:** This can require work proportional to the numeric width of the interval, potentially near $10^{15}$, and ignores the sparse constructive structure.
- **Inclusive endpoints:** The `<=` checks count `low` or `high` whenever the endpoint itself is strobogrammatic.
- **Different endpoint lengths:** All generated lengths strictly between them automatically fit numerically, while the common filter correctly handles both boundary lengths.
- **Single value `0`:** The one-digit base contains `0`, and the inclusive check counts it exactly once.
- **No leading zeros:** `00` is excluded only at the outermost recursive level. Internal zeros remain necessary for values such as `1001`.
- **Odd-length center:** Only `0`, `1`, and `8` remain unchanged in place. A center `6` or `9` would rotate into the other digit and invalidate the number.
- **Pair direction:** Both `69` and `96` must be generated. Neither `66` nor `99` is valid.
- **Repeated generation by length:** `dfs` has no cache, but each call forms a single chain of decreasing lengths, so no sublength is recomputed within one outer iteration. A later outer-loop length starts a fresh generation.
- **Closure over `n`:** The zero-pair rule relies on the current target length captured from the loop. Moving the helper elsewhere or evaluating it later would require passing the final length explicitly to preserve this meaning.
