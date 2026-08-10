## General

The required groups are determined completely by position. The first starts at index $0$, the next at index $k$, then $2k$, and so on. Every group takes up to $k$ consecutive source characters, and only the final group can be short.

The exact solution expresses that procedure in one list comprehension:

`[s[i : i + k].ljust(k, fill) for i in range(0, len(s), k)]`

**Generate every group start exactly once**

The range `range(0, len(s), k)` begins at zero and advances by `k`. Since $k \ge 1$, it produces the strictly increasing starts $0,k,2k,\ldots$ that are still less than `len(s)`. Each source index belongs to exactly one interval beginning at one of these positions. There are no gaps because one slice ends where the next begins, and there is no overlap because starts are spaced by exactly the desired group length.

The string is guaranteed non-empty, so the range always produces at least index zero and the result always contains at least one group.

**Slice at most k characters**

For a start `i`, `s[i : i + k]` selects source indexes from `i` through `i + k - 1`. Python’s slice end is exclusive. If `i + k` is past the string’s end, slicing safely stops at `len(s)` rather than raising an error.

Every non-final start has at least $k$ characters remaining and therefore yields a slice of length exactly $k$. The final start may also yield exactly $k$ characters when the source length is divisible by $k$, or it may yield the remaining $r$ characters where $1 \le r < k$.

Because all earlier slices have full length, padding each generated slice is equivalent to padding only the last short group. The code does not need to identify the last iteration explicitly.

**Pad with the required fill character**

The call `.ljust(k, fill)` returns a string of at least width `k`. If the slice already has length $k$, it is returned unchanged. If it has length $r<k$, `ljust` appends exactly $k-r$ copies of `fill` on the right.

Right padding is essential: the original remaining characters must appear first, followed by fill characters. Prepending fill characters would change the order obtained after removing padding.

The contract guarantees that `fill` is exactly one lowercase English character, which is the valid kind of fill argument for `str.ljust`.

For `s = "abcdefghij"` and `k = 3`, the starts are $0,3,6,9$. Their raw slices are `"abc"`, `"def"`, `"ghi"`, and `"j"`. The first three already have width three. The last is extended by two `"x"` characters to `"jxx"`.

**Why the reconstruction requirement holds**

Each source character appears in exactly one slice and retains its original relative order. Full slices receive no fill characters. Only the short suffix receives padding after its real characters. Removing those known trailing fill additions and concatenating groups therefore restores every character of `s` in order.

There is a subtle conceptual point: `fill` might also naturally occur in `s`. The output does not mark which equal-looking characters are padding. That is not a correctness problem because the procedure determines the number of added characters from the original length modulo $k$. The code appends exactly that number only after all original characters.

**Why no mutable group builder is required**

Python slicing already creates each consecutive substring, and `ljust` already implements the precise final completion rule. A manual nested loop would track the same boundaries and append the same characters but would add more state without changing the algorithm.

## Complexity detail

Let $n=\lvert s\rvert$, and let $G=\lceil n/k\rceil k$ be the total number of characters in the returned groups after padding. The slices collectively copy all $n$ source characters. The `ljust` operations produce the group strings whose total length is $G$. Thus the precise time bound is $O(G)$, equivalently $O(n+k)$ because $n \le G < n+k$.

This distinction matters when $k>n$: a one-character source with $k=100$ must still create a 100-character output group. The manifest’s simplified $O(n)$ bound treats group size as bounded or focuses on scanning the source, but the exact output-sensitive cost includes padding.

The returned list and its strings contain $G$ characters and therefore use $O(G)$ output space. Apart from the required output and temporary slice or group being constructed, the comprehension keeps constant loop state. If output space is counted, as the local manifest does, the bound is $O(n+k)$ in the two input variables.

## Alternatives and edge cases

- **Explicit while loop:** Advance a pointer by `k`, append each slice, and pad the final result after the loop. This mirrors the editorial and has the same complexity but uses more statements than the exact comprehension.
- **Manual character accumulation:** Build a current group one character at a time and flush it at size `k`. This works but duplicates behavior already provided by slicing and `ljust`.
- **Pad the whole source first:** Append enough fill characters to make the total length divisible by `k`, then slice fixed-size groups. This is correct but constructs another padded source string in addition to the output groups.
- **Length divisible by k:** Every slice already has length `k`, so `ljust` makes no change and no fill character is added.
- **Length not divisible by k:** Exactly `k - (n % k)` fill characters are appended to the final slice.
- **k greater than the source length:** The range yields only zero. The entire source becomes the first and last group and is padded to length `k`.
- **k equals one:** Every character becomes its own one-character group, and padding is never needed.
- **Source consists of the fill character:** Original fill-looking characters remain ordinary source content. Only the computed suffix padding is newly added.
- **One-character source:** It forms one group; that group is unchanged when `k = 1` and receives `k-1` padding characters otherwise.
- **No empty final group:** When $n$ is divisible by $k$, `range` stops at $n-k$ and never produces start $n$, so the method does not append an unnecessary all-fill group.
- **Exclusive slice endpoint:** `s[i : i + k]` contains at most $k$ characters because `i + k` itself is excluded.
- **Input immutability:** Strings are immutable; slicing and padding create the returned strings without changing `s`.
