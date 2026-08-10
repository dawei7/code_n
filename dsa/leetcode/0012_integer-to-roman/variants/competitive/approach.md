## General

**The intended method is descending greedy token selection**

`numeral_map` contains all seven base symbols and all six allowed subtractive pairs:

```text
1 I, 4 IV, 5 V, 9 IX,
10 X, 40 XL, 50 L, 90 XC,
100 C, 400 CD, 500 D, 900 CM, 1000 M
```

The keys are sorted and traversed in reverse, so the intended order is `1000, 900, 500, ... , 1`. For each value `key`, the algorithm is meant to append its token while that value still fits into the remaining `num`, subtracting `key` each time.

This is the same greedy principle as the Optimal variant: always choose the largest canonical token that does not exceed the remainder. Subtractive values are ordinary entries in the map, so cases such as `4`, `9`, and `900` do not need custom branches.

**What the nested loops are intended to mean**

Conceptually, the code aims to perform:

```python
while num > 0:
    for key in descending_values:
        while num >= key:
            num -= key
            append numeral_map[key]
```

The outer `while num > 0` is redundant for a correct descending scan, because the `for` loop includes key `1` and can reduce every legal positive input to zero in one pass. It nevertheless expresses the intended idea of continuing until no remainder exists.

`result` is a list, and the source uses

```python
result += numeral_map[key]
```

List `+=` with a string extends the list by individual characters. Appending `"CM"` therefore stores `"C"` and `"M"` separately rather than one token. Because the final operation is `"".join(result)`, the output characters are still identical to appending the whole token; this choice affects internal grouping, not the intended final text.

**The exact Python 3 source has a division defect**

The inner condition is actually written as

```python
while num / key > 0:
```

This code appears to come from Python 2, where dividing two integers with `/` performed integer division. Under those old semantics,

```text
num / key > 0
```

was equivalent to `num >= key` for positive integers.

Under Python 3, `/` performs true division and returns a floating-point quotient. Every positive `num / key` is greater than zero even when `key` is much larger than `num`. The very first key is `1000`, so input `3` behaves incorrectly:

1. `3 / 1000` is `0.003`, which is greater than zero.
2. The loop subtracts `1000`, making `num = -997`.
3. It adds `"M"` to the result.
4. The inner and outer loops then stop, returning `"M"` instead of `"III"`.

Thus the selected Competitive source does **not** implement the contract under the repository's Python 3 runtime. Replacing the condition with either

```python
while num >= key:
```

or

```python
while num // key > 0:
```

would restore the intended greedy behavior. This approach document explains the intended algorithm but does not represent the unchanged source as correct.

**How the corrected greedy process would convert `1994`**

Using the intended `num >= key` condition:

| Largest fitting key | Token | Remainder before | Remainder after | Output |
|---:|:---:|---:|---:|---|
| `1000` | `M` | `1994` | `994` | `M` |
| `900` | `CM` | `994` | `94` | `MCM` |
| `90` | `XC` | `94` | `4` | `MCMXC` |
| `4` | `IV` | `4` | `0` | `MCMXCIV` |

Every skipped larger key exceeds the current remainder. Including subtractive keys ensures canonical decimal-place forms rather than repeated lower symbols.

**Why descending greedy is valid once the condition is corrected**

Subtracting a token and appending its representation preserves the equality between the original number and the value of the output plus the remainder. Key `1` ensures termination at remainder zero.

The ordered token set includes every canonical threshold where fourfold repetition must be replaced: `4`, `9`, `40`, `90`, `400`, and `900`. Choosing the largest fitting entry therefore emits symbols in canonical nonincreasing token-value order and automatically respects the subtractive forms.

That reasoning establishes the corrected algorithm. It cannot establish correctness for the literal Python 3 `/` condition, which does not test whether a token fits.

## Complexity detail

For the **intended corrected implementation** under `1 <= num <= 3999`:

- **Time complexity: $O(1)$.** There are thirteen fixed token values, and the canonical output length is bounded by the input range. The source comment's `O(n)` can describe work proportional to the emitted numeral length, but that length is at most a constant here.
- **Space complexity: $O(1)$.** The map and sorted key list have thirteen entries, and the result has bounded length. Excluding the output, storage is fixed.

For the **literal Python 3 source**, the method often terminates quickly after subtracting an oversized first key, but that runtime is irrelevant to a valid complexity claim because the produced answer is incorrect. Complexity guarantees are meaningful only after restoring the fit condition.

## Alternatives and edge cases

- **Fix the condition with `num >= key`:** This is the clearest repair because it states the exact greedy eligibility rule and avoids division entirely.
- **Fix with floor division:** `num // key > 0` recreates the old Python 2 behavior for positive values, but direct comparison is easier to read.
- **Use `divmod`:** Compute how many copies of each token fit in one operation, append them, and carry the remainder forward. This removes the nested repeated-subtraction loop.
- **Parallel tuples instead of a dictionary:** A preordered list of `(value, token)` pairs avoids sorting a fixed map on every call and makes the required descending order explicit.
- **Hardcoded place-value tables:** Constant-time lookup for thousands, hundreds, tens, and ones is correct but less adaptable.
- **Input smaller than `1000`:** This is where the Python 3 defect is immediately visible, because the oversized `1000` token is still selected.
- **Subtractive values:** A corrected greedy scan emits `IV`, `IX`, `XL`, `XC`, `CD`, and `CM` directly from the map.
- **Two-character tokens with list `+=`:** They are split into characters internally, but `join` reconstructs the same output order. `result.append(token)` would communicate intent more clearly.
- **Outer `while num > 0`:** It is unnecessary after correction because one complete descending pass through key `1` exhausts every legal input.
- **Maximum `3999`:** A corrected version emits `MMMCMXCIX` using only the existing map.
- **No representation for zero:** The contract excludes zero. The unchanged source would return an empty string for zero, but that behavior is outside scope.
- **Current variant status:** Under Python 3, this source is defective and should not be described as an accepted expert implementation until separately authorized code repair and validation occur.
