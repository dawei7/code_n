## General
**Count the shared pool once.** Build a frequency table for the 26 lowercase letters in `chars`. This table is never mutated while testing words, which models the rule that the full pool is available again for each word.

**Measure each word's requirements.** Build another 26-letter frequency table for the current word. The word is good exactly when every required count is at most the pool's count for that letter. If this componentwise comparison succeeds, add `len(word)` to the answer; otherwise add nothing.

The test is both necessary and sufficient. Exceeding the pool count for even one letter makes construction impossible because occurrences cannot be reused within a word. When every letter count fits, assign the required occurrences of each letter to distinct matching occurrences in `chars`; the assignments for different letters cannot conflict. Processing all words independently and summing precisely the accepted lengths therefore yields the requested total.

## Complexity detail
Counting `chars` and every word visits exactly the $S$ characters in the displayed definition, so the total time is $O(S)$. Each frequency table has 26 entries because inputs contain only lowercase English letters. That alphabet size is fixed, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Remove letters from a copied pool:** This is correct but repeatedly copying and searching strings adds avoidable work compared with direct frequency comparison.
- **Call `count` for every word character:** Repeatedly rescanning both strings can make a length-$m$ word require $O(m^2)$ work.
- **Use a set of characters:** A set loses multiplicity and would incorrectly accept a word needing two copies when `chars` contains only one.
- **Reuse a depleted pool across words:** The pool resets for each word, so several good words may all rely on the same occurrences from `chars`.
- **Exact use of the pool:** A word may use every available character and remains good; unused pool characters are also allowed.
- **Repeated candidate words:** Each array entry is evaluated and contributes its length independently, even when two entries have identical text.
