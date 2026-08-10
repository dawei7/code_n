## General

**Process one maximal group at a time**

A group is a maximal run of equal adjacent characters. The answer needs the inclusive start and end indices of every run whose length is at least three.

The two-pointer solution maintains:

- `i` as the first index of the current group;
- `j` as the first index after that group.

Once `j` is known, the group occupies the half-open interval `[i,j)`. Its length is `j-i`, and its inclusive final index is `j-1`.

**Find the right boundary**

At the start of each outer-loop iteration, `i < n` and therefore `s[i]` is the character defining the new group. The code sets `j = i` and advances while

`j < n and s[j] == s[i]`.

Every position passed by `j` contains the group character. The loop stops for exactly one of two reasons:

- `j == n`, so the group reaches the end of the string;
- `s[j] != s[i]`, so index `j` begins the next group.

Therefore, all indices from `i` through `j-1` belong to the group, and the run cannot be extended farther right. It is also maximal on the left because `i` was set to the end boundary of the preceding group, or zero for the first group.

**Record only large groups**

The test `j - i >= 3` implements the definition of large. When it succeeds, the code appends `[i, j - 1]`.

Subtracting one is necessary because `j` is exclusive while the output interval's end is inclusive. For a run beginning at 3 and stopping before index 7, the length is `7-3=4` and the reported interval is `[3,6]`.

Groups of length one or two are fully scanned but not appended.

**Advance directly to the next group**

After evaluating the current run, `i = j` makes the first different character—or the end of the string—the next outer-loop position.

No character is reconsidered as part of a later group. Although one loop is nested inside another, both pointers move only forward. This is a linear scan, not quadratic work.

**Why output order is automatic**

The outer loop discovers groups from left to right, and appends a large group immediately when it finishes. Consequently, intervals enter `ans` in increasing start-index order. No separate sort is needed.

For `s = "abbxxxxzzy"`:

- `"a"` spans `[0,0]` and is skipped;
- `"bb"` spans `[1,2]` and is skipped;
- `"xxxx"` spans `[3,6]` and is appended;
- `"zz"` and `"y"` are skipped.

The result is `[[3,6]]`.

**Why every and only valid group is returned**

Each outer iteration identifies one maximal equal-character run because `j` advances to the first different character. Every string index belongs to exactly one such run, so no group is skipped or split.

The length comparison accepts exactly runs containing three or more characters. The reported endpoints are their true inclusive boundaries. Since each accepted run is appended once in traversal order, the output contains every large group exactly once and is already sorted as required.

## Complexity detail

Let `n = len(s)`. Pointer `j` advances across every character once in total, while `i` jumps from one group boundary to the next. All work besides pointer movement and output appends is constant. The time complexity is `O(n)`.

If `g` large groups are found, the returned list stores `g` two-integer intervals, so output space is `O(g)`. Apart from the required result, only `i`, `j`, `n`, and a few temporary values are stored, giving `O(1)` auxiliary working space.

No sorting cost is present because discovery order already matches the requested order.

## Alternatives and edge cases

- **Run-length encoding:** Build character/count/start triples, then filter counts at least three. It is correct but stores information for every group when only large intervals are needed.

- **Track a start and detect boundary events in one loop:** This is equivalent and can use a sentinel at the end. The exact two-pointer form makes the exclusive boundary explicit.

- **Check every length-three window:** It can detect that a large run exists but needs additional logic to merge overlapping windows and find maximal endpoints.

- **Whole string is one large group:** `j` reaches `n`, and `[0,n-1]` is appended.

- **No large group:** Every run has length one or two, so `ans` remains empty.

- **Length exactly three:** The `>= 3` condition includes it.

- **Length two:** It is rejected even though its characters repeat.

- **Large group at the beginning:** Initial `i = 0` reports the correct start without a special case.

- **Large group at the end:** The `j < n` guard stops safely at `n`, and `j-1` is the final string index.

- **Several adjacent groups are large:** A character change ends one group and starts the next; both are appended separately.

- **Single-character string:** One length-one group is scanned and rejected, returning an empty list.

- **Inclusive output boundary:** The internal interval is `[i,j)`, so the output must use `j-1` rather than `j`.

- **Input immutability:** Both pointers are integers; the string is only read.
