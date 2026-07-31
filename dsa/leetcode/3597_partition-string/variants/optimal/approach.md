## General
**Exploit the prefix-closed history:** Suppose the current candidate must grow from length one through length $k$ before it becomes new. Every shorter prefix was therefore emitted earlier. This means the set of emitted segments is prefix-closed: whenever a segment is present, every nonempty proper prefix on its trie path is present too. Consequently, trie path existence is enough to test whether a candidate has been seen; separate terminal markers are unnecessary.

For each new starting index, begin at the trie root and consume characters while the corresponding child edge exists. Each successful edge represents a candidate already in the history. The first missing edge makes the extended candidate new. Create that edge, append the matching slice to the result, and continue immediately after it.

If traversal consumes the entire remaining suffix without finding a missing edge, that suffix is already a recorded segment. There is no next character with which to form a new candidate, so the procedure stops without appending it. This matches the prescribed behavior for inputs such as `"aaaa"`.

Each emitted segment is the shortest unseen candidate at its start because all candidates represented by earlier nodes were found in the trie and the algorithm stops on the first absent edge. Adding that edge records exactly the chosen segment while preserving prefix closure. Processing starts again at the next unused character, so the returned list is precisely the greedy partition in order.

## Complexity detail
Let $n = \lvert\texttt{s}\rvert$. Every character belongs to exactly one candidate traversal, including a possible final unrecorded suffix. Trie traversal and edge insertion take expected $O(1)$ time per character with hash-map children. The output slices contain at most $n$ characters in total, so the complete algorithm runs in $O(n)$ expected time.

The trie creates at most one node for each character consumed by an emitted segment, and the returned strings contain at most $n$ characters. Auxiliary storage is therefore $O(n)$.

## Alternatives and edge cases
- **Hash set plus incremental strings:** It mirrors the statement directly, but immutable-string concatenation and repeated hashing can recopy growing candidates. On `"a"` repeated $n$ times, this can take $\Theta(n^{3/2})$ character work rather than linear time.
- **Hash set plus substring slicing:** Testing every growing slice has the same repeated-copying and repeated-hashing issue even though membership is expected constant time after the string is hashed.
- **Trie with terminal flags:** It is correct, but terminal flags are redundant because the greedy process guarantees that the emitted set is prefix-closed.
- **Internal repeated characters:** A segment such as `"aa"` is valid; only equality with an earlier whole segment matters.
- **Final seen suffix:** When no extension is available, the already-seen suffix is not appended a second time.
- **All distinct characters:** Every singleton is new and becomes its own segment.
- **One character:** The only candidate is new, so the result contains that character.
- **Long repeated run:** Segment lengths grow as `1, 2, 3, ...` until the remaining suffix is too short to form the next new prefix.
