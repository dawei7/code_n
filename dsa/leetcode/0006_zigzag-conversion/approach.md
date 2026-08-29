## General

**The output is a row-by-row reading of a repeated movement**

The zigzag writes characters in their original order while a row pointer moves:

1. downward from row `0` to row `numRows - 1`;
2. upward from row `numRows - 1` to row `0`;
3. downward again, repeating until the string ends.

Only the row assigned to each character matters for producing the answer. Horizontal matrix coordinates and blank cells are visual aids, not data the algorithm needs to store. The solution therefore creates one character list per row, simulates the vertical row movement, and concatenates the row lists at the end.

For `numRows = 4`, the visited row indices are

```text
0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ...
```

Appending each input character to the corresponding list recreates the same layout's row contents without constructing a sparse two-dimensional grid.

**Why one row must return immediately**

When `numRows == 1`, every character belongs to row zero, so the converted string is exactly `s`.

The early return is also required for the movement logic. With one row, the top and bottom are the same position. A direction that flips at that position and then advances would attempt to move to row `1` or `-1`, neither of which exists. Returning `s` handles both the mathematical identity case and the index-safety case.

**Store row contents separately**

The line

```python
g = [[] for _ in range(numRows)]
```

creates `numRows` distinct inner lists. `g[r]` will contain exactly the characters written on row `r`, already in their left-to-right order.

Using a list comprehension is important in Python. An expression such as `[[]] * numRows` would repeat references to one shared inner list; appending to any row would then appear in every row. The comprehension evaluates `[]` once per row and gives each row independent storage.

**Represent direction with `k`**

The state begins as

```python
i, k = 0, -1
```

`i` is the current row. `k` is the next row change:

- `k = 1` means move downward to the next larger row index;
- `k = -1` means move upward to the next smaller row index.

Although `k` initially equals `-1`, the first character is appended at row `0` before movement occurs. Row `0` is a boundary, so this condition flips the direction:

```python
if i == 0 or i == numRows - 1:
    k = -k
```

The initial `-1` therefore becomes `1`, and the next row is `1`. This compact initialization avoids a separate “first step” branch.

At the bottom row, negating `1` gives `-1`, so movement turns upward. At the top row, negating `-1` gives `1`, so it turns downward. At an interior row, the direction stays unchanged.

The order inside the loop is deliberate:

```python
g[i].append(c)
if i == 0 or i == numRows - 1:
    k = -k
i += k
```

The character belongs to the current row, so it is appended before `i` changes. The direction is changed while still standing on a boundary, and only then is the next row calculated. This guarantees that `i` remains between `0` and `numRows - 1` whenever another character is processed.

**Walk through the first cycle**

For `s = "PAYPALISHIRING"` and `numRows = 3`, the row path is `0, 1, 2, 1, 0, 1, 2, 1, ...`.

| Character | Current row `i` | Row lists after append | Boundary action | Next row |
|:---:|---:|---|---|---:|
| `P` | `0` | `P / /` | flip `k` to `1` | `1` |
| `A` | `1` | `P / A /` | none | `2` |
| `Y` | `2` | `P / A / Y` | flip `k` to `-1` | `1` |
| `P` | `1` | `P / AP / Y` | none | `0` |
| `A` | `0` | `PA / AP / Y` | flip `k` to `1` | `1` |

Continuing the same movement produces:

```text
row 0: P A H N
row 1: A P L S I I G
row 2: Y I R
```

The required result is the concatenation `"PAHNAPLSIIGYIR"`.

**Flatten rows only after every character is placed**

The final expression is

```python
''.join(chain(*g))
```

`chain(*g)` yields every character from row `0`, then every character from row `1`, and so on. `join` consumes that single flattened sequence and creates the output string once. It does not insert a separator because the joining string is empty.

This is more efficient and clearer than repeatedly adding characters to an immutable result string. It also matches the problem's reading rule exactly: complete the zigzag assignment first, then read rows from top to bottom.

**Why every character reaches the correct output position**

The boundary-flipping rule generates precisely the down-then-up zigzag row sequence. Each iteration consumes the next input character, so original order is preserved among characters written during the traversal. Appending to `g[i]` preserves left-to-right order within each row because later visits to a row occur farther right in the conceptual layout.

At the end, every input character appears in exactly one row list: the loop appends once per character, and it never copies or drops a character. Concatenating row lists in increasing row order is exactly how the zigzag must be read. The returned string therefore has the required row-major order and the same length and character multiset as `s`.

## Complexity detail

Let $n$ be `len(s)` and let $R$ be `numRows`.

- **Time complexity: $O(n+R)$.** Creating `R` empty row lists costs $O(R)$. The character loop performs $O(1)$ work for each of $n$ characters. Flattening and joining traverses the `R` row containers and emits all $n$ characters. When $R \le n$, this simplifies to the commonly stated $O(n)$ bound. The contract also allows $R > n$, so $O(n+R)$ is the exact two-parameter bound for this source.
- **Space complexity: $O(n+R)$.** The row lists collectively store all $n$ characters and have $R$ list objects. `chain` is lazy and does not create another flattened list, while the returned immutable string contains $n$ characters. Excluding the required output still leaves $O(n+R)$ row storage. Under the common assumption $R \le n$, the bound simplifies to $O(n)$, matching the manifest.

The scalar state `i`, `k`, and the current character uses $O(1)$ space. No two-dimensional matrix or blank placeholder cells are allocated.

## Alternatives and edge cases

- **Read indices by cycle arithmetic:** A full down-and-up cycle has length `2 * numRows - 2`. Visiting each row's vertical and diagonal indices directly avoids storing row buckets. It uses constant auxiliary state besides the result but requires more delicate index formulas.
- **Sparse matrix simulation:** Place characters into a `numRows`-by-columns grid and then scan all cells. It mirrors the picture literally but allocates many blank cells and may take $O(Rn)$ space and scanning time.
- **Repeated immutable-string concatenation:** Appending each output character with `result += c` is concise, but Python strings are immutable and the language-level worst case can repeatedly copy the prefix. Row lists plus one `join` provide a robust linear construction.
- **One row:** The early return avoids invalid movement and correctly leaves the string unchanged.
- **More rows than characters:** The pointer moves downward but never reaches the bottom before input ends. Each character occupies a different early row, and row concatenation returns the original string. This case also explains the explicit $O(n+R)$ initialization cost.
- **Rows equal to string length:** Every character occupies its own row, so reading rows returns `s` unchanged.
- **Two rows:** The path alternates `0, 1, 0, 1, ...`. Both boundaries are visited on every step, and the same direction flip logic remains valid.
- **A partial final cycle:** The loop stops when characters end; it does not need to complete the upward or downward path. The populated row lists already contain exactly the visible partial zigzag.
- **Punctuation:** Commas and periods are appended like letters. No character is treated as a separator or structural marker.
- **Case sensitivity:** Uppercase and lowercase characters retain their exact identity and order.
- **Input preservation:** The algorithm reads `s` and stores its characters in new lists; it never modifies the original string.
