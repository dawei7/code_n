## General
**Pair only the outermost unprocessed vowels**

The first vowel in the result must be the last vowel from the input, the second must be the second-to-last, and so on. Two pointers can identify those pairs without collecting vowel indices separately.

Convert the immutable string into a mutable character list. Place `left` at the start and `right` at the end. Advance `left` until it reaches a vowel, and move `right` backward until it reaches a vowel. If the pointers have not crossed, swap those two vowels and continue inward.

**Why skipped positions remain correct**

At every swap, all positions outside `[left, right]` are final: non-vowels were skipped without being moved, while any encountered outer vowels were paired with their corresponding vowels from the opposite end. The remaining interval contains exactly the unpaired middle portion of the original vowel sequence. Swapping its outer vowels therefore extends the reversed prefix and suffix correctly. When the pointers meet or cross, every vowel pair has been processed and every non-vowel stayed at its original position.

**Trace the vowel sequence itself**

For `"IceCreAm"`, the vowel sequence is `I, e, e, A`. The outer swap exchanges `I` and `A`; the inner two `e` values exchange without changing their visible characters, producing `"AceCreIm"`.

## Complexity detail
Each pointer moves across the string at most once, so scanning and swapping take $O(n)$ time. Python strings are immutable, so the mutable character list and returned string require $O(n)$ space. The pointer state itself is $O(1)$.

## Alternatives and edge cases
- **Collect vowels in a stack:** also takes $O(n)$ time but stores the vowel sequence separately and uses $O(n)$ auxiliary space.
- **Rebuild after every swap:** can take $O(n^2)$ because immutable-string reconstruction repeatedly copies the whole string.
- The vowel test must include `a`, `e`, `i`, `o`, and `u` in both cases.
- A string with no vowels is unchanged; one vowel has no partner and remains in place.
- Equal vowels may be exchanged internally without changing the visible output.
