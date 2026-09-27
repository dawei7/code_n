# Guided Example: Most Popular Video Creator

## 1. The Instance We Will Trace

- **Input:** `creators = ["alice", "bob", "alice", "chris"]`, `ids = ["one", "two", "three", "four"]`, `views = [5, 10, 5, 4]`
- **Required output:** `[["alice", "one"], ["bob", "two"]]` (any order is acceptable)

Video $i$ was made by $\text{creators}[i]$, carries identifier $\text{ids}[i]$, and has $\text{views}[i]$ views. A creator's **popularity** is the sum of the views of *all* their videos. We must return every creator whose popularity is maximal, paired with the identifier of that creator's most-viewed video; when two of a creator's videos tie on views, the lexicographically smallest identifier wins. This instance is chosen because it contains both tie kinds at once: `alice` and `bob` finish with equal popularity, and `alice`'s two videos have equal view counts but different identifiers, so both the creator-level tie and the video-level tie must be resolved, and they are resolved by different rules.

## 2. Two Aggregates Per Creator, and Two Different Tie Rules

The whole problem lives in two quantities indexed by creator:

$$
\text{total}[c] = \sum_{i \,:\, \text{creators}[i] = c} \text{views}[i],
\qquad
\text{best}[c] = \text{the identifier of the most-viewed video of } c .
$$

The creator-level rule is a maximum over popularity: return every $c$ attaining $\max_c \text{total}[c]$, and all of them when several tie. The video-level rule inside a creator is a maximum over view counts with a **lexicographic** tie-break on the identifier. These are distinct orderings operating on distinct objects, and conflating them is the main way to go wrong:

- popularity decides *which creators* appear in the answer;
- view count decides *which video* represents each of those creators;
- only when two of that creator's videos have identical view counts does the identifier ordering become decisive, and then it prefers the smaller string, never the larger one and never the earlier index.

The pair $(\text{views}, \text{id})$ can be ordered by a strict total order $\succ$ that encodes both parts at once:

$$
(v_1, d_1) \succ (v_2, d_2) \iff v_1 > v_2 \ \text{or}\ \bigl(v_1 = v_2 \ \text{and}\ d_1 < d_2\bigr).
$$

Because $\succ$ is a strict total order on pairs with no ties possible, $\text{best}[c]$ is uniquely determined for every creator, so the answer is well defined even when several videos share the maximum view count.

## 3. The Full Trace

Both aggregates are updated as the videos are read in order. The `best` column shows the pair currently selected for that creator.

| step | $i$ | $\text{creators}[i]$ | $\text{ids}[i]$ | $\text{views}[i]$ | $\text{total}$ after | leader after | $\text{best}$ after |
|---|---|---|---|---|---|---|---|
| 1 | 0 | `"alice"` | `"one"` | $5$ | $\{\text{alice} \mapsto 5\}$ | `alice` | $\{\text{alice} \mapsto (5, \text{"one"})\}$ |
| 2 | 1 | `"bob"` | `"two"` | $10$ | $\{\text{alice} \mapsto 5,\ \text{bob} \mapsto 10\}$ | `bob` | $\{\text{bob} \mapsto (10, \text{"two"})\}$ added |
| 3 | 2 | `"alice"` | `"three"` | $5$ | $\{\text{alice} \mapsto 10,\ \text{bob} \mapsto 10\}$ | tie | $\text{alice}$ keeps $(5, \text{"one"})$ |
| 4 | 3 | `"chris"` | `"four"` | $4$ | $\{\text{alice} \mapsto 10,\ \text{bob} \mapsto 10,\ \text{chris} \mapsto 4\}$ | tie | $\{\text{chris} \mapsto (4, \text{"four"})\}$ added |

Step 3 is the decisive one. `"three"` has the same view count as `"one"`, so the view-count part of $\succ$ is not decisive and the identifier part takes over: since `"one"` is lexicographically smaller than `"three"`, the stored pair does **not** change and `"three"` is discarded. A rule that replaced the stored video on any equal view count, or that preferred the later video, would answer `["alice", "three"]` here.

The finished aggregates:

