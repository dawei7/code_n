## General
**Search the infinite repetition without building it**

Character `i` of endlessly repeated `a` is simply `a[i mod A]`. Any distinct starting alignment occurs within the first `A` positions. Therefore, if `b` occurs at all, its first occurrence ends before $A + B - 1$ virtual characters have been inspected.

**Build the target's KMP fallback table**

Compute the longest proper-prefix/suffix length for every prefix of `b`. While scanning virtual characters, a mismatch can then reuse the longest target prefix already known to match instead of restarting from the next position.

**Convert the first match endpoint into repetitions**

When KMP finishes matching all `B` target characters at virtual index `i`, the shortest repeated text prefix containing that occurrence has length $i + 1$. The required number of complete copies is $ceil((i + 1) / A)$. Because the scan encounters match endpoints in increasing order, the first match gives the minimum repeat count.

**Why a bounded scan proves impossibility**

Starts separated by `A` see exactly the same repeating character sequence. Testing enough virtual text for every start offset from zero through $A - 1$ to cover `B` characters exhausts all alignments. If KMP finds no match within $A + B - 1$ characters, later starts only repeat an already failed alignment, so the answer is `-1`.

## Complexity detail
Building the KMP table takes $O(B)$ time and space. The virtual scan examines at most $A + B - 1$ characters, with amortized constant fallback work per character, for total $O(A + B)$ time. The only growing auxiliary structure is the $O(B)$ prefix table.

## Alternatives and edge cases
- **Build the minimum-length concatenation plus one copy:** if $A=\lvert a\rvert$ and $B=\lvert b\rvert$, test `b` inside `a` repeated $\lceil B/A\rceil$ and one additional time; it is concise but allocates the repeated string and relies on the substring-search implementation.
- **Rabin-Karp over virtual characters:** can scan linearly with rolling hashes, but collision handling complicates an exact result.
- **Restart matching at every source offset:** compares `b` character by character for each alignment and can take $O(AB)$ time.
- A match may begin near the end of one copy and cross more than one repetition boundary.
- Even when `b` is shorter than `a`, the minimum valid answer is one rather than zero.
- A character appearing in `b` but absent from `a` makes the answer `-1`.
