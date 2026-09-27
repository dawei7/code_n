# Guided Example: Subsequence With the Minimum Score

## 1. The score charges a span, not a count

Characters may be deleted from `t` until what remains is a subsequence of `s`. If nothing is deleted the score is $0$; otherwise the score is

$$
\text{right} - \text{left} + 1
$$

where `left` is the smallest deleted index and `right` is the largest. The score therefore charges the whole interval between the outermost deletions, including characters that were *kept*.

| Deleted indices | `left` | `right` | Score $\text{right} - \text{left} + 1$ |
|---|---|---|---|
| `{1}` inside `"bzaa"` | 1 | 1 | 1 |
| `{1, 3}` inside `"axbyc"` | 1 | 3 | 3 |
| `{0, 4}` inside `"axyzb"` | 0 | 4 | 5 |
| `{0, 1, 2}` inside `"xyz"` | 0 | 2 | 3 |

The second row is the crucial one: two deletions three positions apart cost three, matching the sample where `s = "abc"` and `t = "axbyc"` has answer `3`. Deleting the middle character `"b"` as well would cost exactly the same, because `right` and `left` would not move.

This yields the structural reduction. If an optimal deletion set spans `[left, right]`, then deleting *every* character in that span is also legal — the retained characters are a subset of what was retained before, and a subsequence of a subsequence of `s` is still a subsequence of `s` — and it has the same score. Hence some optimal solution deletes one **contiguous block** of `t`. The problem becomes: choose a block of `t` to delete, keeping a prefix and a suffix, and minimize the block length.

## 2. The shape of a candidate solution

Let $n$ be the length of `t`. A candidate is described by two numbers: the start $k$ of the deleted block, and its length $x$. The block occupies indices $k, \dots, k+x-1$, so the surviving characters are

$$
t[0..k-1] \quad \text{(a prefix, empty when } k = 0\text{)}
\qquad \text{and} \qquad
t[k+x..n-1] \quad \text{(a suffix, empty when } k+x \ge n\text{)}.
$$

The candidate is feasible when those two surviving pieces can both be found in `s` **in order and without sharing a character**. The answer is the smallest feasible $x$, and $x = 0$ is the case where `t` is already a subsequence of `s`, which scores $0$ because nothing is removed.

## 3. Two greedy anchors

Feasibility needs to know, for every prefix of `t`, how little of `s` it needs, and for every suffix of `t`, how late it can start. Two arrays answer exactly that.

| Anchor | Direction of the scan | Meaning | Value when no embedding exists | Sentinel for the empty piece |
|---|---|---|---|---|
| $L_k$ | left to right through `s`, matching `t` front to back | the smallest index in `s` at which the prefix $t[0..k-1]$ can finish | "no embedding" | $L_0 = -1$, the artificial position before `s` |
| $R_j$ | right to left through `s`, matching `t` back to front | the largest index in `s` at which the suffix $t[j..n-1]$ can start | "no embedding" | $R_n = m$, the artificial position after `s` |

Both arrays come from one pass each, and both directions are forced by an exchange argument:

- **A prefix should finish as early as possible.** If some embedding of $t[0..k-1]$ finishes at position $p$, then matching each character to the earliest position available at or after the previous one finishes no later than $p$. So the greedy left-to-right match gives the minimum possible finishing position, leaving the most room for the suffix.
- **A suffix should start as late as possible.** Symmetrically, matching $t$ from its last character backwards, always taking the latest available position in `s`, gives the maximum possible starting position, which is the most permissive constraint for the prefix.

A candidate block is then feasible exactly when

$$
L_k < R_{k+x}
$$

with the sentinels covering the empty pieces. The inequality is strict because the two embeddings are disjoint: the prefix ends at $L_k$ and the suffix begins at $R_{k+x}$, and one character of `s` cannot serve both sides.

## 4. Worked instance: the first official sample

Take `s = "abacaba"` and `t = "bzaa"`, whose required answer is `1`. Writing `s` by position:

| Position in `s` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Character | `a` | `b` | `a` | `c` | `a` | `b` | `a` |