| creator | videos | view counts | total popularity | best identifier | best views | in the answer? |
|---|---|---|---|---|---|---|
| `"alice"` | 2 | $5, 5$ | $10$ | `"one"` | $5$ | yes — ties for the maximum |
| `"bob"` | 1 | $10$ | $10$ | `"two"` | $10$ | yes — ties for the maximum |
| `"chris"` | 1 | $4$ | $4$ | `"four"` | $4$ | no — strictly smaller popularity |

The maximum popularity is $10$, attained by two creators, so both are emitted with their own best identifier: `[["alice", "one"], ["bob", "two"]]`, which agrees with the authored expected output for this input.

## 4. Lexicographic Ordering Is Its Own Trap

The identifier comparison is ordinary string order over lowercase letters, where a proper prefix is smaller than the longer string that extends it. Previewing a few pairs shows that no length-, index-, or numeric-based substitute reproduces it:

| pair | lexicographically smaller | what a wrong rule would pick |
|---|---|---|
| `"one"` vs `"three"` | `"one"` | the later index (`"three"`), wrongly |
| `"a"` vs `"ab"` | `"a"` | the longer string, if length were preferred |
| `"z"` vs `"a"` | `"a"` | the earlier index (`"z"`), wrongly |
| `"ab"` vs `"ac"` | `"ab"` | the same answer, but for the wrong reason if the second letter were ignored |
| `"x"` vs `"x"` | indistinguishable | a tie on the identifier itself, which is harmless because the videos are distinct but the answer string is not |

Identifiers are *not* unique across videos: two videos may carry the same identifier and are still counted as separate videos with their own view counts. Likewise, identical identifiers do not merge a creator's entries; only the creator name groups anything.

## 5. The Invariant and Why the Method Is Correct

**Total invariant.** After the first $t$ videos have been read, $\text{total}[c]$ equals the sum of $\text{views}[i]$ over all $i < t$ with $\text{creators}[i] = c$.

*Proof by induction on $t$.* For $t = 0$ every creator's total is implicitly $0$ and the claim is vacuous. Given the claim at $t-1$, reading video $t-1$ adds $\text{views}[t-1]$ to exactly one entry, the entry of $c = \text{creators}[t-1]$; every other entry is untouched. The equality therefore continues to hold, and because each video contributes to exactly one creator, no view is counted twice and none is lost. When all $n$ videos have been read, the totals are the true popularities.

**Best invariant.** After the first $t$ videos have been read, for every creator $c$ that has appeared, $\text{best}[c]$ holds the pair $(\text{views}, \text{id})$ of a video of $c$ among the first $t$, and no other video of $c$ among the first $t$ is strictly greater under $\succ$.

*Induction step.* A newly read video of $c$ replaces the stored pair only when it is strictly greater under $\succ$, and $\succ$ is a strict total order, so the stored pair remains a maximum of the creator's videos seen so far. Every video of $c$ is examined and either displaces the incumbent or is dominated by it, so at the end the stored pair is the maximum over *all* of $c$'s videos. This is exactly the statement's rule: maximum view count, and the lexicographically smallest identifier among those maxima.

**Selection soundness and completeness.** The answer contains creator $c$ if and only if $\text{total}[c]$ equals the maximum of all totals. By the total invariant this is precisely the set of creators that the statement calls most popular, so no qualifying creator is omitted and no qualifying creator is spurious. The identifier attached to each is supplied by the best invariant and is therefore that creator's required identifier.

**Uniqueness and output order.** For each creator the pair $\text{best}[c]$ is unique, so the two-element answer rows are determined; the statement permits any ordering of the rows, and rows are distinct because they are keyed by distinct creator names.

## 6. Boundaries and Traps This Instance Exposes

