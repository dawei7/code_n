## Examples

**Example 1**

- Input: `rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]`
- Output: `true`
- Explanation: All five rectangles tile one rectangular region exactly.

The first source coordinate illustration is represented below; labels identify the five input rectangles.

```text
y=4  +---+---+---+
     | D | E | C |
y=3  +---+---+   |
     |       |   |
y=2  |   A   +---+
     |       | B |
y=1  +-------+---+
      x=1 2   3   4
```

**Example 2**

- Input: `rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]`
- Output: `false`
- Explanation: A vertical gap separates the two covered regions.

The second source illustration exposes that uncovered gap:

```text
y=4  +---+   +---+
     |   |   |   |
y=3  +---+   |   |
     |   |   +---+
y=2  |   |   |   |
     |   |   |   |
y=1  +---+   +---+
      x=1 2   3   4
```

**Example 3**

- Input: `rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]`
- Output: `false`
- Explanation: Two rectangles overlap over the region from `(2,2)` to `(3,3)`.

The hatched cell in the third source illustration marks the overlap:

```text
y=4  +---+-------+
     |   |       |
y=3  +---+###    |
     |   |###    |
y=2  |   +-------+
     |       |   |
y=1  +-------+---+
      x=1 2   3   4
```
