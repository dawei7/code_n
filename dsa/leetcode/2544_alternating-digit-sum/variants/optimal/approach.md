## General

Digits are easiest to extract arithmetically from right to left, although the required signs are defined from left to right. A recurrence avoids first counting the digits.

Suppose `answer` is the correctly alternating sum of the suffix already removed, with that suffix's first digit treated as positive. When a new digit `digit` is prepended, every sign in the previous suffix flips, so the new alternating sum is `digit - answer`. Extract `digit = n % 10`, apply that update, and remove the digit with `n //= 10`.

Initially the processed suffix is empty and has sum zero. After each iteration, the recurrence therefore gives the required alternating sum of all digits removed so far in their original order. When the working value becomes zero, that suffix is the entire decimal representation, so `answer` is the requested result.

## Complexity detail

Let $d$ be the number of decimal digits. Each iteration removes exactly one digit and performs constant work, giving $O(d)$ time and $O(1)$ auxiliary space. Legal inputs have at most ten digits, too few for an honest runtime scaling verdict, so the package uses a bounded-domain certificate with exhaustive and boundary-focused regression.

## Alternatives and edge cases

- **String conversion:** Iterating over `str(n)` with an explicit sign is also $O(d)$ time but allocates $O(d)$ space for the digit string.
- **Count digits first:** Determining whether the rightmost sign is positive or negative works, but requires an extra pass or logarithm calculation that the prepend recurrence avoids.
- **Single digit:** Its sign is positive, so the answer is the digit itself.
- **Internal zeroes:** A zero contributes nothing but still flips the sign assigned to the next digit.
- **Even digit count:** The least significant digit then has a negative sign; the recurrence handles this without a parity branch.
- **Upper boundary:** The legal ten-digit value `1000000000` has alternating sum 1.
