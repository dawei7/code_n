## General
**Translate letters into alien ranks.** Build a 26-entry map from each character in `order` to its index. Comparing rank integers then implements the alien alphabet without modifying the words.

**Only adjacent pairs need checking.** A sequence is sorted under a total lexicographic order exactly when every adjacent pair is ordered. Compare `words[i]` with `words[i + 1]` from left to right until their first unequal characters. Their ranks decide the pair immediately: a larger rank in the first word makes the whole sequence invalid, while a smaller rank finishes that pair successfully.

**Handle a shared prefix explicitly.** If no compared character differs, the shorter word must precede the longer one. Reject the pair when the first word is longer; equal words and a shorter first word are valid. If all adjacent pairs pass, transitivity of lexicographic order proves every earlier word is no greater than every later word, so the full sequence is sorted.

## Complexity detail
The rank table has fixed size 26. Across adjacent comparisons, no word's characters are examined more than a constant number of times, so the total time is $O(S)$. The fixed alphabet table uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Transform then compare:** Replace every character by its alien rank sequence and use ordinary lexicographic comparison. This is clear but stores $O(S)$ additional data.
- **Compare every word pair:** Verifying all earlier/later pairs is correct but can cost $O(NS)$ time instead of using transitivity through adjacent pairs.
- **Sort and compare:** Sorting a copy under an alien comparator and comparing it with the input adds unnecessary $O(S\log N)$ comparison work and extra storage.
- **Prefix inversion:** `"apple"` must not precede `"app"`, even though all characters of the shorter word match.
- **Equal words:** Equality is allowed because the requested sequence is non-decreasing.
- **One word:** With no adjacent pair to violate the order, the sequence is sorted.
