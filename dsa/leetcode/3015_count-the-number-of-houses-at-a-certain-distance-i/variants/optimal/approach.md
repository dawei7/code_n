## General

Consider two houses $a<b$. A shortest simple route has only three relevant forms. It can stay on the original line for distance $b-a$, use the added street from $x$ to $y$, or use it from $y$ to $x$. Their lengths are

$$
b-a,
\qquad
\lvert a-x\rvert+1+\lvert b-y\rvert,
\qquad
\lvert a-y\rvert+1+\lvert b-x\rvert.
$$

No shortest route needs the added street more than once: traversing it twice creates a cycle that can be removed without increasing distance. Any route that uses it once has one of the two listed orientations, while the remaining segments follow the unique line. The minimum of the three expressions is therefore the exact shortest distance.

Enumerate each unordered pair once, compute that minimum in constant time, and add two to the corresponding bucket because `(a,b)` and `(b,a)` are distinct ordered pairs with the same distance. Self-pairs are never enumerated. The final bucket may remain zero because no two distinct houses need distance $n$.

## Complexity detail

There are $n(n-1)/2$ unordered pairs, and each evaluates three constant-time route lengths. Total time is $O(n^2)$. The returned count list contains $n$ entries; apart from that required output, the algorithm uses $O(1)$ working state, for $O(n)$ total space including the result.

## Alternatives and edge cases

- **BFS from every house:** The graph is sparse and this is correct, but it rebuilds distances when the three closed-form routes give each pair directly.
- **Floyd-Warshall:** All-pairs dynamic programming takes $O(n^3)$ time and ignores the special path-plus-one-edge structure.
- **Count unordered pairs once:** The contract counts directions separately, so every unordered pair contributes two.
- **Equal shortcut endpoints:** Using the self-loop adds a street without improving a route; the direct-line expression wins.
- **Adjacent shortcut endpoints:** The extra street duplicates an existing connection and leaves all ordinary path distances unchanged.
- **Reversed `x` and `y`:** Both shortcut orientations are evaluated, so swapping the input endpoints cannot change the result.
