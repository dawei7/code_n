## General

**Translate distance from the right into an index**

For a string of length $n$, the character paired with index $i$ is at $n-i-1$. This formula maps the first character to the last, the second to the second-last, and so on. When $n$ is odd, it maps the center index to itself.

**Scan in the order required by the answer**

Visit indices from `0` upward. At each index, compare `s[index]` with `s[len(s) - index - 1]`. Return immediately on equality. Because every smaller index has already been tested and rejected, the first returned index is necessarily the minimum one requested. If the scan ends, every legal index has failed and `-1` is correct.

More formally, before testing index $i$, the loop has established that no index below $i$ satisfies the mirrored-character equality. If the characters at $i$ match, that fact plus the established failures proves $i$ is the smallest valid index. Otherwise the same statement extends to the next iteration. Exhausting all indices therefore proves that no valid index exists.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The scan examines at most $n$ mirrored pairs, so it takes $O(n)$ time. It keeps only the current index and uses $O(1)$ auxiliary space.

The benchmark defines size as the string length and uses no-match strings of `8`, `32`, and `100` characters. The accepted direct-index scan and an independent inward two-pointer scan should scale linearly. A correct implementation that walks backward from the end anew to locate each mirrored character performs a triangular number of character visits and should fail only the scaling verdict.

## Alternatives and edge cases

- **Reverse once:** Comparing `s` with `s[::-1]` finds the same index in $O(n)$ time, but materializing the reversed string uses $O(n)$ auxiliary space.
- **Rebuild or rewalk the suffix for every index:** Recomputing each mirror independently is correct but repeats work and can take $O(n^2)$ time.
- **Two pointers:** Move one pointer from each end and count the left index. This has the same $O(n)$ time and $O(1)$ space as direct indexing.
- **Single character:** Index `0` mirrors itself, so it is always returned.
- **Odd length:** The center mirrors itself; therefore an odd-length input always has a valid index at or before the center.
- **Even length:** No position is forced to match itself, so `-1` is possible.
- **Symmetric match:** If a noncentral index matches, its mirror matches as well; scanning left to right still returns the smaller qualifying index first.
