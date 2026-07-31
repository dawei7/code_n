## Examples

**Example 1**

- Input: `head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]`
- Output: `[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]`

```text
next:    (7) -> (13) -> (11) -> (10) -> (1) -> null
random:   |      |       |       |       |
         null   (7)     (1)     (11)    (7)
```

**Example 2**

- Input: `head = [[1, 1], [2, 1]]`
- Output: `[[1, 1], [2, 1]]`

```text
next:    (1) -> (2) -> null
random:   \------^      ^
                    \---/
Both random pointers target node 2.
```

**Example 3**

- Input: `head = [[3, null], [3, 0], [3, null]]`
- Output: `[[3, null], [3, 0], [3, null]]`

```text
next:    (3a) -> (3b) -> (3c) -> null
random:  null    |       null
                 +-----> (3a)
```
