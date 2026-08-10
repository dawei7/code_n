## General

**Version II adds an ordering condition.** A letter is special only if both cases occur and every lowercase occurrence lies before the first uppercase occurrence. It is not enough to know that lowercase and uppercase are present. The decisive positions are:

- the last occurrence of the lowercase form;
- the first occurrence of the uppercase form.

All lowercase copies precede all uppercase copies exactly when:

$$
\text{lastLower}(c)<\text{firstUpper}(c).
$$

If that strict inequality holds, even the latest lowercase is before the earliest uppercase, so every other lowercase is also before every uppercase. If it fails, at least one lowercase appears at or after the first uppercase and the letter is not special.

**Record first and last occurrence of every case-sensitive character.** The source builds two dictionaries, `first` and `last`, while scanning `word` with indices.

When character `c` has not been seen before, `first[c] = i` records its earliest position. Every occurrence executes `last[c] = i`, so that entry ends as its latest position.

Lowercase `a` and uppercase `A` are different dictionary keys. This case-sensitive separation is essential because the test compares information from the two forms.

**Pair the alphabet cases.** `zip(ascii_lowercase, ascii_uppercase)` produces `(a,A)` through `(z,Z)`. For one pair, the generator checks:

`a in last and b in first and last[a] < first[b]`.

The first membership condition proves at least one lowercase occurrence exists. The second proves an uppercase occurrence exists. The inequality applies the complete ordering rule.

Using `last` for lowercase existence and `first` for uppercase existence is enough because either dictionary actually contains every seen character. The selected dictionary also already holds the needed extreme position.

**Sum Boolean results.** Each true expression contributes one to Python's `sum`, and each false expression contributes zero. Since every English letter is paired exactly once, the returned total is the number of special letters.

**A trace for `"aaAbcBC"`.** Lowercase a ends at index one, and uppercase A first appears at index two, so a qualifies. Lowercase b ends at index three and uppercase B first appears at five. Lowercase c ends at four and uppercase C first appears at six. Three pairs satisfy the inequality.

For `"AbBCab"`, uppercase A appears before lowercase a, so `last["a"] < first["A"]` fails. Uppercase B appears before a later lowercase b, so b fails as well. Other letters lack both cases, giving zero.

**Why strict inequality is required.** A lowercase and uppercase character cannot occupy the same string index, so equality cannot occur for different case forms. Still, `<` directly states “before.” Reversing it or using only first occurrences would solve a different condition.

**Why first lowercase is insufficient.** Consider `"aAa"`. The first lowercase a precedes uppercase A, but a later lowercase occurs afterward. The letter is not special. Recording `last["a"]` exposes the violation.

**Why last uppercase is unnecessary.** Once the last lowercase lies before the first uppercase, every uppercase automatically lies at or after that first uppercase and therefore after all lowercase copies. Later uppercase positions add no new constraint.

**A correctness proof.** For each letter, the generator returns true only when both cases exist and the latest lowercase index is smaller than the earliest uppercase index. That condition implies every lowercase precedes every uppercase, so every counted letter is special.

Conversely, if a letter is special, both forms exist by definition. Its latest lowercase must occur before its first uppercase, so all three generator conditions are true and it is counted. The test is both necessary and sufficient.

**Manifest mechanism mismatch.** The local manifest describes a four-state automaton maintained during one scan. The exact `solution.py` instead stores first and last positions in dictionaries and performs a 26-pair check afterward. Both are linear and constant-space under the fixed alphabet, but the implementation behavior is position-map based.

## Complexity detail

The occurrence scan takes $O(n)$ expected time using dictionary operations. The final generator performs exactly 26 constant-time checks. Total expected time is $O(n+26)=O(n)$.

At most 52 distinct case-sensitive English characters can enter each dictionary. Fixed-alphabet auxiliary space is $O(52)=O(1)$ relative to $n$. In a generalized alphabet, it would be linear in the number of distinct symbols.

The generator and `zip` are lazy. The dictionaries dominate storage.

## Alternatives and edge cases

- **Four-state automaton:** Track unseen, lowercase-only, valid uppercase-after-lowercase, and invalid ordering per letter. This matches the manifest.
- **Two 26-element position arrays:** Store last lowercase and first uppercase indices, avoiding hash maps.
- **Set-only solution from version I:** Incorrect because it forgets occurrence order.
- **Only lowercase form:** Fails uppercase membership.
- **Only uppercase form:** Fails lowercase membership.
- **Uppercase before lowercase:** The position inequality fails.
- **Lowercase after an uppercase:** Latest lowercase exposes the violation even if an earlier lowercase was validly placed.
- **Several lowercase then several uppercase:** Qualifies.
- **Interleaved cases:** Fails whenever any lowercase occurs after the first uppercase.
- **One occurrence of each:** Their index order alone decides.
- **Strict case sensitivity:** Lowercase and uppercase are different keys.
- **First uppercase:** It is the earliest boundary every lowercase must precede.
- **Last lowercase:** It is the strongest lowercase boundary to test.
- **No input mutation:** The method only records indices.
- **Source/manifest mismatch:** Exact source uses two occurrence dictionaries, not an automaton.
