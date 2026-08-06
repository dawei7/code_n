## Function Contract

`solve(words: list[str], s: str) -> str`

Let $n$ be the length of `s`.

**Inputs**

- `words`: an array of lowercase keywords whose appearances must be bolded.
- `s`: the lowercase source string to annotate.

**Return value**

Return `s` with each maximal consecutive range covered by at least one complete keyword appearance enclosed in `<b>` and `</b>`. The tags must be properly paired and ordered, and the result must use the minimum possible number of tags.
