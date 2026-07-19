## General
**Build from the center outward**

The empty center seeds even lengths; `0`, `1`, and `8` seed odd lengths. Wrap every shorter valid center with one of `00`, `11`, `69`, `88`, or `96`.

**Leading zero is forbidden only at the final wrapper**

`00` is valid inside a numeral but invalid as the outermost pair when the final length exceeds one.

Every intermediate string is strobogrammatic and has the required parity. Wrapping with a valid rotating pair preserves that property.

**Removing the outer pair reverses the construction uniquely**

Every valid length-`n` numeral has one allowed outer rotating pair. Removing that pair leaves a valid length-`n-2` center, so repeated removal reaches the appropriate empty or one-digit seed. The recursive construction can therefore reproduce every answer. Conversely, each allowed wrapper preserves rotational symmetry, and excluding only the outermost `00` pair removes exactly the multi-digit strings with a leading zero.

## Complexity detail
The output family grows exponentially with roughly five choices per digit pair; constructing each length-$n$ string gives output-sensitive $O(n \cdot 5^{n/2})$ time and result space.

## Alternatives and edge cases
- **Enumerate all $10^{n}$ numerals then test:** explores overwhelmingly invalid candidates.
- One digit has exactly three answers; internal zeros remain allowed.
