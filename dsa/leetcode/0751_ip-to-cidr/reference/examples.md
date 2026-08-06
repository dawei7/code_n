## Examples

**Example 1**

- Input: `ip = "255.0.0.7", n = 10`
- Output: `["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]`
- Explanation: The requested addresses and their 32-bit representations are:

| Address | Binary representation |
|---|---|
| `255.0.0.7` | `11111111 00000000 00000000 00000111` |
| `255.0.0.8` | `11111111 00000000 00000000 00001000` |
| `255.0.0.9` | `11111111 00000000 00000000 00001001` |
| `255.0.0.10` | `11111111 00000000 00000000 00001010` |
| `255.0.0.11` | `11111111 00000000 00000000 00001011` |
| `255.0.0.12` | `11111111 00000000 00000000 00001100` |
| `255.0.0.13` | `11111111 00000000 00000000 00001101` |
| `255.0.0.14` | `11111111 00000000 00000000 00001110` |
| `255.0.0.15` | `11111111 00000000 00000000 00001111` |
| `255.0.0.16` | `11111111 00000000 00000000 00010000` |

The `/32` block at `255.0.0.7` covers the first address. `255.0.0.8/29` covers the middle eight addresses, whose binary form matches `11111111 00000000 00000000 00001xxx`. The final `/32` block covers `255.0.0.16`.

The source also warns that `255.0.0.0/28` is unusable because it includes addresses outside the requested interval. More precisely, that block covers `255.0.0.0` through `255.0.0.15`, so it both includes earlier addresses and fails to include `255.0.0.16`; either defect prevents exact coverage.

**Example 2**

- Input: `ip = "117.145.102.62", n = 8`
- Output: `["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]`
