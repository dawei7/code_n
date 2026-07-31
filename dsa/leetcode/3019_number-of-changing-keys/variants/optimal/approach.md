## General

Normalize each adjacent pair to the same case and compare its physical letters. A transition contributes one exactly when the normalized characters differ.

The app-local implementation visits indices from $1$ through $N-1$. At each index, the Boolean expression comparing the lowercase forms of the current and previous characters is true precisely for a key change. Summing those Boolean values counts every adjacent transition once.

This directly matches the definition: case-only changes normalize to equal letters and contribute zero, while different alphabetic letters normalize to distinct values and contribute one. No non-adjacent character can affect whether the user changed keys at a particular position.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. The algorithm examines the $N-1$ adjacent pairs once, so it takes $O(N)$ time. It uses $O(1)$ auxiliary space apart from short-lived one-character normalized strings.

## Alternatives and edge cases

- **Normalize the full string first:** Convert `s` to lowercase and compare adjacent characters. This remains $O(N)$ time but materializes an $O(N)$ copy.
- **Compare alphabet codes:** For English letters, comparing `ord(character) | 32` avoids temporary lowercase strings and keeps the same bounds.
- **Rebuild prefixes:** Lowercasing or slicing growing prefixes for each transition is correct but can take $O(N^2)$ time.
- **Single character:** There is no adjacent transition, so the answer is zero.
- **Case alternation:** A sequence such as `"aAaA"` never changes physical keys.
- **Every adjacent letter differs:** The maximum answer is $N-1$.
