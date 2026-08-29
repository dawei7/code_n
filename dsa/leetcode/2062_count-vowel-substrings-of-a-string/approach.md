## General

**Fix a start and extend every vowel-only substring**

The source considers every index `i` as a possible substring start. For that start, it scans characters in `word[i:]` from left to right.

Set `t` stores which of the five vowel kinds have appeared in the current substring. Each encountered vowel is added, and once `len(t) == 5`, the substring ending at that character contains all five vowels and contributes one.

Extending farther through vowels keeps all previously seen vowel kinds, so every later endpoint is evaluated independently and may also contribute.

**Stop at the first consonant**

A valid vowel substring may contain only vowels. Once the inner scan encounters `c not in s`, every longer substring with the same start also contains that consonant.

The source breaks immediately. No later endpoint for this start can recover validity, even if more vowels appear afterward.

This pruning separates the string into vowel-only runs implicitly.

**Why a set captures the all-five requirement**

The required property depends on presence, not frequency. Seeing several `a` characters still supplies only one of the five required vowel types.

`t.add(c)` automatically ignores repeated values. Because the vowel universe has exactly five elements, `len(t)==5` is equivalent to having `a,e,i,o,u` all present.

The outer set `s = set("aeiou")` provides constant-time membership testing.

**Trace `"aeiouu"`**

Starting at index zero, the set grows through sizes one, two, three, four, and five at the first `u`. That endpoint contributes one.

The final repeated `u` leaves set size five, so the longer substring contributes another one. Other start indices never collect every vowel, producing total two.

**Trace a consonant-separated string**

If a start lies before a consonant, its scan stops there. It does not combine vowels from the two sides because that would create a noncontiguous selection or a substring containing the consonant.

Starting positions after the consonant receive their own fresh set and may form valid substrings entirely within the later vowel run.

**Why every valid substring is counted**

Take any valid substring from index `i` through `j`. The outer loop reaches `i`. Every character through `j` is a vowel, so the inner loop does not break before `j`.

By endpoint `j`, set `t` contains all five vowels, so the source adds one for that exact start-end pair.

**Why no invalid substring is counted**

The inner loop never continues past a consonant for a fixed start, so every considered endpoint forms a vowel-only substring.

An increment occurs only when the distinct-vowel set has size five. Therefore every counted substring contains all five required vowel types. Each start-end pair is visited once, preventing duplicates.

**The exact source is not the manifest's linear method**

There are two nested dimensions: every start index, then potentially every later character until a consonant. For an all-vowel word, the source examines

$$
N+(N-1)+\cdots+1=\frac{N(N+1)}2
$$

characters.

It also evaluates `word[i:]`. Python slicing creates a new suffix string for each outer iteration, adding linear copying work per start in the worst case. The protected implementation is therefore quadratic, not the manifest's stated $O(N)$.

**How a linear approach would differ**

A genuine linear solution can track the most recent position of each vowel and the most recent consonant. At each right endpoint, the earliest of the five last-vowel positions determines how many valid starts lie after the last consonant.

That method counts many substrings at once. The exact source instead enumerates their start-end pairs, so this document keeps the two complexity claims separate.

## Complexity detail

Let $N=len(word)$. In the worst case of all vowels, the nested scan performs $\Theta(N^2)$ character visits. Creating every suffix slice also totals $\Theta(N^2)$ copied characters over the execution. Exact time is $O(N^2)$.

The vowel sets themselves hold at most five elements. However, one `word[i:]` slice can contain $O(N)$ characters, so peak auxiliary space of the exact Python implementation is $O(N)$, not the manifest's $O(1)$. Without slicing, an index-based nested loop would use $O(1)$ extra state while remaining quadratic.

## Alternatives and edge cases

- **Last-occurrence linear scan:** Track all five latest vowel indices and the last consonant to count valid starts per endpoint in $O(N)$ time.
- **Index-based nested loop:** Avoid suffix allocations but still takes $O(N^2)$ time.
- **Fewer than five characters:** Cannot contain all five vowels, so answer is zero.
- **All consonants:** Every inner scan breaks on its first character.
- **Repeated vowel:** Does not increase the set size but may create additional valid endpoints after all five exist.
- **Consonant boundary:** Vowels on opposite sides cannot belong to one valid substring.
- **All-vowel word:** Produces the quadratic worst case.
- **Exactly one occurrence of each vowel:** The whole five-character run contributes once.
- **Different vowel order:** Presence matters, not ordering.
- **Manifest mismatch:** Exact source is quadratic time with linear peak slice space.
- **Input preservation:** The string is immutable; slices are new strings.
- **Small constraint:** $N\le100$ makes the exhaustive implementation practical despite the mismatch.
