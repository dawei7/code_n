## Examples

**Example 1**

- Input: `color = "#09f166"`
- Output: `"#11ee66"`
- Explanation: The three squared channel contributions are `-(0x09 - 0x11)^2 = -64`, `-(0xf1 - 0xee)^2 = -9`, and `-(0x66 - 0x66)^2 = 0`. Their total is `-64 - 9 - 0 = -73`, which is the highest similarity attainable by any shorthand color.

**Example 2**

- Input: `color = "#4e3fe1"`
- Output: `"#5544dd"`
