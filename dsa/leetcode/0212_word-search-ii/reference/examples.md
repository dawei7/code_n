## Examples

**Example 1**

```text
board                 valid paths
o  a  a  n            oath: (0,0) -> (0,1) -> (1,1) -> (2,1)
e  t  a  e            eat:  (1,3) -> (1,2) -> (1,1)
i  h  k  r
i  f  l  v
```

- Input: `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]`
- Output: `["eat","oath"]`

**Example 2**

```text
a -- b
|    |
c -- d

The path for "abcb" would have to use the b cell twice.
```

- Input: `board = [["a","b"],["c","d"]], words = ["abcb"]`
- Output: `[]`
