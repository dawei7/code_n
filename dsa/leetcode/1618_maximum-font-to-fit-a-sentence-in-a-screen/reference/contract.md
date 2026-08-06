## Function Contract

**Inputs**

- `text`: A string of lowercase English letters ($1 \le \text{text.length} \le 10^5$).
- `w`: Maximum screen width ($1 \le w \le 10^5$).
- `h`: Maximum screen height ($1 \le h \le 10^5$).
- `fonts`: A strictly increasing array of available font sizes ($1 \le \text{fonts.length} \le 10^5$, $1 \le \text{fonts}[i] \le 10^5$).
- `fontInfo`: An object providing `getWidth(fontSize, ch)` and `getHeight(fontSize)` methods.

**Return value**

Return the maximum integer font size from `fonts` that allows `text` to fit within `w` and `h` on a single line, or `-1` if no font size fits.
