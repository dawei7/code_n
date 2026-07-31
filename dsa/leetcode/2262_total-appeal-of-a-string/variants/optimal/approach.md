## General

**Track only substrings ending at the current position**

Let `ending_appeal` be the sum of appeals of all substrings whose right
endpoint is the previous index. Appending the current character preserves all
existing distinct-character contributions. The only change is that the
current character becomes newly distinct for some suffixes.

**Count where the new character first contributes**

Suppose character `s[index]` last appeared at position `previous`, using `-1`
when it has not appeared. A substring ending at `index` gains a new distinct
character exactly when its start lies after `previous`. There are
`index - previous` such start positions. Therefore update
`ending_appeal += index - previous`, add that value to the global total, and
record `index` as the character's latest occurrence.

Every substring belongs to exactly one right endpoint. At that endpoint,
`ending_appeal` counts each character once for precisely the starts after its
last earlier occurrence. It is therefore the exact sum of distinct counts for
all substrings ending there. Summing these endpoint totals counts the appeal of
every substring exactly once.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The algorithm performs constant work per
character, so time is $O(n)$. The latest positions of the fixed 26-letter
alphabet and two running totals use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate starts and extend a set:** Maintaining a distinct-character set for every start is correct but takes $O(n^2)$ time.
- **Build every substring separately:** Recomputing its character set can take $O(n^3)$ time and unnecessary allocations.
- **Per-character combinatorial contribution:** Summing each occurrence's range of influence also gives $O(n)$ time, but the ending-substring recurrence is compact.
- **Single character:** Its only substring has appeal `1`.
- **All characters equal:** Every substring has appeal `1`, so the result is $n(n+1)/2$.
- **All characters distinct:** Each substring's appeal equals its length.
- **Repeated character after a gap:** Only starts after its previous position gain a new contribution.
- **Large result:** The sum can exceed 32-bit integer range.
