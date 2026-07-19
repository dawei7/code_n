## General
**Characterize a row's successful flip patterns:** To turn a row into all zeros, flip exactly the columns where that row contains `1`. To turn it into all ones, flip exactly the columns where it contains `0`. Those two patterns are bitwise complements.

**Normalize complements to one key:** XOR every value in a row with its first value. A row beginning with zero remains unchanged, while a row beginning with one is complemented. Thus identical rows and complementary rows produce the same normalized tuple, and no other pair does.

**Count compatible rows:** Store the frequency of every normalized tuple. All rows sharing a key can be made uniform by one column-flip set, some becoming all zeros and the complementary originals becoming all ones. Return the largest frequency.

If two rows share a normalized key, their original bits agree in every column when their first bits agree and differ in every column otherwise, so one flip pattern makes both uniform. Conversely, rows simultaneously made uniform must each equal the flip pattern or its complement before flipping, making them identical or complementary and therefore giving them the same key.

## Complexity detail
Normalizing each of $M$ rows reads all $N$ entries, for $O(MN)$ time. Up to $M$ tuple keys of length $N$ are stored, requiring $O(MN)$ auxiliary space in the worst case.

## Alternatives and edge cases
- **Compare every pair of rows:** Group rows by testing whether each pair is identical or complementary. It is correct but costs $O(M^2N)$ time.
- **Enumerate column subsets:** Trying all $2^N$ flip patterns is exponential and repeats equivalent work.
- **Count only identical rows:** It misses complementary rows, which can become uniform under the same flips with opposite final values.
- **One column:** Every row is already uniform, so the answer is $M$.
- **All rows identical:** Their normalized keys match and all $M$ qualify together.
- **All rows complementary pairs:** Both orientations belong to the same key.
- **Uniform rows of zeros and ones:** They normalize to the same all-zero key and require no flips to qualify together.
- **Duplicate rows:** Every occurrence is a separate row and contributes to the frequency.
