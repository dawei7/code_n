## General

The sign cannot change, so positive and negative inputs require opposite digit orders. For a positive number, a smaller magnitude gives a smaller value. For a negative number, a larger magnitude gives a more negative—and therefore smaller—value.

**Separate the sign from the digits**

The boolean `neg = num < 0` remembers whether the result must be negative. The assignment `num = abs(num)` removes the sign so every remaining operation deals only with decimal digits.

A ten-entry frequency array `cnt` stores how many copies of each digit occur. Repeatedly taking `num % 10` extracts the last digit, and `num //= 10` removes it. Incrementing `cnt[digit]` preserves duplicates without needing to remember their original order, because arbitrary rearrangement is allowed.

The special input zero makes the extraction loop empty. All counts remain zero and the method later returns zero, which is already the only rearrangement.

**Construct a negative answer in descending digit order**

For a negative input, minimizing the signed value means maximizing its positive magnitude. Among numbers with the same number of digits, the largest digit must occupy the highest place value, the next-largest the next position, and so on.

The loop visits digits from nine down to zero. For every occurrence, `ans *= 10` shifts the number left one decimal place and `ans += i` appends digit `i`.

An exchange argument proves this order. If a smaller digit $a$ appears before a larger digit $b$, swapping them increases the magnitude because the larger digit receives the greater place-value coefficient. Repeating exchanges yields descending order and maximum magnitude. Returning `-ans` then gives the smallest signed value.

For `-7605`, descending digits form magnitude 7650, and the result is `-7650`.

Leading zeros are not a concern in the negative branch: if any nonzero digit exists, descending order places it first. If all digits are zero, the original number is simply zero and never enters this branch.

**Construct a positive answer without a leading zero**

For a positive input, ascending digit order would ordinarily minimize the number, but a zero cannot be the first written digit. If zeros exist, the code finds the smallest digit from one through nine with a positive count. It places that digit into `ans` first and decrements its frequency.

All remaining digits are then appended in ascending order from zero through nine. Consequently, every zero follows the required nonzero leading digit and occupies the earliest remaining, most valuable positions.

This is optimal because the leading position must contain some nonzero digit, so choosing the smallest available nonzero digit minimizes the greatest place-value contribution. After that forced choice, ordinary ascending order minimizes every remaining suffix position by the same exchange argument.

For `310`, the smallest nonzero digit one is placed first. The remaining digits zero and three are appended ascending, producing 103 rather than illegal `013`.

**Why the frequency representation is sufficient**

Only digit multiplicities and the unchanged sign affect the possible rearrangements. The frequency array contains exactly that information. Each construction loop consumes every count once, so no digit is omitted or duplicated.

**Why the result is globally minimal**

For negative inputs, descending magnitude digits maximize the magnitude and hence minimize the signed number. For positive inputs, the smallest legal leading digit is necessary, and the ascending remainder is optimal. Zero is handled directly. These cases exhaust every legal input sign.

## Complexity detail

Let $d$ be the number of decimal digits. Extraction takes $O(d)$ time. Construction scans ten possible digit values and appends exactly $d$ digits, so total time is $O(d+10)$.

The constraint limits the magnitude to $10^{15}$, so $d$ is bounded by a small constant and the manifest reports $O(1)$ time. The ten-entry counter and scalar variables also use $O(1)$ space.

Python integers grow as digits are appended and safely represent the legal result.

## Alternatives and edge cases

- **Sort digit characters:** Sorting ascending for positives and descending for negatives is concise, but the positive leading-zero repair is still required.
- **Enumerate permutations:** This is factorial in the digit count and repeats arrangements when digits are duplicated.
- **Positive number with no zero:** All digits are appended in ordinary ascending order.
- **Positive number with several zeros:** Exactly one smallest nonzero digit leads, followed immediately by all zeros, then remaining positive digits.
- **Negative number with zeros:** Descending order naturally places zeros at the end, increasing magnitude relative to placing them earlier.
- **Input zero:** The extraction loop is empty and the final answer remains zero.
- **Repeated digits:** Frequency counts preserve every copy and avoid redundant sorting comparisons.
- **Single nonzero digit plus zeros:** That digit must lead a positive result; all zeros follow it.
- **Sign preservation:** `abs` is only temporary; `neg` determines whether the constructed magnitude is negated.
- **No leading-zero string is built:** The method constructs an integer arithmetically, and its positive first appended digit enforces legality.
- **Bounded digit alphabet:** Scanning all ten digit values is constant regardless of how often each occurs.
- **Input immutability:** Reassigning local integer `num` cannot mutate the caller’s integer object.
