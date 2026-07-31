## General

Build a trie whose edges are decimal digits. While inserting a number, each visited trie node represents the prefix formed by the digits processed so far.

Before following the next digit, check whether the current node is already terminal. If it is, an earlier number ends at the current prefix, so that earlier number prefixes the number being inserted. Otherwise, follow or create the edge for the next digit.

After all digits have been consumed, the final node must be empty. A terminal marker there means the same number was inserted earlier, so the two distinct entries prefix each other. A child edge means an earlier, longer number extends the current number, making the current number its prefix. Either condition returns `false`; otherwise mark the node terminal and continue.

If every insertion finishes without either conflict, no pair has a prefix relationship and the array is prefix-free. The two insertion checks cover both possible orders for a shorter and longer pair, while the existing terminal marker covers duplicates.

## Complexity detail

Let $S$ be the total number of characters across all phone numbers. Each character follows or creates exactly one trie edge, so the algorithm takes $O(S)$ time. This is asymptotically optimal because distinguishing inputs may require inspecting every character.

The trie stores at most one new node per input character, giving $O(S)$ auxiliary space. A terminal marker adds only constant storage per number.

The benchmark size is $S$. Equal-length strings with a long shared opening force complete trie traversal while remaining prefix-free. The calibrated slower implementation compares every ordered pair and may inspect their long common prefixes, taking $O(nS)$ time when $n$ strings have comparable lengths.

## Alternatives and edge cases

- **Sort and compare adjacent strings:** Lexicographic sorting makes every possible prefix pair adjacent and is concise, but comparison sorting takes up to $O(S\log n)$ time rather than the trie's linear bound.
- **Compare every pair:** Checking `startswith` for all distinct pairs is simple but takes $O(nS)$ time in the worst case.
- **Duplicate strings:** Equal entries are prefixes of one another; reaching an existing terminal node after consuming the string detects them.
- **Longer number inserted first:** Children at the new terminal node reveal that the current shorter number prefixes an earlier number.
- **Shorter number inserted first:** Encountering a terminal marker before the new number ends reveals the earlier prefix immediately.
- **Leading zeros:** Phone numbers are strings, so zeros at the beginning are ordinary characters and must never be removed.
- **Shared partial prefixes:** Sharing trie nodes is harmless unless one input actually ends at a node on another input's path.
