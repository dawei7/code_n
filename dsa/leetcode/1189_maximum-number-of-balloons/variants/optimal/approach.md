## General
**Translate the word into resource requirements.** One copy of `"balloon"` consumes one `b`, one `a`, two `l` characters, two `o` characters, and one `n`. Count the occurrences of every character in `text`. Other letters never constrain the result and can be left unused.

**Measure how many copies each letter can support.** The counts of `b`, `a`, and `n` directly give their respective copy limits. Because each word needs two `l` characters and two `o` characters, their limits are `count["l"] // 2` and `count["o"] // 2`. The smallest of these five limits is attainable: reserving that many copies never asks for more of any required letter than is available. It is also an upper bound, because producing one additional word would exceed at least one limiting supply. Therefore that minimum is exactly the answer.

## Complexity detail
The single scan of the $n$ input characters takes $O(n)$ time, and evaluating the five resource limits takes constant time. Since `text` uses a fixed alphabet of 26 lowercase English letters, the frequency table occupies $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Repeated word removal:** Searching for and deleting one set of letters at a time is correct, but repeated searches and shifts can require $O(n^2)$ time.
- **Sort and group:** Sorting `text` makes equal letters adjacent, but costs $O(n\log n)$ time when direct counting is sufficient.
- **Missing required letter:** If any of `b`, `a`, `l`, `o`, or `n` is absent, its copy limit is zero and so is the answer.
- **Doubled requirements:** A single `l` or a single `o` cannot support a word; integer division correctly accounts for both repeated letters.
- **Surplus and irrelevant characters:** Extra required letters and letters outside `"balloon"` do not increase the result once another required letter is limiting.
- **Character ownership:** Every input occurrence contributes to at most one output word, which is exactly what the frequency subtraction implicit in the ratios enforces.
