## Examples

**Example 1**

- Input: `lights = [0,0,0,0]`
- Output: `2`
- **Explanation:** One optimal plan installs a bulb at position `1`, illuminating `[0, 1, 2]`, and another at position `3`, illuminating `[2, 3]`. Every position is then visible, and one added bulb cannot cover all four positions, so the minimum is `2`.

**Example 2**

- Input: `lights = [0,0,0,2,0]`
- Output: `1`
- **Explanation:** The existing bulb at position `3` has radius `2` and illuminates positions `[1, 2, 3, 4]`. Installing one bulb at position `1` illuminates `[0, 1, 2]`, making the entire road visible. Thus exactly one additional bulb is required.
