## General

**Find all starts without quadratic matching**

An index `i` is eligible only when pattern `a` starts there. It is beautiful when at least one start `j` of pattern `b` satisfies `|i-j| <= k`.

The large constraints make repeated substring comparison unsuitable. The exact solution uses KMP twice to obtain sorted occurrence lists `resa` and `resb`, then merges those lists with one forward-only proximity pointer.

**Prefix functions capture reusable pattern borders**

For each pattern, the prefix function at index `i` stores the longest length that is both a proper prefix of the pattern and a suffix of the prefix ending at `i`.

During construction, mismatch fallback `j = prefix_function[j - 1]` tries the next viable border. Characters already known to match are not reread from scratch. Both `i` and total fallback movement are linear in pattern length.

Patterns `a` and `b` receive independent prefix arrays.

**KMP reports overlapping matches**

During text search, `j` is the current matched pattern-prefix length. Mismatches follow prefix links; matches advance `j`.

When a complete pattern ends at text index `i`, the start `i - j + 1` is appended. Then `j` falls back to the longest border rather than zero. This permits overlaps, such as both starts of `"aaa"` inside `"aaaa"`.

Each text scan is linear because fallback never causes the text index to move backward. Occurrences are appended in ascending start order.

**Use sorted geometry for proximity**

Pointer `j` into `resb` is shared across all `a` occurrences. For current start $p$:

- if the current `b` start is within `k`, append $p$;
- otherwise, if the next `b` start is strictly closer, advance `j`;
- otherwise stop, because later sorted starts only move farther away.

Absolute distance from a fixed $p$ to an increasing sequence decreases until the sequence passes $p$ and then increases. The inner loop therefore reaches a closest candidate without scanning the full list.

As `p` itself increases across `resa`, the best candidate index cannot move left. Total pointer advances across the whole merge are at most `len(resb)-1`.

**Why each answer is complete and unique**

KMP finds every occurrence start of both patterns, including overlaps. For each $p$ in `resa`, the merge checks a closest reachable `b` start. If its distance exceeds `k`, all `b` starts do; if it fits, the existential condition is satisfied.

The code appends $p$ at most once even if many `b` occurrences are nearby. Traversing `resa` in order makes the result sorted automatically.

**Large-input importance**

Here `s`, `a`, and `b` may each be as large as 500,000 characters. KMP preprocessing and scans are proportional to their actual lengths, and the occurrence merge is proportional to the number of matches. No substring copies proportional to pattern length are made per text position.

**An unintended debug side effect**

The protected source executes `print(resa, resb)`. With highly repetitive input, each occurrence list can have $\Theta(N)$ entries, so this may print enormous arrays. The return value is still correct, but the method is not silent and I/O can materially harm performance or pollute application output.

This line should be removed in a solution-correction pass. It is not part of KMP or the intended algorithm, and this document records it as an exact-source defect.

**Why KMP remains linear on repetitive text**

A string such as hundreds of thousands of `'a'` characters creates many partial matches and many overlapping full matches. KMP does not restart the text scan for each start. Prefix-function fallback changes only the pattern state while the text index continues forward.

Although one text character can trigger several fallback assignments, every fallback shortens `j`, and advances rebuild that length only a bounded total number of times. This amortized argument is why highly repetitive inputs produce large occurrence output but do not make the matching computation quadratic.

## Complexity detail

Let $N=|s|$, $A=|a|$, $B=|b|$, with $P$ and $Q$ occurrences. Prefix construction is $O(A+B)$; both searches total $O(N)$ up to a constant factor; merging is $O(P+Q)$. Algorithmic time is $O(N+A+B)$ because $P,Q=O(N)$.

Prefix arrays and occurrence lists require $O(A+B+P+Q)$ space, bounded by $O(N+A+B)$. Debug printing adds $O(P+Q)$ output volume in numeric entries and can dominate wall-clock behavior, though not the internal asymptotic algorithm.

## Alternatives and edge cases

- **Naive substring comparisons:** They can cost $O(N(A+B))$ in the large version.
- **Z algorithm:** It can find each occurrence list in linear time and is a valid alternative to KMP.
- **Binary-search `resb` for every `a`:** This costs $O(P\log Q)$; the monotone pointer uses list ordering more fully.
- **Overlapping pattern matches:** KMP’s post-match fallback preserves them.
- **`a` or `b` longer than `s`:** Its occurrence list is empty and the result is naturally empty.
- **`a == b`:** Every occurrence witnesses itself at distance zero.
- **Many witnesses:** A beautiful start appears only once.
- **Sorted result:** Occurrence discovery and append order already satisfy it.
- **Debug print:** Exact source emits potentially huge internal lists and is not production-clean.
