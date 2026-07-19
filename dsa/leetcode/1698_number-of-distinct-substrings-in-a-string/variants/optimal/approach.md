## General
**Represent every substring with a suffix automaton**

Build a suffix automaton while reading `s` from left to right. Each state stores transitions by next character, a suffix link, and `longest[state]`, the maximum length of any substring represented by that state. `last` represents the entire processed prefix.

For a new character, create a current state whose maximum length is one greater than `last`. Walk suffix links and add missing transitions to the current state. If an existing transition is reached and already has the required next length, use that target as the current state's suffix link.

Otherwise clone the target: copy its transitions and suffix link, give the clone maximum length `longest[source] + 1`, redirect precisely the suffix-chain transitions that formerly reached the old target, and link both the target and current state to the clone. Cloning separates two sets of substring endings without adding a new substring occurrence.

**Count the length interval owned by each state**

All substrings represented by one noninitial state have lengths from one more than its suffix link's maximum through its own maximum, inclusive. Each distinct nonempty substring belongs to exactly one such state-and-length pair. State `v` therefore contributes

$$
\texttt{longest[v]}-\texttt{longest[suffix\_link[v]]}
$$

new distinct substrings. Summing this difference over every state except the initial state gives the answer without materializing the substring texts.

The automaton construction preserves exactly the substrings of each processed prefix. Suffix links group equivalent ending contexts, and cloning restores deterministic minimal state boundaries when a transition would otherwise combine incompatible maximum lengths. The length-interval partition then counts every accepted nonempty string once.

## Complexity detail
A suffix automaton for a length-$n$ string has at most $2n-1$ states. Across construction, suffix-link walking and transition redirection are amortized $O(n)$ for a fixed alphabet, and the final state sum is linear. Transitions, links, and maximum lengths occupy $O(n)$ space.

## Alternatives and edge cases
- **Substring set:** generating all `s[left:right]` values is simple but creates $O(n^2)$ entries and may copy $O(n^3)$ characters in languages with copying slices.
- **Suffix trie:** inserting every suffix counts one new node per distinct substring in $O(n^2)$ time and space; it is useful as an oracle but not needed for the linear follow-up.
- **Suffix array plus LCP:** sorting suffixes and subtracting adjacent longest-common-prefix lengths also counts distinct substrings, typically in $O(n\log n)$ time with an appropriate construction.
- **Rolling hashes:** hashing all substrings can use $O(n^2)$ time, but a single modular hash risks collisions unless equality is verified or collision-resistant pairing is used.
- **One character:** exactly one nonempty substring exists.
- **All characters equal:** there is one distinct substring for each possible length, so the answer is $n$.
- **Repeated occurrences:** positions do not distinguish equal contents; the automaton's shared state structure performs this deduplication.
