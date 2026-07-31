## General

**Mark every disagreement with XOR**

At a bit position, XOR produces `1` exactly when the corresponding bits of `start` and `goal` differ. Thus `start ^ goal` is a mask containing precisely the positions that must change.

Each marked position requires at least one flip because no operation at another position can alter it. Flipping every marked position once is sufficient, while flipping an unmarked position would create a new mismatch. The number of set bits in the XOR mask is therefore both a lower bound and an achievable answer.

Use the integer population-count operation to count those set bits directly. XOR naturally handles displayed digits and implicit leading zeros alike.

## Complexity detail

The legal values occupy at most 30 binary positions and fit in one bounded machine-scale integer. XOR and population count therefore take $O(1)$ time and $O(1)$ space under the problem's fixed domain.

The bounded-domain complexity certificate records why runtime scaling cannot honestly establish another class within only 30 legal bit positions.

## Alternatives and edge cases

- **Compare padded binary strings:** Aligning and scanning both representations is correct but creates temporary strings.
- **Shift one bit at a time:** Repeatedly testing the XOR mask is also correct, though the built-in population count expresses the operation directly.
- **Breadth-first flip search:** Exploring intermediate integers is unnecessary because bit positions are independent.
- **Equal values:** Their XOR is zero, so no flips are required.
- **One value is zero:** Every set bit in the other value must be flipped.
- **Leading zeros:** XOR includes a high bit present in only one value without requiring explicit padding.
