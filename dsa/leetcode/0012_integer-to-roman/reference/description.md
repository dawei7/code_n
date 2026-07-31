## Description

Roman numerals use seven symbols:

| Symbol | Value |
|:---:|---:|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

Convert an integer to its Roman numeral by processing decimal place values from highest to lowest and appending their representations.

- When a place value does not begin with 4 or 9, repeatedly append the greatest symbol value that can be subtracted, subtract it, and continue with the remainder.
- A place value beginning with 4 or 9 uses subtraction: a smaller power-of-ten symbol precedes a larger symbol. The only subtractive forms are `IV` (4), `IX` (9), `XL` (40), `XC` (90), `CD` (400), and `CM` (900).
- The power-of-ten symbols `I`, `X`, `C`, and `M` may appear consecutively at most three times. The five-based symbols `V`, `L`, and `D` cannot repeat; a fourth occurrence is replaced by the corresponding subtractive form.

Return the resulting Roman-numeral string.
