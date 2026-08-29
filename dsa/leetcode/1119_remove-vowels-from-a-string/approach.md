## General

**Filter characters while preserving order**

The result contains every consonant from the input in its original left-to-right order and contains none of the five lowercase vowels. This is a filtering operation, not a search for words, syllables, or pronunciation.

The generator expression visits each character `c` in `s`. Condition `c not in "aeiou"` yields the character only when it is not one of the five forbidden values.

Because the input contains lowercase English letters only, this literal membership test covers the complete vowel set required by the contract. Uppercase handling, accented letters, and sometimes-vowel rules for `y` are outside the domain.

**Build the immutable result once**

Python strings are immutable. Repeatedly appending to a string inside a loop can create many intermediate objects. Instead, the generator lazily supplies retained characters to `"".join(...)`, which constructs the final string in one coordinated operation.

The empty string before `join` is the separator, so retained characters are placed directly adjacent to one another. No commas, spaces, or other new characters are inserted.

**Why the order cannot change**

A generator expression processes `s` in its native iteration order. It may skip a vowel, but it never reorders the characters it yields. Therefore, if consonant `a` appeared before consonant `b` in the input, it also appears before `b` in the output.

This property is important because the operation removes characters; it does not sort or group consonants.

**Walk through a short example**

For `"leetcode"`, the generator examines `l` and yields it. It skips `e` and the next `e`, yields `t`, `c`, and `d`, then skips `o` and `e`. Joining the yielded sequence produces `"ltcd"`.

Repeated vowels are each tested and discarded independently. Repeated consonants are each yielded, so multiplicity is preserved.

**Why the membership test is exact**

For each input position, there are two cases. If the character belongs to `"aeiou"`, the contract says to remove it and the generator does not yield it. Otherwise, the contract says to retain it and the generator yields it exactly once.

Every position is processed once and falls into exactly one case. Joining all yielded characters therefore returns precisely the input with all and only vowels removed.

The generator is also a stable filter. “Stable” means retained elements keep their relative order. Stability follows automatically because the comprehension has one forward loop and no secondary traversal, sorting key, or container whose iteration order could differ from the source.

**Empty output is valid**

The input itself is nonempty, but every character may be a vowel. In that case the generator yields nothing. Joining an empty iterable returns `""`, which is the required empty result without any special branch.

Similarly, a string with no vowels yields every input character and returns text equal in value to the original.

The result length equals the input length minus the number of vowel positions. The method does not calculate that number explicitly because `join` can consume the retained stream directly, but this identity explains both extremes: zero retained characters for an all-vowel input and $n$ retained characters for a vowel-free input.

## Complexity detail

Let $n$ be the string length. The generator examines every character once. Membership testing against the fixed five-character string takes constant time, and joining writes at most $n$ retained characters. Total time is $O(n)$.

The returned immutable string can contain up to $n$ characters, so output space is $O(n)$. The generator itself is lazy and uses constant iteration state rather than first building a separate list. The manifest’s $O(n)$ space includes the required result.

No algorithm can generally use less than $\Omega(n)$ time because the final character could be the only vowel or consonant, so every input position may affect the answer.

Membership in the five-character literal performs at most five character comparisons, a fixed constant. Thus it does not introduce an additional factor that grows with $n$.

## Alternatives and edge cases

- **Explicit loop with list:** Append consonants to a list and join at the end. It has the same asymptotic bounds and may be easier for beginners to debug.
- **Set membership:** Use `set("aeiou")` for expected constant lookup. With only five vowels, the string test is already constant and avoids constructing a set per call.
- **Repeated `replace` calls:** Replace each vowel with empty text. Five full scans are still $O(n)$ because five is constant, but they create several intermediate strings.
- **Regular expression:** A vowel character class can remove matches, but regex machinery is unnecessary for five fixed characters.
- **All vowels:** The generator yields nothing and `join` returns the empty string.
- **No vowels:** Every character is yielded, preserving the entire input.
- **Repeated consonants:** Each occurrence remains; filtering does not deduplicate.
- **Repeated vowels:** Every occurrence is removed independently.
- **Single vowel:** The result is empty.
- **Single consonant:** The same one-character text is returned.
- **Letter `y`:** It remains because the contract lists only `a`, `e`, `i`, `o`, and `u`.
- **Lowercase guarantee:** No uppercase vowel conversion is needed.
- **Input immutability:** The original string cannot be modified; a new result is returned.
- **Stable order:** Filtering never sorts or rearranges retained characters.
