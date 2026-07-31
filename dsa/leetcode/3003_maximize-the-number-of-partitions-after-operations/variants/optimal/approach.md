## General

**Encode the current greedy prefix.** A 26-bit mask records exactly which
letters occur in the partition currently being built. Adding the next letter
continues that partition when the merged mask has at most `k` set bits.
Otherwise the current partition is forced to end and a new mask containing
only the next letter begins.

**Keep both replacement phases.** A rolling dynamic program maps
`(mask, changed)` to the greatest number of already completed partitions for
that state. Before the replacement is used, the current character may remain
unchanged or become any of the 26 letters. After it is used, only the original
letter is legal. States with the same mask and replacement flag have identical
futures, so retaining only their greatest completed count is safe.

The transition exactly mirrors the mandated longest-prefix procedure: a
partition boundary occurs only when adding the next character would introduce
the $(k+1)$-st distinct letter. After the final character, add one for the
still-open last partition and take the best state.

## Complexity detail

The alphabet has fixed size 26. The number of reachable rolling masks after at
most one replacement is bounded solely by that alphabet, and each state tries
at most 26 letters. Thus the fixed alphabet factors are constants: the method
uses $O(N)$ time and $O(1)$ auxiliary space with respect to string length.

## Alternatives and edge cases

- **Try every replacement separately:** Repartitioning the whole string for every index and letter is correct but costs $O(26N^2)$ time.
- **Recursive memoization:** It represents the same states, but a length-10,000 recursion chain is unsafe in Python.
- **No replacement:** The unchanged transition remains available until the end, so changing a character is never forced.
- **Replacement by the same letter:** This is equivalent to leaving the character unchanged and need not consume the operation.
- **`k = 26`:** Every possible string remains one partition.
- **Single character:** The only possible partition count is one.
