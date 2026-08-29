## General

**There is only one possible substring for each index**

Fix an index `i` and let `t = str(i)`. Suppose `t` has length `k`. Any substring equal to `t` must also have exactly `k` characters. The problem additionally requires that the substring end at index `i`.

A substring's length and ending position uniquely determine its start:

$$
\text{start}=i-k+1.
$$

Therefore the only possible candidate is

$$
\texttt{s}[i-k+1\ldots i].
$$

There is no need to try every earlier start position. A shorter substring cannot equal the $k$-digit representation, and a longer substring cannot equal it either. This simple length observation turns what might appear to be a substring-search problem into one direct comparison per index.

The source expresses the half-open Python slice for that candidate as

`s[i + 1 - k : i + 1]`.

The right endpoint is `i + 1` because Python excludes the slice's stop position. The slice therefore includes characters from `i + 1 - k` through `i`, exactly $k$ characters.

**Use the canonical decimal representation**

`str(i)` produces the ordinary decimal representation required by the contract. It has no leading zeros, except that index 0 is represented by the one-character string `"0"`.

This matters for indices with multiple digits. For index 12, the only successful candidate is `"12"` at positions 11 and 12. A longer ending substring such as `"012"` does not count, because it is not equal to `str(12)`. A two-character candidate `"02"` also fails even though converting it numerically would produce 2; the problem asks for exact string equality to the representation, not numeric parsing with ignored leading zeros.

The source performs direct string comparison:

`if s[i + 1 - k : i + 1] == t`

Both length and every digit must match. If they do, `i` is appended to `ans`.

**Every tested slice is within the processed prefix**

For every nonnegative index `i`, the number of decimal digits in `i` is at most `i + 1`. At index 0, both values are 1. For larger indices, even a multi-digit index is far larger than its digit count. Thus `i + 1 - k` is never negative for a valid index in the loop.

The candidate slice always lies fully inside `s[0:i+1]` and ends at the required location. The code does not accidentally rely on Python's special handling of negative slice starts.

**Scanning left to right automatically orders the output**

`for i in range(len(s))` visits indices 0, 1, 2, and so on through $N-1$. Whenever an index is good, it is appended immediately. Because the visit order is increasing, `ans` is already sorted as required. No final sort is needed.

For `s = "0234567890112"`:

- at `i = 0`, `t` is `"0"`, `k = 1`, and the slice `s[0:1]` is `"0"`, so 0 is appended;
- at `i = 11`, `t` is `"11"`, `k = 2`, and `s[10:12]` is `"11"`, so 11 is appended;
- at `i = 12`, `t` is `"12"` and `s[11:13]` is `"12"`, so 12 is appended.

Every other index fails its one candidate comparison. The answer is already `[0, 11, 12]` in increasing order.

**Why the test is both necessary and sufficient**

If the source appends `i`, the compared slice is contiguous, ends at `i`, and equals the decimal representation of `i`. It directly witnesses that `i` is good.

In the other direction, suppose `i` is good. By definition, some substring ending at `i` equals `str(i)`. Equality forces that substring to have length `k = len(str(i))`. There is only one length-$k$ substring ending at `i`, namely the exact slice checked by the source. That comparison must succeed, so the algorithm cannot omit a good index.

Together, these directions show that `ans` contains every good index and no bad index. The reasoning does not depend on surrounding digits: characters before the uniquely determined start are irrelevant, and characters after `i` cannot belong to a substring that must end at `i`.

**Why a general pattern-matching algorithm is unnecessary**

The pattern changes with every index: index 7 looks for `"7"`, index 42 looks for `"42"`, and so on. Yet each pattern has a prescribed ending position. Algorithms such as KMP or rolling hash are designed to locate a pattern at unknown positions or answer many arbitrary substring comparisons. Here the location is already known, and the pattern length is only the number of digits in the index.

Direct comparison is simpler and exact. It also avoids collision concerns that a rolling hash would introduce. With $N\le 10^5$, each index has at most five digits because the largest possible index is 99999, making the per-index work very small in practice.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$ and let $D$ be the maximum number of decimal digits among indices 0 through $N-1$. At index `i`, converting `i` to a string costs $O(k_i)$ for its digit count $k_i$. Creating the candidate slice also copies $k_i$ characters in Python, and comparing it with `t` takes up to $O(k_i)$ time.

The exact total is

$$
O\left(\sum_{i=0}^{N-1} k_i\right),
$$

which is bounded by $O(ND)$. Since $D=O(\log N)$ in the general decimal model, this can also be written as $O(N\log N)$. Under the explicit $N\le10^5$ constraint, $D\le5$, so the practical bound is linear with a small fixed factor. The manifest states $O(ND)$, accurately reflecting the source's conversions, slices, and comparisons.

At one iteration, `t` and the slice each contain at most $D$ characters, so temporary auxiliary space is $O(D)$. The answer may contain all $N$ indices, as in `"01234"`, and therefore uses $O(N)$ output space. The manifest's $O(D)$ space should be read as auxiliary space excluding the required returned list.

## Alternatives and edge cases

- **Compare characters without slicing:** Walk backward through the digits of `i` and compare them directly with `s`. This avoids allocating a substring and can reduce temporary space, but still performs $O(D)$ digit work per index.
- **Use `endswith` on each processed prefix:** `s.startswith(t, i + 1 - k, i + 1)` or an equivalent bounded comparison can avoid an explicit slice. It represents the same unique-candidate test.
- **Parse numeric suffixes:** Maintaining values of suffixes up to $D$ digits can work, but numeric equality needs extra care with leading zeros. Direct representation comparison matches the contract more transparently.
- **Rolling hash:** Hashing could compare candidates in constant expected time after preprocessing, but constructing `str(i)` still costs digit time, and collision handling makes it unnecessarily complex for at most five characters here.
- **Index zero:** Its representation is `"0"`, not an empty string. It is good exactly when `s[0] == "0"`.
- **Single-digit indices:** For indices 0 through 9, the candidate is just `s[i]`. Each is good exactly when that character equals the index's digit.
- **Transition from 9 to 10:** The candidate length changes from one to two. Index 10 checks `s[9:11]` against `"10"`; checking only `s[10]` would be wrong.
- **Leading zeros near an index:** Only the last $k$ characters are compared. Extra zeros before the candidate start neither help nor hurt, while a zero inside the candidate must match the corresponding character of `str(i)`.
- **No good indices:** `ans` remains empty and the function returns `[]` without special handling.
- **Every index good:** The result can contain $N$ integers, so output space is necessarily $O(N)$ even though working memory is only $O(D)$.
- **Increasing-order requirement:** The source's left-to-right scan already establishes the required order; sorting afterward would add unnecessary $O(G\log G)$ work for $G$ good indices.
