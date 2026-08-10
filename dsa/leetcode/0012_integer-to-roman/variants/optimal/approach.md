## General

**Treat subtractive pairs as complete Roman tokens**

Canonical Roman notation uses seven one-character symbols plus six allowed subtractive pairs. The solution places all thirteen tokens in descending numerical order:

| Value | Token | Value | Token |
|---:|:---:|---:|:---:|
| `1000` | `M` | `900` | `CM` |
| `500` | `D` | `400` | `CD` |
| `100` | `C` | `90` | `XC` |
| `50` | `L` | `40` | `XL` |
| `10` | `X` | `9` | `IX` |
| `5` | `V` | `4` | `IV` |
| `1` | `I` |  |  |

The two tuples `cs` and `vs` store these tokens and values at matching positions. `zip(cs, vs)` therefore yields pairs such as `('M', 1000)`, then `('CM', 900)`, down through `('I', 1)`.

Including `900`, `400`, `90`, `40`, `9`, and `4` directly is the key simplification. The main loop does not need separate logic for numbers whose decimal place begins with four or nine; it selects `CM`, `CD`, `XC`, `XL`, `IX`, or `IV` just like any other largest fitting token.

**Choose the largest token that fits the remaining value**

For each descending pair `(c, v)`, the loop appends the token while its value can still be subtracted:

```python
while num >= v:
    num -= v
    ans.append(c)
```

At every append:

- `c` represents exactly `v`;
- subtracting `v` maintains the unrepresented remainder;
- appending tokens in descending scan order keeps the Roman numeral in canonical high-to-low order.

If `v` is too large, the loop performs zero iterations and the scan moves to the next smaller token. If it fits several times, the method uses it repeatedly before considering anything smaller. Under the range up to `3999`, `M`, `C`, `X`, and `I` can each appear at most three times in their additive role. Five-unit symbols do not repeat because the next lower tokens consume the remainder according to the canonical table.

**Why greedy selection creates the required decimal-place forms**

The token list encodes every special boundary at which ordinary repetition would become noncanonical.

- A remainder from `1` through `3` uses one to three `I` tokens; `4` selects `IV`; `5` selects `V`; `6` through `8` select `V` followed by `I` tokens; `9` selects `IX`.
- The same structure is scaled by ten for `X`, `XL`, `L`, and `XC` in the tens place.
- It is scaled by one hundred for `C`, `CD`, `D`, and `CM` in the hundreds place.
- The thousands place uses up to three `M` tokens because `num <= 3999`.

Since tokens are processed from largest to smallest, a lower decimal place cannot be used prematurely to replace an available canonical higher-place form. For example, remainder `49` does not become `IL`: `40` is selected as `XL`, leaving `9`, which is selected as `IX`. The result is `XLIX`, respecting the rule that conversion is based on decimal places.

**Trace `3749` from remainder to result**

The result list begins empty.

| Current token | Remainder before | Copies appended | Remainder after | Output so far |
|---|---:|---:|---:|---|
| `M = 1000` | `3749` | `3` | `749` | `MMM` |
| `CM = 900` | `749` | `0` | `749` | `MMM` |
| `D = 500` | `749` | `1` | `249` | `MMMD` |
| `C = 100` | `249` | `2` | `49` | `MMMDCC` |
| `XL = 40` | `49` | `1` | `9` | `MMMDCCXL` |
| `IX = 9` | `9` | `1` | `0` | `MMMDCCXLIX` |

Tokens skipped in the table do not fit the current remainder. Once `num` reaches zero, every later `while num >= v` condition is false. Joining `ans` yields the expected `"MMMDCCXLIX"`.

**Why the value and format remain exact**

At every moment,

$$
\text{original input}
= \text{value of tokens in `ans`} + \texttt{num}.
$$

This is true initially because `ans` is empty. Every iteration appends a token worth `v` and subtracts the same `v`, preserving the equality. The `I = 1` token guarantees that a positive remainder can always be reduced to zero, so the final token values sum exactly to the input.

Canonical form follows from the descending greedy choice and the complete subtractive-token table. Whenever a token fits, using smaller tokens instead would either begin with a lower-valued symbol or create a forbidden fourfold repetition that one of the included subtractive tokens replaces. The method therefore constructs the accepted largest-token-first representation for each decimal place.

**Build with a list and join once**

`ans.append(c)` stores whole tokens, including two-character pairs such as `CM`. The final

```python
''.join(ans)
```

concatenates them without separators. Using a list avoids repeatedly copying an immutable growing string and keeps the representation of a subtractive pair visibly atomic during construction.

## Complexity detail

Under the stated range `1 <= num <= 3999`:

- **Time complexity: $O(1)$.** The outer table has exactly thirteen entries, and a canonical result has bounded length (at most fifteen Roman letters, as in `3888 -> MMMDCCCLXXXVIII`). The total number of successful `while` iterations is therefore bounded by a constant independent of a growing input parameter.
- **Space complexity: $O(1)$.** The two thirteen-entry tuples are fixed, and `ans` has a bounded number of tokens under the contract. The returned string is also bounded. Excluding output, all storage is constant.

For a hypothetical unbounded extension that kept only these symbols and allowed unlimited `M` repetition, repeated subtraction would take $O(\texttt{num}/1000)$ successful iterations and output space of the same order. The constant bounds rely on the explicit maximum `3999`.

## Alternatives and edge cases

- **Use `divmod` per token:** Compute `count, num = divmod(num, v)` and append `c * count`. This reduces each table entry to one division and makes the number of outer iterations visibly fixed; it produces the same canonical sequence.
- **Hardcode each decimal digit:** Use lookup arrays for thousands, hundreds, tens, and ones, then concatenate four entries. This is also constant time but less flexible if the symbol system or supported range changes.
- **Handle 4 and 9 with branches:** One can convert each decimal place using separate cases. Treating subtractive pairs as tokens produces simpler uniform greedy code.
- **Omit subtractive tokens:** A greedy scan of only `I,V,X,L,C,D,M` would generate noncanonical forms such as `IIII` and `VIIII`. The six pairs are required.
- **Minimum input `1`:** Every larger token is skipped and one `I` is appended.
- **Maximum input `3999`:** Produces `MMMCMXCIX` without requiring a symbol above `M`.
- **Pure additive digit:** `8` becomes `VIII`: one `V` and three `I` tokens.
- **Subtractive boundary:** `4`, `9`, `40`, `90`, `400`, and `900` are each consumed by one explicit pair token.
- **Mixed decimal places:** `49` becomes `XLIX`, not `IL`, because the descending table respects independent tens and ones forms.
- **No zero input:** The contract starts at `1`, so the method never needs to define a Roman representation for zero.
- **Input preservation:** The local integer variable `num` is reduced, but integers are immutable and the caller's value is unaffected.
