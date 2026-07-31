## Examples

**Example 1**

- Input: `s = "101", t = "011"`
- Output: `"110"`
- Explanation: One optimal arrangement leaves `t` as `"011"`. Position-wise XOR then gives `"101" XOR "011" = "110"`, and no other arrangement yields a larger value.

**Example 2**

- Input: `s = "0110", t = "1110"`
- Output: `"1101"`
- Explanation: Rearranging `t` to `"1011"` produces `"0110" XOR "1011" = "1101"`. This is the greatest XOR string obtainable from the available bits.

**Example 3**

- Input: `s = "0101", t = "1001"`
- Output: `"1111"`
- Explanation: The arrangement `"1010"` is the bitwise complement of `s`. Consequently, `"0101" XOR "1010" = "1111"`, which is the maximum possible length-four binary value.