| situation | concrete instance | outcome and the trap it exposes |
|---|---|---|
| Creator-level tie | the traced instance | `alice` and `bob` both reach $10$; both must be returned. Keeping only the first maximum found loses `bob`. |
| Video-level tie, smaller identifier arrives later | `creators = ["a", "a", "b"]`, `ids = ["z", "a", "b"]`, `views = [7, 7, 13]` | `"a"` is selected over `"z"` even though it arrives second. A rule that keeps the first video on a tie fails. |
| Higher view count arrives later | `creators = ["aa", "bb", "aa"]`, `ids = ["z", "m", "q"]`, `views = [2, 6, 5]` | `aa` keeps `"q"` at $5$ views, displacing `"z"` at $2$. The best video is not the first video. |
| Duplicate identifiers | `creators = ["a", "a", "b"]`, `ids = ["x", "x", "y"]`, `views = [4, 5, 8]` | The two `"x"` videos are distinct; `a`'s best is `"x"` at $5$ and its popularity is $9$. Treating the identifier as a primary key would drop a video and change the total. |
| Zero views | `creators = ["b", "a", "b"]`, `ids = ["z", "y", "x"]`, `views = [0, 0, 0]` | All creators tie at $0$ popularity and all are returned; `b`'s two zero-view videos still need the tie-break, giving `"x"`. A method that treats $0$ as "no video" produces a missing identifier. |
| Single video | `creators = ["solo"]`, `ids = ["only"]`, `views = [0]` | Answer `[["solo", "only"]]`. A creator with zero views can still be the most popular creator of the input. |
| Three-way creator tie | `creators = ["a", "b", "c", "a"]`, `ids = ["a1", "b1", "c1", "a2"]`, `views = [2, 5, 5, 3]` | All three creators reach $5$ and all three are returned, each with its own best identifier; `a`'s best is `"a2"` at $3$, not the earlier `"a1"` at $2$. |
| Different identifier lengths | any input | Lexicographic order is not length order, and identifiers may have lengths from $1$ to $5$. Comparing by length is wrong. |
| Distinct creators, one video each | any input | Every creator's best is trivially their only identifier; the popularity comparison decides alone. |
| Ordering of the output rows | any input | Rows are unordered by the statement; sorting them is optional and must not be relied upon by a judge that accepts any order. |

## 7. Alternative Methods and Their Trade-offs

| method | time | auxiliary space | trade-off |
|---|---|---|---|
| One pass with a popularity map plus a best-pair map (derived above) | $O(n)$ expected | $O(C)$ | Each video performs a bounded number of hash lookups and updates; no grouping pass, no sort, and the answer is formed directly from the totals. |
| Group video indices per creator, then reduce each group | $O(n)$ expected | $O(n)$ | Conceptually simple and easy to debug, but it stores every video index instead of only the current best, using more memory than the answer needs. |
| Sort all videos by creator, then by descending views, then by identifier | $O(n \log n)$ | $O(n)$ | The first element of each creator run is that creator's best, so the tie-break falls out of the ordering; costs a logarithmic factor and reorders the entire input. |
| Per-creator heap of the top videos | $O(n \log n)$ | $O(n)$ | Useful when a creator must report a whole ranking rather than a single best video; here only one element per creator is ever needed. |
| Two passes: totals first, then a second scan for bests | $O(n)$ expected | $O(C)$ | Same asymptotics as the single pass with one extra traversal; clearer if the two aggregates are thought of as separate phases. |
| Compare identifiers numerically by parsing digits | not applicable | $O(1)$ | Identifiers are lowercase-letter strings, so numeric parsing is undefined for most inputs; a numeric shortcut is a defect, not an optimization. |

## 8. Complexity Derivation

Let $n$ be the common length of the three input arrays and let $C \le n$ be the number of distinct creators. Let $L \le 5$ be the maximum length of a creator name or identifier, which the constraints bound by a constant.

- **One video.** The step performs a popularity lookup and an increment, plus a best-pair lookup with at most one comparison of two small integers and, on a tie, one string comparison of length at most $L$. Hash operations are expected $O(1)$ in $n$ and the string comparison is $O(L)$, so one video costs $O(L)$ expected, which is $O(1)$ for the given limits.
- **All videos.** Summing over $n$ videos gives $O(nL)$ expected time, i.e. $O(n)$ with constant-length strings. No sort and no second pass over the input are needed.
- **Final selection.** Walking the popularity map to find its maximum and then emitting the matching rows costs $O(C)$ — one traversal plus one comparison of identifier strings per emitted row.

The total expected running time is $\Theta(n)$.

For auxiliary space, the popularity map and the best-pair map each hold at most one entry per distinct creator, so together they need $O(C)$ storage; nothing per video is retained, because a video is reduced to two numbers and one identifier as soon as it is read. The returned array contains one row per creator in the argmax set, so the output is $O(C)$ as well. Since $C \le n$, the bound is $O(n)$ auxiliary space in the worst case — attained only when every video has a different creator — and it stays constant-space when the whole input comes from a single creator.