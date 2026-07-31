## General

The vowel alphabet is fixed: in increasing ASCII order it is `AEIOUaeiou`. This constant-size domain permits counting sort instead of comparison sorting.

Map each of those ten characters to its index and count the vowels during one scan of `s`. Convert `s` to a mutable character list for the result. During a second scan, skip every consonant. At each vowel position, advance a pointer through the ten counts until it reaches the smallest vowel that remains, write that vowel, and decrement its count.

**Why consonants and vowel order are both preserved correctly**

The second scan writes only at indices whose original characters are vowels, so every consonant remains unchanged. The pointer through `AEIOUaeiou` never moves backward; therefore successive replacement vowels have non-decreasing ASCII values. Each write consumes one counted occurrence, so the output contains exactly the original vowel multiset. These facts satisfy both required properties of the returned permutation.

## Complexity detail

Let $n$ be the length of `s`. The counting and reconstruction scans each take $O(n)$ time. Advancing the vowel pointer costs only $O(10)$ over the entire reconstruction. The mutable result and returned string require $O(n)$ space; the ten counts and ten-entry lookup map use $O(1)$ auxiliary space beyond the output.

## Alternatives and edge cases

- **Comparison sorting:** Extract the vowels, sort them, and place them back in their original slots. This is concise but costs $O(v\log v)$ time for $v$ vowels instead of exploiting the ten-character domain.
- **Priority queue:** A min-heap can provide the next vowel in $O(\log v)$ time per replacement, but it has the same avoidable logarithmic factor and more machinery.
- **No vowels:** Every count remains zero and the reconstruction scan returns the original string unchanged.
- **One vowel:** Its position and value remain unchanged because it is already sorted by itself.
- **Uppercase versus lowercase:** ASCII ordering places all five uppercase vowels before all five lowercase vowels; case-insensitive alphabetic order would be incorrect.
- **Repeated vowels:** Counts preserve every duplicate, and equal vowels naturally occupy consecutive vowel slots.
