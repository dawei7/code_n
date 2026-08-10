## General

**Use a matcher that never needs to rewind the stream.** An infinite stream exposes only `next()`. Once a bit has been consumed, the algorithm cannot index it again. Knuth-Morris-Pratt matching is ideal because it summarizes the useful suffix of all bits seen so far with one integer and the pattern's prefix table.

**Precompute how the pattern overlaps with itself.** Array `prefix` has one entry per pattern position. `prefix[i]` is the length of the longest proper prefix of `pattern[0..i]` that is also a suffix.

While constructing it, `matched` is the current border length. If `pattern[index]` differs from `pattern[matched]`, the source falls back to `prefix[matched - 1]`. This does not discard a possible match: any shorter candidate that can still work must itself be a border of the already matched prefix.

If the two bits agree, `matched` increases. The resulting length is stored at `prefix[index]`. Building this table once gives the stream scan instructions for recovering from every mismatch.

**Interpret `matched` during streaming.** Before reading a new bit, `matched` is the length of the pattern prefix equal to the suffix of the consumed stream. After `bit = stream.next()`:

- while there is a mismatch and `matched > 0`, fall back through `prefix`;
- if the bit equals the next pattern bit, extend `matched` by one;
- if `matched` reaches the pattern length, the current stream position ends a full match.

No old stream value is requested. All relevant history is encoded by `matched` and the precomputed pattern borders.

**Why fallback does not miss a start.** Suppose $q$ pattern symbols matched before a mismatch. Any occurrence continuing at the current bit must overlap the failed match. The portion already consumed that could begin such an occurrence must be both a suffix of the $q$ matched symbols and a prefix of the pattern. `prefix[q-1]` is the longest such portion. If it also fails, the loop follows shorter borders. KMP therefore tests every viable overlap while skipping impossible restarts.

**Calculate the starting index.** Variable `index` is the zero-based position of the bit just read. A length-$M$ match ending at `index` begins at

$$
\texttt{index}-M+1.
$$

The source returns exactly `index - len(pattern) + 1` as soon as a full match is reached.

Because bits are read in increasing index order, this is the first match. A later ending position cannot correspond to an earlier unreported complete window.

**A trace with overlap.** Let the pattern be `[1,1,0,1]` and the stream begin `[1,0,1,1,0,1,...]`. KMP first matches 1, then sees 0 instead of the second 1 and falls back. That 0 matches no nonempty prefix, so progress becomes zero. The next bits 1, 1, 0, 1 advance progress to four. The match ends at index 5 and starts at $5-4+1=2$.

**Why the infinite loop is acceptable.** The source uses `while True` because the stream has no finite length and the reference guarantees that the pattern begins within the first $10^5$ bits. Under that contract, a return occurs. Without the guarantee, the interface would need a maximum-read parameter or a not-found outcome.

**Difference from rolling windows.** The method does not store the last $M$ stream bits or compare each window. It retains only one match length. Self-overlap information in `prefix` is what makes that compression exact.

## Complexity detail

Let $M$ be the pattern length and $S$ the number of stream bits consumed through the end of the first occurrence. Prefix construction is $O(M)$. During streaming, each bit advances the scan once, and total fallback movements are amortized $O(S)$, giving $O(M+S)$ time.

Array `prefix` uses $O(M)$ space. All streaming state—`matched`, `index`, and `bit`—is constant-sized. No stream history is stored, so auxiliary space is $O(M)$.

The input pattern is read but not modified. The stream itself owns its external state and advances once for each requested bit.

## Alternatives and edge cases

- **Store a length-$M$ deque:** It uses $O(M)$ space, but comparing the deque to the pattern at every position can cost $O(MS)$ time.
- **Rolling hash:** It offers expected constant-time window checks but can collide; KMP is deterministic.
- **Bit packing:** Exact rolling bits are attractive for small bounded patterns, but this version permits length $10^4$, so KMP gives clean linear bounds without large-integer shifts.
- **Naive restart on mismatch:** Re-reading prior stream bits is impossible through this interface. KMP fallback avoids any rewind.
- **Pattern length one:** `prefix` contains one zero. The first equal stream bit makes `matched == 1` and returns its index.
- **First bit starts the match:** A full match ending at index $M-1$ returns start zero.
- **Overlapping pattern structure:** Prefix fallbacks preserve the longest viable overlap instead of discarding it.
- **Long run of mismatches:** With `matched == 0`, each mismatching bit is consumed in constant work.
- **Optional stream annotation:** The type permits `None` syntactically, but the contract supplies a real stream. Passing `None` would fail at `next()`.
- **Guaranteed occurrence:** Termination depends on the reference guarantee; the source has no independent read limit.
