## General

**Binary-search the maximum allowed run length.** For a candidate `m`, `check(m)` asks whether at most `numOps` flips can make every identical-character run have length at most `m`.

Feasibility is monotone: if limit `m` is achievable, any larger limit is also achievable with the same flips. Candidate results therefore form false values followed by true values, which `bisect_left` can search.

**Handle target length one separately.** Maximum run length one means no equal adjacent characters. A binary string must be exactly one of two alternating patterns:

`010101...` or `101010...`.

The source compares `s` with the first pattern. Expression

`sum(c == t[i & 1] for i,c in enumerate(s))`

counts matches, not mismatches. If this count is `cnt`, flips needed to reach the opposite pattern are `cnt`, while flips to reach the first pattern are `n-cnt`. Taking `min(cnt,n-cnt)` chooses the cheaper alternation.

**Why ordinary run splitting needs a different formula.** For `m>1`, inspect each maximal original run independently. A run of length `k` can be broken by flipping one character after each block of `m` retained equal characters. The minimum number is

$$
\left\lfloor\frac{k}{m+1}\right\rfloor.
$$

Each flip accounts for a group of `m+1` positions that otherwise forces an overlong run.

**Collect maximal run lengths in one scan.** Variable `k` increments for every character. A run ends at the final index or when `c != s[i+1]`. At that boundary, the source adds `k // (m+1)` to `cnt` and resets `k`.

The feasibility result is `cnt <= numOps`.

**Why `m=1` cannot use the run formula.** Flips placed independently inside neighboring original runs can interact: a flipped boundary character may merge with the adjacent opposite run. Requiring a globally alternating target captures these interactions exactly. For `m>1`, the standard run-splitting count is sufficient.

**Trace a long run.** For six zeros and candidate `m=2`, cost is `6//3=2`. Flipping positions two and five can divide the zeros into pieces no longer than two. With only one allowed flip, candidate two fails.

For run length five and `m=2`, cost is one. A centrally placed flip creates zero runs of lengths two and two.

**Search candidates one through n.** The source passes virtual sorted sequence `range(n)` to `bisect_left` with `lo=1` and key `check`. It probes indices representing candidate lengths.

Although `range(n)` contains only 0 through `n-1`, if every probed candidate is false, insertion position is `n`. That correctly returns maximum run length `n`, which is always achievable without flips.

**Why first true is the optimum.** Every smaller candidate was proven to require too many flips, and the returned candidate itself is feasible. Monotonicity makes it the minimum possible longest run.

**Interpret a feasible flip placement inside one run.** For cap `m>1`, divide a run conceptually into blocks of `m+1`. Flipping one carefully chosen character in each full block ensures no untouched stretch contains more than `m` equal symbols. A leftover suffix shorter than `m+1` needs no additional flip. This constructive picture explains the quotient rather than treating it as a memorized formula.

**Why the operation budget is only compared at the end.** `cnt` is the minimum flips required across all runs. If it is below `numOps`, unused flips need not be performed because operations are allowed at most that many times. Equality also succeeds. The source does not require consuming the entire budget.

**Version-I constraint context.** Here `n<=1000`, so an $O(n)$ check repeated $O(\log n)$ times is comfortably within bounds. The algorithm is identical to version II even though version I could tolerate slower alternatives.

**The manifest's space bound is loose.** The source does not allocate a run list or transformed string. `range` is lazy, and the alternating pattern is represented by constant string `"01"`. Auxiliary space is $O(1)$ apart from interpreter iteration state, not $O(n)$.

## Complexity detail

Each feasibility check scans $n$ characters and uses constant work, so it costs $O(n)$. Binary search performs $O(\log n)$ checks, giving $O(n\log n)$ time.

Counters and the lazy range use $O(1)$ auxiliary space. No candidate string of length $n$ is built. This corrects the manifest's $O(n)$ space claim.

## Alternatives and edge cases

- **Try every limit:** It costs $O(n^2)$ rather than binary searching monotone feasibility.
- **Dynamic programming over flips:** It is unnecessary once run costs are derived.
- **Already alternating:** `check(1)` needs zero flips and answer is one.
- **All characters equal:** Run cost drives the search; answer may be `n` when no flips exist.
- **`numOps=0`:** The result is the original longest run.
- **Unlimited useful flips:** Alternating output makes answer one.
- **Odd string length:** The two alternating patterns have unequal zero/one counts, but match counting still works.
- **Run exactly `m`:** It needs zero flips.
- **Run exactly `m+1`:** It needs one flip.
- **Leftover run fragment:** Fewer than `m+1` positions add no quotient.
- **Unused budget:** Feasibility uses `<=`, not equality.
- **Candidate `m=1`:** Global alternation logic is mandatory.
- **Insertion index `n`:** It represents the always-feasible unmodified upper bound.
- **Python bisect key:** It applies `check` to virtual candidate values.
- **Input preservation:** The string is never modified.
- **Import requirement:** `bisect_left` must support the `key` argument.
