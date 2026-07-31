## General

**Every legal index pair is independent.** The required answer counts pairs rather than constructing a shared structure or choosing a subset. The constraint $i<j$ gives a direct enumeration: use each index as the first position, then inspect every later index as the second.

For a candidate pair, let `first = words[i]` and `second = words[j]`. The pair is valid precisely when `second.startswith(first)` and `second.endswith(first)` are both true. These checks also handle all length relationships: a longer `first` cannot match, while equal strings match at both ends.

The nested loops visit every pair with $i<j$ exactly once. A visited pair increments the answer exactly when the definition of `isPrefixAndSuffix` holds. Consequently, every valid pair contributes once, and no invalid or reversed pair contributes at all.

## Complexity detail

Let $n=\lvert\texttt{words}\rvert$ and let $L$ be the maximum word length. There are $n(n-1)/2=O(n^2)$ candidate pairs, and checking both ends takes $O(L)$ time in the worst case, for total time $O(n^2L)$. The indices, string references, and counter use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Explicit slicing:** Comparing `second[:m]` and `second[-m:]` with a first word of length `m` is equally direct, but each slice allocates a temporary string.
- **Trie or paired-character trie:** A specialized trie can aggregate earlier words more efficiently and is useful for much larger constraints, but it adds unnecessary structure for $n\le50$ and $L\le10$.
- **Rolling hash:** Prefix and suffix hashes can make comparisons constant-time after preprocessing, but collision handling and setup outweigh the bounded direct checks here.
- **One word:** No indices satisfy $i<j$, so the answer is `0`.
- **Equal words:** Two equal strings at distinct ordered indices form a valid pair because a string is both its own prefix and suffix.
- **Earlier word longer:** It cannot match either end of the later word and contributes nothing.
- **Prefix only or suffix only:** Both conditions are required; satisfying just one must not be counted.
- **Overlapping ends:** A short word may overlap itself inside the longer word, as `"aba"` does in `"ababa"`; prefix and suffix positions need not be disjoint.
