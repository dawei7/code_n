## Function Contract

**Inputs**

- `color`: a seven-character lowercase RGB string in the form `"#ABCDEF"`.

The leading character is `#`; the remaining six characters encode the red, green, and blue bytes in hexadecimal. A valid returned channel must repeat one hexadecimal digit, so the expanded result has the form `"#XXYYZZ"` for some shorthand `"#XYZ"`.

**Return value**

- A six-digit shorthand-expressible color with maximum similarity to `color`. Any co-optimal answer is valid.
