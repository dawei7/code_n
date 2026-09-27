# Guided Example: Shortest Distance to Target String in a Circular Array

## 1. The Instance We Will Solve

The input is a **0-indexed circular** array of words together with a target word and a starting index. "Circular" is not a metaphor here: it is a rewrite rule for indices. For an array of length $n$, the successor of position $i$ is

$$\mathrm{next}(i) = (i + 1) \bmod n, \qquad \mathrm{prev}(i) = (i - 1 + n) \bmod n,$$

so stepping right past the last cell lands on cell $0$, and stepping left from cell $0$ lands on cell $n-1$. Every step moves exactly one array position, in either direction, and the cost of a candidate route is simply the number of steps taken.

We work the first official instance:

- `words` = `["hello", "i", "am", "leetcode", "hello"]`
- `target` = `"hello"`
- `startIndex` = `1`

Here $n = 5$ and the starting position is $s = 1$, whose word is `"i"`. The required result is the shortest number of steps that reaches **any** position holding the target word, or `-1` when no position holds it. For this instance the two occurrences sit at positions $0$ and $4$; we will derive the two arc lengths for each of them, keep the smaller, and confirm the answer.

The whole difficulty of this problem is that a single matching position does not have one distance — it has two, one per direction — and the wrap-around causes the *numerically farther* index to be the *cheaper* one. Choosing this instance exposes exactly that.

## 2. Two Arcs Between Two Positions

Fix the start position $s$ and one matching position $k$. On a line there is exactly one distance, $\lvert k - s \rvert$. On a circle there are two disjoint arcs joining the same two cells, and their lengths add to the full circumference:

- the **clockwise / forward** arc, obtained by repeatedly applying $\mathrm{next}$:
  $$F(k) = (k - s) \bmod n,$$
- the **counter-clockwise / backward** arc, obtained by repeatedly applying $\mathrm{prev}$:
  $$B(k) = (s - k) \bmod n.$$

Because stepping right from $s$ reaches $k$ in $F(k)$ steps and stepping left from $s$ reaches $k$ in $B(k)$ steps, every route from $s$ to $k$ costs at least $\min\{F(k), B(k)\}$, and that value is achieved by simply walking the cheaper arc. Two facts make this computable with ordinary arithmetic:

$$F(k) + B(k) = n \quad \text{for every } k, \qquad \min\{F(k), B(k)\} = \min\{\lvert k - s \rvert,\; n - \lvert k - s \rvert\}.$$

The right-hand identity is the one worth remembering: the offset $d = \lvert k - s \rvert$ measures how far $k$ lies from $s$ in the *linearized* array, and the complementary arc is $n - d$. This is why the shortest circular distance never exceeds $\lfloor n/2 \rfloor$; an answer larger than half the circumference always has a cheaper counterpart going the other way.

## 3. Locating the Candidate Positions

Only positions whose word equals the target can be endpoints, so the first job is a linear scan that records matches. Scanning `words` from index $0$ upward for `target` = `"hello"` with $n = 5$:

| Index $i$ | `words[i]` | Match? | Role in the instance |
|:---:|:---|:---:|:---|
| 0 | `"hello"` | yes | candidate endpoint, one step to the left of the start |
| 1 | `"i"` | no | the start position $s$; it is not itself a match |
| 2 | `"am"` | no | irrelevant to the answer, but must still be inspected |
| 3 | `"leetcode"` | no | irrelevant to the answer |
| 4 | `"hello"` | yes | candidate endpoint, wrapping required |

So the candidate set is $\{0, 4\}$. Note that position $1$ being the start does not exempt it from inspection: had `words[1]` been `"hello"`, the correct distance would be $0$, and a scan that skipped the start index would miss it.

Because `words` may contain repeated words, we cannot stop at the first match either. Position $0$ and position $4$ both match; picking the first one found is a tempting shortcut that would be wrong for other inputs (for example `["a","x","x","a","x","x"]` with target `"a"` and `startIndex` = `1`, where the later match at index $3$ is the nearest). The scan therefore has to consider **every** matching position and keep the best.

## 4. Measuring Each Candidate on the Circle

For each candidate we compute the offset, the complementary arc, and the true circular cost. With $s = 1$:

| Candidate $k$ | Offset $d = \lvert k - s \rvert$ | Complementary arc $n - d$ | Cheaper arc $\min\{d, n-d\}$ | Direction it uses | Cumulative best |
|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | 1 | 4 | 1 | backward: $1 \to 0$ | 1 |
| 4 | 3 | 2 | 2 | backward through the wrap: $1 \to 0 \to 4$ | 1 |

