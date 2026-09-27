# Guided Example: Append Characters to String to Make Subsequence

## 1. Reading the Problem as a Repair Budget

Two lowercase strings are given: a source `s` and a target `t`. Characters may only be
**appended to the right end of `s`**; nothing already inside `s` may be deleted, reordered, or
edited. The request is for the minimum number of appended characters that makes `t` a
**subsequence** of the resulting string.

The freedom is smaller than it first appears. Three properties fix the shape of every solution:

1. Appended characters land strictly after every character of `s`, in a single block.
2. Nothing that `s` already contributes can be moved, so the contribution of `s` to a
   subsequence match is constrained by its own left-to-right order.
3. Because the appended block sits at the extreme right, whatever `s` supplies must be consumed
   **before** the appended block begins.

Property 3 is the decisive one. Subsequence matching is order-preserving, so the characters that
`s` provides must be matched to an initial segment of `t` that lies entirely to the left of every
character taken from the appended block. There is no way for `s` to supply `t`'s middle while the
append block supplies `t`'s beginning. Consequently the problem collapses to a single question:

> How long is the longest prefix of `t` that is already a subsequence of `s`?

Call that length $k$. Then $t[0 .. k-1]$ is already realizable inside `s`, and the remaining
suffix $t[k ..]$ must be produced by appending, costing exactly $\lvert t \rvert - k$ new
characters. No cheaper repair exists, because the first $k+1$ characters cannot all be found in
`s` in order, so at least one of them must be appended — and appending a later character without
its predecessors would not preserve the required order.

## 2. Why the Matched Part Must Be a Prefix

Let the final string be $s + u$, where $u$ is the appended block. Suppose $t$ is a subsequence of
$s + u$. Split the witnessing embedding of $t$ at the boundary: the characters mapped into the
copy of $s$ form $t[0 .. k-1]$, and the characters mapped into $u$ form $t[k ..]$. This split is
forced, because positions inside $s$ all precede positions inside $u$ and the embedding is strictly
increasing in the original string.

So exactly one prefix of `t` can be charged to `s`. That also explains why "count the characters
of `t` that appear anywhere in `s`" is not the answer: a character may be present in `s` and still
be unusable, either because it appears before the characters that must precede it in `t`, or
because `s` does not contain enough copies of it.

## 3. The Decisive Instance: `s = "coaching"`, `t = "coding"`

This is the official medium instance (expected answer `4`). Indexing `t` from $0$:

| Position in `t` | 0 | 1 | 2 | 3 | 4 | 5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Character | `c` | `o` | `d` | `i` | `n` | `g` |

Scanning `s` left to right, a single cursor $j$ records how much of `t` has been matched so far.
The cursor only ever moves forward, and it advances only when the current character of `s` equals
the character of `t` the cursor currently points at.

| Step $i$ | `s[i]` | Cursor $j$ before | `t[j]` | Match | Cursor $j$ after | Matched prefix |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `c` | 0 | `c` | yes | 1 | `c` |
| 1 | `o` | 1 | `o` | yes | 2 | `co` |
| 2 | `a` | 2 | `d` | no | 2 | `co` |
| 3 | `c` | 2 | `d` | no | 2 | `co` |
| 4 | `h` | 2 | `d` | no | 2 | `co` |
| 5 | `i` | 2 | `d` | no | 2 | `co` |
| 6 | `n` | 2 | `d` | no | 2 | `co` |
| 7 | `g` | 2 | `d` | no | 2 | `co` |

The scan ends with $j = 2$: the matched prefix is `co`, so $k = 2$ and the answer is
$\lvert t \rvert - k = 6 - 2 = 4$. The repair is to append `ding`, producing `coachingding`, in
which `t` is embedded as `co` + `aching` + `ding`.

Note how three characters that visibly exist in `s` were wasted. The second `c` at index 3 and the
`i`, `n`, `g` at indices 5–7 are all letters of `coding`, yet none can be used: after the cursor
reached 2 it demanded `d`, and `d` never appears in `s` at all. Once the cursor stalls, every later
character of `s` is compared against the same stalled demand, and no amount of remaining input can
unstick it.

## 4. The Trap Instance: `s = "abcdef"`, `t = "fed"`

A counting argument gives the wrong answer here and exposes exactly what the cursor protects
against. Every letter of `fed` — `f`, `e`, and `d` — occurs in `abcdef`, so a multiset comparison
would suggest that nothing needs appending. Order says otherwise.

| Step $i$ | `s[i]` | Cursor $j$ before | `t[j]` | Match | Cursor $j$ after |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `a` | 0 | `f` | no | 0 |
| 1 | `b` | 0 | `f` | no | 0 |
| 2 | `c` | 0 | `f` | no | 0 |
| 3 | `d` | 0 | `f` | no | 0 |
| 4 | `e` | 0 | `f` | no | 0 |
| 5 | `f` | 0 | `f` | yes | 1 |

Only `f` is consumed, and the scan is then exhausted with $j = 1$. The answer is
$3 - 1 = 2$: append `ed`. The `d` and `e` sitting earlier in `s` are unreachable because the
cursor needed `f` first, and `f` is the last character of `s`. This is precisely the failure mode
of any method that ignores position.

## 5. Invariant and Why the Greedy Scan Is Optimal

**Invariant.** Immediately before examining `s[i]`, the cursor value $j$ equals the maximum length
of a prefix of `t` that is a subsequence of `s[0 .. i-1]`.

