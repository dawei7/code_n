## General

**Translate divisibility into four prime-exponent requirements.** Every nonzero decimal digit factors entirely into the primes $2$, $3$, $5$, and $7$. For example, digit 8 contributes three factors of 2, while digit 6 contributes one factor of 2 and one factor of 3. The table `DIGIT_FACTORS` records these four exponents for every digit.

The solution first divides `t` repeatedly by $2,3,5,7$ and stores how many copies of each prime were removed. This produces `required = [a,b,c,d]`, meaning the answer's digits must collectively provide at least $a$ twos, $b$ threes, $c$ fives, and $d$ sevens. If a remainder larger than one survives, `t` has some other prime factor. No digit from 1 through 9 can supply that factor, so returning `"-1"` is necessary.

**Find the shortest way to supply missing twos and threes.** Digits 2, 3, 4, 6, 8, and 9 can bundle these two primes. For instance, using one 8 is shorter than using three 2s. The cached helper `pack_twos_threes(twos, threes)` explores each bundling digit. It subtracts that digit's contribution, never lets a deficit become negative, recursively packs what remains, sorts the resulting digits, and chooses the candidate with the smallest pair `(length, candidate)`.

This ordering has two purposes. Fewer digits are always preferable because a shorter required pack leaves more positions available for leading ones. Among equal-length packs, the lexicographically smaller sorted digit string produces the smaller decimal suffix. Memoization ensures that each deficit pair is solved once rather than through every possible digit ordering.

Factors 5 and 7 are simpler. Among decimal digits, only digit 5 supplies prime 5 and only digit 7 supplies prime 7; neither can be bundled with another prime in a zero-free digit no greater than 9. Therefore each missing factor of 5 needs one `"5"`, and each missing factor of 7 needs one `"7"`.

**Construct the smallest suffix of a fixed length.** `minimum_digits` reports how many non-one digits are needed for a missing exponent tuple. `smallest_suffix(length, missing)` combines the optimal two/three pack with the required fives and sevens, sorts all contributing digits, and prepends enough ones to reach `length`.

Digit 1 contributes no prime factors, so padding with it cannot break divisibility. Placing those ones first, followed by all other digits in sorted order, is lexicographically smallest among suffixes using that multiset. For equal-length positive decimal strings, lexicographic and numeric order are the same.

**Check whether the input itself already works.** The first scan accumulates prime exponents until it encounters the first zero. If no zero exists and every accumulated exponent reaches its requirement, `num` is already the smallest allowed answer because equality is permitted.

The location of the first zero is important. A zero-free answer cannot preserve a prefix containing that zero. Consequently, when a zero exists, the rightmost position that can first be increased is that zero's position; positions farther right cannot repair an unchanged earlier zero.

**Search for the smallest same-length successor.** The algorithm tries change positions from right to left, beginning at the first zero or, when there is no zero, at the last digit. Moving right to left maximizes the prefix kept equal to `num`. Keeping a longer equal prefix always produces a smaller successor than changing an earlier position.

For a chosen position, it tries replacement digits from the original digit plus one through 9. Increasing that position guarantees that the completed number is greater than `num`, so every later position becomes free to minimize. The vector `prefix` stores prime contributions from the unchanged digits before this position. When the search moves one position left, the old digit at that position is subtracted because it will no longer belong to the fixed prefix.

For each candidate replacement, `covered` combines the prefix and replacement exponents, and `deficits` computes what the suffix must still provide. If the shortest required pack fits in `suffix_length`, the source immediately returns the unchanged prefix, the smallest feasible replacement digit, and the lexicographically smallest fixed-length suffix.

This first return is globally minimal. Every possibility that changes a later position was tested first. At the current position, every smaller greater digit was tested first. Once those choices are fixed, `smallest_suffix` supplies the least possible tail.

**Use a longer number only when every same-length choice fails.** Any positive number with more digits is greater than `num`. The smallest possible answer length is therefore the larger of `len(num)+1` and the number of digits needed to pack all required factors. The source builds the smallest suffix across that entire length, which places harmless ones in front and the required factor digits in sorted order.

**Why the first feasible construction is the answer.** Prime factorization makes the exponent test equivalent to divisibility by `t`. The packing helper finds a shortest, lexicographically least set of digits that covers every remaining exponent. The right-to-left search considers same-length successors in order of the first position where they exceed `num`. Therefore the first feasible construction is the smallest zero-free answer; if none exists, the minimal longer construction is the smallest answer overall.

## Complexity detail

Let $n$ be the length of `num`, and let $a$ and $b$ be the exponents of 2 and 3 in `t`. The main scans examine at most nine replacement digits per position, so they take $O(n)$ time. Creating the returned string and sorting its short factor pack takes $O(n)$ time overall.

The cached packer has at most $O((a+1)(b+1))$ states and six transitions per state. Its stored strings have $O(a+b)$ length in a generalized analysis, so constructing and sorting candidates adds a small factor depending on $\log t$. Under `t <= 10^14`, $a$ and $b$ are bounded constants, making the complete stated complexity $O(n)$ time.

The input-sized output work and prefix accounting use $O(n)$ space, while the exponent cache is constant-sized under the given bound. Thus the manifest's $O(n)$ space bound is valid; excluding the returned string, auxiliary storage is $O(1)$ with respect to $n$ plus the bounded cache.

## Alternatives and edge cases

- **Editorial GCD residual array:** Track the remaining divisor after every original prefix and greedily fill a suffix. It reaches the same goal, but the exact source instead works with explicit prime-exponent vectors and a cached packer.
- **Digit dynamic programming with tight state:** A full left-to-right DP can model whether the prefix equals `num`, but its state and reconstruction are more elaborate than the right-to-left first-change search.
- **Forbidden prime factor:** If `t` contains 11, 13, or any prime outside $\{2,3,5,7\}$, no zero-free decimal digit product can be divisible by it.
- **`t = 1`:** Every zero-free product is divisible by one; the method returns `num` if it has no zero, otherwise it minimally increases at or before the first zero and fills the suffix with ones.
- **Input already valid:** The early return preserves `num` exactly.
- **First zero:** Searching only from that position leftward prevents an invalid zero from surviving in the fixed prefix.
- **Zero after the changed position:** It is discarded with the free suffix and replaced by a nonzero constructed digit.
- **Current digit is 9:** There is no larger digit at that position, so the search moves left.
- **Over-covering an exponent:** A digit may supply more copies of a prime than required; `max(0, deficit - contribution)` correctly allows that because divisibility needs at least the required factors.
- **Repeated factor digits:** Sorting preserves multiplicity and puts the same multiset into its smallest numeric order.
- **Padding with ones:** Ones are zero-free, do not affect the product, and are the smallest possible padding digits.
- **No same-length answer:** Increasing the length guarantees numeric superiority, even if the new leading digit is one.
- **Very long input:** Runtime depends linearly on its $2\cdot10^5$ characters rather than on the numeric value represented by the string.
- **Imports and shared constants:** The source requires `lru_cache` and relies on the exact exponent meanings encoded by `DIGIT_FACTORS` and `PACK_DIGITS`.
