## Description

Implement `myAtoi`, which converts a string `s` into a signed 32-bit integer by applying these rules in order:

1. **Whitespace:** Skip every leading space character.
2. **Signedness:** If the next character is `-` or `+`, consume it and use the corresponding sign. Otherwise, keep a positive sign.
3. **Conversion:** Ignore leading zeroes in the numeric value, then consume consecutive decimal digits until the string ends or the next character is not a digit. If no digit is consumed, the result is `0`.
4. **Range adjustment:** Clamp a value below $-2^{31}$ to $-2^{31}$ and a value above $2^{31}-1$ to $2^{31}-1$.
5. Return the resulting integer.

Characters after the first non-digit encountered during conversion do not affect the result.
