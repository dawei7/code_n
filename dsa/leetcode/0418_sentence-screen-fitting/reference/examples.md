## Examples

In the layouts below, each `-` represents one empty screen position.

**Example 1**

- Input: `sentence = ["hello","world"], rows = 2, cols = 8`
- Output: `1`
- Explanation: One complete sentence occupies the two rows as follows.

```text
hello---
world---
```

**Example 2**

- Input: `sentence = ["a", "bcd", "e"], rows = 3, cols = 6`
- Output: `2`
- Explanation: Two complete repetitions fit in this layout.

```text
a-bcd-
e-a---
bcd-e-
```

**Example 3**

- Input: `sentence = ["i","had","apple","pie"], rows = 4, cols = 5`
- Output: `1`
- Explanation: The screen contains one complete repetition followed by the beginning of another.

```text
i-had
apple
pie-i
had--
```
