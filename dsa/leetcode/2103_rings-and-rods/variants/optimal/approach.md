## General
**Encoding color presence**

Assign one bit to each color, such as red `1`, green `2`, and blue `4`. Maintain one integer mask for each of the ten rods. Process `rings` two characters at a time, decode the rod digit, and combine the color bit into that rod's mask with bitwise OR.

Duplicate rings of a color leave the same bit set, so the masks record presence rather than frequency. A rod has all three colors exactly when its mask equals `1 | 2 | 4`, which is `7`.

**Counting completed rods**

After all pairs are processed, count masks equal to `7`. Every encoded ring contributes its color to exactly its named rod. Therefore each final mask contains precisely the set of colors present on that rod, and the equality test selects exactly the requested rods.

## Complexity detail
Processing the $n$ pairs takes $O(n)$ time, followed by a scan of exactly ten rods. The mask array always has length ten, so it uses $O(1)$ auxiliary space independent of $n$.

## Alternatives and edge cases
- **Set per rod:** Store color characters in ten sets and count sets of size three. This is equally linear and remains constant-space because both rods and colors have fixed domains.
- **Three boolean arrays:** Track red, green, and blue presence separately for each rod. This is explicit but uses more parallel state than a bitmask.
- **Repeated string searches:** For each encoded ring, search the input for the other colors on the same rod. This can be correct but costs $O(n^2)$ time.
- Multiple rings with the same color and rod do not affect the result after the first one.
- Colors may arrive in any order within the string.
- Several rods may independently contain all three colors, up to all ten rods.
- A rod with many rings still does not count if even one color is absent.