The forward pass walks `s` once, always trying to match the next unmatched character of `t`:

| Step | Cursor in `s` | `s[i]` | Next unmatched character of `t` | Match? | Recorded |
|---|---|---|---|---|---|
| 1 | 0 | `a` | `b` | no | — |
| 2 | 1 | `b` | `b` | yes | $L_1 = 1$, the prefix `"b"` finishes at position 1 |
| 3 | 2 | `a` | `z` | no | — |
| 4 | 3 | `c` | `z` | no | — |
| 5 | 4 | `a` | `z` | no | — |
| 6 | 5 | `b` | `z` | no | — |
| 7 | 6 | `a` | `z` | no | — |
| end | 7 | past the end | `z` still unmatched | — | $L_2, L_3, L_4$ have no embedding |

The backward pass walks `s` from the right, matching `t` from its last character:

| Step | Cursor in `s` | `s[i]` | Next unmatched character of `t` | Match? | Recorded |
|---|---|---|---|---|---|
| 1 | 6 | `a` | `a` at `t[3]` | yes | $R_3 = 6$, the suffix `"a"` starts at position 6 |
| 2 | 5 | `b` | `a` at `t[2]` | no | — |
| 3 | 4 | `a` | `a` at `t[2]` | yes | $R_2 = 4$, the suffix `"aa"` starts at position 4 |
| 4 | 3 | `c` | `z` at `t[1]` | no | — |
| 5 | 2 | `a` | `z` at `t[1]` | no | — |
| 6 | 1 | `b` | `z` at `t[1]` | no | — |
| 7 | 0 | `a` | `z` at `t[1]` | no | — |
| end | -1 | before the start | `z` still unmatched | — | $R_0, R_1$ have no embedding |

The single character `z` occurs nowhere in `s`, and that one absence decides everything: any prefix of `t` that includes `z` (length 2 or more) has no embedding, and any suffix that includes `z` (starting at index 1 or earlier) has no embedding.

## 5. Testing candidate block lengths

First test $x = 0$, the case of deleting nothing. Every $k$ from $0$ to $n = 4$ is tried, and the whole of `t` splits at that point:

| $k$ | Deleted block | Prefix kept | Suffix kept | $L_k$ | $R_k$ | $L_k < R_k$? |
|---|---|---|---|---|---|---|
| 0 | none | empty | `bzaa` | -1 | no embedding | no |
| 1 | none | `b` | `zaa` | 1 | no embedding | no |
| 2 | none | `bz` | `aa` | no embedding | 4 | no |
| 3 | none | `bza` | `a` | no embedding | 6 | no |
| 4 | none | `bzaa` | empty | no embedding | 7 | no |

Every split fails, which is correct: `t` contains `z`, so `t` is not a subsequence of `s` and the score cannot be $0$.

Now test $x = 1$, deleting a single character. Here $k$ ranges over $0 \dots 3$, and the suffix begins at $k+1$:

| $k$ | Deleted character | $L_k$ | $R_{k+1}$ | $L_k < R_{k+1}$? | Verdict |
|---|---|---|---|---|---|
| 0 | `b` at index 0 | -1 | no embedding for `zaa` | fails | rejected; the retained suffix still contains `z` |
| 1 | `z` at index 1 | 1 | 4 | $1 < 4$, true | feasible |
| 2 | `a` at index 2 | no embedding for `bz` | 6 | fails | rejected; the retained prefix still contains `z` |
| 3 | `a` at index 3 | no embedding for `bza` | 7 | fails | rejected; the retained prefix still contains `z` |

Exactly one candidate survives, at $k = 1$. The minimum feasible block length is therefore $1$, matching the required answer. Reconstructing the deletion from the anchors:

| Retained piece | Characters | Embedding in `s` | Ordering constraint |
|---|---|---|---|
| prefix of length $k = 1$ | `"b"` | position 1, the greedy leftmost match | must finish before the suffix starts, $L_1 = 1$ |
| deleted block | `"z"` at `t[1]` | removed; here `left` = `right` = 1 | score $1 - 1 + 1 = 1$ |
| suffix from $k + x = 2$ | `"aa"` | positions 4 and 6, the greedy rightmost match | must start after the prefix ends, $R_2 = 4 > 1$ |

