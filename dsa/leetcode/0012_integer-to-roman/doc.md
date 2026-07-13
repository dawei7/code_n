# Integer to Roman

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 12 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-to-roman/) |

## Problem Description
### Goal
Convert an integer `num` from `1` through `3999` into its standard Roman-numeral representation. The symbols `I`, `V`, `X`, `L`, `C`, `D`, and `M` represent `1`, `5`, `10`, `50`, `100`, `500`, and `1000`, respectively.

Write symbols from larger values toward smaller ones. Powers-of-ten symbols may repeat at most three consecutive times, while `V`, `L`, and `D` are never repeated. Values beginning with `4` or `9` use the six subtractive forms `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`. Return the unique conventional representation without spaces or nonstandard subtractive pairs.

### Function Contract
**Inputs**

- `num`: `int` in `[1, 3999]`

**Return value**

A `str` containing the canonical Roman representation of `num`.

### Examples
**Example 1**

- Input: `num = 3749`
- Output: `"MMMDCCXLIX"`

**Example 2**

- Input: `num = 58`
- Output: `"LVIII"`

**Example 3**

- Input: `num = 1994`
- Output: `"MCMXCIV"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn subtractive notation into ordinary denominations**

Treat Roman notation as a descending list of value-symbol pairs. Alongside `1000 -> M`, `500 -> D`, and the other single symbols, include `900 -> CM`, `400 -> CD`, `90 -> XC`, `40 -> XL`, `9 -> IX`, and `4 -> IV` at their numeric positions.

This turns the special subtraction rules into ordinary greedy denominations.

**Emit the largest legal symbol repeatedly**

For each value, use `divmod` to determine how many copies belong in the result and what remainder is left. Append that symbol the required number of times, then continue with the smaller denomination.

Because the input range and the 13 denominations are fixed, the loop and the maximum output length are both bounded constants.

**Why the greedy order stays canonical**

Before a denomination is processed, the emitted prefix is the canonical representation of the portion already removed, and the remainder is smaller than every previously processed value. Consuming the current largest allowed denomination preserves descending Roman-symbol order.

The denomination table encodes all places where ordinary descending repetition would be noncanonical. For example, value `9` appears before `5` and `1`, so the algorithm emits `IX` rather than `VIIII`; value `40` appears before `10`, so it emits `XL` rather than `XXXX`. No later repair step is needed.

**Trace a representative input**

For 1994, consume `M` to leave 994, `CM` to leave 94, `XC` to leave 4, and `IV` to leave zero. Concatenating the chosen symbols produces `MCMXCIV`.

**Why descending denominations produce the canonical form**

The table contains not only the seven base symbols but also every permitted subtractive pair. Together, those entries encode the unique canonical form for each decimal place. Choosing the largest entry not exceeding the remainder therefore emits the only valid next component; choosing a smaller one would either violate descending order or spell a value that canonical notation represents with the larger entry.

After each emission, the written prefix plus the numeric remainder still equals the original input, and the remainder is smaller than the last fully exhausted denomination. Reaching zero proves the symbols have the correct total value, while descending selection and explicit subtractive entries prove the spelling is canonical.

#### Complexity detail

For the fixed input range `1..3999`, the table always contains 13 entries and a Roman numeral has bounded length. Therefore both time and auxiliary space are $O(1)$. The result string itself is also bounded by a constant under this contract.

#### Alternatives and edge cases

- **Digit-place lookup tables:** directly map thousands, hundreds, tens, and ones. This is also constant time and concise, but encodes the same rules across four separate tables.
- **Use only single-character symbols:** requires backtracking or post-processing to replace forms such as `IIII` with `IV`.
- **Repeated subtraction without quotienting:** remains bounded here, but `divmod` states the multiplicity directly.
- The input constraint excludes zero and negative values because standard Roman notation in this problem has no representation for them.
- Subtractive pairs are limited to `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`; forms such as `IL` or `IC` are never canonical.

</details>
