## General

A word matches the pattern when character relationships are identical. Whenever two pattern positions contain the same letter, the corresponding word positions must also contain the same letter. Whenever the pattern positions contain different letters, the corresponding word positions must contain different letters. Together these conditions describe a bijection.

The helper `match(s, t)` compares a candidate word `s` with pattern `t` using two arrays of last-seen positions:

- `m1[ord(a)]` stores the latest position where word character `a` appeared.
- `m2[ord(b)]` stores the latest position where pattern character `b` appeared.

Both arrays start with zeros, meaning “not seen.” The loop numbers actual positions from 1, so zero can remain an unambiguous sentinel.

At each paired position $i$, word character `a` and pattern character `b` may correspond only if their previous occurrence positions are equal:

```text
if m1[ord(a)] != m2[ord(b)]:
    return False
```

After the check, both last-seen entries are assigned the current position `i`.

**Why equal histories enforce same-letter consistency.** Suppose a pattern letter appeared previously at position $r$. Its last-seen value is $r$. For the current word letter to map consistently to it, that word letter must also have last appeared at $r$. If it was never seen or last appeared somewhere else, the equality check fails.

**Why equal histories also prevent two-to-one mappings.** Suppose two different pattern letters tried to map to the same word letter. When the second pattern letter is first paired with that already-seen word letter, its pattern last-seen value is zero while the word letter's value is nonzero. The mismatch rejects the candidate.

The same argument works in the other direction: two different word letters cannot correspond to one pattern letter because the pattern side would have a nonzero history unmatched by the new word letter. Maintaining both arrays therefore enforces a bijection without explicitly constructing forward and reverse dictionaries.

**Fresh characters match fresh characters.** When both characters have never appeared, both stored values are zero, so the pair is accepted and both are stamped with the same current position. Their histories remain synchronized on every later occurrence.

For word `mee` and pattern `abb`:

- Position 1 pairs fresh `m` with fresh `a`; both histories become 1.
- Position 2 pairs fresh `e` with fresh `b`; both become 2.
- Position 3 sees `e` and `b` again; both last appeared at 2, so they match.

For word `ccc` and pattern `abb`, position 1 pairs `c` with `a`. At position 2, `c` was already seen at 1 but `b` is fresh with history zero, so the word is rejected. This catches the forbidden mapping of both `a` and `b` to `c`.

**Why the test is sufficient.** If every position passes, each occurrence pattern of a word letter is identical to the occurrence pattern of its paired pattern letter. First occurrences pair distinct new letters, and repeats preserve the same pairing. This defines a one-to-one mapping from the pattern's used letters to the word's used letters that transforms the pattern into the word. Unused alphabet letters can be assigned arbitrarily to complete a full alphabet permutation if necessary.

The outer list comprehension applies this test independently to every word and retains exactly the matches. All words have the same length as the pattern, so `zip` covers every position and no extra length check is needed.

## Complexity detail

Let $N$ be the number of words and $L$ the common word and pattern length. Each match attempt scans $L$ paired characters and performs constant-time array operations.

- **Time complexity:** $O(NL)$.
- **Space complexity:** $O(N+L)$ under the manifest's output-inclusive accounting. The returned list can hold $N$ matching word references, while each helper call uses two fixed arrays of length 128.

Because the alphabet is lowercase English letters, the two 128-entry arrays are constant-size auxiliary storage. No mapping grows with $L$.

## Alternatives and edge cases

- **Two dictionaries:** Store pattern-to-word and word-to-pattern mappings explicitly. This is equally correct and often more readable, with $O(L)$ per-check mapping space.
- **Normalize each string:** Replace each character by the index of its first occurrence and compare normalized forms. This also tests the same equality pattern in $O(L)$ time.
- **Only one forward map:** It ensures a pattern letter stays consistent but does not stop two different pattern letters from mapping to the same word letter. A reverse constraint is required.
- **Compare character frequency counts:** Equal multiplicities alone do not preserve positions; strings can have the same counts but different occurrence patterns.
- **One-character pattern:** Every one-character word matches because any single letter can map bijectively to any other.
- **All pattern letters equal:** A matching word must also repeat one identical letter at every position.
- **All pattern letters distinct:** A matching word must have distinct letters at every position.
- **Repeated blocks:** Last-seen positions capture arbitrary recurrence patterns, not merely adjacent duplicates.
- **Equal word and pattern:** Their histories evolve identically and the word matches.
- **Same length guarantee:** Without it, `zip` would ignore an unmatched suffix; a general-purpose helper should compare lengths first.
- **ASCII-sized arrays:** `ord` values for lowercase letters fit within 128. A broader Unicode alphabet would require dictionaries.
- **Any answer order:** The comprehension preserves input order, which is valid even though the problem does not require it.
- **Original words returned:** The output contains the existing strings, not transformed versions or mappings.
