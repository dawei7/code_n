## General

**Treat the input as a subsequence of repeated `abc`**

Insertions may add characters anywhere but cannot delete, replace, or reorder existing characters.

Therefore, the task is to find the shortest valid string:

$$
(\texttt{abc})^q
$$

that contains `word` as a subsequence. The number of inserted letters is:

$$
3q-|\texttt{word}|.
$$

The exact solution constructs this shortest supersequence conceptually, one expected pattern character at a time, without storing the resulting string.

**Track the next expected character**

`s = 'abc'` is the repeating pattern. Pointer `i` identifies the currently expected character:

- zero means `a`;
- one means `b`;
- two means `c`.

After every conceptual output character, `i = (i + 1) % 3` advances to the next pattern position and wraps from `c` back to `a`.

Pointer `j` identifies the next unconsumed character of `word`.

**Match or insert at each step**

While input remains:

- if `word[j] == s[i]`, the existing character fits the next valid-string position, so increment `j`;
- otherwise, the expected character is missing before `word[j]`, so count one insertion and leave `j` unchanged.

In both cases, advance `i`. A match consumes the expected character from input; a mismatch supplies it through insertion.

The loop eventually consumes every source character because the repeating pattern visits `a`, `b`, and `c` forever.

**Why inserting the expected character is forced**

Suppose the next valid output position requires character $c=\texttt{s[i]}$, but the next input character is different.

The input character cannot be changed or skipped. It must appear later in the supersequence. The current required pattern position must therefore be filled by an inserted $c$ before that input character can be consumed at its own matching pattern position.

So every mismatch represents one unavoidable insertion. Taking it immediately cannot hurt future choices because valid strings have only one fixed cyclic order.

**Trace a single `b`**

Start expecting `a` while input points to `b`.

- `b != a`: insert `a`, answer one, now expect `b`;
- `b == b`: consume it, now expect `c`.

The main loop ends, but the current `abc` block lacks `c`. The tail logic adds one more insertion. Total two creates `abc`.

**Trace repeated `a` characters**

For `word = "aaa"`:

- first `a` matches;
- before the second `a`, expected `b` and `c` must be inserted;
- second `a` then matches;
- the same happens before the third;
- after the third, trailing `b` and `c` are added.

Six insertions produce `abcabcabc`. No shorter valid string can preserve three input `a` characters because every `abc` block contains only one `a`.

**Complete the final block**

The loop stops immediately after consuming the last input character, even if the current pattern block is incomplete.

Because `word` is nonempty:

- if its last character is `c`, the last block is complete;
- if it is `b`, one trailing `c` is required;
- if it is `a`, trailing `b` and `c` are required.

The code implements:

`ans += 1 if word[-1] == 'b' else 2`

only when the final character is not `c`.

This tail completion is necessary because a valid string must end at a block boundary, not merely after all source characters have been embedded.

**Why the last character determines the tail**

Whenever an input character is consumed, it exactly fills the matching pattern position. Thus, after the final consumption, the pattern state is immediately after that character:

- after `a`, two positions remain;
- after `b`, one remains;
- after `c`, zero remain.

Prior insertions do not change this fact; they only ensured the final input character was reached in the correct cycle.


After each loop step, the conceptual sequence generated so far is a prefix of repeated `abc`, and it contains exactly the first `j` input characters as a subsequence. `ans` counts generated characters that were not taken from input.

If the next input character matches the required pattern position, using it avoids an insertion and cannot be worse. If it does not match, every valid supersequence must insert the required pattern character before eventually consuming that input character.

Therefore, each step uses the fewest possible insertions for its generated prefix. After all input is consumed, the forced tail is the unique shortest completion to a whole number of blocks. The final count is globally minimal.

**Relationship to descending adjacent letters**

An equivalent observation is that every adjacent pair that is not strictly increasing in the order `a < b < c` forces a new `abc` block. One can count blocks and compute $3q-n$.

The exact source instead simulates the expected cyclic characters, which handles missing letters and block boundaries uniformly.

**Input limitations**

Every character is one of `a`, `b`, or `c`, so the pattern is guaranteed to match it within at most three expected positions. The word is nonempty, making `word[-1]` safe.

## Complexity detail

Let $n=|\texttt{word}|$. Each input character is consumed once. Between two consumed characters, at most two missing pattern characters are inserted, so the loop performs $O(n)$ iterations.

The algorithm stores two pointers, the count, and constant pattern text, using $O(1)$ auxiliary space. It does not construct the completed string.

## Alternatives and edge cases

- **Count `abc` groups:** Start one group and increment when adjacent characters are non-increasing, then return three times groups minus word length.
- **Dynamic programming:** Can model pattern position and input prefix but is unnecessary because every mismatch insertion is forced.
- **Construct the full supersequence:** Easier to visualize but uses $O(n)$ additional space when only the count is requested.
- **Already `abc` repeated:** Every character matches and the last character is `c`, so answer is zero.
- **Single `a`:** Needs trailing `b` and `c`, answer two.
- **Single `b`:** Needs leading `a` and trailing `c`, answer two.
- **Single `c`:** Needs leading `a` and `b`, answer two.
- **Repeated same letter:** Each occurrence belongs to a different block and forces the other two letters.
- **Missing middle character:** For `ac`, one `b` is inserted between them.
- **Nonempty guarantee:** It makes the final-character tail check safe.
