## General
**Only matching endpoint characters permit progress**

At any stage, every legal prefix begins with the current leftmost character and every legal suffix ends with the current rightmost character. If those characters differ, no pair can satisfy the same-character rule, so the current length is already minimal.

**Discard both complete boundary runs**

When the endpoints share character $c$, advance the left pointer past every consecutive $c$ and retreat the right pointer past every consecutive $c$. Removing less cannot produce a better outcome: any surviving boundary $c$ still has to be paired with $c$ from the other side before a different inner character can become exposed. Therefore an optimal sequence may remove both maximal boundary runs immediately.

**Stop safely when the pointers meet or cross**

Repeat while at least two characters remain and the endpoint characters match. Each pointer moves only inward. If the runs consume the entire remaining interval, the pointers cross and the result is zero; if one character remains, its length is one because nonempty prefix and suffix selections may not overlap. Otherwise, differing endpoints prove that no further operation exists.

## Complexity detail
Each character is passed by the left or right pointer at most once, so the total time is $O(n)$. The algorithm keeps only two indices and the current removable character, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Repeated string slicing:** Applying the same maximal-run logic by constructing a new substring after every operation is correct, but nested boundary layers can make the copied work $O(n^2)$.
- **Run-length encoding:** Compressing the string into character-count runs makes the boundary process explicit, but uses $O(n)$ additional space in the worst case.
- **Different endpoints initially:** Zero operations are possible, so the original length remains.
- **One character:** Prefix and suffix cannot be disjoint, leaving length one.
- **Uniform string:** Equal boundary runs consume the entire string, leaving zero.
- **Unequal run sizes:** Remove each complete boundary run independently; their lengths need not match.
- **Pointers meet:** The remaining middle character cannot be selected by both sides and therefore survives.
- **Pointers cross:** The final pair of runs was disjoint before deletion, so an empty result is legal.
