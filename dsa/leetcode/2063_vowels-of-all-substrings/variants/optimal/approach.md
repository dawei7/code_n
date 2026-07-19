## General
**Reverse the order of counting**

Enumerating substrings repeats the same work. Instead, consider one vowel occurrence at index $i$ and count how many substrings include that position. The left endpoint has $i+1$ choices, from index $0$ through $i$, while the right endpoint has $n-i$ choices, from $i$ through index $n-1$.

**Add each occurrence's contribution**

The vowel at index $i$ therefore contributes

$$
(i+1)(n-i)
$$

to the requested sum. Scan the string and add this product only when the current character is a vowel.

Each pair of substring boundaries contributes once for every vowel position it encloses. The contribution formula counts exactly those boundary pairs for one position, so summing it over vowel positions counts the same `(substring, vowel occurrence)` pairs as the original definition, without constructing any substring.

## Complexity detail
The algorithm inspects each of the $n$ characters once and performs constant work per character, for $O(n)$ time. The vowel membership test and accumulated total require $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all substrings:** Maintaining a running vowel count for each start avoids recounting characters, but still requires $O(n^2)$ time.
- **Ending-at dynamic total:** Track the vowel count summed over all substrings ending at each index and add those totals; this also achieves $O(n)$ time.
- A vowel at either endpoint still participates in many substrings; its contribution is not merely one.
- Repeated vowels are distinct occurrences and each makes its own contribution.
- A string with no vowels returns zero, while a one-character vowel returns one.
- The maximum result requires an integer type wider than signed 32 bits in languages with fixed-width integers.
