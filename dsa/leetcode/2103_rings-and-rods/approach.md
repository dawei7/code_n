## General

**Represent three Boolean color facts with three bits**

For each rod, the algorithm needs to remember only whether red, green, and blue have appeared. Counts and ring order do not matter.

The mapping `d` assigns one distinct bit to each color:

- red maps to binary `001`, value 1;
- green maps to binary `010`, value 2;
- blue maps to binary `100`, value 4.

`mask` contains ten integers, one per rod label. A set bit means that color has appeared on that rod.

When all three bits are set, the value is

$$
1\mathbin{\vert}2\mathbin{\vert}4=7,
$$

whose binary form is `111`.

**Read the string in complete pairs**

The string alternates color and rod characters. The loop uses

`range(0, len(rings), 2)`,

so `i` always points to a color. `rings[i + 1]` is the corresponding rod digit.

The rod character is converted with `int`, producing an index from 0 through 9. The update

`mask[j] |= d[c]`

sets the current color bit while preserving colors already seen on rod `j`.

Bitwise OR is exactly the desired accumulation operation: once a bit becomes 1, later rings never clear it.

**Why duplicate rings do not distort the state**

Placing another ring of a color already recorded performs OR with the same bit. For example, `101 | 001` remains `101`.

This idempotence is useful because the question asks whether each color is present, not how many rings of each color exist. No duplicate filtering or counters are necessary.

**Count complete masks**

After every pair is processed, `mask.count(7)` counts how many of the ten rod states equal binary `111`.

A rod with only red and blue has mask `101`, value 5, and is not counted. A rod with all three colors plus any number of duplicates still has exactly 7 and is counted once.

The fixed ten-element array includes rods that receive no rings; their mask stays zero.

**Trace the first example**

For `"B0B6G0R6R0R6G9"`:

- `B0` sets rod 0 to 4;
- `B6` sets rod 6 to 4;
- `G0` changes rod 0 to $4|2=6$;
- `R6` changes rod 6 to $4|1=5$;
- `R0` changes rod 0 to $6|1=7$;
- another `R6` leaves rod 6 at 5;
- `G9` sets rod 9 to 2.

Only rod 0 has state 7, so the result is one.

**Why the algorithm is correct**

For each processed pair, the mapped bit corresponds uniquely to its color and is ORed into exactly the indicated rod. By induction over the pairs, a rod's mask has a bit set if and only if at least one ring of that color has appeared on that rod.

Therefore, a mask equals 7 if and only if all red, green, and blue bits are present. Counting masks equal to 7 returns exactly the number of rods holding all three colors.

The input format guarantees an even length, valid color positions, and digit rod positions, so every loop iteration reads a complete valid pair.

The source does not change `rings`.

**Why constant space is possible**

There are always exactly ten rods and three colors. Neither dimension grows with the number of rings. The mask array and color mapping consequently occupy fixed space.

If rod labels were unbounded, a dictionary could replace the array and the space analysis would depend on the number of rods used. That is not needed here.

## Complexity detail

Let $n$ be the number of rings, so `len(rings) = 2n`.

The loop performs one constant-time update per ring, taking $O(n)$ time. Counting within the ten-element mask array is constant time, so total time remains $O(n)$.

The mask array has ten entries and the color map has three entries. Both are fixed-size, giving $O(1)$ auxiliary space.

The returned integer is constant-size with respect to the input.

## Alternatives and edge cases

- **Set per rod:** Ten sets of color characters are easy to understand and correct, but bit masks encode the same three Boolean facts more compactly.
- **Three Boolean arrays:** Separate red, green, and blue presence arrays also use constant space, but a single mask makes the final completeness test one equality.
- **Count rings per rod:** A rod can have three rings of the same color and still be incomplete. Counts alone do not prove color diversity.
- **Duplicate color on a rod:** OR is idempotent, so duplicates do not change the result.
- **One ring:** At most one bit is set, and the answer is zero.
- **All rings on one rod:** That rod is counted once if all three colors appear, regardless of duplicates.
- **All ten rods complete:** Every mask equals 7 and the result is ten.
- **Unused rods:** Their zero masks are not counted.
- **Rod label zero:** Converting character `"0"` produces valid array index 0.
- **Pair alignment:** Stepping by two is essential; iterating every character would confuse colors with rod digits.
- **Mask value seven:** It is not an arbitrary magic number; it is the OR of the three assigned single-bit values.
- **Input preservation:** The string is read-only.
