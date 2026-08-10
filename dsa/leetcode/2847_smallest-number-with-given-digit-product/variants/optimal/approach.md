## General

**Factor the target into decimal digits.** A result digit can be one through nine. Digits zero cannot appear when the required product `n` is positive because they would make the product zero. Digit one does not help factor a value greater than one and only makes a multi-digit result longer.

The useful factor digits are therefore two through nine. The method repeatedly extracts the largest possible one, beginning at nine and ending at two.

**Why larger composite digits are valuable.** Numeric magnitude is determined first by digit count: every positive number with fewer digits is smaller than every number with more digits, provided there are no leading zeros. Packing several small prime factors into one large digit minimizes the number of digits.

For example, factors three and three should become digit nine rather than digits three and three. Three twos should become eight. A two and a three should become six. Two twos should become four.

Descending extraction implements this packing automatically.

**Count each extracted digit.** `cnt` has ten buckets. For current digit `i` from nine down through two, while `n % i == 0`:

- Divide `n` by `i`.
- Increment `cnt[i]`.

Every division records one result digit whose value contributes factor `i`. When that loop ends, the remaining value is no longer divisible by `i`, and the scan tries the next smaller digit.

**Detect impossibility.** Decimal digits two through nine contain only prime factors two, three, five, and seven. If extraction finishes with `n > 1`, the leftover contains a prime factor larger than seven or a combination that no allowed digit can absorb. No decimal digit product can equal the original target, so the method returns `"-1"`.

Conversely, if `n == 1` after extraction, multiplying all recorded digits reconstructs the original input because every division removed exactly that factor.

**Why descending packing minimizes digit count.** Factors five and seven can only appear in digits containing those primes, and the largest usable combinations with other primes are already tested before their single digits. For factors two and three, the efficient packs are nine, eight, six, and four before leftover threes and twos.

Any representation using smaller digits can be transformed by replacing combinations such as `3,3` with nine, `2,2,2` with eight, or `2,3` with six whenever possible, never increasing digit count. The descending divisibility loop chooses these packs at the earliest opportunity.

**Arrange recorded digits in ascending order.** Once the multiset and minimum digit count are determined, the smallest number with those digits places the smallest digit first, then the next smallest, and so on. The source constructs

`"".join(str(i) * cnt[i] for i in range(2, 10))`.

Although factors were extracted from large to small, output order is small to large. Any inversion with a larger digit before a smaller one can be swapped to reduce the number lexicographically and numerically.

**The special input one.** No factor from two through nine divides one, so the generated string is empty. The smallest positive integer whose digit product is one is `"1"`. The final conditional returns that value.

Adding digit one to any other representation would increase its digit count and make it larger, so one appears only for target one.

**A trace for 105.** Nine and eight do not divide 105. Seven divides it, leaving fifteen. Five divides, leaving three. Three divides, leaving one. Counts produce ascending digits three, five, seven and answer `"357"`.

**Why output is a string.** The target can reach $10^{18}$ and the resulting decimal representation is naturally constructed digit by digit. A string avoids numeric conversion limits and directly satisfies the contract.

## Complexity detail

Every successful division by a digit at least two reduces `n` by a constant factor. The number of successful divisions is $O(\log n)$ and equals the output digit count up to constants.

The outer loop checks only eight candidate digits. Failed modulus tests are constant in number. Constructing the result writes $O(\log n)$ characters. Total time is $O(\log n)$.

The count array has fixed length ten, so it is $O(1)$ auxiliary storage. The returned string has $O(\log n)$ digits. Including required output space gives $O(\log n)$; excluding it, scratch space is $O(1)$.

Under arbitrary-precision bit complexity, division cost grows with operand length, but the conventional bound treats the at-most-$10^{18}$ arithmetic as fixed-width.

## Alternatives and edge cases

- **Prime-factor count construction:** Count twos, threes, fives, and sevens, reject any other prime, then pack exponents into digits nine, eight, six, and four. This can make the optimality argument more explicit but requires careful case ordering.
- **Breadth-first search over numbers:** Generating candidate decimal strings grows exponentially and is unnecessary.
- **Target one:** Return digit one; an empty string is not a positive integer representation.
- **Prime target two through seven:** The one-digit target itself is the smallest answer.
- **Prime factor above seven:** No decimal digit can supply it, so negative one is required.
- **Repeated factors:** The while loop records as many copies as needed.
- **Digit one in a larger answer:** It never changes the product and only makes the number longer, so it is omitted.
- **Digit zero:** It would force product zero and cannot occur for positive target.
- **Ascending final order:** It minimizes the number among all permutations of the chosen digit multiset.
- **Minimum digit count first:** A lexicographically attractive longer representation can never beat a shorter positive integer.
- **Large output:** String construction avoids integer overflow or parsing concerns.
