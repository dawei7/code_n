## General

Only five character types can move, so the ordering problem is smaller than sorting every vowel occurrence. Scan `s` once. For each vowel type, record its total frequency and the index where it first appears.

Order the vowel types that actually occur by the pair consisting of negative frequency and first position. The negative frequency puts larger counts first, and the first position resolves exactly the required ties. Because this list contains at most five types, its sorting cost is constant with respect to the input length. Expand the ordered types into one vowel stream by repeating each type according to its frequency.

Convert `s` to a mutable character list and scan it in original order. Leave consonant positions untouched; at each vowel position, consume the next character from the ordered stream. The stream contains exactly one character for every original vowel occurrence, so every vowel slot receives a replacement. Its construction follows the required frequency and tie keys, while the replacement scan changes no other index, proving that the returned string satisfies both the ordering and position rules.

## Complexity detail

Counting, expanding the vowel stream, and rebuilding the result each take $O(n)$ time. Sorting at most five vowel types takes $O(1)$ time, so the total is $O(n)$. The mutable result and ordered vowel stream use $O(n)$ extra space; the frequency and first-position maps contain at most five entries.

## Alternatives and edge cases

- **Sort every vowel occurrence:** Assigning each occurrence the key `(-frequency, first_position)` is correct but sorting up to $n$ characters takes $O(n \log n)$ time instead of exploiting the fixed five-type alphabet.
- **Five explicit buckets:** The five vowel types can be selected repeatedly by the same ordering key and emitted by count, preserving $O(n)$ time without a general sort but with more manual control flow.
- **No vowels:** The ordered stream is empty, every position is a consonant position, and the input is returned unchanged.
- **Equal frequencies:** Ties compare first-occurrence indices, not alphabetical order and not the most recent occurrence.
- **One occurring vowel type:** Replacing its slots with identical copies leaves the original string unchanged.
- **Consonant positions:** Consonants are never consumed from or inserted into the vowel stream, so their indices cannot move.
