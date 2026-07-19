## General
**Summarize a prefix by its final vowel.** Track five counts for valid strings of the current length ending in `a`, `e`, `i`, `o`, and `u`. Strings with the same last vowel have identical legal choices for the next position, so their internal characters no longer need to be retained.

**Reverse the stated transitions to update ending counts.** A new string ending in `a` may come from previous endings `e`, `i`, or `u`; one ending in `e` comes from `a` or `i`; one ending in `i` comes from `e` or `o`; one ending in `o` comes only from `i`; and one ending in `u` comes from `i` or `o`. Compute all five new values from the old tuple simultaneously and reduce them modulo $M$.

**Why the recurrence counts every valid string once.** Removing the last character from a valid length-$\ell$ string leaves one valid length-$(\ell-1)$ prefix and an allowed transition to its final vowel. Conversely, appending any permitted successor to a counted prefix creates a valid longer string. The predecessor groups are disjoint because a complete string has one final vowel, so the recurrence neither omits nor duplicates strings. Starting with one string per vowel at length one and summing the five counts after `n` positions gives the answer.

## Complexity detail
Each of the `n - 1` extensions performs a fixed number of arithmetic operations, so the time is $O(n)$. Only five rolling counts are retained, giving $O(1)$ auxiliary space. Modular reduction keeps every stored value bounded by $M$.

## Alternatives and edge cases
- **Enumerate every valid string:** Recursive generation follows the rules directly but visits exponentially many prefixes before reducing the final count.
- **Full dynamic-programming table:** Storing five counts for every length is correct and takes $O(n)$ space, but older rows are never needed.
- **Matrix exponentiation:** Encoding the transitions in a $5\times5$ matrix reduces time to $O(\log n)$, though the constant-size matrix machinery is more complex than required here.
- **Length one:** No adjacency rule is applied, so all five vowels count.
- **Simultaneous updates:** Every new count must use the previous length's tuple; overwriting one count early corrupts later transitions.
- **Modulo placement:** Reducing after each fixed-size sum is equivalent to reducing only at the end and prevents unbounded integers.
