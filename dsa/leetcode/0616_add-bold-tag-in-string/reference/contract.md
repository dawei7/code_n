## Function Contract

**Inputs**

- `s`: the nonempty source string in which occurrences are located
- `words`: the array of distinct dictionary strings; the array itself may be empty

Let $N = \lvert\texttt{s}\rvert$ and let

$$
D = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

- Return a string containing all characters of `s` in their original order.
- Enclose every maximal span covered by one or more complete dictionary-word occurrences in `<b>` and `</b>`.
- Merge overlapping or consecutive covered spans into one tagged region.
- If no dictionary word occurs, return `s` unchanged.
