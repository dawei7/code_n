# Roman Numerals - Optimal Approach

## Algorithm Explanation

Find the total number of characters saved by converting $1000$ Roman numerals in `roman.txt` to their minimal form.

### Subtractive Combination Reduction
In Roman numerals, non-minimal representations arise exclusively from un-subtracted runs of 4 identical symbols or 5-unit prefixes:
- `VIIII` ($9$) $\to$ `IX` (saves $3$ chars)
- `IIII` ($4$) $\to$ `IV` (saves $2$ chars)
- `LXXXX` ($90$) $\to$ `XC` (saves $3$ chars)
- `XXXX` ($40$) $\to$ `XL` (saves $2$ chars)
- `DCCCC` ($900$) $\to$ `CM` (saves $3$ chars)
- `CCCC` ($400$) $\to$ `CD` (saves $2$ chars)

Replacing any of these 6 patterns with a generic $2$-character replacement preserves length delta precisely.

### Strategy:
Run regex substitution `re.sub(r"VIIII|IIII|LXXXX|XXXX|DCCCC|CCCC", "XX", line)` across all lines and calculate total character reduction.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot L)$ where $N = 1000$ lines and $L \le 20$ chars. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(N \cdot L)$ - Input text buffer.
