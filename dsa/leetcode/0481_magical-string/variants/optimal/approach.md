## General
**Seed the self-describing prefix**

The magical string begins `1, 2, 2`. Starting at index two, each existing symbol says how many copies belong to the next generated run. A read pointer consumes these run lengths while the output list grows.

**Alternate the generated symbol**

The initial next symbol is `1`. Append it either once or twice according to the current run-length symbol, advance the read pointer, and toggle between `1` and `2` using `3 - symbol`. Continue until at least `n` symbols exist.

**Why generation remains synchronized**

Every read entry corresponds to exactly one maximal run in output order. Appending its requested count and toggling guarantees adjacent runs use different symbols. Inductively, the consumed run-length sequence equals the generated prefix, preserving the defining property.

**Count only the requested prefix**

The final run may extend past position `n`. Slice or inspect only the first `n` entries when counting ones so the extra generated symbol is not included.

## Complexity detail
Each generated symbol is appended once and only a constant number beyond `n` are needed, giving $O(n)$ time. The generated prefix uses $O(n)$ space.

## Alternatives and edge cases
- **Count ones during append:** avoids a final scan by incrementing only for positions below `n`.
- **Generate from scratch for every prefix length:** is correct but repeats earlier construction and takes $O(n^2)$ total work.
- **String-character storage:** works like an integer list but requires conversions for run lengths.
- **$n = 0$:** the empty prefix contains no ones.
- **$n \le 3$:** return the count from the seed prefix without reading beyond it.
- **Overshooting final run:** exclude appended positions at indices `n` and above.
- **Run length values:** the construction uses only one or two, matching the alphabet of the magical string.
