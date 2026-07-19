## General
**Update one binary prefix:** Appending `bit` to a binary number transforms its value to `value * 2 + bit`. Divisibility by `5` depends only on the remainder, so update `remainder = (remainder * 2 + bit) % 5` rather than storing the entire growing integer.

**Report after every append:** Once the current bit is included, append `remainder == 0` to the answer. The same remainder becomes the starting state for the next prefix.

**Why reducing early is exact:** If two integers have the same remainder modulo `5`, doubling them and adding the same bit preserves equal remainders. Replacing the full prefix with its remainder therefore loses no information relevant to any current or future divisibility test.

By induction, after processing index `i`, `remainder` equals $x_i\bmod5$. Each emitted boolean is consequently true exactly for the required prefixes.

## Complexity detail
Each of the $N$ bits performs one constant-time remainder update, giving $O(N)$ time. The rolling remainder uses $O(1)$ auxiliary space; the required $N$-element returned array is output space and is excluded from the bound.

## Alternatives and edge cases
- **Recompute each prefix:** Reading from index zero for every endpoint is correct but takes $O(N^2)$ time.
- **Store the full integer:** Arbitrary-precision arithmetic avoids overflow but grows more expensive as the prefix gains bits.
- **Leading zeroes:** A zero prefix has value zero and is divisible by five.
- **Single bit:** Return one boolean based on whether that bit is zero.
- **Very long input:** Keeping only the remainder prevents integer overflow and unbounded numeric storage.
