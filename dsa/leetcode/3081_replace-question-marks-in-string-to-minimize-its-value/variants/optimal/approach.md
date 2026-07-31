## General

For each letter $c$, let $f_c$ be its final frequency. Its occurrences contribute

$$
0 + 1 + \cdots + (f_c-1) = \frac{f_c(f_c-1)}{2}
$$

to the string's value, regardless of their positions. Adding one new occurrence of a letter whose current frequency is $f_c$ therefore increases the value by exactly $f_c$.

**Choose the replacement multiset by marginal cost.** Count the fixed lowercase letters. Store all 26 letters in a min-heap ordered by `(frequency, letter)`. For every `?`, select the letter with the smallest current frequency, breaking equal-frequency ties alphabetically, record one addition for it, increment its frequency, and return it to the heap.

Choosing any letter with a larger current frequency would pay a larger marginal cost immediately. Repeatedly taking a minimum marginal cost distributes all additions as evenly as the fixed frequencies permit. An exchange of a higher-cost choice with an available lower-cost choice cannot increase any later opportunity, so the selected multiset has minimum total value.

**Separate selection from placement.** The value depends only on final frequencies, so permuting the selected letters among the `?` positions does not affect the minimum value. The lexicographically smallest placement puts the smallest selected letter in the earliest placeholder, the next smallest in the next placeholder, and so on. The `additions` counts already describe this sorted multiset: scan letters from `a` through `z` while replacing question marks from left to right.

The first phase minimizes the frequency-based value, and the second phase chooses the lexicographically smallest string among all placements of that optimal multiset. Together they satisfy both priorities of the contract.

## Complexity detail

Let $n = \lvert s \rvert$. Heap operations use a fixed 26-element heap, so each operation is $O(\log 26)=O(1)$. Counting, selecting replacements, and constructing the result each take $O(n)$ time, for $O(n)$ total time. The mutable output representation uses $O(n)$ space; all frequency structures use $O(1)$ additional space.

## Alternatives and edge cases

- **Scan all 26 frequencies:** Selecting the minimum by a direct alphabetical scan is also $O(n)$ because the alphabet size is fixed, and avoids the heap.
- **Recount for every placeholder:** Repeatedly counting each letter throughout the growing replacement list is correct but can take $O(n^2)$ time.
- **Sort selected letters:** Collecting replacements and sorting them before placement is correct but costs $O(n \log n)$; 26 addition counters generate the same sorted multiset in linear time.
- **No question marks:** The selection phase does nothing and the original string is returned unchanged.
- **More than 26 placeholders:** Letters are reused only after every currently less-frequent letter has been chosen.
- **Lexicographic tie break:** Heap tie-breaking alone does not determine the final string; selected letters must still be assigned to placeholder positions in sorted order.
- **Existing imbalances:** A frequently occurring fixed letter may receive no replacements until other letters catch up.
