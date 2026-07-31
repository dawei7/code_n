## General

**Grow the palindromic part before spending the deletion**

Every palindrome has either one central character or a gap between its two central characters. Enumerate both center types at every position. For one center, move `left` and `right` outward while their characters match. The interval between the stopped pointers is a palindrome. It is already an almost-palindromic candidate: an odd palindrome can lose its middle character, and an even palindrome can lose either one of its equal middle characters while remaining palindromic.

If one adjacent character remains on either side of a palindromic interval, including that character also forms a valid candidate—delete the added character to recover the palindrome. This boundary case is what recognizes strings such as `"aab"`: the `"aa"` core reaches the left boundary, and the trailing `b` supplies the required deletion.

**At the first mismatch, try both possible deletions**

When both stopped pointers are in bounds, their characters are the first mismatch. One valid continuation may delete the left character; the other may delete the right character. For each choice, move past the deleted position and resume matching outward. Every later matched pair adds two characters to the original substring, while the skipped mismatch contributes the one deleted character. Stop that branch at its next mismatch because the only deletion has already been used.

Each length recorded this way is valid: removing the explicitly added or skipped character leaves the symmetric pairs and the palindromic core. Conversely, take a longest valid substring and the character whose removal makes it a palindrome. The center of that remaining palindrome is among the enumerated odd and even centers. Expanding from it either reaches the removed character as an adjacent boundary character or encounters the alignment where one of the two skip branches removes it, so the scan records a candidate of the same length.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. There are $2N$ odd/even center starts. The direct expansion and each of the two possible skip expansions move across at most $O(N)$ characters for one center, giving $O(N^2)$ time overall. The algorithm stores only indices, lengths, and a fixed number of loop variables, so it uses $O(1)$ auxiliary space.

The benchmark defines size as $N$ and uses one repeated character. Every center then expands to a string boundary, exercising quadratic center work while the full string remains the answer. The accepted implementation and an independently indexed center-expansion formulation preserve $O(N^2)$ scaling. A correct control that tests every substring with a linear two-pointer one-deletion validator performs $O(N^3)$ work.

## Alternatives and edge cases

- **Rolling dynamic programming:** Track whether each length-$L$ interval is a palindrome and whether it becomes one after one deletion, using the $L-1$ and $L-2$ diagonals. This also takes $O(N^2)$ time but uses $O(N)$ auxiliary space.
- **Full dynamic-programming tables:** Storing every palindrome and almost-palindrome interval is conceptually direct, but two $N\times N$ boolean tables consume $O(N^2)$ space and are unnecessarily large at $N=2500$.
- **Enumerate and validate substrings:** Checking every candidate substring with its own deletion test is correct but introduces a principal slower class, at least $O(N^3)$ with a linear one-deletion validator.
- **Exactly one deletion:** A substring that is already a palindrome still qualifies when one middle character is removed; the operation is not an “at most one” exception.
- **Length two:** Any two-character substring qualifies because deleting either position leaves one character.
- **Deletion at an endpoint:** The best answer may add a disposable character immediately before or after a palindrome, as in `"zabba"`.
- **Deletion inside the substring:** At a mismatch, both the left and right deletion branches matter; choosing only one can miss the optimum.
- **Odd and even centers:** Testing only character centers misses even palindromic remnants such as `"abba"`, while testing only gaps misses odd remnants such as `"aba"`.
- **Uniform string:** The entire string qualifies even though expansion encounters no mismatch; deleting a middle occurrence leaves another palindrome.
