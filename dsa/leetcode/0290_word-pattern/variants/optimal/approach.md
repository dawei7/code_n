## General

**The required relationship is a bijection**

Matching positions is not enough unless the mapping works in both directions. Every pattern character must always represent the same word, and every word must always belong to the same pattern character.

For example, pattern `"abba"` and words `"dog cat cat dog"` are valid because `a -> dog` and `b -> cat` remain consistent. Pattern `"ab"` with words `"dog dog"` is invalid even though each character could individually be assigned a word: two different characters would map to the same word, violating uniqueness in the reverse direction.

The exact solution enforces the bijection with two dictionaries:

- `d1` maps each pattern character to its word;
- `d2` maps each word back to its pattern character.

Keeping both directions makes every consistency check an expected constant-time hash lookup.

**Split the sentence and reject a cardinality mismatch first**

The source uses `s.split()` to obtain the sequence of words. Under the contract, words are separated by single spaces with no leading or trailing space. Python's no-argument `split()` also tolerates repeated or surrounding whitespace, although legal inputs do not require that extra robustness.

There must be exactly one word for every pattern position. If `len(pattern) != len(ws)`, no full position-by-position match is possible, so the method returns false immediately.

This check is also essential before using `zip`. Python's `zip(pattern, ws)` stops when the shorter input ends. Without the explicit length comparison, an extra character or extra word would be silently ignored and an incomplete match could incorrectly return true.

**Check the forward mapping**

For each aligned pair `(a, b)`, where `a` is a pattern character and `b` is a word, the first possible violation is:

```text
a already appears in d1, but d1[a] is not b
```

If this occurs, one character is trying to represent two different words. For example, in pattern `"aaaa"` and words `"dog cat cat dog"`, the first pair establishes `a -> dog`, while the second asks for `a -> cat`. The forward check rejects that contradiction immediately.

If `a` has never appeared, no forward commitment exists yet, so this direction alone permits establishing `a -> b`.

**Check the reverse mapping**

The second possible violation is:

```text
b already appears in d2, but d2[b] is not a
```

If this occurs, one word is trying to represent two different pattern characters. This is the collision a single character-to-word map cannot detect.

For pattern `"ab"` and words `"dog dog"`, the first pair establishes both `a -> dog` and `dog -> a`. At the second pair, `b` has no forward mapping, but reverse map entry `dog -> a` conflicts with proposed character `b`, so the method correctly returns false.

**Update both maps only after the pair passes**

The source joins the two violation checks with `or`. If either direction conflicts, it returns false before modifying state.

Otherwise, it assigns both `d1[a] = b` and `d2[b] = a`. For a new pair, these statements establish the bijection. For a previously seen valid pair, they simply rewrite the same values, which is harmless.

Updating both directions together preserves their inverse relationship. No map can acquire a pair that the other map does not confirm.

**A prefix invariant proves correctness**

After processing the first $i$ character-word positions without returning false:

1. every repeated pattern character in that prefix is paired with the same word each time;
2. every repeated word in that prefix is paired with the same character each time; and
3. `d1` and `d2` represent inverse associations for every encountered pair.

The invariant is initially true for an empty prefix. At a new position, the two checks reject exactly the ways it could fail. If neither fails, storing the pair preserves all three statements.

When all positions are processed, equal lengths ensure every pattern character and every word occurrence participated. The invariant then states exactly that the full sequences follow one bijection, so returning true is correct.

If the method returns false early, it has found either a forward contradiction, a reverse contradiction, or a length mismatch. Each is independently sufficient to prove no valid bijection exists.

**Trace the first example**

For pattern `"abba"` and `s = "dog cat cat dog"`:

| Pair | Forward state after pair | Reverse state after pair |
|---|---|---|
| `a`, `dog` | `a -> dog` | `dog -> a` |
| `b`, `cat` | add `b -> cat` | add `cat -> b` |
| `b`, `cat` | same mapping | same mapping |
| `a`, `dog` | same mapping | same mapping |

No conflict occurs, so the result is true.

For `"abba"` and `"dog cat cat fish"`, the final `a`, `fish` pair conflicts with stored `a -> dog`, so the result is false. For `"aaaa"` and `"dog cat cat dog"`, the second position conflicts immediately for the same reason.

**Why word contents need no special parsing**

Words are treated as complete string keys. Their lengths and internal letters matter only through exact string equality and hashing. The algorithm does not need to compare word structure with character structure; it only verifies consistent pair identity at corresponding positions.

## Complexity detail

Let $P$ be the pattern length and $S$ be the number of characters in `s`. Splitting the sentence takes $O(S)$ time and creates word strings whose total character content is $O(S)$. The pair loop runs $P$ iterations.

With expected constant-time hash-table operations after accounting for string hashing, total expected time is $O(P+S)$. The manifest's $O(n)$ notation can be understood as linear in the combined input size.

The word list created by `split()` uses $O(S)$ space. The dictionaries store at most one entry per distinct pattern character and distinct word. Stored word content is bounded by the sentence content, so total auxiliary space is $O(S+P)$, usually simplified to $O(S)$ because the number of lowercase pattern characters is at most 26 and $P$ is bounded by the token count.

The algorithm can return early on the first contradiction, but its worst-case bounds assume the whole input is valid or the conflict appears last.

## Alternatives and edge cases

- **One forward map only:** It detects one character mapping to several words but misses two characters mapping to the same word. A reverse map or used-word set is required.
- **Forward map plus used-word set:** For a new character, reject an already-used word; otherwise record both. This enforces the same bijection with slightly less reverse information.
- **First-occurrence indices:** Record where each character and each word first appeared and require paired first-occurrence indices to match. It can use one carefully namespaced map but is less direct than explicit inverse maps.
- **Scan map values for collisions:** A single map can test whether a new word is already among its values, but value lookup is linear in the number of mappings rather than expected constant time.
- **More words than characters:** The length check rejects before `zip` can hide the extra suffix.
- **More characters than words:** The same check rejects the unmatched pattern suffix.
- **Repeated valid pair:** Reassigning the same forward and reverse entries changes nothing and remains valid.
- **One character, multiple words:** The forward check rejects the first differing word.
- **One word, multiple characters:** The reverse check rejects the second character.
- **All positions identical:** A pattern of repeated one character is valid only when every word is also the same.
- **Single position:** One character and one nonempty word always form a valid bijection.
- **Whitespace behavior:** Legal input uses single spaces. No-argument `split()` would also normalize multiple whitespace characters rather than creating empty words.
- **Case sensitivity:** Legal strings are lowercase. Without that restriction, Python keys would still treat uppercase and lowercase forms as distinct.
