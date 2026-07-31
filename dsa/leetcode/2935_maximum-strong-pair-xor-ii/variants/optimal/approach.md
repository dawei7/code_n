## General

**Turn the strong condition into a sorted range.** Sort the values and consider
the current larger endpoint $y$. For an earlier value $x\le y$, the condition
$\lvert x-y\rvert\le\min(x,y)$ becomes

$$
y-x\le x \iff y\le2x.
$$

Thus the valid partners for $y$ are exactly the processed values satisfying
$x\ge\lceil y/2\rceil$. Maintain a left pointer and remove smaller values while
$2x<y$. Insert $y$ before querying, which preserves the permitted self-pair and
guarantees a nonempty window.

**Maximize XOR with a counted binary trie.** Store every value in the current
window as a 20-bit path. To maximize XOR with $y$, inspect bits from most
significant to least significant and prefer the child with the opposite bit;
that choice sets the highest still-undecided result bit. If no active value
uses the preferred branch, follow the matching branch. Greedy bit choice is
optimal because no combination of lower bits can outweigh a higher XOR bit.

Each trie node stores the number of active values passing through it. Insertion
increments those counts and window removal decrements them, so duplicate values
are handled independently and dead branches are never selected. For every
sorted $y$, the trie contains exactly all processed strong partners. The query
therefore returns the best XOR ending at $y$, and the maximum across all such
queries is the global answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. Sorting costs
$O(n\log n)$. Every value is inserted and removed at most once and queried
once, with each trie operation taking $O(\log V)$ time. Total time is
$O(n\log n+n\log V)$, which is $O(n\log n)$ here because $V<2^{20}$. The trie
uses $O(n\log V)$ auxiliary space.

## Alternatives and edge cases

- **Direct pair enumeration:** Check all pairs and their XOR values in $O(n^2)$ time; this works for the small companion problem but not for 50,000 values.
- **Per-window linear XOR scan:** The two-pointer window identifies valid partners, but scanning it for every endpoint can still be quadratic; the trie is needed for fast maximization.
- **Self-pair:** Inserting the current value before querying makes `(y, y)` available and yields zero when no better partner exists.
- **Equality boundary:** A partner with $y=2x$ remains in the window because removal uses the strict test $2x<y$.
- **Duplicate values:** Trie counts prevent removing one copy from invalidating another active copy.
- **Maximum value:** Exactly 20 bit levels cover every legal value below $2^{20}$.
