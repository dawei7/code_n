## General

**Equal word lengths turn characters into aligned tokens**

Let $S=\lvert s\rvert$, let $W=\lvert\texttt{words}\rvert$, and let $L=\lvert\texttt{words}[0]\rvert$. Every valid answer has exactly $W$ words and therefore exactly $WL$ characters.

The equal-length guarantee is what makes a sliding window possible. Once a starting alignment is chosen, `s` can be read in chunks of exactly $L$ characters. A valid concatenation starting at index `p` belongs to the alignment `p % L`. The outer loop tries every remainder from zero through `L - 1`, so no possible start is omitted.

For `L = 3`, one scan considers starts `0, 3, 6, ...`, another considers `1, 4, 7, ...`, and the third considers `2, 5, 8, ...`.

**Store required multiplicities, not just membership**

`cnt = Counter(words)` records how many copies of every word are required. This matters when `words` contains duplicates. A set could say that `"foo"` is allowed but could not distinguish a requirement of one copy from a requirement of three.

For one alignment, `cnt1` stores the word counts in the current half-open window `s[l:r]`. Both boundaries always move in multiples of $L$, and `r` points just after the last accepted token.

The window invariant is:

- every token in `s[l:r]` belongs to `cnt`;
- for every word, its count in `cnt1` is at most its required count in `cnt`; and
- `cnt1` exactly describes the aligned tokens between `l` and `r`.

The empty initial window satisfies all three facts.

**Read one complete token at the right boundary**

The condition `while r + k <= m` requires a full $L$-character chunk. The source slices

```python
t = s[r : r + k]
r += k
```

and advances `r` immediately. An incomplete suffix shorter than one word is never treated as a candidate token.

Here the exact source names string length `m`, word count `n`, and word length `k`; this explanation uses $S$, $W$, and $L$ to avoid confusing those roles.

**Reset after a token that is not in the word bank**

`Counter` returns zero for a missing key, so

```python
if cnt[t] == 0:
```

recognizes a token that can never belong to a valid concatenation. No window can cross it. The code sets `l = r`, placing the next window after the bad token, and clears `cnt1` because none of the earlier tokens remain relevant.

The `continue` then moves directly to the next right token. This reset is safe because every candidate crossing the unrecognized chunk would contain a word absent from `words`.

**Shrink only when the newly added word exceeds its quota**

For a recognized token, `cnt1[t] += 1` adds it to the window. Before this addition, every count was within quota. Therefore only the count of `t` can now be too large. It is sufficient to test

```python
while cnt1[t] > cnt[t]:
```

rather than scan all dictionary entries.

Each loop iteration removes the leftmost aligned token:

```python
rem = s[l : l + k]
l += k
cnt1[rem] -= 1
```

The loop stops once one occurrence of the excess `t` has been removed. Other removed words may fall below their quotas, but none can become excessive by removal. The invariant is restored.

This handles duplicate words precisely. If two copies of `"good"` are required, the window may contain two; the third forces the left boundary forward until only two remain.

**Window length alone becomes enough after normalization**

After reset or shrinking, all tokens are recognized and every count is within its required quota. The total of all quotas is $W$, so such a window can contain at most $W$ tokens.

When

```python
if r - l == n * k:
```

the window contains exactly $W$ aligned tokens. Since no word exceeds its quota and all quotas together also total $W$, every quota must be met exactly. The window is a permutation-concatenation, and `l` is appended.

There is no need to compare two entire counters at every step; the invariant plus exact window size proves equality of the multisets.

**Why the source does not remove a match immediately**

After recording a valid window, the code leaves it intact. On the next recognized token, the window would temporarily contain $W+1$ tokens. Because total allowed multiplicity is only $W$, the newly added word must exceed its quota. The overflow loop then removes tokens from the left until validity is restored. This naturally exposes an overlapping next match when one exists.

For `s = "barfoofoobar"` and `words = ["bar", "foo"]`, the aligned window finds `"barfoo"` at zero. Adding the next `"foo"` makes `foo` excessive, so the leftmost `bar` and then the older `foo` are removed as needed; later tokens can form the next valid window. No special post-match slide is required.

**Trace the first example**

With `words = ["foo", "bar"]`, quotas are one each and $L=3$. In alignment zero, the tokens are `bar`, `foo`, `the`, `foo`, `bar`, `man`.

`bar` and `foo` form a six-character normalized window, so index zero is appended. `the` is unknown, causing a reset to index nine. `foo` and `bar` then form another complete window, appending nine. `man` resets again. The other two alignments find no valid window, producing `[0, 9]`.

**Why every answer is found exactly once**

Any valid start has one unique remainder modulo $L$, so exactly one outer scan visits its token boundaries. Within that scan, unrecognized words reset only impossible crossings, and quota shrinking removes only prefixes that cannot participate in a normalized window ending at the current `r`. When a valid multiset occupies $W$ tokens, its bounds satisfy the invariant and exact-size test, so it is appended. Each `l`/`r` state is reached in only its alignment scan, preventing duplicate reporting of the same start.

## Complexity detail

Let $U$ be the number of distinct words.

- **Time complexity: $O((S+W)L)$ with Python slicing and hashing.** Across all $L$ alignments, the right boundary processes $O(S)$ tokens in total, and the left boundary also removes at most $O(S)$ tokens in total. Each token slice and string hash/lookup can cost $O(L)$. Constructing `Counter(words)` processes $W$ length-$L$ strings. Under a model treating fixed-length token operations as constant, the window movement itself is linear in $S$.
- **Auxiliary space: $O(U+L)$ in a reference-counting view, or $O(UL)$ when accounting for stored token characters.** `cnt` and `cnt1` hold at most one entry per distinct word. Temporary slices have length $L$. The answer list is output space and is excluded.

The manifest's `O(n * L)` time and `O(k)` space use different symbol conventions; the explicit symbols above identify the string length, word count, word length, and distinct-word count separately.

## Alternatives and edge cases

- **Check every character start independently:** Build a fresh frequency table for each $WL$-character candidate. It is simpler but repeats token work and can cost $O(SWL)$.
- **Enumerate word permutations:** Duplicate words and factorial growth make this infeasible.
- **Rolling hashes:** They can reduce substring comparison cost but add collision or verification complexity; multiplicity tracking is still required.
- **Duplicate entries in `words`:** Counter quotas preserve exact multiplicity rather than mere membership.
- **Total concatenation longer than `s`:** Every alignment ends without reaching a $WL$ window, so the result is empty.
- **Unknown token:** It clears the window because no valid answer can cross it.
- **Incomplete final characters:** `r + L <= S` prevents treating them as a word.
- **Overlapping answers:** Leaving a found window in place lets the next addition and shrink expose them.
- **One word:** Every aligned occurrence of that word is reported.
- **Non-empty word list:** Guaranteed by the contract; the exact source reads `words[0]` without an empty guard.
- **Any result order:** Offset-by-offset traversal determines an order that need not be globally sorted, which the contract permits.