Reading the first row: position $0$ is one place to the left of the start, so a single backward step suffices; the alternative is four forward steps, which is worse. Reading the second row is the instructive part: position $4$ is three positions to the right by index arithmetic, yet walking right costs $3$ steps while walking left costs only $2$, because the leftward walk falls off the front of the array and re-enters at the back. Comparing raw index distances ($1$ versus $3$) and picking position $0$ would still give the correct answer here, but it gives the wrong *reason* — position $4$'s distance is $2$, not $3$, and on inputs such as $n = 10$ with $s = 3$ and $k = 9$ (offset $6$, true cost $4$) the raw offset is not the distance at all.

The two arcs for each candidate also satisfy $F(k) + B(k) = 5$, which is a useful self-check: if the two directions you computed do not sum to $n$, one of them is wrong.

## 5. Step-by-Step Trace of the Linear Scan

The method walks the array once in index order, tests equality, and folds each match into a running minimum:

$$A_i = \min\Big( A_{i-1},\; \min\{d_i,\; n - d_i\} \Big) \quad \text{when } \texttt{words[i]} = \texttt{target}, \qquad A_i = A_{i-1} \text{ otherwise,}$$

with the accumulator seeded at $A_{-1} = n$. Seeding at $n$ is deliberate: it is strictly larger than every achievable distance ($0 \le d \le n-1$, so $\min\{d, n-d\} \le \lfloor n/2 \rfloor < n$), so the first match always replaces it, and an untouched accumulator at the end is an unambiguous "no match" signal.

| Scan step $i$ | `words[i]` | Equality test | $d_i$ | Arc cost $\min\{d_i, n-d_i\}$ | Accumulator $A_i$ | Note |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| seed | — | — | — | — | 5 | $A = n$ means "nothing found yet" |
| 0 | `"hello"` | true | 1 | 1 | 1 | first match immediately displaces the seed |
| 1 | `"i"` | false | — | — | 1 | start position, no update |
| 2 | `"am"` | false | — | — | 1 | no update |
| 3 | `"leetcode"` | false | — | — | 1 | no update |
| 4 | `"hello"` | true | 3 | 2 | 1 | candidate $2$ does not beat the incumbent $1$ |

The accumulator is monotone non-increasing across the scan, ends at $A_4 = 1$, and $1 \ne n$, so the reported answer is $1$. That agrees with the official example, which reaches the answer by enumerating four explicit routes: $3$ right, $2$ left, $4$ right, and $1$ left. The table above shows that we never need to enumerate routes at all — each endpoint is summarized by the minimum of its two arcs.

For the negative instance, take `words` = `["i","eat","leetcode"]`, `target` = `"ate"`, `startIndex` = `0`. No position matches, so the accumulator is never written, stays at $n = 3$, and the final guard converts that sentinel into `-1`.

## 6. Correctness and the Loop Invariant

**Invariant.** After processing scan step $i$, the accumulator $A_i$ equals the minimum circular distance from $s$ to every target position in the already-scanned prefix $\texttt{words}[0..i]$, and $A_i = n$ exactly when that prefix contains no target position.

*Initialization.* Before any element is read the prefix is empty, no candidate has been measured, and $A_{-1} = n$ records "no candidate yet". Since no distance can equal $n$, the sentinel is never confused with a genuine measurement.

*Preservation.* If `words[i]` is not the target, position $i$ is not an endpoint, no completion ending there can exist, and the minimum over the enlarged prefix is unchanged, so $A_i = A_{i-1}$. If `words[i]` is the target, the set of admissible endpoints for the prefix grows by exactly one element, and the new prefix minimum is the smaller of the old minimum and the new element's cost $\min\{d_i, n - d_i\}$ — precisely the update rule.

*Termination.* After step $n-1$ the invariant covers the whole array, so the accumulator equals the minimum distance over **all** target positions, or $n$ if there is none.

**Optimality.** Every route from $s$ to a position $k$ is a walk on the cycle graph $C_n$ between two of its vertices, so its length is at least the shorter arc length $\min\{F(k), B(k)\} = \min\{\lvert k-s \rvert, n-\lvert k-s \rvert\}$, and that lower bound is attained by walking the shorter arc. The accumulator therefore minimizes an exact per-candidate cost rather than a heuristic proxy. Combining this with the termination invariant gives the final claim: the returned value is the globally shortest distance to any occurrence of the target, and it is `-1` exactly when the target occurs nowhere.

## 7. Traps and Boundary Behaviour

