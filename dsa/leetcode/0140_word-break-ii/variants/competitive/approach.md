## General

**Separate valid cut discovery from sentence enumeration**

The competitive solution first identifies dictionary-word intervals that begin after a reachable prefix. It stores those intervals in a Boolean matrix `valid`. It then runs depth-first search over that cut graph to construct sentences.

Its main structures are:

- `can_break[i]`: whether prefix `s[0:i]` has at least one segmentation;
- `valid[start][end]`: whether `s[start:end + 1]` is a dictionary word and `start` is reachable from zero;
- `path`: the words selected along the current DFS route;
- `result`: the final joined sentences.

This two-phase organization avoids retesting dictionary membership during enumeration.

**Build only edges from reachable prefix positions**

`can_break[0]` is true because the empty prefix is the starting state. For each ending length `i`, the loop tries word length `l` from one through `min(i, max_len)`.

The possible word occupies `s[i-l:i]`. It becomes a usable graph edge only if `can_break[i-l]` is true and the substring appears in `wordDict`.

When both conditions hold, the source:

- marks `valid[i-l][i-1] = True`;
- sets `can_break[i] = True`.

It deliberately does not break after finding one word. Word Break II must preserve every valid edge, because different final sentences may reach the same prefix length through different words or continue from it in different ways.

The maximum-word-length bound prevents testing intervals that cannot equal a dictionary word.

**What the matrix represents**

Think of string positions `0` through `n` as vertices. A true `valid[a][b]` represents an edge from position `a` to position `b + 1`, labeled by `s[a:b + 1]`.

Because the edge is stored only when `can_break[a]` is true, every stored edge is reachable from position zero. The matrix does not prove that the edge can eventually reach position `n`; some stored edges may lead to dead ends.

If `can_break[n]` is false after preprocessing, there is no complete path from zero to `n`, so the code returns an empty result without invoking DFS.

**Enumerate paths and restore the mutable path**

`wordBreakHelper` receives a starting position. If it equals `len(s)`, the selected intervals cover all characters. The helper joins `path` with single spaces and appends that sentence.

Otherwise, it tries every ending index `i` from `start` to `n - 1`. A true matrix cell indicates an allowed next word. The statement:

`path += [s[start:i+1]]`

mutates the existing list in place, just like appending one element. Recursion explores every continuation from `i + 1`. After return, `path.pop()` removes exactly that word and restores the caller’s path before the next edge is tried.

That restoration is essential. Without it, words from one branch would leak into sentences built by another branch.

**Why outputs are sound and complete**

Every DFS step follows a matrix edge whose substring belongs to the dictionary. Endpoints advance from `start` to `i + 1`, so pieces are contiguous and never overlap. A sentence is emitted only at position `n`, proving it covers the full string.

Conversely, every valid sentence determines a sequence of prefix endpoints. During preprocessing, each earlier endpoint is reachable and each next word belongs to the dictionary, so every corresponding matrix edge is marked. DFS tries those edges and reaches `n`, emitting the sentence.

Different cut sequences follow different edge paths. Joining them produces every valid sentence in an allowed order.

**The input-container assumption**

The docstring says `wordDict` is a `Set[str]`, but the current Reference supplies a list. Direct `substring in wordDict` remains correct with a list, yet membership becomes a linear scan.

Converting the list to a set is needed before relying on expected hash-lookup complexity. This exact source does not perform that conversion.

## Complexity detail

Let $n$ be the string length, $m$ the dictionary size, $L$ the maximum word length, and $P$ the total number of partial DFS path states visited. Let $R$ be the total size of emitted sentence strings.

Preprocessing tests at most $nL$ intervals. Under the source’s set assumption, slicing and hashing a candidate of length at most $L$ gives $O(nL^2)$ time. Under the actual list contract, membership may scan $m$ words, giving a conservative $O(nmL^2)$ worst-case bound.

Enumeration scans up to $n$ possible endpoints at each visited path state and constructs output strings at leaves, so a clear output-aware bound is $O(nP+R)$. The source comment summarizes this as $O(nr)$ when `r` is the result count, but $P$ is more precise because the matrix can contain reachable edges that cannot reach the end. Those dead partial paths may still be explored whenever at least one complete segmentation makes `can_break[-1]` true.

The `valid` matrix alone uses $O(n^2)$ space, and `can_break` plus recursion/path use $O(n)$. Results use $O(R)$. Total space including output is $O(n^2+n+R)$, plus the input dictionary. This contradicts the manifest’s omission of the quadratic matrix in `O(D+n+R)` unless its undefined $D$ is explicitly intended to include that matrix.

The stated manifest time $O(S+n+R)$ also omits interval preprocessing and path exploration.

## Alternatives and edge cases

- **Memoized suffix sentences:** Cache all sentences beginning at each index. It avoids recomputing suffix enumeration but can retain output-sized intermediate lists.
- **Trie plus suffix feasibility:** Walk dictionary prefixes in a trie and recurse only to indices that can reach the end. This avoids both repeated slicing and dead branches.
- **Pure backtracking with a set:** It is simpler and uses no quadratic matrix, but repeats membership checks and can revisit identical suffixes.
- **Sparse edge lists:** Store only actual word endpoints for each start instead of an $n\times n$ Boolean matrix. This can reduce storage when valid intervals are sparse.
- **One complete word:** Preprocessing creates edge `0 -> n`, and DFS emits the word without extra spaces.
- **No complete segmentation:** `can_break[-1]` is false, so enumeration is skipped and `[]` is returned.
- **Several words sharing prefixes:** All matching interval lengths remain marked because preprocessing does not break after the first match.
- **Word reuse:** The dictionary and matrix rules do not consume entries, so the same value can label multiple intervals.
- **Mutable path operation:** `path += [word]` mutates the list; the matching `pop()` must execute after every recursive call.
- **Empty string outside the contract:** The matrix has no rows, `can_break[-1]` is true, and the helper would emit the empty string. The Reference requires nonempty `s`.
- **List-versus-set mismatch:** Correctness survives, but the source’s membership-based time comment assumes a container different from the current input type.
- **Quadratic storage:** Even when there are few results, allocating `valid` costs $O(n^2)$; this must not be hidden behind an output-only bound.
