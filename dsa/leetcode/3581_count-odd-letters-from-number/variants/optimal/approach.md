## General

Only the parity of each letter's frequency matters. Represent the 26 lowercase letters by the bits of one integer. Whenever a letter is encountered, XOR its bit into the mask: an even occurrence turns the bit off, and an odd occurrence turns it on. After every digit word has been processed, the mask contains exactly the letters requested by the problem.

Extract decimal digits with remainder and integer division by `10`. This visits them from right to left rather than their written order, but frequency counts—and therefore parity—are independent of concatenation order. Look up the English word for each digit and toggle the bit for each of its letters. The population count of the final mask is the number of distinct letters with odd frequency.

The mask update is equivalent to incrementing a frequency modulo two. XOR is associative and commutative, so processing all digit words in reverse order produces the same final parity as explicitly concatenating them in original order. No string or frequency table is required.

## Complexity detail

Let $D$ be the number of decimal digits. Each digit name contains at most five letters, so the scan performs $O(D)=O(\log n)$ work and stores only the word table and one fixed-width bit mask, giving $O(1)$ auxiliary space.

The legal range limits $D$ to ten. Such tiny timing tiers cannot support a stable measured growth verdict, so the package uses a bounded-domain certificate. Its proof records at most ten digit iterations and fifty bit toggles, while boundary/property cases exercise the full range of relevant digit patterns.

## Alternatives and edge cases

- **Build the concatenated string:** Literal simulation is correct but allocates text that is unnecessary when only frequency parity is needed.
- **Frequency dictionary:** Counting exact occurrences also works in $O(D)$ time but stores more state than a parity bit mask.
- **Original digit order:** Order affects the constructed text but not letter counts, so arithmetic extraction from the least significant digit is safe.
- **Repeated digit words:** Two identical occurrences cancel every parity contribution from that word; an odd number leaves one copy's parity.
- **Repeated letters inside a word:** Letters such as the two `n` characters in `"nine"` cancel within that single word.
- **Zero digits:** Every zero inside the number contributes the letters of `"zero"`; only nonexistent leading zeros are omitted.
- **Upper boundary:** `1000000000` has ten digits and remains within the certificate's fixed work bound.
