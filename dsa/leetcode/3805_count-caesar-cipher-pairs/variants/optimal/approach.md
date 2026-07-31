## General

A uniform cyclic shift changes every character code in a word by the same amount modulo 26. Subtracting the first character therefore removes that common shift. For a word, build the tuple whose position `k` is `(ord(word[k]) - ord(word[0])) % 26`. Its first entry is always `0`, and the remaining entries record the word's complete relative letter pattern.

For example, `"az"` already has normalized offsets `(0, 25)`. Shifting `"ba"` backward until its first letter is `'a'` gives the same offsets `(0, 25)`, including the cyclic wrap from `'a'` to `'z'` in the relative difference.

Two similar strings must have equal normalized tuples: adding a common cyclic shift to every position cancels when each position is compared with the first. Conversely, if two tuples are equal, shifting one word's first letter to the other word's first letter also aligns every remaining position. Equality of the keys is therefore exactly equivalent to similarity.

Process the words from left to right. A map stores how many earlier words produced each key. When the current key has appeared `c` times, the current index completes exactly `c` new pairs with those earlier indices. Add `c` to the answer, then increment the key's frequency. This counts every pair once, at its larger index.

## Complexity detail

With $S$ defined as the total number of input characters, constructing and hashing all normalized keys takes expected $O(S)$ time. The frequency map and its stored tuple keys can collectively retain at most $S$ offset entries, so auxiliary space is $O(S)$.

## Alternatives and edge cases

- **Adjacent-difference key:** Recording each consecutive character difference modulo 26 is an equivalent $O(S)$ representation, because those differences determine every offset from the first letter.
- **Compare every pair:** Testing all $\binom{n}{2}$ word pairs character by character is correct but can take $O(n^2m)$ time.
- **Generate cyclic shifts:** Materializing up to 26 shifted copies of every word preserves linear asymptotic time only because the alphabet size is fixed, but it performs substantially more character work and allocation than direct normalization.
- **One-character words:** Every length-one word has the same key `(0)`, so every pair of such words is similar regardless of their letters.
- **Duplicate words:** Equal words are similar with zero operations and must be counted separately for every distinct pair of indices.
- **Alphabet wraparound:** All offsets require modulo 26; ordinary subtraction misclassifies patterns such as `"az"` and `"ba"`.
- **Large answer:** With $n=10^5$, the result may reach $\binom{n}{2}=4{,}999{,}950{,}000$, so fixed-width implementations need a 64-bit count.
