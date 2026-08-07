## Function Contract

**Inputs**

- `s`: a nonempty string containing lowercase English letters.
- `shift`: a nonempty matrix whose row `shift[i]` is `[direction_i, amount_i]`.

For each operation, `direction_i = 0` means left and `direction_i = 1` means right. `amount_i` is the requested number of cyclic positions and may be zero.

**Return value**

Return the string obtained after applying all rows of `shift`. Every operation acts on the result of the preceding operation, and every shift preserves the string's length and character multiplicities.
