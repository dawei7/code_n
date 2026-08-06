## Description

Given a non-negative integer `num`, return its encoding string.

The encoding is produced by a secret integer-to-string function. Deduce that function from the following source mappings:

Treat every displayed string literally, including an empty result or zeros at the beginning. The table supplies the function's initial values; infer one consistent rule from that pattern and apply the same rule to inputs beyond the rows shown. The returned value must be the corresponding binary-character string, not an integer with visually similar digits.

| $n$ | $f(n)$ |
|---:|:---|
| `0` | `""` |
| `1` | `"0"` |
| `2` | `"1"` |
| `3` | `"00"` |
| `4` | `"01"` |
| `5` | `"10"` |
| `6` | `"11"` |
| `7` | `"000"` |
