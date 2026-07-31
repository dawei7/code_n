## Description

Apply either of these operations to every character of a string at once:

- **Right shift:** Replace each letter with its next English letter, wrapping `z` to `a`. For example, `"abc"` becomes `"bcd"`, and `"xyz"` becomes `"yza"`.
- **Left shift:** Replace each letter with its preceding English letter, wrapping `a` to `z`. Thus `"bcd"` becomes `"abc"`, and `"yza"` becomes `"xyz"`.

Repeating shifts in either direction produces an endless shifting sequence. For example:

`... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> ...`

Likewise, `... <-> "zab" <-> "abc" <-> ...` belongs to the same sequence.

Given the array `strings`, group entries that belong to the same shifting sequence. The groups and their members may be returned in any order.
