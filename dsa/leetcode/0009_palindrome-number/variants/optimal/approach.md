## General
**Reject decimal forms that cannot mirror**

A negative number cannot be a decimal palindrome because its minus sign has no matching symbol at the end. A nonzero number ending in zero also cannot be palindromic: its representation would need to begin with zero, which standard integer notation never does.

**Reverse only the lower half**

Repeatedly remove the last digit from `x` and append it to `reversed_half`. Stop once `reversed_half` is greater than or equal to the remaining prefix. Reversing only half avoids any possibility of overflowing a 32-bit integer, because the constructed half has at most five digits for a 32-bit input.

For an even number of digits, the halves must be equal. For an odd number of digits, the reversed half contains the middle digit; discard it with integer division by ten before comparing.

**Know when the two halves have met**

After each iteration, `reversed_half` is the reversal of exactly the suffix digits removed from the original value, while `x` is the untouched prefix. Continue while `x > reversed_half`. Once that condition is false, at least half of the digits have moved; continuing farther would merely reverse digits that have already found their partners.

For an even digit count, the two halves must be equal. For an odd digit count, `reversed_half` contains the middle digit as its final digit. The middle digit has no partner and can be discarded with integer division by ten, giving the single final test:

```text
x == reversed_half or x == reversed_half // 10
```

**Follow even and odd examples**

For `1221`, first move digit 1 to obtain prefix `122` and reversed half `1`. Then move digit 2 to obtain prefix `12` and reversed half `12`. The equal halves prove the number is palindromic.

For `121`, the process ends with prefix `1` and reversed half `12`; dropping the middle digit gives `12 // 10 = 1`, which matches the prefix.

**Why meeting halves decide the whole number**

The preliminary checks remove precisely the decimal forms that cannot mirror: a one-sided minus sign and a nonzero trailing zero with no possible leading counterpart. During the loop, `reversed_half` is the removed suffix read in reverse, while `x` remains the untouched prefix.

When the reversed suffix catches the prefix, every digit has either moved into the opposite half or is the single unpaired middle digit. Equal halves therefore mean every mirrored pair agrees in the even case; dividing `reversed_half` by ten discards exactly that middle digit in the odd case. If neither equality holds, at least one mirrored pair differs, so the complete number is not palindromic.

## Complexity detail
Each iteration removes one digit from the remaining prefix, and only half of the decimal digits are processed. This is $O(\log x)$ time for positive `x`. The algorithm stores two integer halves and a temporary digit, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **String reversal:** concise, but allocates a decimal representation and does not satisfy the arithmetic-only variant.
- **Reverse the complete integer:** remains $O(\log x)$ but may overflow fixed-width storage.
- **Compare outer digits using powers of ten:** uses constant space but requires careful divisor updates and more boundary handling.
- `0` is palindromic even though it ends in zero; the trailing-zero rejection must therefore exclude zero itself.
- All negative numbers fail because the minus sign occurs only at the left edge of their decimal representation.
