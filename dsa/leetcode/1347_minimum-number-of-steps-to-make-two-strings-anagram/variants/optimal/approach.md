## General

Two strings are anagrams when every character has the same frequency in both strings. The positions do not matter. Since one operation replaces one character of `t`, the minimum number of operations is the number of character occurrences in `t` that exceed the quantities needed by `s`.

The checked-in solution counts this excess in a single pass over `t`.

**Treat the frequencies of `s` as available quotas**

`cnt = Counter(s)` records how many copies of each character the target anagram needs. Before processing `t`, `cnt[c]` is the full quota for character `c`.

For each character `c` in `t`, the solution executes `cnt[c] -= 1`:

- If the new count is zero or positive, this occurrence of `c` can be matched to one required occurrence in `s`.
- If the new count is negative, `t` has supplied more copies of `c` than `s` needs. This occurrence is surplus and must eventually be replaced.

`ans += cnt[c] < 0` uses the fact that Python Booleans behave as integers in addition: `True` contributes one and `False` contributes zero. Once a character’s quota has been exhausted, every additional occurrence makes its count more negative and adds one more required replacement.

For `s = "bab"`, the quotas are two `b` characters and one `a`. Processing `t = "aba"` consumes the `a` quota and one `b` quota. The final `a` drives its count below zero, so exactly one surplus occurrence is counted. Replacing that surplus `a` with the missing `b` makes the strings anagrams.

**Why counting surplus occurrences gives the minimum**

Every surplus occurrence in `t` has a character whose final frequency is greater than its frequency in `s`. Leaving that occurrence unchanged would keep the frequency too high, so at least one replacement is necessary for each surplus. This gives a lower bound of `ans` operations.

The strings have the same length. Therefore, the total amount by which some character frequencies in `t` exceed those in `s` is exactly equal to the total amount by which other frequencies fall short. Each replacement can take one surplus occurrence and change it into one missing character, reducing both totals by one. Repeating this pairing performs exactly `ans` replacements and reaches the target frequency multiset.

The lower bound is achievable, so it is the minimum.

Preloading all of `s` before scanning `t` is important. It means the algorithm knows the complete quota even if a matching occurrence conceptually appears at a later position. Because anagram matching ignores positions, no ordering decision is necessary.

The method does not need to construct the final anagram or decide which specific missing character replaces each surplus while counting. Equal lengths guarantee that a one-to-one pairing with deficits exists.

## Complexity detail

Let $n$ be the common string length.

Constructing `Counter(s)` takes $O(n)$ time. The loop processes each of the $n$ characters in `t` once with expected constant-time counter access, so it also takes $O(n)$ time. Total expected time is $O(n)$.

Both strings contain only lowercase English letters. The counter can therefore hold at most twenty-six character keys, including keys first encountered through a decrement. Its space is $O(26) = O(1)$. The scalar answer uses constant space.

If the alphabet were not fixed, the same code would use $O(a)$ space for $a$ distinct characters, up to $O(n)$. The manifest’s constant-space claim relies on the stated lowercase-English-letter constraint.

## Alternatives and edge cases

- **Fixed array of twenty-six counts:** Increment positions for `s`, decrement for `t`, and sum the surplus or deficit side. It has the same $O(n)$ time and $O(1)$ space with lower hashing overhead.
- **Two counters:** Build frequencies for both strings and sum positive differences. This is straightforward but stores duplicate map structure and performs a separate comparison pass.
- **Sorting both strings:** Equal sorted strings reveal whether no work is needed, but deriving the replacement count through sorting takes $O(n\log n)$ time.
- **Counting deficits instead of surpluses:** Because lengths are equal, the total missing occurrences in `t` equals the total excess occurrences. Either side gives the same answer.
- **Already anagrams:** No quota becomes negative, so `ans` remains zero even when character orders differ.
- **All characters different:** Every occurrence in `t` outside the quotas becomes surplus, and each must be replaced.
- **Repeated characters:** The counter distinguishes occurrences through the quota; only copies beyond the required count contribute.
- **One-character strings:** Equal characters return zero, while different characters produce one replacement.
- **Equal-length guarantee:** The proof that every surplus can pair with a deficit depends on equal total lengths. A generalized unequal-length problem would also require insertions or deletions.
- **Position independence:** A character at one position may satisfy a quota originating anywhere in `s` because anagrams depend only on frequencies.
- **Input preservation:** Neither string is modified; the algorithm changes only counter values.
- **Boolean arithmetic:** `cnt[c] < 0` is a Boolean expression, and Python adds it as zero or one. In a language without this conversion, use an explicit conditional increment to preserve the same counting logic.
