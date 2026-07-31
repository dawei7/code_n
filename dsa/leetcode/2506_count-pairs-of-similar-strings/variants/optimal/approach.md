## General

**Turn a character set into one integer**

Similarity ignores both order and multiplicity. Assign bit $0$ to `a`, bit $1$ to `b`, and so on through bit $25$ for `z`. While scanning a word, set the bit belonging to each character. Repeated characters set an already-set bit and therefore do not change the mask. Two words produce the same mask exactly when they contain the same distinct letters.

**Count each pair when its later endpoint arrives**

Maintain a frequency table of masks for words already processed. If the current word's mask has appeared $k$ times, the current index completes exactly $k$ new pairs: one with each earlier word having that mask. Add $k$ to the answer, then increment the mask's frequency.

Every qualifying pair is counted once, when its larger index is processed. No non-similar pair is counted because different character sets have different masks.

## Complexity detail

Define the total input length as

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

Building all masks examines each character once, so the running time is $O(S)$. Dictionary operations have expected $O(1)$ time. At most $n$ different masks are stored, giving $O(n)$ auxiliary space; the fixed 26-letter alphabet also limits the table to at most $2^{26}$ keys.

## Alternatives and edge cases

- **Compare every pair directly:** Building and comparing two character sets for every pair is straightforward but takes $O(n^2L)$ time when $L$ is the maximum word length.
- **Sorted unique-character signature:** `''.join(sorted(set(word)))` is also canonical, but sorting introduces extra work and allocates strings instead of using a compact integer.
- **Count after collecting all masks:** A second pass can add $k(k-1)/2$ for every frequency $k$; the online count produces the same total without that pass.
- **Repeated letters:** Multiplicity is irrelevant, so `"a"`, `"aa"`, and `"aaaa"` all receive the same mask.
- **One word or all distinct masks:** No earlier matching signature is found, and the result remains $0$.
- **Many identical signatures:** Each new occurrence adds the number already seen, producing all $\binom{k}{2}$ pairs without listing them.
