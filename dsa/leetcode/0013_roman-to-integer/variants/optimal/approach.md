## General

**A symbol's next neighbor determines whether it adds or subtracts**

Most Roman symbols are written from larger value to smaller value and are added. The six subtractive forms are exactly the places where a smaller symbol occurs immediately before a larger one:

```text
IV, IX, XL, XC, CD, CM
```

Therefore a symbol at index `i` contributes

$$
\begin{cases}
-\text{value}(s[i]), & \text{if value}(s[i]) < \text{value}(s[i+1]), \\
+\text{value}(s[i]), & \text{otherwise}.
\end{cases}
$$

The final symbol has no larger symbol after it and is always added. This local sign rule converts a subtractive pair such as `IV` into $-1+5=4$ while treating an additive sequence such as `VIII` as $5+1+1+1=8$.

**Map the seven letters to their numerical values**

The dictionary `d` contains the fixed symbol table. Dictionary access makes each comparison and contribution constant time. The input is guaranteed to be a valid Roman numeral, so every character is a dictionary key and every increase corresponds to one of the permitted subtractive relationships. The method does not need to validate illegal strings such as `IC`.

**Use adjacent pairs without manual indices**

`pairwise(s)` yields

```text
(s[0], s[1]), (s[1], s[2]), ..., (s[n-2], s[n-1])
```

For each `(a, b)`, the generator expression chooses `-1` when `d[a] < d[b]` and `1` otherwise, then multiplies by `d[a]`:

```python
(-1 if d[a] < d[b] else 1) * d[a]
```

Every character except the last appears once as `a`, so every one of those symbols receives exactly one signed contribution. The separate `+ d[s[-1]]` supplies the final always-positive symbol.

**Trace `MCMXCIV` symbol by symbol**

| Current `a` | Next `b` | Comparison | Contribution |
|:---:|:---:|---|---:|
| `M` | `C` | `1000 >= 100` | `+1000` |
| `C` | `M` | `100 < 1000` | `-100` |
| `M` | `X` | `1000 >= 10` | `+1000` |
| `X` | `C` | `10 < 100` | `-10` |
| `C` | `I` | `100 >= 1` | `+100` |
| `I` | `V` | `1 < 5` | `-1` |
| final `V` | none | always add | `+5` |

The total is

$$
1000-100+1000-10+100-1+5=1994.
$$

Notice that a large symbol can be the positive half of a subtractive pair and still participate normally in the next comparison. The pairwise rule assigns a sign to each position, not a value to overlapping two-character substrings.

**Why the local contributions equal the numeral's value**

In a valid Roman numeral, an additive symbol contributes its own value. In a subtractive pair `ab`, the required value is `value(b) - value(a)`, which is exactly the sum of the two local contributions `-value(a) + value(b)`. The larger second symbol is added because it is not smaller than its next neighbor, or because it is the final symbol.

Every position belongs either to ordinary descending notation or to the smaller first half of one permitted pair. The rule handles both exhaustive cases, so summing all signed symbol values yields the represented integer.

The non-empty constraint makes `s[-1]` safe. For a one-character numeral, `pairwise(s)` is empty and the result is simply that character's value.

**Why looking only one position ahead is sufficient**

Subtraction in this Roman-numeral system is local. `I` can precede only `V` or `X`, `X` can precede only `L` or `C`, and `C` can precede only `D` or `M`. A valid numeral never asks one symbol to be subtracted from a nonadjacent symbol or from an entire later group. Therefore the comparison with `b` contains all information needed to assign `a`'s sign.

This matters in strings with several adjacent changes. In `XIX`, the first `X` is followed by the smaller `I`, so it contributes `+10`; that `I` is followed by the larger final `X`, so it contributes `-1`; the last `X` contributes `+10`. The result is `19`. The first `X` is not incorrectly grouped with the last `X`, because each position is classified using its immediate successor.

Likewise, `VIII` has comparisons `V >= I`, `I >= I`, and then a final positive `I`. Equal neighbors do not trigger subtraction. The exact strict inequality is therefore essential: replacing `<` with `<=` would wrongly negate repeated symbols.

## Complexity detail

Let $n$ be the Roman numeral length.

- **Time complexity: $O(n)$.** `pairwise` and `sum` examine each of the first `n - 1` symbols once, followed by one final lookup. Every dictionary access and comparison is constant time.
- **Space complexity: $O(1)$.** The seven-entry dictionary is fixed. `pairwise` and the generator are lazy, so they do not build a list of all pairs. Only a running sum and a constant number of references are needed.

The contract bounds `n` by `15`, making work absolutely bounded, but $O(n)$ accurately describes the scan and matches the manifest.

## Alternatives and edge cases

- **Consume subtractive pairs explicitly:** Scan with an index; when the current value is smaller than the next, add their difference and advance two positions. It is equally linear but needs variable pointer increments and an end check.
- **Scan right to left:** Start with the last value and subtract a current symbol when it is smaller than the symbol to its right. This expresses the same sign rule without `pairwise`.
- **Thirteen-token lookup:** Recognize the six two-character forms before falling back to one-character symbols. This is clear but uses substring/token checks rather than the simple value comparison.
- **One symbol:** The adjacent generator is empty and the last symbol is returned.
- **Pure additive notation:** No adjacent increase exists, so every symbol is added.
- **Several subtractive pairs:** Each smaller-left symbol is independently negated, as in `MCMXCIV`.
- **Repeated symbols:** Equal neighbors are added because the comparison is strict.
- **Invalid notation:** The algorithm may assign a numerical value to malformed input, but validation is outside the guaranteed contract.
- **Non-empty guarantee:** `d[s[-1]]` depends on at least one character, which the Reference guarantees.
- **Immediate-neighbor rule:** A symbol is never subtracted merely because some larger symbol appears later; only a larger next symbol changes its sign in valid canonical notation.
- **Strict comparison:** Equal repeated symbols remain additive, which is required for values such as `III`, `XXX`, and `CCC`.
