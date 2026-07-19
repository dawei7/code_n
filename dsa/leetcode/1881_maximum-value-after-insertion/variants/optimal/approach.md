## General
**Positive numbers favor a larger earliest digit**

For a positive `n`, scan from left to right and insert `x` immediately before the first digit smaller than `x`. Earlier digits have greater place value, so this is the earliest position where insertion improves the digit sequence. Passing a digit at least as large as `x` preserves the better prefix; inserting before it cannot improve the result.

**Negative numbers reverse the comparison**

The greatest negative integer has the smallest absolute magnitude. Skip the minus sign, then insert `x` before the first digit larger than `x`. This creates the lexicographically smallest magnitude at the first position where the inserted digit can improve it. Digits no larger than `x` should remain earlier.

**Append when no strict comparison is found**

If the scan reaches the end, every existing digit is at least `x` for a positive number or at most `x` for a negative number. Appending changes the least significant available position and is therefore optimal. Equal digits can be crossed without changing the resulting digit sequence.

## Complexity detail
Let $N$ be the length of `n`, including a possible sign. The scan examines at most $N$ characters, and constructing the returned string copies $O(N)$ characters, so time is $O(N)$. The immutable output string and the slices used to form it occupy $O(N)$ space.

## Alternatives and edge cases
- **Try every insertion position:** Comparing all $O(N)$ candidate strings is correct but requires $O(N^2)$ time.
- **Convert candidates to integers:** It is unnecessary and unsuitable for a representation of up to $10^5$ characters.
- **Negative sign:** Begin scanning at index `1`; `x` cannot be placed before `'-'`.
- **Equal digits:** Inserting before or after an equal run produces the same representation.
- **Insertion at the front:** For a positive number, this occurs when its first digit is smaller than `x`.
- **Insertion at the end:** It occurs when no digit satisfies the sign-specific strict comparison.
- **Single digit:** The same comparison determines whether `x` precedes or follows it.
