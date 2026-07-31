## General

**Locate the retained prefix boundary**

Trailing characters are the only ones that can be removed, so start an `end` boundary immediately after the last character. While the character just before that boundary is one of the five vowels, move `end` one position left.

The scan maintains a simple fact: every character from `end` to the original end of the string is a vowel and therefore must be removed. When the scan stops at a non-vowel, that character and everything before it must remain because the removable suffix cannot cross a consonant. If the boundary reaches zero, the invariant shows that every original character was a vowel. Returning the prefix `s[:end]` is therefore correct in both cases.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. In the worst case every character is a vowel, so the boundary scan takes $O(N)$ time. Constructing the returned prefix also takes up to $O(N)$ time and $O(N)$ output space in Python; the scan itself uses $O(1)$ auxiliary space.

The benchmark defines size as $N$ and uses all-vowel strings, forcing inspection of every character. The accepted boundary scan is $O(N)$. The correct slower control tests every possible prefix boundary and rescans its remaining suffix, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Built-in character-set trim:** Python's `s.rstrip("aeiou")` expresses the same operation concisely, but the explicit scan keeps the five-character contract and stopping boundary visible.
- **Enumerate prefix boundaries:** Checking from scratch whether every suffix after each possible boundary is a vowel is correct but requires $O(N^2)$ time.
- **All vowels:** The boundary reaches zero and the result is the empty string.
- **No trailing vowel:** The first inspected character is a non-vowel, so the entire input is returned.
- **Internal vowels:** Vowels before the last consonant are retained because they are not part of the trailing suffix.
- **The letter `y`:** It is not included in the problem's explicit vowel set and stops trimming.
- **Single character:** A one-character vowel becomes empty; a one-character consonant remains.
