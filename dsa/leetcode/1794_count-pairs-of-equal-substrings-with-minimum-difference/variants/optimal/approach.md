## General

**Long equal substrings can never create a better difference than their first characters**

A valid quadruple `(i, j, a, b)` selects equal nonempty substrings. Equal substrings have the same length, so for some $L\geq1$,

$$
j=i+L-1
\quad\text{and}\quad
b=a+L-1.
$$

The quantity being minimized is

$$
j-a=i-a+L-1.
$$

Because the substrings are equal, their first characters are equal:

`firstString[i] == secondString[a]`.

Those two matching characters alone form another valid quadruple, `(i, i, a, a)`, whose difference is `i - a`. For $L>1$, this single-character difference is smaller by $L-1$.

Therefore, no multi-character substring can attain the global minimum. If it supposedly did, its matching first characters would produce an even smaller valid value, a contradiction. Every quadruple that achieves the true minimum must have length one, with `i = j` and `a = b`.

This observation removes all actual substring comparison from the task. The problem reduces to finding pairs of equal characters, one from each string, that minimize `i - a`, and counting how many pairs attain that minimum.

**For a fixed first-string index, use the latest matching second-string index**

Fix index $i$ in `firstString` and let its character be $c$. Among all positions $a$ where `secondString[a] == c`, the value `i - a` becomes smaller as $a$ becomes larger. Thus only the last occurrence of $c$ in `secondString` can be optimal for this $i$.

The dictionary comprehension

`{c: i for i, c in enumerate(secondString)}`

builds exactly that information. When a character repeats, the later assignment overwrites the earlier one. At completion, `last[c]` is the greatest index containing $c$.

Earlier occurrences never need to be retained. For the same $i$, each would subtract a smaller $a$ and produce a strictly larger difference. It could not tie the candidate using `last[c]`.

**Scan the first string and maintain the global minimum**

The solution initializes `mi` to positive infinity and `ans` to zero. It then visits each pair `(i, c)` in `firstString`.

If $c$ does not exist in `last`, there is no equal character in the second string and therefore no valid length-one pair for this index.

Otherwise, the best difference involving this $i$ is

`t = i - last[c]`.

Three cases update the running answer:

- if `t < mi`, a new smaller global value has been found, so `mi` becomes `t` and `ans` resets to one;
- if `t == mi`, this first-string index creates another distinct minimizing quadruple, so `ans` increases by one;
- if `t > mi`, it contributes nothing to the minimum count.

Differences may be negative. A late position in `secondString` can make $a>i$, giving `i - a < 0`. "Minimum" means the numerically smallest value, so negative candidates are correctly preferred. Infinity initialization allows the first actual candidate, regardless of sign, to establish the baseline.

**Following the first example**

For `firstString = "abcd"` and `secondString = "bccda"`, the last positions are: `a -> 4`, `b -> 0`, `c -> 2`, and `d -> 3`.

The first-string candidates are:

- character `a` at index 0 gives `0 - 4 = -4`;
- `b` at index 1 gives `1 - 0 = 1`;
- `c` at index 2 gives `2 - 2 = 0`;
- `d` at index 3 gives `3 - 3 = 0`.

The minimum is -4 and occurs once, corresponding to `(0, 0, 4, 4)`. The function returns one.

For `"ab"` and `"cd"`, neither first-string character appears in the second string. No candidate is formed, `ans` remains zero, and the returned count correctly reports that no valid quadruple exists.

**Why each counted candidate corresponds to exactly one quadruple**

For a scanned index $i$ with minimum candidate, the second-string index is uniquely `last[c]`. The corresponding quadruple is

`(i, i, last[c], last[c])`.

Different first-string indices give different quadruples, even if their characters are the same. For one fixed $i$, no earlier matching second-string position can tie because it gives a larger `i - a`. Multi-character substrings cannot tie because dropping to their first character makes the difference strictly smaller.

Thus incrementing `ans` once per first-string index whose best candidate equals `mi` counts every and only globally minimizing quadruples.

**Why the reduction and scan are correct**

Every valid multi-character quadruple is dominated by its length-one first-character quadruple, so a global minimizer must be a character pair. For each first-string position, choosing the last matching second-string position produces the smallest character-pair difference involving that position. The scan compares all such per-position minima and counts all ties at the global minimum. These facts jointly prove the returned count.

## Complexity detail

Let $n$ be the length of `firstString` and $m$ the length of `secondString`. Building `last` takes $O(m)$ time, and scanning the first string takes $O(n)$ expected time with expected $O(1)$ dictionary operations. Total expected time is $O(n+m)$.

Both strings contain only lowercase English letters, so `last` has at most 26 entries. Auxiliary space is therefore $O(1)$ under the fixed alphabet, matching the manifest. For an unbounded alphabet with $U$ distinct second-string characters, the generalized space bound would be $O(U)$.

No substrings are materialized, hashed, or compared; all work is on individual character positions.

## Alternatives and edge cases

- **Enumerate all substring pairs:** There are quadratically many substrings in each string, making direct comparison far beyond the constraints.
- **Rolling hashes or suffix structures:** They accelerate substring equality but are unnecessary because every optimum has length one.
- **Store every occurrence per character:** Only the largest second-string index can minimize `i - a` for a fixed $i$; earlier positions are dominated.
- **Use the first occurrence:** This maximizes rather than minimizes the subtraction target and can produce the wrong result.
- **No shared character:** No valid equal substring exists, so the answer remains zero.
- **Negative minimum:** It is valid and often desirable when a matching character occurs much later in `secondString`.
- **Repeated character in the second string:** Dictionary overwriting intentionally retains its latest occurrence.
- **Repeated character in the first string:** Different indices may create different candidates and can both count if they tie globally.
- **Single-character strings:** Matching characters produce one quadruple; different characters produce zero.
- **Long equal substrings:** They remain valid quadruples, but their $L-1$ addition prevents them from minimizing.
- **Tie reset:** Finding a smaller `t` must reset `ans` to one because previously counted candidates no longer attain the minimum.
- **Tie increment:** Equal `t` values arise from distinct first indices and therefore represent distinct quadruples.
- **Lowercase guarantee:** It turns dictionary storage into constant space despite potentially long strings.
- **Input preservation:** The solution reads both strings and never constructs or modifies substring data.
