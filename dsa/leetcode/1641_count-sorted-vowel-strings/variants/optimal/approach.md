## General
**A sorted string is determined by vowel multiplicities.** Once the counts of `a`, `e`, `i`, `o`, and `u` are fixed, their sorted order is forced: all `a` characters come first, then all `e` characters, and so on. The problem is therefore equivalent to counting nonnegative integer solutions of

$$
x_a+x_e+x_i+x_o+x_u=n.
$$

**Apply stars and bars.** Represent the $n$ character positions as stars and divide them into five possibly empty vowel groups with four separators. Choosing the separator locations among $n+4$ total symbols gives

$$
\binom{n+4}{4}
=\frac{(n+1)(n+2)(n+3)(n+4)}{24}.
$$

Every nonnegative count tuple maps to exactly one sorted vowel string, and every sorted vowel string supplies exactly one tuple, so this count is neither missing nor duplicating any string. Evaluate the four-factor expression directly with integer arithmetic.

## Complexity detail
The closed form performs a fixed number of additions, multiplications, and one integer division, independent of `n`, so it takes $O(1)$ time and $O(1)$ auxiliary space. The source domain contains only the 50 legal inputs from 1 through 50; the package therefore uses a bounded-domain complexity certificate with an exhaustive independent dynamic-programming regression rather than claiming a measured scaling trend over this small scalar range.

## Alternatives and edge cases
- **Five-state dynamic programming:** Track counts of strings ending in each vowel and update prefix sums for each length. This is intuitive and takes $O(n)$ time with $O(1)$ space.
- **Memoized recursion:** Choose the next vowel without decreasing and cache `(remaining_length, minimum_vowel)` states; it also takes $O(n)$ time because the alphabet has fixed size.
- **Enumerate all vowel strings:** Generating $5^n$ strings and filtering sorted ones is exponentially wasteful.
- At `n = 1`, each of the five vowels contributes exactly one result.
- Vowels may repeat any number of times, including zero for a particular vowel.
- “Sorted” means non-decreasing, not strictly increasing; otherwise no length above five could succeed.
- The factor 24 is $4!$, reflecting the four stars-and-bars separators rather than the five vowels themselves.