| Scenario | Instance | Arithmetic | Result | Why the rule still holds |
|:---|:---|:---|:---:|:---|
| start is itself a match | `["x","y","z"]`, target `"y"`, `startIndex` = `1` | $d_1 = 0$, $\min\{0, 3\} = 0$ | 0 | The zero-length walk is a legal route, so the minimum can be $0$; the seed is still replaced. |
| duplicate matches on both sides | `["hello","i","am","leetcode","hello"]`, target `"hello"`, `startIndex` = `1` | $\{1, 2\} \to 1$ | 1 | Scanning all matches is what makes the choice between arcs meaningful; stopping early is unsafe. |
| exactly opposite positions | `["a","b","c","goal","d","e"]`, target `"goal"`, `startIndex` = `0` | $d = 3$, $\min\{3, 6-3\} = 3$ | 3 | With even $n$ the two arcs tie; the minimum is still well defined and both directions are equally cheap. |
| target absent | `["i","eat","leetcode"]`, target `"ate"`, `startIndex` = `0` | accumulator stays at $n = 3$ | -1 | The sentinel is unreachable as a real cost, so "unchanged" faithfully means "no occurrence". |
| single-cell circular array | `["only"]`, target `"only"`, `startIndex` = `0` | $d = 0$, $\min\{0, 1-0\} = 0$ | 0 | For $n = 1$ the only arc is the empty one; both formulas agree on $0$. |
| large offset near the wrap | $n = 6$, $s = 0$, match at $k = 5$ | $d = 5$, $\min\{5, 1\} = 1$ | 1 | Linear intuition says "five steps"; the complementary arc shows the true cost is one backward step. |

Two semantic traps deserve to be named explicitly. First, **value identity versus index identity**: the target is a word, not a position, and the array may hold that word many times; the algorithm must answer over the *set* of matching indices, and it compares words by exact equality, since `"ate"` and `"eat"` are unrelated even though they are anagrams. Second, **the sentinel is not an answer**: `n` is a legitimate array length but never a legitimate step count, which is what makes the final `-1` conversion sound. Returning the sentinel directly, or initializing the accumulator to `0`, would silently report nonsense.

## 8. Complexity: Time and Auxiliary Space

**Time.** The scan inspects each of the $n$ positions exactly once. Per position it performs one string equality comparison and, only for a match, a constant number of arithmetic operations (one offset, one complement, one minimum, one accumulator minimum). With $m$ matching positions the total work is $n$ comparisons plus $\mathrm{O}(m)$ arithmetic steps, and since $m \le n$ the bound is

$$T(n) = \mathrm{O}(n) + \mathrm{O}(m) = \mathrm{O}(n).$$

The word-length limit does not change this class: each comparison inspects at most a constant number of characters under the stated constraints, so comparisons are $\mathrm{O}(1)$ with respect to the array length. Both directions are handled inside one scan, so no second pass is needed and no sorting is performed — sorting the matching indices would cost $\mathrm{O}(n \log n)$ for no benefit.

**Auxiliary space.** The method keeps a single integer accumulator and a loop index; it never materializes the list of matching positions, a distance array, or a visited set. The extra memory is therefore constant:

$$S_{\text{aux}}(n) = \mathrm{O}(1).$$

That low space cost is the practical advantage over the alternative of collecting every match and then scanning that collection: both are linear in time, but the one-pass form needs no second container.

## 9. Alternatives and Their Trade-offs

| Alternative | How it would work | Cost | Why it is not preferred |
|:---|:---|:---|:---|
| Two separate directed sweeps | Walk forward from $s$ until a match, then walk backward from $s$ until a match; take $\min$. | $\mathrm{O}(n)$ time, $\mathrm{O}(1)$ space | Correct and equally cheap, but it needs two wrap-aware loops and two termination rules; the single formula $\min\{d, n-d\}$ collapses both directions into one comparison. |
| Duplicate the array and scan the window | Concatenate `words` with itself and slide a window of length $n$ around $s$. | $\mathrm{O}(n)$ time, $\mathrm{O}(n)$ space | The duplicate is pure overhead: the circular distance formula already encodes the wrap, so doubling the array buys nothing. |
| Sort the matching indices first | Collect matches, sort by circular distance from $s$, return the head. | $\mathrm{O}(m \log n)$ time | Sorting is unnecessary work when a running minimum over the same set already yields the head value in $\mathrm{O}(m)$. |
| Stop at the first match found | Return the first matching index's distance without scanning further. | $\mathrm{O}(n)$ to $\mathrm{O}(1)$ in the lucky case | Incorrect in general: a later match can be strictly nearer through the wrap, as $["a","x","x","a","x","x"]$ with target `"a"` and `startIndex` = `1` demonstrates. |
| Walk the circle step by step outward | Alternate one forward and one backward step, checking the word at each landing position. | $\mathrm{O}(n)$ time | Each position is compared on each attempt and wrap arithmetic is duplicated; the per-candidate formula gives the same answer with fewer comparisons and a cleaner invariant. |

The lesson of this instance generalizes: on a cycle, never measure separation with a single linear difference. Compute the offset from the start, and remember that the cheaper way around is the complement $n - d$ whenever that complement is smaller.
