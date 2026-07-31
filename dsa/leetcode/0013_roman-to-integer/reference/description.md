## Description

Roman numerals use these seven symbols:

| Symbol | Value |
|:---:|---:|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

Symbols normally appear from larger to smaller values and are added. Thus 2 is `II`, 12 is `XII`, and 27 is `XXVII` (`XX + V + II`).

A smaller symbol before a larger one instead indicates subtraction. Only six such forms are valid:

- `I` may precede `V` or `X`, producing 4 or 9.
- `X` may precede `L` or `C`, producing 40 or 90.
- `C` may precede `D` or `M`, producing 400 or 900.

Given a valid Roman numeral `s`, return its integer value.
