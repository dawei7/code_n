## General

**Translate a letter into its weight-array index**

The 26 entries of `weights` correspond to `a` through `z`. Lowercase letters have consecutive character codes, so

`ord(c) - ord('a')`

maps `'a'` to 0, `'b'` to 1, and `'z'` to 25.

For each word `w`, the source evaluates:

`sum(weights[ord(c) - ord('a')] for c in w)`.

The generator visits every character once, looks up its assigned weight, and adds it to the word total `s`.

No frequency table is required because words have at most ten characters, and direct traversal already gives the exact sum. Repeated letters naturally contribute their weight once per occurrence.

**Reduce the sum to one of 26 residues**

Only `s % 26` affects the mapped letter. Let

$$
r=s\bmod26.
$$

The remainder is always between 0 and 25, even if the word's raw sum is much larger than 26.

Modulo groups totals that differ by multiples of 26. For example, totals 8, 34, and 60 all have residue 8 and therefore map to the same output character.

The exact source computes the full sum before applying modulo. It could reduce after every addition without changing the final residue, but the constraints make the full sum small and direct summation clearer.

**Reverse the alphabet index**

`ascii_lowercase` is the standard ordered string:

`"abcdefghijklmnopqrstuvwxyz"`.

Ordinary alphabet index 0 is `a` and index 25 is `z`. The problem reverses this association:

- residue 0 maps to `z`, index 25;
- residue 1 maps to `y`, index 24;
- residue 25 maps to `a`, index 0.

The general index is

$$
25-r.
$$

The source appends:

`ascii_lowercase[25 - s % 26]`.

Because `s % 26` is in `[0,25]`, the index is always valid.

This is equivalent to `chr(ord('z') - r)` from the local editorial, but indexing the fixed alphabet string makes the reversed position explicit.

**Build one output character per word**

`ans` begins as an empty list. The outer loop visits `words` in input order, calculates one mapped character, and appends it.

After all words are processed, `''.join(ans)` creates one string. The result length equals the number of words, not the total number of input characters.

Joining once is preferable to repeatedly concatenating immutable strings, which can copy an increasingly long partial result.

**Trace the first example**

For `"abcd"`, the assigned weights sum to

$$
5+3+12+14=34.
$$

The residue is $34\bmod26=8$. Reverse index $25-8=17$ is `r`.

For `"def"`, the sum is 17, so reverse index 8 is `i`.

For `"xyz"`, the sum is 16, so reverse index 9 is `j`.

Appending in word order yields `"rij"`.

**Why the direct simulation is exact**

The generator adds precisely `weights[index(c)]` for every character in a word, matching the weight definition. Modulo produces the required residue, and reverse index `25-r` is exactly the stated mapping. The outer loop preserves the input word order.

Each appended output character is therefore correct for its corresponding word, and their concatenation is the requested result.

**The mapping is numeric, not a reversal of each word**

The phrase “reverse alphabetical order” applies only after a word has been reduced to one residue. The source does not reverse the characters inside `w`, and it does not map each input character separately into the output.

Character order happens not to affect a sum, so permutations of the same multiset of letters have the same word weight. Nevertheless, every occurrence must still be visited because its assigned weight contributes. Once the total is known, exactly one output character is selected. This distinction explains why an input word of length ten still produces one character rather than a ten-character transformed word.

The 26-entry `weights` array is not itself reversed. Letter `c` first uses its ordinary forward index in `weights`; only the final residue uses reverse index `25-r` in the output alphabet.

## Complexity detail

Let $W=\lvert\texttt{words}\rvert$ and

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

Every character is visited once, so weight accumulation costs $O(S)$. Appending and joining $W$ output characters costs $O(W)$, and every word is nonempty, so $W\le S$. Total time is $O(S)$.

`ans` stores $W$ characters before the final output string is built, giving $O(W)$ working/output-construction space. Excluding the required output and its builder, the current word total and generator state are $O(1)$. The 26-entry weight array and alphabet string have fixed size.

## Alternatives and edge cases

- **Character-code subtraction:** `chr(ord('z') - s % 26)` implements the same reverse mapping without `ascii_lowercase`.
- **Precompute a character-to-weight dictionary:** This avoids `ord` subtraction but stores redundant mappings for a fixed contiguous alphabet.
- **Reduce modulo during accumulation:** Updating `s = (s + weight) % 26` keeps the running value bounded and gives the same result, though full sums are already tiny here.
- **Residue zero:** It maps to `z`, not `a`; this is the most common direction mistake.
- **Residue 25:** It maps to `a` at reverse index zero.
- **Weight values above 26:** Only their residues matter after summation; direct indexing still retrieves the full assigned weights correctly.
- **Repeated words:** Each array position produces its own character, so repeated strings create repeated output characters.
- **One-character word:** Its assigned weight alone determines the residue.
- **Input order:** Words are never sorted; the returned characters align with their original positions.
- **Library symbol availability:** The exact source assumes `ascii_lowercase` is supplied or imported from Python's `string` module.
