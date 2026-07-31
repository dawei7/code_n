## General

Any feasible length must divide $n$, because `s` must be partitioned into whole pieces of that length. Test candidate lengths from smallest to largest and skip every non-divisor. The first successful candidate is therefore the minimum possible answer.

**Comparing anagrams without sorting**

For a candidate length, count the occurrences of all 26 lowercase letters in the first block. Scan every later aligned block and build the same fixed-size frequency vector. A block is an anagram of the first exactly when the two vectors are equal; character order is irrelevant, but every multiplicity must match.

Reject a candidate as soon as one block differs. If all of its blocks match, the first block itself can serve as `t`, while every later block is an anagram of it. This proves that the candidate is feasible. Conversely, any valid `t` requires every aligned block to have the same frequency vector, so the test cannot reject a genuinely feasible length.

The whole string is always a divisor-sized candidate with only one block, so the search is guaranteed to return.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$ and let $\tau(n)$ be the number of positive divisors of $n$. A tested divisor scans at most $n$ characters, while walking through all integers to identify divisors costs $O(n)$. The tighter bound is $O(n\tau(n) + n)$; since $\tau(n) = O(\sqrt n)$, this is within the required $O(n\sqrt n)$ time bound.

Each frequency vector has exactly 26 entries. The algorithm does not store data proportional to $n$, so its auxiliary space is $O(1)$ under the fixed lowercase-English alphabet.

## Alternatives and edge cases

- **Sort every block:** Sorting exposes a canonical anagram signature, but it adds a logarithmic factor to each block comparison and creates block-sized temporary data.
- **Global frequency greatest common divisor:** Divisibility of total character counts can rule out some block counts, but it cannot prove that the actual aligned pieces are anagrams; `"aabb"` is the smallest instructive counterexample.
- **Rolling frequency prefixes:** Prefix vectors can derive any block's counts, but storing all prefixes uses $O(n)$ space without improving the worst-case divisor scan enough to justify it here.
- A one-character string and a string made from one repeated letter both return $1$.
- Candidate boundaries are fixed by the chosen length; letters may be rearranged only conceptually within each block, never moved between blocks.
- The complete string is always a valid fallback, even when no proper divisor works.
