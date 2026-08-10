## General

**Every maximal run can keep at most two characters**

A violation consists of three equal consecutive characters. Consider a maximal run of one letter with length $L$. If $L\le2$, all of it can remain. If $L>2$, at least $L-2$ characters must be deleted, and keeping exactly the first two achieves that lower bound.

Different runs are separated by another letter. The algorithm never deletes an entire nonempty run—it keeps at least its first character—so deleting extras cannot merge two runs of the same letter across the separator. Each run can be optimized independently.

**Read the exact condition**

The solution scans the original string with index `i` and character `c`. It appends `c` when at least one of these is true:

- `i < 2`, meaning fewer than two original predecessors exist;
- `c != s[i - 1]`;
- `c != s[i - 2]`.

It skips a character only when $i\ge2$ and the current character equals both immediately preceding original characters. That is exactly the third or later position inside a run of equal characters.

For a run `"aaaaa"`, the first two positions are appended. Every later `a` has two original `a` predecessors and is skipped. For `"aabaa"`, no position is the third equal character of its run, so the entire string remains.

**Why comparing the original string is safe**

Many streaming solutions compare the current character with the last two characters already kept. This exact code instead compares `s[i - 1]` and `s[i - 2]` in the original string.

That works because the decision is purely run-based. Inside a long run, every character from the third onward has two equal original predecessors and must be removed. At the beginning of a new run, at least one of the two original predecessors differs, so the first character is kept; the second is also kept. Since every separating run keeps characters, deletions never create a new cross-run triple that was not already inside one original run.

**Why the number of deletions is minimum**

Any fancy result can retain at most two characters from a run of length $L$, so it must delete at least $\max(0,L-2)$ there. The solution keeps exactly $\min(L,2)$ from every run, deleting exactly that unavoidable number.

Concatenating these locally optimal retained prefixes remains fancy because adjacent runs have different characters. Summing per-run lower bounds proves the global deletion count is minimum.

**Why the returned string is unique**

The statement guarantees uniqueness. For equal characters within a run, deleting different physical occurrences can lead to the same output value. Every minimum deletion keeps two copies when possible, and those copies are indistinguishable as characters. Thus the resulting string is the original run sequence with every length capped at two, which is unique.

The answer list stores retained characters and `"".join(ans)` creates the final string.

**Trace deletions across multiple runs**

For `s = "aaabaaaa"`, indices zero and one of the first `a` run are appended, while index two is skipped because it matches its two predecessors. The `b` begins a new run and is appended because it differs from prior `a` characters. In the final run of four `a` characters, the first two are appended and the last two are skipped. The output is `"aabaa"`.

Skipping the third `a` in the first run does not endanger the original-index checks for the later `b`. That `b` is retained and permanently separates the two `a` runs. This concrete behavior is why the source can consult original predecessors instead of maintaining a retained-run counter.

**Why retaining the first two is canonical**

Within a run, all characters have the same value. A minimum-deletion result keeps exactly two when the run length is at least two. Whether those copies came from the beginning, middle, or end cannot change the returned string. The implementation keeps the first two simply because the scan sees them before any violation exists.

## Complexity detail

Let $N$ be the string length.

The loop examines each character once and performs constant-time comparisons and a possible append. Joining the retained characters takes $O(N)$ in the worst case. Total time is $O(N)$.

The answer list and returned string can each contain all $N$ characters when the input is already fancy, so space is $O(N)$. Apart from output construction, scalar iteration state is constant.

## Alternatives and edge cases

- **Compare against output tail:** Append unless the last two retained characters both equal the current one. This is more general and has the same $O(N)$ bounds.
- **Run-length encoding:** Explicitly find every run and append its first two characters. It expresses the proof directly but needs more indexing code.
- **Repeated string deletion:** Removing characters from immutable strings can cause quadratic copying.
- **Length below three:** Every character satisfies `i < 2` or no triple exists, so the string is returned unchanged.
- **Exactly three equal characters:** The first two are kept and the third is removed.
- **Very long run:** Exactly two copies survive regardless of length.
- **Run length one:** Its sole character is always retained and cannot form a triple.
- **Alternating letters:** No character equals both prior originals, so all are retained.
- **Two same, one different, two same:** Both runs of length two remain and the separator prevents merging.
- **Original-versus-output comparison:** It is safe here specifically because the property and optimal deletions operate independently on maximal runs.
- **Unique value result:** Different choices of identical occurrences to delete cannot change the resulting character sequence.
- **Input immutability:** The source does not modify `s`; it builds a new result.
