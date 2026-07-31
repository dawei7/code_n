## Examples

**Example 1**

- Input: `board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCCED"`
- Output: `true`

Numbers in the independent diagram mark the matching cell order:

```text
A1 B2 C3 E
S  F  C4 S
A  D6 E5 E
```

**Example 2**

- Input: `board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "SEE"`
- Output: `true`

```text
A B C E
S F C S1
A D E3 E2
```

**Example 3**

- Input: `board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCB"`
- Output: `false`

After following `A1 → B2 → C3`, no unused adjacent cell supplies the final `B`:

```text
A1 B2 C3 E
S  F  C  S
A  D  E  E
```
