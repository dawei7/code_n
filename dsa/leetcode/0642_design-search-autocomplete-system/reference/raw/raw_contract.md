## Function Contract

**Inputs**

- `sentences`: The historical sentences known when the system is constructed.
- `times`: The corresponding historical frequencies; `times[i]` belongs to `sentences[i]`.
- `c`: The single character supplied to an `input(c)` call.

Construct `AutocompleteSystem(sentences, times)` from the parallel history arrays. Ordinary lowercase letters and spaces extend the current sentence prefix. For each such character, `input` returns at most three matching historical sentences ordered by decreasing hot degree and then by increasing ASCII-code order.

When `c == '#'`, add the completed current sentence to the history or increase its existing frequency, clear the current search, and return `[]`. The next ordinary character begins a new search.

In the app-local operation trace, construction produces `null`, and each later result occupies the position of its corresponding `input` call.
