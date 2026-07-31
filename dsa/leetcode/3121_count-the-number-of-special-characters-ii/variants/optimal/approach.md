## General

**Model each letter's legal progression.** Because the ordering rule is independent for the 26 English letters, keep one small state for each letter. State 0 means unseen. State 1 means one or more lowercase occurrences have appeared and the letter is still eligible. State 2 means at least one uppercase occurrence has followed those lowercase occurrences, so the letter is currently special. State 3 is permanently invalid.

**Apply the only legal transitions.** A lowercase occurrence moves state 0 or 1 to state 1. If lowercase arrives in state 2, it appears after the first uppercase and therefore moves the letter to invalid state 3. An uppercase occurrence moves state 1 to state 2. If uppercase appears in state 0, it precedes every possible future lowercase occurrence, so the letter immediately becomes invalid. Further uppercase occurrences preserve state 2, and state 3 is absorbing.

After the left-to-right scan, a letter is in state 2 exactly when it has at least one lowercase occurrence, at least one later uppercase occurrence, and no lowercase occurrence after that first uppercase. These are precisely the three parts of the special-letter definition, so counting state-2 entries gives the required answer.

## Complexity detail

Let $n$ be the length of `word`. Each character causes one constant-time state update, followed by a scan of the fixed 26-entry state array, for $O(n)$ time. The array always has 26 entries, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **First-uppercase and last-lowercase indices:** Record the first uppercase position and last lowercase position for every letter, then count letters satisfying both existence checks and `last_lowercase < first_uppercase`. This is also $O(n)$ time and $O(1)$ space.
- **Repeated full-string scans:** Recompute the relevant first and last positions for every occurrence. It is correct but can require $O(n^2)$ time.
- **Uppercase first:** Once a letter appears uppercase before any lowercase occurrence, no later sequence can make every lowercase occurrence precede that uppercase, so its invalid state is permanent.
- **Late lowercase:** A letter that was temporarily special becomes invalid if its lowercase form appears after the first uppercase occurrence.
- **Repeated uppercase:** Additional uppercase occurrences after a legal lowercase-to-uppercase transition do not affect validity.
- **Missing one case:** Letters ending in the unseen or lowercase-only states do not contribute.
