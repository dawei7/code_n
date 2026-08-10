## General

An integer is good based only on its multiset of digits: if one arrangement of those digits forms an $n$-digit palindrome divisible by `k`, every legal $n$-digit arrangement of the same multiset is a good integer. The solution enumerates divisible palindromes, deduplicates their digit multisets, and counts legal permutations of each multiset.

An $n$-digit palindrome is determined by its first $\lceil n/2\rceil$ digits. `base = 10 ** ((n - 1) // 2)` is the smallest integer with that many relevant leading-half digits. Looping from `base` through `base * 10 - 1` enumerates every half with a nonzero first digit.

For half string `s`, the source appends a reversed slice. When `n` is even, `n % 2` is zero and the entire half is mirrored. When `n` is odd, slicing from one skips the reversed center digit so it is not duplicated. The result is every $n$-digit palindrome exactly once.

Palindromes not divisible by `k` are discarded. For each surviving palindrome, sorting its digits produces a canonical multiset key `t`. Different divisible palindromes can use the same digit counts; `vis` ensures that multiset's good integers are counted only once.

Let `cnt[d]` be the frequency of digit $d$, especially `cnt["0"] = c_0`. To form a legal $n$-digit integer, choose a nonzero occurrence for the first position and permute the remaining occurrences. Accounting for repeated digits gives

$$
\frac{(n-c_0)(n-1)!}{\prod_{d=0}^{9}c_d!}.
$$

The source computes the numerator as `(n - cnt["0"]) * fac[n - 1]` and divides by every frequency factorial.

This formula can also be derived from all distinct permutations minus those beginning with zero. Total permutations are $n!/\prod c_d!$. Leading-zero permutations are $(n-1)!/((c_0-1)!\prod_{d>0}c_d!)$. Their difference simplifies to the expression above.

Every counted permutation has exactly $n$ displayed digits because its first digit is nonzero. Its multiset has a witnessed divisible palindrome from enumeration, so it is good. Conversely, every good integer's digits rearrange into some enumerated divisible palindrome, and its canonical key is processed. Deduplication assigns it to exactly one multiset count.

For `n=1,k=4`, enumeration checks digits one through nine. Divisible palindromes four and eight produce distinct keys, and each key has one legal permutation, totaling two.

Leading zeros are handled in both places: enumerated palindromes start from a nonzero half, and permutation counting excludes arrangements whose first digit is zero.

## Complexity detail

Let $h=\lceil n/2\rceil$ and let $p=9\cdot10^{h-1}$ be the number of enumerated halves. Constructing, parsing, sorting, and canonicalizing one palindrome costs $O(n\log n)$ because sorting dominates. Time is $O(pn\log n)$.

The set can store up to $p$ canonical strings of length $n$, using $O(pn)$ space. Factorials and one frequency counter use $O(n)$ or constant digit-alphabet space.

With $n\le10$, at most 900,000 halves are enumerated when $h=5$, which makes this direct approach feasible.

## Alternatives and edge cases

- **Enumerate all $n$-digit integers:** There are $9\cdot10^{n-1}$, far more than the roughly square-root-sized palindrome space.
- **Generate digit multisets directly:** This avoids duplicate palindromes but then determining whether any permutation is a divisible palindrome is more complex.
- **Permute each palindrome's digits explicitly:** A multiset can have millions of arrangements. The factorial formula counts them without generation.
- **No multiset deduplication:** Two divisible palindromes with the same digits would cause every good permutation to be counted twice.
- **Odd length:** Exactly one digit may have odd frequency in a palindrome; construction handles the center by skipping its duplicate.
- **Even length:** Every palindrome digit frequency is even, and the whole half is mirrored.
- **Zeros inside a palindrome:** They are allowed away from the leading position and remain part of the multiset.
- **Potential leading-zero permutations:** The factor `n-c0` selects a nonzero first occurrence and excludes them exactly.
- **`k = 1`:** Every enumerated palindrome is divisible, so all multisets witnessed by any palindrome contribute.
- **Repeated digits:** Division by `fac[count]` removes indistinguishable permutations.
- **Same multiset, several witnesses:** `vis` counts it once regardless of how many divisible palindromic arrangements exist.
- **Integer conversion:** Constructed palindromes have nonzero first digits, so converting to integer preserves all $n$ digits.
- **Why the half range has the right width:** `base` has $h$ digits at its lower bound, and values below `10*base` have at most $h$ digits. Thus every enumerated half begins nonzero and has exactly $h$ digits.
- **Factorial precomputation:** All factorials from zero through `n` are computed once, so repeated multisets reuse them instead of recomputing combinatorial denominators.
- **Counter keys omitted for absent digits:** `cnt.values()` divides only by positive frequencies. Missing digits conceptually have frequency zero and `0! = 1`, so omitting them changes nothing.
- **Good integer need not be palindromic:** The formula counts every legal arrangement of a witnessed multiset, including arrangements that are not themselves palindromes. They are good because they can be rearranged to the witness.
- **Divisibility belongs to the witness:** A counted permutation need not be divisible by `k`. The definition requires only that its digits can form a divisible palindrome.
- **Exact integer division:** The combinatorial numerator is divisible by the product of repeated-digit factorials. Sequential `//=` operations therefore retain the exact integer count.
