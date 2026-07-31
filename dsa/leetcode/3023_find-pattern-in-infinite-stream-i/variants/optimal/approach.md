## General

**Preserve useful progress while reading forward.** The stream cannot be indexed or rewound, so every consumed bit must be incorporated immediately. Keep `matched`, the length of the longest prefix of `pattern` that is also a suffix of all bits read so far. When `matched` reaches the pattern length, the current stream index identifies the end of the first match.

**Precompute safe fallback states.** Build the Knuth-Morris-Pratt prefix table for `pattern`. For every pattern position, this table records the longest proper prefix that is also a suffix ending there. If a new stream bit disagrees with the next desired pattern bit, repeatedly follow these prefix links. Each fallback retains every suffix that could still grow into a match instead of discarding the consumed bits or rereading the stream.

After the fallbacks, either the bit extends the current prefix or no nonempty prefix ends at this position. Because the scan examines stream indices in increasing order and returns as soon as all $M$ pattern bits match, no later occurrence can be returned before an earlier one. The reported start `index - M + 1` is therefore the first valid starting index.

## Complexity detail

Building the prefix table takes $O(M)$ time and space. During the stream scan, every successful extension can cause at most one later fallback across the whole KMP process, so consuming $S$ bits takes $O(S)$ time rather than $O(SM)$. Total time is $O(S+M)$ and auxiliary space is $O(M)$.

## Alternatives and edge cases

- **Explicit sliding window:** Retaining the most recent $M$ bits and comparing the full window after every read is straightforward, but it can take $O(SM)$ time on highly repetitive input.
- **Rolling hash:** A binary rolling hash can compare windows in expected constant time, but collision-free verification either adds a second comparison or requires more machinery than KMP's deterministic guarantee.
- **Restart after every mismatch:** Resetting the match length to zero misses overlapping candidates, such as searching for `[1, 1, 0]` in a long run of ones.
- **One-bit pattern:** The prefix table is all zeroes, and the scan returns the index of the first equal bit.
- **Match at index zero:** Reaching length $M$ after consuming the first $M$ bits correctly returns `0`.
- **Long self-overlap:** Prefix links reuse the longest valid border, preventing repeated reads even when the pattern contains many copies of the same prefix.