The invariant is established vacuously for $i = 0$, where the scanned region is empty and $j = 0$.
For the inductive step, the prefix of length $j$ remains realizable inside `s[0 .. i-1]`, so it
remains realizable inside `s[0 .. i]`, and the only candidate for a longer prefix is length $j+1$.
That length is realizable exactly when $t[j]$ occurs somewhere in `s[0 .. i]` after the position
used for $t[j-1]$. The scan has already consumed every earlier character of `s` while the cursor
sat at $j$, so no earlier occurrence of $t[j]$ was skipped; therefore $t[j]$ is reachable for the
first time precisely when `s[i] = t[j]`. Advancing the cursor on that equality is thus not merely
safe — it is required to keep $j$ maximal.

**Leftmost matching is optimal.** Suppose some other embedding of a prefix of `t` into `s` chose a
strictly later occurrence for some character than the greedy scan does. Exchanging that choice for
the earlier one can only free up more of `s` to the right, so it cannot destroy any completion. By
induction on the prefix length, the greedy cursor is pointwise no larger than the cursor of any
other valid embedding at every index of `s`. Since the final answer depends only on $k$, the
monotonicity of this comparison transfers directly: greedy attains the maximum $k$, hence the
minimum $\lvert t \rvert - k$.

**Termination and exactness.** The scan visits each character of `s` once and halts. The appended
block `t[k ..]`, taken as a whole, is a subsequence of the repaired string by construction, so the
answer is feasible. No smaller count is feasible, since any repair needs all of `t[k ..]` plus at
least one more character (the first unmatchable character at index $k$), for a total of at least
$\lvert t \rvert - k$. Feasibility and the lower bound coincide, so the computed value is the
optimum.

## 6. Boundary Analysis

Each row is an authored case whose expected value matches the lesson's rule
$\lvert t \rvert - k$ exactly.

| Instance | `s` | `t` | $k$ (matched prefix) | Appended suffix | Expected | Why it is a boundary |
|:---|:---|:---|:---:|:---|:---:|:---|
| Already done | `abcde` | `a` | 1 | empty | 0 | `t` has length 1 and its single character opens `s`; the repair budget is empty. |
| No overlap at all | `z` | `abcde` | 0 | `abcde` | 5 | The cursor never advances, so every character of `t` must be appended. |
| Single-character source | `c` | `coding` | 1 | `oding` | 5 | `s` contributes one character, and only because it is the very first demand. |
| Repeated source, wrong letters | `ccc` | `coding` | 1 | `oding` | 5 | Extra copies of `c` are useless: the cursor has already moved past `c`. |
| Repeated target prefix | `aaaa` | `aaab` | 3 | `b` | 1 | `s` exhausts exactly as the cursor reaches the one character `s` cannot supply. |
| Order inversion | `abcdef` | `fed` | 1 | `ed` | 2 | All letters exist in `s`; only positional order decides the answer. |
| Interleaved but complete | `axbyc` | `abc` | 3 | empty | 0 | Gaps in `s` are harmless as long as the demanded order survives. |
| Identical strings | `abc` | `abc` | 3 | empty | 0 | The degenerate best case: $k = \lvert t \rvert$ and no append is needed. |

The last two rows matter because they show the method does not require adjacency — only order. The
subsequence relation tolerates arbitrary deletions from `s`; it never tolerates a swap.

## 7. Alternatives and What They Cost

| Approach | Idea | Verdict |
|:---|:---|:---|
| Greedy leftmost cursor | Walk `s` once and advance a cursor into `t` on equality. | Correct and optimal; a single pass, constant auxiliary state. |
| Multiset intersection | Count letters common to `s` and `t` up to multiplicity. | Wrong: ignores order entirely, as `s = "abcdef"`, `t = "fed"` shows. |
| Longest common subsequence | Compute the full LCS of `s` and `t`, then subtract. | Wasteful and subtly wrong: the LCS need not be a prefix of `t`, so its length is not $k$. |
| Suffix-anchored matching | Try to place an interior part of `t` inside `s`. | Structurally impossible while appends are confined to the end of `s`. |
| Binary search over $k$ | Test each candidate prefix length with a fresh two-pointer check. | Correct but strictly more work: a linear scan already yields the maximal prefix in one pass. |

The LCS row is the instructive rejection. For `s = "coaching"`, `t = "coding"`, the LCS is `cong`
with length 4, which would suggest a budget of $6 - 4 = 2$ — but `cong` is not a prefix of `coding`,
and the true prefix match is only `co`. Only a prefix-shaped match is purchasable with a
suffix-only append.

## 8. Complexity Derivation

Let $m = \lvert s \rvert$ and $n = \lvert t \rvert$.

**Time.** The scan examines each character of `s` exactly once, performing one comparison and at
most one cursor increment per character. Cursor increments total at most $n$ across the whole run,
because the cursor is bounded by $n$ and never decreases. The total work is therefore
$O(m + n)$, which the stated constraint $m, n \le 10^{5}$ handles comfortably in one pass. When
$n = 0$ the loop still performs $m$ comparisons but appends nothing, and when $m = 0$ the answer is
immediately $n$; both are covered by the same bound without special-casing.

**Auxiliary space.** The method stores only the cursor $j$ and the two string lengths — a constant
number of integer values regardless of input size — so the auxiliary space is $O(1)$. No
intermediate string, table, or index structure proportional to the input is required; the appended
suffix is never materialized, only its length $\lvert t \rvert - k$ is returned. The input strings
themselves are read-only and are not counted as auxiliary space.

**Answer recomputation.** The final step is the subtraction $\lvert t \rvert - k$ on two integers
bounded by $10^{5}$, a constant-time operation. Nothing in the method depends on the alphabet
beyond equality testing of single characters, so the bound holds unchanged for lowercase English
letters or any larger alphabet.
