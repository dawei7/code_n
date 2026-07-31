## General

Convert `forbidden` to a hash set. Maintain a sliding window `word[left...right]` that contains no forbidden substring and record the largest window length.

When `right` advances, any newly created forbidden occurrence must end at `right`; every other substring was already present in the previously valid window. Since forbidden strings have length at most ten, only suffixes beginning from `right` down through `max(left, right - 9)` can matter. Test those suffixes from shortest to longest. If `word[start...right]` is forbidden, advance `left` to `start + 1`, which removes that occurrence.

The suffixes are checked from greatest `start` to smallest. Consequently, the first match has the latest starting position among all forbidden occurrences ending at `right`. Moving past this start is both necessary and sufficient: a smaller move would retain that forbidden occurrence, while a larger move would discard characters without being forced by any ending occurrence. After the update, `word[left...right]` is the longest valid substring ending at `right`; maximize its length over all right endpoints.

**Why a single moving boundary captures every invalid candidate**

Assume the window before adding `word[right]` is valid. If the enlarged window is invalid, at least one newly present forbidden substring must use the new final character, so the bounded suffix scan finds it. Moving `left` past the latest start eliminates every forbidden suffix ending there: any other match starts no later and is removed as well. Earlier forbidden occurrences cannot reappear because `left` never moves backward. Thus the maintained window is valid after every iteration and is maximal for its right endpoint.

## Complexity detail

Let $n$ be the length of `word`, let $L \le 10$ be the maximum forbidden-string length, and let $S$ be the total number of characters in `forbidden`. Building the set costs $O(S)$ time and space. For each of the $n$ right endpoints, at most $L$ suffixes are created and hashed; accounting for their lengths gives $O(nL^2)$ scan time in Python. Because $L$ is capped at ten by the contract, this is $O(n)$, for total time $O(n+S)$. The set uses $O(S)$ auxiliary space, while the window state is $O(1)$.

## Alternatives and edge cases

- **Trie of reversed forbidden strings:** Scan backward from each right endpoint through a trie, avoiding temporary substring creation while retaining $O(nL+S)$ time; it is more code for the same bounded-depth idea.
- **Aho-Corasick automaton:** Multi-pattern matching handles unrestricted pattern lengths in $O(n+S+z)$ time, where $z$ is the number of matches, but is unnecessary when every pattern has length at most ten.
- **Enumerate every candidate substring:** Checking all $O(n^2)$ substrings is correct but exceeds the input limit.
- **Single-character forbidden strings:** Each occurrence moves `left` immediately past itself and may make the current window empty.
- **Overlapping patterns:** Advancing beyond the latest starting forbidden suffix removes every earlier-starting forbidden suffix ending at the same position.
- **No forbidden occurrence:** `left` stays zero and the entire `word` is returned.
- **Length-ten boundary:** The suffix beginning at `right - 9` must be included; longer suffixes cannot equal a forbidden string.
