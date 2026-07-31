## General

**Separate each initial from its suffix**

Place `idea[1:]` into one of 26 sets selected by `idea[0]`. For two initials
$a$ and $b$, a suffix present in both sets is unusable: attaching either
initial to it already forms an original idea.

**Count only suffixes unique to each initial**

Suppose the two sets contain $x$ and $y$ suffixes and share $c$. There are
$x-c$ suffixes exclusive to $a$ and $y-c$ exclusive to $b$. Pairing any
exclusive suffix from one side with any exclusive suffix from the other makes
both swapped names new. This gives $(x-c)(y-c)$ unordered selections.

Each such selection has two valid orientations, and their concatenated company
names differ in order, so add

$$
2(x-c)(y-c)
$$

for every unordered pair of initials.

A selection whose suffix is shared by the other initial necessarily recreates
an existing idea and is excluded. Conversely, two mutually exclusive suffixes
cannot form an existing swapped name, because membership in the opposite set
would contradict exclusivity. Thus the formula counts every and only valid
selection, with exactly its two ordered names.

## Complexity detail

Let $S$ be the total number of characters across `ideas`. Building the 26 hash
sets takes $O(S)$ expected time and space. There are only
$\binom{26}{2}$ initial pairs; set intersections collectively cost $O(S)$ up
to this fixed alphabet factor. Total expected time and auxiliary space are
$O(S)$.

## Alternatives and edge cases

- **Test every ordered pair:** Directly constructing both swapped names is correct but takes $O(n^2)$ pair checks.
- **Store whole names only:** A global set validates direct swaps, but without suffix grouping it does not avoid quadratic pair enumeration.
- **Shared suffix:** If two initials already occur with the same suffix, no pair using that suffix across those groups is valid.
- **Same initial:** Swapping equal first letters leaves both names unchanged, so such a pair can never qualify.
- **Ordered result:** Every valid unordered selection contributes two company names.
- **One-character ideas:** Their suffix is the empty string and participates in the same set logic.
- **Duplicate suffixes across many initials:** Each pair of initial groups excludes that suffix independently.
- **Large count:** The result can exceed 32-bit range, so fixed-width implementations need a 64-bit integer.
