## General

The requested result depends only on how often each letter occurs, not on the order of the letters. Because the input alphabet is exactly the 26 lowercase English letters, map each character to an index from `0` through `25` and increment its slot while scanning `s` once.

After counting, inspect the five vowel slots to obtain `max_vowel`. Inspect the remaining 21 slots to obtain `max_consonant`. Every occurrence contributes to exactly one slot, and the two scans examine every eligible letter in their respective categories, so the selected values are precisely the two required maxima. A category absent from the string still has only zero-valued slots, which naturally produces the required value $0$.

## Complexity detail

Let $n$ be the length of `s`. Counting takes $O(n)$ time, and examining the fixed 26-letter alphabet takes $O(1)$ time, so the total is $O(n)$. The 26 counters and five vowel indices occupy $O(1)$ auxiliary space because the alphabet size does not grow with $n$.

## Alternatives and edge cases

- **Hash map counting:** A frequency map is also linear and concise, but a fixed array directly uses the guaranteed alphabet and avoids dynamic keys.
- **Repeatedly count each character:** Rescanning the entire string for every position is correct but can take $O(n^2)$ time.
- **Only vowels:** Every consonant slot remains zero, so the consonant contribution is correctly $0$.
- **Only consonants:** Every vowel slot remains zero, so the vowel contribution is correctly $0$.
- **Tied maxima:** Any tied letter gives the same frequency, and the algorithm needs only the maximum value.
- **Single character:** One category contributes $1$ and the other contributes $0$.
