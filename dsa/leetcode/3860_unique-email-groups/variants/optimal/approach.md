## General

**Normalize each part according to its own rules**

An email address has two logically separate components:

- the local name before `'@'`; and
- the domain name after `'@'`.

Two addresses belong to one group only when both normalized components match. The normalization function must therefore produce a stable representation of the ordered pair

$$
(\text{normalized local},\text{normalized domain}).
$$

The source begins with `local, domain = email.split("@")`. The contract guarantees exactly one `'@'`, so unpacking produces exactly two strings.

For the local part, the source applies the rules in a compact chain:

`local.split("+")[0].replace(".", "").lower()`.

Splitting on plus and taking element zero retains everything before the first plus. If no plus exists, the split produces a one-element list containing the whole local name. Any later plus signs and all characters after the first are ignored. Dots are then removed from the retained prefix, and the remaining letters are converted to lowercase.

The order of plus truncation and dot removal does not change the intended local result: dots after the first plus are ignored with the entire suffix, while dots before it are removed. Lowercasing could also occur before these two character-structure operations because input is restricted to English letters, digits, dots, and plus signs.

For the domain, the only normalization rule is case conversion, so `domain.lower()` is correct. Dots inside the domain remain meaningful. For example, `"leetcode.com"` and `"lee.tcode.com"` are different domains and must not be merged merely because removing their dots would make them look similar.

**Use a set to count normalized identities**

After normalization, inserting one canonical identity into a set for each email is the right high-level strategy. A set retains one copy of each equal key, regardless of how many original addresses normalize to it. The number of set entries is then the number of groups.

For the first example, the first two locals both normalize to `"testemail"` and both domains normalize to `"leetcode.com"`. They should insert the same identity. The third local is again `"testemail"`, but its domain remains `"lee.tcode.com"`, so it should insert a second identity.

Case conversion applies on both sides. Thus `"A@B.com"` and `"a@b.com"` both normalize to the pair `("a","b.com")`. By contrast, `"a.b@b.com"` normalizes to `("ab","b.com")`, which differs in the local component.

**The exact protected source loses the component boundary**

The source does not insert the pair into the set. It constructs

`normalized = local + domain`

with no separator and inserts that concatenated string. This encoding is not one-to-one: when reading the key back, there is no way to know where the local name ends and the domain begins.

For a concrete valid counterexample, consider:

- `"ab@c.com"`, which normalizes to the pair `("ab","c.com")`; and
- `"a@bc.com"`, which normalizes to the pair `("a","bc.com")`.

These pairs are different in both their component boundary and their intended email identity, so the correct answer for the two-address array is two. The protected source concatenates both pairs into `"abc.com"` and stores only one set entry. It therefore returns one.

This is a genuine correctness defect, not merely a stylistic concern. The reference contract says equality must hold for both normalized components. Plain concatenation preserves that implication in one direction—equal pairs always produce equal concatenations—but the reverse implication is false. The source may merge different groups and undercount. It cannot create two keys for one normalized pair, so this defect can undercount but not overcount.

No correctness argument can establish the source for every valid input while this non-injective key remains. The surrounding normalization steps and set strategy are sound; only the representation of the component pair is defective.

**The collision-safe Optimal representation**

The smallest conceptual repair is to insert a tuple:

`st.add((local, domain))`.

Python tuples preserve both values and their boundary. Two tuples are equal exactly when their first components are equal and their second components are equal, matching the grouping definition directly.

Another safe representation is `local + "@" + domain`. The contract guarantees that neither component contains `'@'` because the original address contains exactly one separator, so the delimiter cannot be confused with component content. Retaining the separator reconstructs a conventional normalized email address and prevents the demonstrated collision.

With either safe key, the invariant after processing a prefix of `emails` is straightforward: the set contains exactly one key for every normalized local-domain pair seen in that prefix. Normalizing the next address and inserting its pair either leaves an existing group unchanged or adds one new group. At the end, set size is the required answer.

**Exact source behavior versus intended algorithm**

The protected implementation correctly:

- separates the original address at its single `'@'`;
- ignores the local suffix starting with the first plus;
- removes every dot from the retained local prefix;
- lowercases both local and domain;
- preserves domain dots; and
- deduplicates constructed keys with a set.

It fails only at the final key construction. An expert explanation must preserve that distinction: the intended Optimal approach is linear-time canonicalization plus hashing, while the exact source is not fully correct until it encodes the ordered pair without ambiguity. This document reports the defect rather than silently claiming acceptance-level correctness.

## Complexity detail

Let

$$
S=\sum_{e\in\texttt{emails}}\lvert e\rvert
$$

be the total number of input characters. Splitting, replacing dots, lowercasing, concatenating, and hashing each normalized string all take time proportional to the relevant email length. Across the array, expected total time is `O(S)`. Set insertion is expected `O(1)` per key after its hash is computed. The collision-safe tuple or delimited-key correction has the same `O(S)` expected time.

The set may retain normalized content whose total size is `O(S)`. Temporary split strings and normalized strings are also bounded by the current email length, so peak additional storage remains `O(S)`. The source and corrected representation therefore match the manifest's `O(S)` time and `O(S)` space bounds, even though the source's correctness does not match its “canonical key” summary.

Python's `str.lower` is safe for the promised English-letter alphabet. Hash-table complexity is expected rather than worst-case deterministic; pathological collision analysis can produce worse theoretical bounds, but customary Python set analysis uses expected constant-time operations.

## Alternatives and edge cases

- **Tuple key:** Store `(local,domain)` directly. This is the clearest collision-safe representation because its equality semantics exactly mirror the problem definition.
- **Delimited normalized address:** Store `local + "@" + domain`. It is safe because `'@'` cannot occur inside either component under the valid-address contract.
- **Length-prefixed concatenation:** Encode the local length before the two strings. This is collision-safe but unnecessarily complicated when tuple keys or the existing separator are available.
- **Sort normalized keys:** Normalize every address, sort the safe keys, and count adjacent changes. This is deterministic but costs `O(E\log E)` key comparisons for `E` emails instead of expected linear hashing.
- **Nested mapping by local then domain:** A dictionary from normalized local names to sets of normalized domains also preserves boundaries, but a set of pairs is simpler.
- **Unseparated concatenation:** The exact source's `local + domain` is unsafe. Different component pairs can share the same character sequence, as `"ab@c.com"` and `"a@bc.com"` demonstrate.
- **Multiple plus signs:** Everything beginning with the first plus is ignored. Taking index zero after `split("+")` produces the intended prefix, although `split("+",1)` would avoid creating unnecessary later pieces.
- **Dots after the first plus:** They are in the ignored suffix and have no effect. Dots before the plus are removed.
- **Dots in the domain:** They must remain. Dot-removal is a local-name rule only.
- **Case differences:** Both components are lowercased, so case alone never creates a new group.
- **Digits:** They are preserved in both components; `lower` affects only letters.
- **Already normalized email:** It maps to the same local-domain pair and inserts normally.
- **Normalized local possibly unusual:** The contract guarantees a nonempty original local name that does not begin with plus, but independent of whether normalization leaves a short or dot-only-derived prefix, tuple encoding still preserves the boundary safely.
- **Source status:** The protected solution should not be represented as fully correct for the stated domain until its key construction is repaired. The complexity remains optimal, but optimal complexity does not compensate for a collision bug.
