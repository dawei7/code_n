## General

**Treat each source character as one repeated block**

Inside a word, character at zero-based position `i` appears `i+1` times in the expanded string. A word of length `m` therefore expands to

$$
1+2+\cdots+m=\frac{m(m+1)}2
$$

characters.

The source calls this length `m` locally after computing the triangular formula. Knowing a whole word's expanded length lets the algorithm skip it without constructing any repetitions.

Spaces behave differently: each separator contributes exactly one literal space, and the repetition position restarts at one in the next word.

**Maintain `k` relative to the current word**

`s.split()` yields the source words in order. At the start of an iteration, `k` is the zero-based index relative to the current word's expanded block followed, when applicable, by its separator.

Let `expanded_length` be the triangular word length:

- If `k < expanded_length`, the desired character lies inside this word.
- If `k == expanded_length`, it is the single space immediately after the word.
- If `k > expanded_length`, the target lies later. Subtract `expanded_length+1` to skip both the word expansion and its following space.

The exact source writes these comparisons using its variable `m`.

The final word has no following separator. A valid global `k` can never equal or exceed that last word's expanded length, so the `k==m` branch is reached only for a real inter-word space.

**Locate the repeated character inside one word**

Once `k` lies inside a word, `cur` accumulates block endings:

$$
1,\ 1+2,\ 1+2+3,\ldots.
$$

After processing source position `i`, `cur` equals the number of expanded characters through that position's block. The condition `k < cur` means the zero-based index lies before this exclusive endpoint, so the answer is `w[i]`.

For a word `"abc"`, block endpoints are one, three, and six. Indices zero maps to `a`, indices one and two map to `b`, and indices three through five map to `c`.

For `"hello world"`, the first word expands to length fifteen. `k=15` equals that length and returns the separator. A later index would subtract sixteen before scanning `"world"`, correctly restarting block sizes.

Suppose instead `k=18`. The first block plus separator consumes sixteen positions, so the next relative index is two. In `"world"`, `w` occupies relative index zero and `o` occupies indices one and two. The cumulative endpoints become one and three; two is not below one but is below three, so the source returns `'o'`.

The comparison order also prevents subtracting past a separator. Equality is tested before the greater-than branch, so a separator index is returned directly rather than transformed into a negative or next-word index.

**Why no expanded string is needed**

Every output position belongs uniquely to a word block, a character repetition block within that word, or a separator. The outer scan identifies the word/separator by subtracting complete lengths. The inner cumulative scan identifies the character block. The returned character is exactly what explicit expansion would place at `k`.

Validity of `k` guarantees some branch returns. The method never needs a fallback return for out-of-range input.

The loop's nested appearance does not imply quadratic work. Only the one word containing `k` is scanned character by character; preceding words are skipped by their formula, and later words are never visited. Even scanning every word's length through `len(w)` remains proportional to the split input size.

## Complexity detail

Let `n=len(s)`. The total number of characters across all words is at most `n`. The outer and inner scans together inspect each source character at most once before returning, so time complexity is $O(n)$.

The manifest claims $O(1)$ space, but the exact Python source calls `s.split()`. That operation constructs a list and word strings totaling $O(n)$ storage. Therefore actual auxiliary space is $O(n)$ in Python. A manual index scan over `s` could realize constant extra space, but it is not this implementation.

The triangular length for a word can be quadratic in its source length, but only the numeric value is computed; expanded characters are not stored.

## Alternatives and edge cases

- **Construct `t` explicitly:** Expanded length can be quadratic in a long word, making time and memory unnecessarily large.
- **Scan `s` manually:** This can preserve the same logic with $O(1)$ auxiliary space and would match the manifest, but the exact source uses `split`.
- **Forget separator length:** Later relative indices would be off by one after every word.
- **Repeat positions across the whole string:** Repetition counts restart for each word, not after each space as a continuing global index.
- **`k=0`:** It lies in the first one-character block and returns the first source character.
- **Index at a block boundary:** Because endpoints are exclusive, `k<cur` assigns the first index after a block to the next block.
- **Index exactly after a word:** `k==expanded_length` returns the separator.
- **One-word input:** No valid index points to a separator after it.
- **One-letter word:** Its expansion length is one, followed by a space only when another word exists.
- **Long word:** Arithmetic skips repetition blocks without materializing their potentially huge expansion.
- **Manifest mismatch:** Space analysis must include the list and substrings allocated by `s.split()`.
