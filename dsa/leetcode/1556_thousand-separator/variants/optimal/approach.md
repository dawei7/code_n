## General

**Read decimal digits from right to left**

Thousands separators divide a decimal representation into groups of three digits counted from the right. The rightmost group always contains the units, tens, and hundreds digits; the next group contains thousands through hundred-thousands, and so on.

Repeated division by ten naturally exposes digits in exactly that right-to-left order. The source uses `divmod(n, 10)`, which returns both the quotient and remainder:

- The remainder `v` is the current last decimal digit.
- The quotient becomes the still-unprocessed prefix.

The digit is converted to a one-character string and appended to list `ans`.

**Count digits within the current group**

Variable `cnt` records how many digits have been appended since the most recent separator. It increases after each extracted digit.

When all remaining digits have been consumed, `n == 0` and the loop stops. That check deliberately occurs before separator insertion.

Otherwise, if `cnt == 3`, the current right-to-left group is complete. The source appends a dot and resets `cnt` to zero so the next three extracted digits form the next group.

Because extraction proceeds backward, `ans` temporarily contains the entire formatted result in reverse order.

**Why the stopping check must precede the dot**

Consider `n = 123`. After extracting three, two, and one, `cnt` equals three, but the quotient is now zero. The result should be `"123"`, not `".123"`.

The source tests `n == 0` first and breaks, so no separator is added beyond the most significant group.

For `n = 1234`, after extracting four, three, and two, unprocessed quotient one remains. The code appends a dot because another group truly exists. It then extracts one and stops, giving reversed pieces `["4","3","2",".","1"]`.

This ordering handles exact multiples of three digits without a special case.

**Reverse once at the end**

Digits and dots were appended from least significant to most significant. `ans[::-1]` creates the pieces in normal reading order, and `''.join(...)` concatenates them into the requested string.

Reversal moves separator positions correctly along with digits. The reversed pieces for 1234 become one, dot, two, three, four, producing `"1.234"`.

Using a list avoids repeatedly prepending to an immutable Python string. Prepending would copy the growing result on every iteration.

**The zero case**

The loop is written as `while 1` rather than `while n > 0`. This is important for input zero.

The first `divmod(0, 10)` produces quotient zero and remainder zero. The source appends `"0"`, increments the count, and then breaks. The final result is correctly `"0"`.

A loop conditioned only on positive `n` would need a separate zero branch or would return an empty string.

**A larger trace**

For `n = 123456789`, digits are extracted in order nine through one.

After nine, eight, and seven, the first dot is appended because digits remain. After six, five, and four, another dot is appended. The final group three, two, one reaches quotient zero and stops without an extra dot.

Reversing produces `"123.456.789"`. Every internal group has exactly three digits, while the leading group contains between one and three digits.

**A useful invariant**

After each iteration, `ans` contains the correctly separated representation of the decimal suffix already removed from `n`, but in reverse order. `cnt` equals the number of digits in the unfinished group at the end of that reversed list.

Extracting one more digit extends that suffix. When the group reaches three and a quotient remains, appending a dot establishes the required boundary. The invariant is preserved until the quotient is zero.

At termination, every original digit has been represented exactly once and every boundary after a three-digit right-side group has exactly one dot. Reversal therefore yields the unique required formatting.

**Why no leading zeros appear**

For a positive integer, ordinary division by ten eventually exposes its nonzero most significant digit and then reaches quotient zero. No additional iterations occur, so the algorithm never invents leading zero digits.

Internal groups still preserve zeros that belong to the number. For 1000, extracted digits are zero, zero, zero, dot, one, resulting in `"1.000"`.

## Complexity detail

Let $D$ be the number of decimal digits. The loop runs once per digit, reversal processes $O(D)$ pieces, and joining copies the $D$ digits plus separators. Time is $O(D)$, equivalently $O(\log n)$ for positive numeric magnitude.

The list stores $O(D)$ characters and separators, and the returned string has $O(D)$ length. Auxiliary construction space is $O(D)$.

The manifest reports $O(1)$ time and space because the contract permanently bounds `n` to a 32-bit signed integer, so $D \le 10$. Under that fixed domain, the digit count is a constant. Parameterized by representation length, the exact source has the linear-in-digits costs above.

## Alternatives and edge cases

- **Built-in comma formatting:** Format with commas and replace commas by dots. It is concise but hides the grouping logic and still creates strings.
- **Convert first and slice groups:** Split the decimal string from the right into chunks of three and join them. It is also $O(D)$.
- **Repeated string prepending:** It is correct but can repeatedly copy the growing immutable result.
- **Zero:** The unconditional loop emits one zero digit rather than an empty string.
- **One to three digits:** No separator is added because no higher group remains.
- **Exactly four digits:** One dot separates the leading digit from the final three.
- **Exactly six digits:** Only one dot is needed; the quotient-zero check prevents a leading dot.
- **Internal zeros:** Values such as 1000 retain a full `000` group.
- **Maximum input:** The same loop handles 2147483647 with three separators.
- **Negative values:** They are outside the contract; the digit-extraction logic is designed for nonnegative integers.
- **Separator placement:** Counting starts at the right, which is why groups remain correct regardless of total digit count.
- **Output allocation:** Returning a string necessarily requires space proportional to its displayed length when the numeric domain is treated as variable.
