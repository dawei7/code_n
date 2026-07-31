## General

Count each character's occurrences across the complete string. For any allowed pair, the difference has the form `odd_count - even_count`. The two choices are independent: making the first term as large as possible and the subtracted term as small as possible can only increase the result.

Therefore, select the maximum frequency among characters with odd counts and the minimum frequency among characters with positive even counts. Their difference is achievable by choosing the corresponding two characters. No other pair can do better because its odd term is no larger and its even term is no smaller.

## Complexity detail

Let $n$ be the length of `s`. Counting the characters takes $O(n)$ time, and examining the resulting frequencies takes at most 26 additional steps. Because the lowercase alphabet has fixed size, the frequency map uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Compare every odd/even pair:** At most 26 letters make this workable, but extrema identify the answer directly.
- **Use the largest even frequency:** The even count is subtracted, so the minimum positive even frequency maximizes the difference.
- **Include absent letters:** A zero count does not belong to a character present in the string and must not be chosen as the even frequency.
- **Negative answer:** The maximum difference can still be negative when every odd frequency is smaller than every even frequency.
- **Several equal extrema:** The identity of the chosen characters is irrelevant because only their frequency difference is returned.
