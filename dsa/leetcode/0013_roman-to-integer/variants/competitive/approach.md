## General

**Add symbols immediately, then correct a previous symbol when necessary**

This implementation scans left to right. Normally it adds the current symbol's value. When the current value is larger than the previous value, the previous symbol was the subtractive half of a pair.

The previous iteration already added that smaller value positively. It should have contributed negatively instead. Changing a contribution from $+v$ to $-v$ requires subtracting $2v$:

$$
(+v)-2v=-v.
$$

That explains the update

```python
decimal += current_value - 2 * previous_value
```

The current value is added, and twice the prior value reverses the sign of the contribution already in `decimal`.

**The ordinary branch handles descending or equal values**

At index zero there is no previous symbol, so the first value is added. At later positions, if the current value is no greater than the previous value, no subtractive relationship ends here and the code simply adds the current value.

The complete condition is

```python
if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
```

`i > 0` protects the previous-index access. The strict greater-than test leaves repeated symbols additive.

**Trace the correction on `IV`**

1. At `I`, add `1`; `decimal = 1`.
2. At `V`, detect `5 > 1` and add `5 - 2 * 1 = 3`.
3. The final total is `1 + 3 = 4`, which is algebraically the intended `-1 + 5`.

For `XC`, the same logic starts with `+10` and then adds `100 - 20 = 80`, producing `90`.

**Trace the complete example `MCMXCIV`**

| Index/symbol | Rule | Change | Running total |
|---|---|---:|---:|
| `0: M` | first symbol | `+1000` | `1000` |
| `1: C` | descending | `+100` | `1100` |
| `2: M` | increase; correct `C` | `+1000 - 200` | `1900` |
| `3: X` | descending | `+10` | `1910` |
| `4: C` | increase; correct `X` | `+100 - 20` | `1990` |
| `5: I` | descending | `+1` | `1991` |
| `6: V` | increase; correct `I` | `+5 - 2` | `1994` |

Although the smaller symbol is corrected one iteration later, the running total after the larger symbol contains exactly the pair value.

**Why every valid symbol gets the correct sign**

Every symbol is initially added on its own iteration. If it is immediately followed by a larger symbol, the next iteration subtracts it twice and changes its net contribution to negative. If it is not followed by a larger symbol, no later step changes it, so it remains positive.

Valid Roman notation uses precisely this adjacent-increase pattern for the six subtractive forms. Therefore each position receives the same sign it would receive in the mathematical expansion, and `decimal` ends as the represented integer.

The method relies on the validity guarantee; it decodes adjacent increases mechanically rather than rejecting illegal forms.

**Why subtracting twice does not also damage the current symbol**

The correction is added as one combined quantity, but its algebra separates cleanly. Suppose the running total before the previous symbol was `T`, the previous value is `a`, and the larger current value is `b`. After the previous iteration the total is `T + a`. The current branch produces

$$
(T+a)+(b-2a)=T-a+b.
$$

Only the previous contribution changes sign. The current value `b` remains fully positive, exactly as the subtractive pair requires. This is why the multiplier is `2`, not `1`: subtracting only one previous value would merely cancel it and incorrectly make the pair worth `b` instead of `b-a`.

After the correction, `b` may still be compared with the following symbol on the next iteration. That causes no double counting. Its positive contribution is already in the total, and it is corrected later only if it itself is the smaller first symbol of another valid adjacent increase. Canonical validity prevents ambiguous malformed chains, so the one-step retrospective rule remains sufficient.

For an additive sequence such as `LVIII`, no current symbol is larger than its predecessor. The correction branch never runs, and the method simply accumulates `50 + 5 + 1 + 1 + 1 = 58`.

## Complexity detail

Let $n = \lvert s\rvert$.

- **Time complexity: $O(n)$.** The `for` loop visits every symbol once. Each iteration performs a constant number of fixed-map lookups, comparisons, and arithmetic operations.
- **Space complexity: $O(1)$.** The seven-symbol map has fixed size, and the method stores only the running total and loop index beyond the input.

The length is at most `15` for the guaranteed range, but the linear bound describes the algorithm's direct dependency on numeral length.

## Alternatives and edge cases

- **Look ahead and assign signs directly:** Subtract a current symbol when it is smaller than the next, then add the final symbol. This avoids retroactive arithmetic and is used by the Optimal variant.
- **Consume a pair at once:** Add `next - current` and advance by two for an increase; otherwise add one symbol and advance by one.
- **Right-to-left scan:** Compare each symbol with the one already processed to its right, subtracting smaller values and adding the rest.
- **One-character numeral:** The first-symbol branch adds it, and the loop ends.
- **Repeated symbols:** Equal values do not trigger correction and are added normally.
- **Subtractive pair at the beginning or end:** The previous-value correction works at any nonzero index, including the final character.
- **Several subtractive pairs:** Each increase independently corrects exactly its immediate predecessor.
- **Valid-input guarantee:** The code does not verify repetition limits or whether an increase is one of the six authorized pairs.
- **All symbols known:** Every legal character is present in `numeral_map`; no missing-key branch is required.
- **Input preservation:** The string is read sequentially and never changed.
- **Why the factor is two:** One copy cancels the earlier positive contribution and the second copy makes it negative; using a factor of one would overvalue every subtractive pair.
- **Pure additive numeral:** If values never increase, the method reduces to a straightforward sum of all mapped symbols.
