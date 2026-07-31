## General

Whether a word qualifies depends only on its two endpoint characters. Convert the word array conceptually into a binary sequence: place `1` at an index when both endpoints belong to the vowel set, and `0` otherwise. Each query then asks for the sum of that binary sequence across an inclusive interval.

Build a prefix array beginning with zero. After processing `words[i]`, append the number of qualifying words among indices $0$ through $i$. With this half-open convention, `prefix[t]` counts qualifying words before index $t$.

For an inclusive query `[left, right]`, `prefix[right + 1]` counts every qualifying word through `right`, while `prefix[left]` counts those strictly before `left`. Their difference therefore counts exactly the requested range. The same precomputation is shared by all queries, avoiding any repeated scan of the words.

## Complexity detail

Let $n$ be the number of words and $q$ the number of queries. Inspecting the first and last character of each nonempty word and building the prefix array takes $O(n)$ time. Every query is answered in $O(1)$ time, giving $O(n+q)$ overall. The prefix array contains $n+1$ integers and uses $O(n)$ auxiliary space; the returned $q$-element result is output space.

## Alternatives and edge cases

- **Scan every range:** Testing every word inside every query is straightforward but can require $O(nq)$ time when many queries cover most of the array.
- **Fenwick tree:** A binary indexed tree also supports range sums, but no word values change, so its logarithmic queries and added machinery are unnecessary.
- **Single-letter words:** A one-character vowel is both the first and last character and therefore qualifies.
- **Only one vowel endpoint:** A word must start and end with vowels; satisfying only one side contributes zero.
- **Inclusive right endpoint:** The subtraction must use `right + 1`; using `prefix[right]` would omit the final queried word.
- **Repeated and overlapping queries:** Each query is independent and is answered in its original position, even when ranges repeat or overlap.
