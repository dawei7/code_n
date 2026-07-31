## General

Each digit contributes its value multiplied by a decimal place value. Minimizing the final sum therefore means assigning smaller digits to more significant positions and keeping the two constructed numbers' lengths as balanced as possible.

**Why the lengths must be balanced:** If one result had at least two more digit positions than the other, transferring its leading digit to the shorter result would replace a larger decimal weight with a smaller one. Thus an optimal split gives the two numbers equal lengths when $d$ is even and lengths differing by one when $d$ is odd.

**Assigning the place values:** After those balanced lengths are fixed, the largest place weights are the leading positions of the two numbers, followed by their next positions, and so on. By the rearrangement principle, the smallest available digits belong on those largest weights. Sort all digits in non-decreasing order, append the first digit to the first number, the second to the second number, and continue alternating. Appending makes each earlier, smaller digit more significant than later digits in the same number.

Leading zeroes require no special case. Appending a zero to an empty numeric accumulator leaves it at zero while still consuming that occurrence, exactly matching the permitted construction.

The alternation creates the required balanced lengths, and the sorted order pairs the digit multiset with the place-weight multiset in the minimum-sum order. Therefore the two accumulated integers have the smallest possible sum.

## Complexity detail

Let $d$ be the number of decimal digits in `num`. Sorting costs $O(d \log d)$ time, and the alternating construction costs $O(d)$ time. The digit representation uses $O(d)$ space.

## Alternatives and edge cases

- **Digit-frequency counting:** Because there are only ten digit values, a frequency array can emit digits in order in $O(d)$ time and $O(1)$ auxiliary space, but sorting is simpler and $d \leq 10$.
- **Trying every partition and permutation:** Exhaustive construction can confirm small examples but grows combinatorially and obscures the place-value argument.
- **Leading zeroes:** Zeroes are genuine input digits and may occupy leading positions; numeric accumulation naturally discards only their visual leading representation.
- **Odd digit count:** The first accumulator receives one additional digit, while the two lengths still differ by only one.
- **Repeated digits:** Sorting retains every occurrence, and alternating consumes each occurrence exactly once.
