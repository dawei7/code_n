## General
**Separate the unread run from the write position**

Use `read` to locate the first character of the next run and advance `end` until the character changes. The run length is `end - read`. Independently maintain `write`, the first array position not yet occupied by compressed output.

**Write one character and only necessary count digits**

Write the run's character at `chars[write]`. A run of length one needs no count. For a longer run, convert the count to decimal and write each digit separately, so length twelve becomes characters `"1"` and `"2"`, not one multi-character element.

**Why unread input is never overwritten**

Every compressed run uses at most as many positions as its original run: one position for a singleton, or one character plus at most the number of run elements needed to represent the count. Thus `write` never advances beyond the processed boundary `end`, so writes cannot destroy characters belonging to a future run.

**Why the returned prefix is complete**

Each maximal run is discovered exactly once and emits its required encoding in original order. After assigning `read = end`, the next iteration begins at the next run. When `read` reaches `n`, `write` is exactly the compressed length and all meaningful output lies in `chars[:write]`.

## Complexity detail
The read boundary visits each input character once, and the total number of written characters is at most `n`, giving $O(n)$ time. Apart from the app's returned verification copy, the compression itself uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Build a separate compressed list:** is straightforward and linear but uses $O(n)$ additional space.
- **Repeatedly append by copying the accumulated output:** remains correct but can take $O(n^2)$ time when many singleton runs are emitted.
- **Single-character run:** write no count digit.
- **Multi-digit count:** write every decimal digit individually.
- **Alternating characters:** compression length equals the original length.
- **Entire array one run:** output one character followed by the run length's digits.
