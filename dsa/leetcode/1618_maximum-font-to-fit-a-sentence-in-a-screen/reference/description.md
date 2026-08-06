## Description

Given a string `text`, display it on a screen of maximum width `w` and maximum height `h`. Select an integer font size from the array `fonts`, which contains the available font sizes sorted in strictly ascending order.

The rendered metrics of any character at a chosen font size are accessible via the `FontInfo` interface:

```java
interface FontInfo {
    // Returns the width of character ch on the screen using font size fontSize.
    public int getWidth(int fontSize, char ch);

    // Returns the height of any character on the screen using font size fontSize.
    public int getHeight(int fontSize);
}
```

For a given font size `fontSize`, the calculated total width of `text` rendered on a single line is the sum of `getWidth(fontSize, text[i])` across all character indices $0 \le i < \text{text.length}$. The calculated height of `text` at that font size is `getHeight(fontSize)`.

The `FontInfo` interface guarantees deterministic responses for identical parameters. Furthermore, font height and individual character widths are non-decreasing functions of font size:

$$
\text{getHeight}(\text{fontSize}) \le \text{getHeight}(\text{fontSize} + 1)
$$

$$
\text{getWidth}(\text{fontSize}, ch) \le \text{getWidth}(\text{fontSize} + 1, ch)
$$

Find the maximum font size from `fonts` that allows `text` to be displayed entirely on a single line within the screen limits `w` and `h`. If `text` cannot fit on the display with any available font size, return `-1`.
