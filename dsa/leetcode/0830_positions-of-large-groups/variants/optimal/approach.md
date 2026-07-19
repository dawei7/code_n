## General
**Keep the start of the current maximal run**

Initialize `run_start = 0` and scan an `end` position from `1` through `len(s)`. A run ends when `end == len(s)` or `s[end] != s[run_start]`. The explicit end-of-string boundary acts like a sentinel and lets the last group follow the same logic as every interior group without indexing beyond the string.

**Record the run before advancing to the next one**

At a boundary, the current group occupies `run_start` through `end - 1` and has length `end - run_start`. Append `[run_start, end - 1]` only when that length is at least `3`, then execute `run_start = end` to begin the next group.

**Why the scan reports exactly the requested intervals**

Between two detected boundaries, every character equals the character at `run_start`; immediately outside that interval is either the string boundary or a different character. The interval is therefore one complete maximal group. The scan processes boundaries from left to right, so each group is considered once and appended intervals are already ordered by start index. The length test includes precisely the groups meeting the large-group threshold.

## Complexity detail
Let $n$ be the string length and $g$ the number of returned large groups. The boundary pointer advances from `1` through $n$ once, so the time is $O(n)$. Apart from the required list of $g$ two-index intervals, the scan uses constant state; counting the returned output, the space is $O(g)$.

## Alternatives and edge cases
- **`itertools.groupby`:** Grouping consecutive characters and tracking a cumulative index is also $O(n)$ and concise, but manual boundaries make the inclusive indices explicit.
- **Regular-expression runs:** A pattern such as repeated-character backreferences can locate groups, though it adds engine-specific syntax for a simple linear scan.
- **Expand around every index:** Finding the full equal-character run separately for every position is correct with deduplication but can take $O(n^2)$ time.
- **Length exactly three:** The group qualifies because the threshold is at least three, not greater than three.
- **Run at either boundary:** Groups beginning at index `0` or ending at index `n - 1` must be reported normally.
- **One long run:** Return its single maximal interval rather than every qualifying subinterval.
- **No large group:** Return an empty list.
- **Inclusive endpoint:** Store `end - 1`, since `end` is the first index outside the completed run.
