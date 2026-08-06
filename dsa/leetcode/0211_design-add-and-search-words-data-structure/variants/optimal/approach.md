## General
Store words in a trie exactly as in an ordinary prefix dictionary: each character is an edge, and a terminal marker distinguishes complete words from prefixes. Wildcard search changes only how a query traverses that structure.

Search keeps an iterative frontier of trie nodes reachable after each processed pattern position:

- For a literal character, add only each frontier node's matching child when that edge exists.
- For `.`, add every nonterminal child because the wildcard matches exactly one arbitrary character.
- If the next frontier is empty, return false immediately.
- After the entire pattern, succeed only if at least one frontier node is terminal.

The final terminal test enforces full-word length. After adding `bad`, pattern `b.` does not match because it consumes only two trie edges, while `b..` can follow `b -> a -> d` and ends at a terminal node.

For `.ad` after adding `bad`, `dad`, and `mad`, the first wildcard frontier contains the nodes for `b`, `d`, and `m`; the remaining literal edges `a` and `d` advance all surviving states together. The final terminal test then succeeds.

After processing `i` pattern positions, the frontier contains exactly the trie nodes reached by stored prefixes matching those `i` positions. A literal transition preserves only paths with the required character; a wildcard transition enumerates all and only possible single-character choices. By induction, the final frontier represents exactly the full-length matching trie paths. Requiring a terminal node makes those paths correspond exactly to stored words, so the returned boolean is correct.

## Complexity detail
Adding a word of length `L` takes $O(L)$ time. Let `d` be the number of dots in a search pattern and `B` the maximum trie branching factor. A frontier can expand by at most `B` at each dot and advances at most one edge per state at a literal, giving $O(LB^d)$ worst-case search time. The source contract has $d \le 2$ and $B \le 26$, and the finite trie also bounds work by its stored nodes. Trie storage is $O(T)$ for `T` inserted characters; the iterative frontier holds at most $O(B^d)$ node references and is covered by the branch's $O(T)$ bound.

## Alternatives and edge cases
- Recursive depth-first search over `(node, position)` states has the same branching behavior but also uses call-stack depth $O(L)$.
- Scanning every stored word repeats comparisons and ignores shared prefixes.
- Grouping words by length can reduce wildcard candidates, but a trie prunes failed prefixes earlier.
- Treating `.` as a literal child violates the search grammar.
- Searches before any insertion fail. Multiple dots can create broad branching.
- A pattern must match the whole word, not merely a prefix or substring.