The surviving string is `"baa"`, which is a subsequence of `"abacaba"` at positions 1, 4, 6, and the score of deleting only index 1 is $1$. Since $x = 0$ was infeasible, no better score exists.

## 6. Monotonicity, and why the smallest feasible length is the answer

Testing every length in increasing order would be correct but slow. The feasibility predicate is **monotone**: if some block of length $x$ works, then every longer block containing it works too. Concretely, if $L_k < R_{k+x}$ holds, then for $x' > x$ the retained suffix $t[k+x'..n-1]$ is a suffix of $t[k+x..n-1]$, so it is a subsequence of `s` from position $R_{k+x}$ onward; and the rightmost embedding of a shorter suffix cannot start earlier than the rightmost embedding of the longer one, so $R_{k+x'} \ge R_{k+x}$ and the inequality survives. Deleting more can never make a feasible candidate infeasible.

Monotone predicates have a first true value, and binary search finds it in $O(\log n)$ evaluations. The search range is $0 \dots n$, and $x = n$ is always feasible: with $k = 0$ both retained pieces are empty, and the sentinels give $L_0 = -1 < m = R_n$. So the answer always exists and never exceeds the length of `t`.

## 7. Why the verdicts are exact

The correctness of every verdict rests on one invariant, which the two passes establish and the feasibility test consumes:

> **Invariant.** For every split point $k$, the pair $(L_k, R_{k+x})$ is the most permissive pair of embeddings available to the retained prefix and the retained suffix: the prefix cannot finish later than $L_k$ under any embedding, and the suffix cannot start earlier than $R_{k+x}$ under any embedding. A block of length $x$ at $k$ is therefore deletable if and only if those optimal anchors can be ordered, that is, if and only if $L_k < R_{k+x}$.

The argument then has two directions.

*A feasible test can be carried out.* When $L_k < R_{k+x}$, embed the prefix greedily at positions ending at $L_k$ and the suffix greedily at positions starting at $R_{k+x}$. All prefix positions are at most $L_k$ and all suffix positions are at least $R_{k+x}$, so every prefix position precedes every suffix position, no position is reused, and the concatenation of the two embeddings is a genuine embedding of the retained string in `s`. Deleting the block is then a legal move with score exactly $x$ (or $0$ when $x = 0$).

*Every legal deletion is discovered.* Take any deletion set with score $x$, and let $l$ and $r$ be its outermost deleted indices, so that $r - l + 1 = x$. Because deleting the whole span $[l, r]$ is at least as permissive and costs the same, consider the deletion of that block with $k = l$: the retained prefix $t[0..l-1]$ and retained suffix $t[r+1..n-1] = t[l+x..n-1]$ are both subsequences of `s`, and their embeddings must be ordered because they are embedded in one string. Any embedding of the prefix finishes at some position at least $L_{l}$, the minimum possible, and any embedding of the suffix starts at some position at most $R_{l+x}$, the maximum possible. Since a valid ordered pair exists, the most permissive pair also works: $L_l < R_{l+x}$.

Together the two directions make the test an exact decision procedure for "is score $x$ achievable", so the smallest $x$ that passes it is the minimum score.

## 8. Boundary behaviour

| Instance | `s` | `t` | Answer | What it shows |
|---|---|---|---|---|
| Already a subsequence | `"abcde"` | `"ace"` | 0 | The test at $x = 0$ succeeds and nothing is removed |
| Middle block only | `"abacaba"` | `"bzzzaa"` | 3 | Deleting `"zzz"` leaves `"baa"`, embedded at positions 1, 4, 6 |
| Prefix removed | `"abc"` | `"xabc"` | 1 | The block starts at index 0, so the retained string is a bare suffix |
| Suffix removed | `"abc"` | `"abcx"` | 1 | The block ends at the last index, so the retained string is a bare prefix |
| Span covers a character that could have been kept | `"abc"` | `"axbyc"` | 3 | Deleting only `"x"` and `"y"` still scores 3, because the score charges the span; deleting `"xby"` is equally cheap |
| One usable character | `"a"` | `"aaaa"` | 3 | Only one `a` can be embedded, so three copies must go, and they cannot be pushed to both ends without enlarging the span |
| Both ends removed | `"xyz"` | `"axyzb"` | 5 | Removing the first and last characters charges the entire string, so the whole of `t` may as well be deleted |
| Nothing matches at all | `"cde"` | `"xyz"` | 3 | No anchor pair can straddle anything, so the answer is the full length |

## 9. Other strategies and their trade-offs

| Strategy | Idea | Time | Assessment |
|---|---|---|---|
| Anchor arrays plus binary search on the block length | the method derived here | $O(m + n \log n)$ | One feasibility sweep per candidate length, over a monotone predicate |
| Anchor arrays plus a single monotone pointer | $L$ and $R$ are both non-decreasing in their indices, so the smallest feasible window can be advanced instead of searched | $O(m + n)$ | Same information, one extra linear scan; removes the logarithmic factor |
| Enumerate every block and test it directly | $O(n^2)$ blocks, each verified by walking `s` | $O(n^2 m)$ | Correct but hopeless for lengths up to $10^5$ |
| Dynamic programming over prefixes of both strings | a classic subsequence table with one state per pair of prefixes | $O(mn)$ | At $10^5 \times 10^5$ states this is far beyond any budget |
| Greedy deletion of every character that fails to match once | walk both strings and delete the mismatches as they appear | linear | Wrong: mismatches encountered in one left-to-right walk are not necessarily the cheapest span, and the walk cannot reconsider its earlier choices |

## 10. Traps this instance exposes

- **Confusing the score with the number of deleted characters.** In `s = "abc"`, `t = "axbyc"`, deleting `"x"` and `"y"` scores 3, not 2. Any reasoning that charges one unit per deletion is wrong.
- **Minimizing over arbitrary deletion sets.** Because a span may be cleared for free, an optimal solution always deletes a contiguous block; searching over subsets is unnecessary work and can even hide the right answer behind a larger score.
- **Off-by-one on the split point.** A block starting at $k$ with length $x$ keeps $k$ characters at the front and resumes at index $k + x$. Pairing $L_k$ with $R_{k+x-1}$ or with $R_{k+x+1}$ tests a different deletion than the one intended.
- **Comparing without strictness.** The condition is $L_k < R_{k+x}$. Equality would claim that one character of `s` ends the prefix and starts the suffix at once, which is impossible.
- **Matching the suffix in the wrong direction.** The prefix must be anchored as early as possible and the suffix as late as possible. A single left-to-right greedy walk cannot establish $R$, because it commits early positions that the suffix may need.
- **Forgetting the sentinels.** The empty prefix is always embeddable, and so is the empty suffix. Without the artificial positions before and after `s`, the case "delete the entire string" has no representation and the search range breaks at $x = n$.
- **Assuming the answer fits inside a small length.** The answer is bounded by the length of `t`, which can be $10^5$, so the candidate range is the whole interval $0 \dots n$.
- **Overlooking the $0$ case.** The score of $0$ is special: it means nothing is deleted, and it can only be reported when `t` is already a subsequence of `s`.

## 11. Time and auxiliary space

Let $m$ be the length of `s` and $n$ the length of `t`.

- **Forward pass.** One walk through `s`, advancing over `t` as matches are found: $O(m)$.
- **Backward pass.** One walk through `s` in the opposite direction: $O(m)$.
- **One feasibility test.** For a fixed candidate length $x$, every split point $k$ is examined once with two array lookups and one comparison: $O(n)$.
- **Binary search.** $O(\log n)$ feasibility tests, since the predicate is monotone on the range $0 \dots n$.
- **Total time complexity.** $O(m) + O(n \log n)$, dominated by the search over candidate lengths.
- **Auxiliary space complexity.** $O(n)$ for the two anchor arrays, one entry per position of `t`; the sentinels are single integers and the candidate scanning needs no extra storage. The strings themselves are only read.