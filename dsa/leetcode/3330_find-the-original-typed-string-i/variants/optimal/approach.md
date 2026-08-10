## General

**No mistake is always one valid explanation.** Alice may have made the long-press mistake at most once, which includes making it zero times. Therefore the displayed `word` itself is always a possible intended string. The source's initial constant one counts this explanation.

**A long press can only explain a repeated run.** If one intended occurrence of character $c$ was held too long, the final output contains additional copies adjacent to that occurrence. It cannot create separated copies or change another character. Therefore possible mistakes are completely contained inside maximal runs of equal characters.

Suppose a displayed run has length $L$. If the mistake occurred in this run, its intended length can be $1,2,\ldots,L-1$. These are $L-1$ distinct original strings. Intended length $L$ is the no-mistake explanation already counted globally.

For displayed run `"cccc"`, possible mistaken originals have one, two, or three `c` characters in that position. The exact identity of which repeated physical copy came from the long press is irrelevant: equal characters yield the same original string, so possibilities are distinguished by intended run length, not by deletion position.

**Adjacent equal pairs count run contributions.** A run of length $L$ contains exactly $L-1$ adjacent equal pairs. Summing `x == y` over `pairwise(word)` therefore adds precisely the total mistaken possibilities across all runs.

Python treats Boolean `True` as integer one and `False` as zero in `sum`. The expression

`1 + sum(x == y for x, y in pairwise(word))`

is consequently identical to one plus $\sum(L-1)$ over repeated runs.

For `"abbcccc"`, the `bb` run contributes one and the `cccc` run contributes three. Adding the unchanged word gives five, matching `"abbcccc"`, three shorter `c`-run versions, and the shorter `b`-run version.

**Why possibilities from different runs do not overlap.** Only one long-press mistake is permitted. A possibility shortens either no run or exactly one run. Shortening different character runs changes different positions or different characters in the resulting string, so the resulting intended strings are distinct. Contributions may therefore be added without inclusion-exclusion.

**Why one adjacent pair represents one possible shorter length.** Within a run, the first character contributes no equal predecessor. Each later position adds one to the pair count. These $L-1$ later positions can be put in one-to-one correspondence with intended run lengths from one through $L-1$. The source does not literally delete that later position; the Boolean count is a compact arithmetic representation of the number of lengths.
Every reported possibility is valid: the unchanged word uses no mistake, and shortening one run from $L$ to any positive smaller length can produce the displayed run by holding one occurrence long enough. Conversely, any legal mistaken original differs from the output in exactly one run and has one of those $L-1$ smaller positive lengths. The adjacent-pair sum counts it. Thus no possibility is missing or duplicated.

The source assumes `pairwise` is imported from `itertools` and a Python version that provides it. `pairwise(word)` lazily yields neighboring pairs $(word[i-1],word[i])$ without constructing a separate list.

## Complexity detail

For a word of length $n$, `pairwise` yields $n-1$ pairs and each equality test is constant-time. Total time is $O(n)$. The generator and running sum use $O(1)$ auxiliary space. The result is one integer.

No substring or alternate original string is materialized, which is why space remains constant even though several possibilities are counted.

## Alternatives and edge cases

- **Run-length scan:** Explicitly find every maximal run and add its length minus one. It has the same bounds and may make the combinatorial reasoning more visible.
- **Generate all candidate strings:** Removing different counts from each run can verify the idea but allocates $O(n^2)$ total text unnecessarily.
- **All characters distinct:** There are no equal adjacent pairs, so only the unchanged word is possible.
- **Entire word one run:** A length-$n$ run gives $n-1$ mistaken originals plus the unchanged word, totaling $n$.
- **Single-character word:** `pairwise` yields nothing, and the answer is one.
- **Several repeated runs:** Their $L-1$ contributions add because at most one run changes in any candidate.
- **One mistake, not exactly one:** The leading one is essential to include the no-mistake case.
- **Deleting a whole run:** Intended run length cannot be zero, because the displayed character must originate from a pressed key.
- **Different deletion positions in one run:** Equal characters make them the same intended string, so they must not be counted separately.
- **Nonadjacent equal letters:** They belong to different runs and cannot be produced as one continuous long press.
- **Import requirement:** `pairwise` requires `from itertools import pairwise` or an equivalent harness import.
- **Boolean arithmetic:** `sum` counts true comparisons because Python Booleans are integer-compatible.
- **Input preservation:** The method only iterates over the immutable string and creates no modified candidates.
- **Run boundaries:** A change from one letter to another contributes false, correctly separating two independent runs instead of treating nearby repeated letters as one long press.
