## General

Let $h = \lceil n/2 \rceil$ and $p = 9 \cdot 10^{h-1}$.

**Enumerate palindromes through their left halves**

An $n$-digit palindrome is determined by its first $h$ digits. Enumerate every $h$-digit half, mirror all of it for even $n$, or mirror everything except its last digit for odd $n$. Because the half starts nonzero, the palindrome cannot have a leading zero.

Keep only palindromes divisible by `k`. Sort each survivor's digits to obtain a canonical multiset signature and insert it into a set. The set is essential: several divisible palindromes may use the same multiset, but every original integer with that multiset must be counted only once.

**Count all legal arrangements of one signature**

For digit counts $c_0,\ldots,c_9$, the number of distinct length-$n$ arrangements is

$$
\frac{n!}{\prod_{d=0}^{9} c_d!}.
$$

If $c_0 > 0$, subtract arrangements beginning with zero. Fixing one zero first leaves

$$
\frac{(n-1)!}{(c_0-1)!\prod_{d=1}^{9} c_d!}
$$

invalid arrangements. Sum the remaining count for every unique qualifying signature.

Every good integer has the same signature as at least one enumerated divisible palindrome, so its signature is retained. Conversely, every non-leading-zero permutation counted from a retained signature can be rearranged back to that palindrome and is good. Signature deduplication makes these groups disjoint and prevents double counting.

## Complexity detail

There are $p$ legal halves. Building and testing a palindrome costs $O(n)$, while sorting its digits costs $O(n \log n)$, so enumeration takes $O(p n \log n)$ time. At most $p$ signatures of length $n$ are stored, giving $O(pn)$ space. The factorial calculations range only through $n \le 10$.

## Alternatives and edge cases

- **Enumerate every $n$-digit integer:** Testing all $9 \cdot 10^{n-1}$ candidates repeats work for equal digit multisets.
- **Store divisible palindromes instead of signatures:** This double-counts integer arrangements when multiple palindromes share one multiset.
- **Rebuild the unique signature collection repeatedly:** Deduplicating the full accumulated list after each palindrome is correct but repeats work that one persistent hash set performs incrementally.
- **Count all multiset permutations:** Arrangements beginning with zero are not $n$-digit integers and must be subtracted.
- For `n = 1`, each positive digit is already a palindrome and only divisibility matters.
- Odd-length palindromes mirror every half digit except the center.
- A zero may appear internally in both the palindrome and counted good integers.
- Repeated digits require factorial denominators to avoid duplicate permutations.
- The answer may be much larger than the number of divisible palindromes because every legal permutation of a qualifying signature is good.
