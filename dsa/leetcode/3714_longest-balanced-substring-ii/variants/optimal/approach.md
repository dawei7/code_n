## General

With only three allowed characters, every balanced substring belongs to one of three exhaustive types: it contains exactly one, exactly two, or all three distinct characters. Find the best interval of each type in linear scans.

**One distinct character.** Any run of identical characters is balanced. Track the longest run while scanning `s` once.

**Exactly two distinct characters.** Choose the character that must be absent. Its occurrences divide `s` into independent segments containing only the other two letters. Inside each segment, treat one allowed letter as `+1` and the other as `-1`. Two equal prefix differences delimit a substring with equal counts. Store the earliest position of each difference, resetting the map after every excluded character. Repeat for each of the three possible excluded letters.

**All three distinct characters.** Let the prefix counts be $A$, $B$, and $C$. A substring adds equally many of all three letters exactly when both differences $(A-B, A-C)$ are unchanged across its endpoints. Store the earliest index of each difference pair; a repeated state gives a balanced three-character substring, and the earliest occurrence makes it as long as possible.

These three scans cover every possible set of distinct characters, and each prefix-state equality is equivalent to equal counts for its type. The maximum length found across them is therefore the longest balanced substring.

## Complexity detail

Let $n=\lvert s\rvert$. A constant number of passes processes each character in $O(1)$ expected time, giving $O(n)$ total time. Prefix-difference maps can hold $O(n)$ states, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Enumerate both endpoints:** Extending every left endpoint with updated frequencies takes $O(n^2)$ time and is too slow for $n=10^5$.
- **Track only the three-character state:** That misses balanced substrings containing one or two distinct characters because absent-letter counts are not required to match.
- **Track only pair differences globally:** A two-character candidate may not cross the excluded third character, so its map must reset at each such occurrence.
- **One-character run:** Repetition of a single letter is balanced even though the other two frequencies are zero.
- **Two-character segment:** Equal prefix differences guarantee both allowed counts increase equally; a non-empty match therefore contains both.
- **All three characters:** Repeating `(A - B, A - C)` makes all three count increments equal.
- **Tied locations:** Only the maximum length is returned, so no substring position needs to be retained.
