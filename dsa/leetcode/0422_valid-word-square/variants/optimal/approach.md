## General

**View the words as a possibly ragged character matrix**

Place `words[i]` in row `i`. Character `words[i][j]`, when it exists, occupies coordinate `(i,j)`. A valid word square requires reflection across the main diagonal: every existing coordinate `(i,j)` must have a mirrored coordinate `(j,i)` containing the same character.

Rows may have different lengths, so this is not necessarily a rectangular matrix. Correctness requires checking both character equality and whether the mirrored coordinate exists at all. Simply comparing characters without bounds checks can raise an indexing error or overlook a row/column length mismatch.

The solution examines every character that actually exists. The outer loop gives row index `i` and row string `w`; the inner loop gives column index `j` and character `c = words[i][j]`.

**Validate the mirrored coordinate in a safe order**

For coordinate `(i,j)`, three conditions can make the square invalid:

`j >= m`

means there is no row `j`, so column position `j` in row `i` has no possible mirrored row. For instance, if there are three words but the first word has a fourth character, that character would belong to a fourth column with no fourth row to match it.

`i >= len(words[j])`

means row `j` exists but is too short to contain mirrored column `i`. The reflected coordinate `(j,i)` is missing.

`c != words[j][i]`

means both cells exist but their characters differ.

These checks appear in one `or` expression. Python evaluates `or` from left to right and stops once a condition is true. Therefore `words[j]` is accessed only after `j < m` is known, and `words[j][i]` is accessed only after `i < len(words[j])` is known. The order prevents out-of-range access while expressing the logical requirements directly.

If any check fails, the method returns `False` immediately. If all existing cells pass, it returns `True`.

**Why scanning existing row characters is enough**

At first glance, the loop seems to check only cells that exist in rows, so one might worry about a character existing at `(j,i)` while `(i,j)` is missing. But every existing character is eventually visited from its own row.

Suppose `(j,i)` exists and `(i,j)` does not. When the loop reaches row `j`, column `i`, it checks the mirror `(i,j)`. Either row `i` does not exist, caught by the first condition, or row `i` is too short, caught by the second. Thus every one-sided coordinate is detected from the side where the character does exist.

This symmetry argument means there is no need to compute a maximum width, pad rows, or separately build column strings.

**A valid ragged example**

For `words = ["abcd","bnrt","crm","dt"]`, the rows have lengths 4, 4, 3, and 2. Raggedness alone does not invalidate the square.

Coordinate `(0,3)` contains `d`, and its mirror `(3,0)` also contains `d`. Coordinate `(1,3)` contains `t`, mirrored by `(3,1)`. Row 3 has no columns 2 or 3, but the potential mirror cells `(2,3)` and `(3,3)` also do not exist, so no asymmetric character is present. Every actual coordinate has an equal mirror, and the square is valid.

For `words = ["ball","area","read","lady"]`, coordinate `(2,0)` contains `r` while `(0,2)` contains `l`; the character comparison fails and the method returns false.

**Connection to equal row and column strings**

For a fixed index $k$, row $k$ lists characters `(k,0)`, `(k,1)`, and so forth. Column $k$ lists `(0,k)`, `(1,k)`, and so forth wherever those coordinates exist. Pairwise diagonal symmetry guarantees the characters agree in order. The existence checks guarantee neither sequence has an unmatched extra character. Therefore the row and column strings are identical.

Conversely, if every row equals its same-index column, each coordinate must have an equal mirror. The local test is therefore exactly equivalent to the word-square definition.

**Why immediate failure is safe**

One mismatched or missing mirror permanently disproves the universal requirement that every row match its corresponding column. No later character can repair an earlier coordinate, so returning at the first violation avoids unnecessary work without changing the result.

## Complexity detail

Let

$$
C = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

be the total number of characters across all rows. The nested loops visit each of these $C$ characters at most once, and each visit performs constant-time bounds and character checks. Time complexity is $O(C)$. This is sharper than $O(nm)$ when rows are short or highly ragged.

Only loop indices, current row references, and the current character are stored. The method creates no transposed matrix or column strings, so auxiliary space is $O(1)$.

In the worst case a valid input must inspect every character, making the linear bound optimal: an unread final character could be the only mismatch.

## Alternatives and edge cases

- **Construct every column string:** Generate column words and compare them with the row list. This is correct but uses $O(C)$ additional space and repeats data already available through mirrored indexing.
- **Pad rows into a rectangle:** Padding introduces sentinel characters and requires careful comparison semantics; direct existence checks are simpler and avoid extra memory.
- **Check only overlapping coordinates:** Comparing characters only when both sides exist is insufficient because an extra unmirrored character must invalidate the square. The two bounds checks are essential.
- **Require all rows to have equal length:** This is too strict. Valid word squares can be ragged, as the second example demonstrates.
- **One word of length one:** Its only character mirrors itself, so the result is true.
- **One word longer than one:** At `j = 1`, no second row exists, so the result is false.
- **A row longer than the number of rows:** The first condition detects its first unrepresentable column.
- **A mirrored row that is too short:** The second condition detects the missing reflected character before indexing it.
- **Diagonal characters:** Coordinates `(i,i)` mirror themselves and necessarily compare equal when they exist.
- **Early mismatch:** The method may finish before scanning all $C$ characters, but $O(C)$ remains the worst-case bound.
- **Lowercase-only guarantee:** Character equality needs no normalization or case folding.
