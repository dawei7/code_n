## General
**Represent identical tiles by counts:** Count each distinct letter and store only the tuple of remaining counts. This removes physical identities that could otherwise create duplicate branches for equal letters.

**Count suffixes from a state:** For a remaining-count tuple, try each letter whose count is positive. Choosing it contributes one sequence consisting of that letter alone, plus every longer sequence obtained by choosing a suffix from the decremented state. Restore the count after the recursive call before considering the next first letter.

**Reuse equivalent subproblems:** Different prefixes can leave exactly the same multiset of unused tiles. Memoizing by the remaining-count tuple computes the number of possible suffixes from that multiset once. The empty sequence is never added: each term enters the total only when an actual letter is chosen.

Every legal non-empty sequence has a unique first letter and a remaining suffix constructible from the state after consuming that letter, so it belongs to exactly one recurrence branch. Conversely, each branch consumes an available tile and recursively consumes only available tiles, so every counted sequence is legal. Count-state representation makes equal-letter tile swaps the same branch rather than duplicates.

## Complexity detail
There are at most $M$ remaining-count tuples. Each state checks $D$ letter types, giving $O(DM)$ time. The memo stores at most $M$ results, while the recursion depth is at most $n$, for $O(M+n)$ auxiliary space.

## Alternatives and edge cases
- **Plain count backtracking:** Omit memoization and construct each distinct sequence implicitly. It is simple and avoids duplicates, but equivalent remaining multisets may be solved repeatedly.
- **Permute physical tile indices into a set:** It eventually deduplicates equal-letter strings, but can explore factorially many redundant index orders when letters repeat.
- **Sort and skip equal choices:** Standard permutation backtracking can avoid duplicates at each depth, but count states express the multiset more directly.
- **All tiles equal:** Exactly the $n$ sequences of lengths one through $n$ are possible.
- **All tiles distinct:** Every ordered selection of every positive length is distinct.
- **Single tile:** The answer is one.
