## General

**Interpret one operation as moving to the previous distinct permutation.** The specified operation is the standard previous-lexicographic-permutation transformation. The largest descent chooses the rightmost pivot that can be reduced. Swapping it with the appropriate smaller suffix character makes the string smaller, and reversing the suffix arranges that suffix as large as possible after the reduction. As a result, one operation moves from the current string to the immediately preceding distinct permutation of the same multiset of characters.

The sorted string is the smallest lexicographic permutation. Therefore, the number of operations needed to reach it is exactly the number of distinct permutations lexicographically smaller than `s`. In other words, the answer is the zero-based lexicographic rank of `s` among all distinct permutations of its characters. Computing that rank combinatorially avoids simulating what may be an enormous number of operations.

**Precompute factorials and inverse factorials.** For a multiset with `L` remaining characters and frequency `count[c]` for each character, the number of distinct permutations is

`L! / product(count[c]!)`.

Division must be performed modulo `1,000,000,007`. The module-level arrays `f` and `g` store factorials and modular inverse factorials:

- `f[i]` is `i! modulo mod`.
- `g[i]` is the modular inverse of `i! modulo mod`.

The modulus is prime, and every needed factorial is smaller than the modulus, so it is nonzero modulo that prime. Fermat’s little theorem gives the inverse as `pow(f[i], mod - 2, mod)`. Multiplying by `g[i]` is therefore modular division by `i!`.

The global limit is 3010, safely above the maximum string length of 3000. `f[0]` and `g[0]` are one, matching `0! = 1`. The precomputation fills all indices the method can need before any `Solution` instance is called.

**Count smaller choices at each position.** `cnt = Counter(s)` records how many copies of every character remain. At position `i` with current character `c`, any distinct permutation smaller than `s` for the first time at this position must:

1. Match `s` at every position before `i`.
2. Place some remaining character `a < c` at position `i`.
3. Arrange all remaining characters arbitrarily afterward.

The code computes

`m = sum(v for a, v in cnt.items() if a < c)`.

This is not merely the number of distinct smaller letters; it is the total number of remaining occurrences whose character is smaller than `c`. That multiplicity is exactly what the combined counting formula needs.

**Derive the formula used by `t`.** Let `L = n - i` be the number of positions remaining including the current one. After choosing a smaller character for this position, `L - 1` suffix positions remain.

For one specific smaller character `a`, the number of suffix permutations would be

`(L - 1)! / ((cnt[a] - 1)! * product of cnt[d]! for d != a)`.

Using `cnt[a]! = cnt[a] * (cnt[a] - 1)!`, this becomes

`(L - 1)! * cnt[a] / product(cnt[d]!)`.

Summing over all `a < c` changes only the numerator factor, producing

`(L - 1)! * m / product(cnt[d]!)`.

That is precisely what the implementation constructs. It starts with `f[n - i - 1] * m` and then, for every remaining frequency `v`, multiplies by `g[v]`. Each inverse factorial divides out the permutations made indistinguishable by duplicate copies. Taking a modulus after every multiplication keeps the value bounded.

**Consume the actual character and continue.** The contribution `t` counts all smaller permutations whose first difference from `s` occurs at position `i`. After adding `t` to `ans`, the algorithm follows the actual string’s path by decrementing `cnt[c]`. If the count becomes zero, the key is removed. On the next iteration, `cnt` represents exactly the unused suffix characters.

Groups counted at different positions cannot overlap. A permutation whose first difference is at position two, for example, is not counted among permutations whose first difference is at position one. Conversely, every permutation smaller than `s` has one unique first differing position and a smaller character there, so it appears in exactly one contribution. Summing all contributions yields the exact lexicographic rank.

**A small duplicate-aware example.** For `s = "aabaa"`, no smaller character than `a` is available at positions zero or one, so both contributions are zero. At position two, the current character is `b` and three `a` characters remain. Choosing an `a` there leaves the multiset containing one `b` and two `a` characters for the last two positions after later prefix accounting; the formula counts the distinct suffix arrangements without treating identical `a` copies as different. Continuing through the actual `b` path adds the remaining smaller permutation at a later first-difference position. The total rank is two, matching two applications of the previous-permutation operation.

For a string that is already sorted, no position has any remaining smaller character than its actual one. Every `m` is zero, every `t` is zero, and the answer is zero. For all distinct characters in descending order, the rank is `n! - 1` because every other permutation is smaller; the modular arithmetic returns that count modulo the required prime.

**Why the operation count and rank coincide with duplicates.** Standard permutation sequences list distinct strings in lexicographic order. The pivot, swap, and reversal rules skip arrangements that differ only by exchanging identical characters because those exchanges do not form a new string. Thus repeated operation moves traverse distinct multiset permutations one at a time. The factorial denominator used by the rank formula removes exactly those duplicate arrangements, so both sides count the same objects.

## Complexity detail

Inside `makeStringSorted`, building the counter takes `O(n)` time. The string uses only 26 lowercase letters, so both the sum over `cnt.items()` and the product over `cnt.values()` inspect at most 26 entries per position. Their cost is `O(26n)`, which is `O(n)` because the alphabet size is fixed. The counter itself holds at most 26 keys.

The module-level precomputation uses arrays of fixed capacity 3011. It calculates one factorial and one modular exponentiation for each index up to 3009. Under ordinary modular-exponentiation analysis, that startup cost is `O(N log mod)` for `N = 3010`, while its storage is `O(N)`. It happens once when the module loads, not once per method call. If the prime modulus and 3000 input ceiling are treated as fixed problem constants, this is fixed setup; if `N` is parameterized with maximum input length, the exact precompute is not strictly linear because it computes every inverse with a separate exponentiation.

For one call, additional working space is `O(1)` with respect to `n` because the alphabet is fixed, while the shared factorial tables occupy `O(N)` space. Describing total prepared storage relative to the maximum supported string length gives `O(n)` space.

## Alternatives and edge cases

- **Simulate each operation:** Generating previous permutations is faithful to the statement but can require a factorial number of steps, far beyond the length limit.
- **Fenwick tree for smaller-character counts:** A tree over character ranks can compute `m` in logarithmic alphabet time. With only 26 letters, directly scanning the counter is simpler and remains linear overall.
- **Recompute multinomial counts separately for every smaller letter:** This is conceptually direct but repeats almost identical denominator work. Factoring out the total `m` yields the compact formula used here.
- **All characters equal:** There is only one distinct permutation, every `m` is zero, and the result is zero.
- **Already sorted string:** No remaining smaller character exists at any position, so its lexicographic rank and operation count are zero.
- **Repeated characters:** Dividing by each frequency factorial is essential; omitting those factors would count swaps of identical copies as different strings.
- **Count becomes zero:** Removing the key is not required for correctness, but it keeps later scans limited to characters that actually remain.
- **Modulo division:** Ordinary integer division after taking a modulus is invalid. The inverse factorials provide division in the prime modular field.
- **Maximum length:** The global tables extend beyond 3000, so every factorial and inverse factorial index used by the method is initialized.
- **Single character:** Its only permutation is already sorted, giving zero.
- **Global precomputation cost:** The exact code computes each inverse factorial using `pow` separately. A reverse recurrence from one final inverse factorial could prepare all inverses in linear time.
- **Character ordering:** Python’s comparison of lowercase English letters matches their required lexicographic order, so `a < c` is the correct smaller-choice test.
