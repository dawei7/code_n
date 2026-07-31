## General

An alphabetical continuous substring is completely characterized by its adjacent pairs: every next character must have code point exactly one greater than the preceding character. Therefore all valid substrings lie inside maximal runs satisfying this local relation.

Scan from left to right while storing the length of the run ending at the current character. Extend it when the current letter is the exact successor of the previous letter; otherwise reset it to 1 because the current character starts a new valid one-letter substring. The maximum run length seen during the scan is the answer. Every qualifying substring belongs to one of these runs, and every recorded run satisfies the definition, so the maximum is exact.

## Complexity detail

Each character after the first is compared with its predecessor once, giving $O(n)$ time. Two integer counters use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all substrings:** Checking every start and end is direct but costs at least $O(n^2)$ time.
- **Split on invalid pairs:** Building explicit run strings is correct, but storing them is unnecessary when only the maximum length is required.
- **Single character:** Every one-letter string is alphabetical continuous, so the minimum answer is 1.
- **Repeated letters:** Equality is not a successor step and resets the run.
- **Alphabet end:** `z` followed by `a` does not wrap and therefore resets the run.
- **Full alphabet:** `"abcdefghijklmnopqrstuvwxyz"` is a valid run of length 26, the largest possible distinct-letter run.
