## Description

Given an integer `n`, you must transform it into `0` using the following operations any number of times:

- Change the rightmost ($0^th$) bit in the binary representation of `n`.

- Change the $$i^{\text{th}}$$bit in the binary representation of `n` if the$(i-1)^th$bit is set to `1` and the$(i-2)^th$through$0^th$ bits are set to `0`.

Return *the minimum number of operations to transform *`n`* into *`0`*.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $n = 3$
- **Output:** `2`
- **Explanation:** The binary representation of 3 is "11".
"<u>1</u>1" -> "<u>0</u>1" with the 2^nd operation since the 0^th bit is 1.
"0<u>1</u>" -> "0<u>0</u>" with the 1^st operation.
#### Example 2

- **Input:** $n = 6$
- **Output:** `4`
- **Explanation:** The binary representation of 6 is "110".
"<u>1</u>10" -> "<u>0</u>10" with the 2^nd operation since the 1^st bit is 1 and 0^th through 0^th bits are 0.
"01<u>0</u>" -> "01<u>1</u>" with the 1^st operation.
"0<u>1</u>1" -> "0<u>0</u>1" with the 2^nd operation since the 0^th bit is 1.
"00<u>1</u>" -> "00<u>0</u>" with the 1^st operation.
### Constraints

- $0 \le n \le 10^{9}$