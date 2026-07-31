## General

Reject `word` immediately when its length is below three. Otherwise, scan its characters once while maintaining two Boolean facts: whether a vowel has appeared and whether a consonant has appeared.

For each character, first determine whether it lies in one of the explicit ASCII ranges for lowercase letters, uppercase letters, or digits. If it lies in none of them, the word contains a forbidden character and can be rejected immediately. A digit requires no further state change. An English letter belongs either to the ten-character uppercase-and-lowercase vowel set or to the complementary consonant set, so update the corresponding Boolean.

After the scan, the length and character-set conditions are known to hold. Returning the conjunction of the two Boolean flags then accepts exactly the words containing at least one vowel and at least one consonant. These categories are exhaustive for an allowed English letter, so no qualifying character can be missed or counted in both groups.

## Complexity detail

With $n$ characters, the scan takes $O(n)$ time. The vowel set has a fixed ten-character size, and the algorithm stores only two Boolean flags plus loop-local values, so auxiliary space is $O(1)$.

The legal constraint $n \le 20$ is too tightly bounded for honest runtime scaling. The package therefore uses a `bounded_domain` certificate proving at most 20 character classifications and backs it with exhaustive category-state and boundary-character regression checks.

## Alternatives and edge cases

- **Regular expression:** A single expression can combine the allowed alphabet and lookaheads for both letter classes, but it obscures the four independent conditions and is easier to misconfigure around case handling.
- **Multiple full scans:** Separate `all(...)` and `any(...)` passes remain linear, but they reread the short word and distribute the validity logic across several predicates.
- **Generic Unicode predicates:** Methods such as `isalnum()` accept many non-ASCII letters and digits. The source alphabet is constrained, but explicit English-letter and decimal-digit ranges state the contract precisely.
- **Digits only:** Digits are allowed and count toward the minimum length, but they are neither vowels nor consonants.
- **Length below three:** Even a two-character string containing a vowel and consonant is invalid.
- **Forbidden character:** Any occurrence of `'@'`, `'#'`, or `'$'` makes the entire word invalid, regardless of the other characters.
- **Letter case:** Uppercase vowels are vowels, and every uppercase English letter outside that set is a consonant.
