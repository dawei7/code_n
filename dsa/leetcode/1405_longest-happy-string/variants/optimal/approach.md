## General
Store the positive remaining counts in a max-heap of at most three `(count, letter)` entries. At each step, tentatively take the most abundant letter.

If appending it would create three equal trailing characters, take the second-most abundant letter instead. Append that fallback, decrement and reinsert it when copies remain, then restore the blocked first entry unchanged. If no fallback exists, no character can be appended and construction stops. Otherwise append the most abundant letter normally and reinsert its reduced count.

Choosing the largest currently legal count prevents the dominant supply from becoming harder to separate later. When the largest is temporarily illegal, some different letter is necessary; choosing the largest alternative preserves the same balance. If the heap offers no alternative, every remaining character equals the forbidden trailing pair, proving that no longer happy extension exists. Thus the greedy process reaches maximum possible length.

## Complexity detail
Each appended character performs a constant number of heap operations on at most three entries, so $O(\log 3)=O(1)$ work per output character and $O(N)$ total time. The heap has at most three entries and uses $O(1)$ auxiliary space, excluding the returned string.

## Alternatives and edge cases
- **Memoized exhaustive search:** Try every legal next letter for every remaining-count state. It finds an optimum but can require $O(abc)$ states and store long suffix results.
- **Always take the largest:** Ignoring the last two output characters can create a forbidden triple even when another letter remains available.
- **Dominant letter:** Some copies must remain unused when the other letters cannot provide enough separators.
- **Only one letter:** At most two copies can be returned.
- **Balanced counts:** Every character can be used.
- **Multiple answers:** Character order need not match a sample; validity and maximum length determine correctness.
