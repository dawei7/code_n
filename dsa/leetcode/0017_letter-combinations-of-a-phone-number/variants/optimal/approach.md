## General

**Build the Cartesian product one digit at a time**

Each input digit contributes one independent choice of letter. A complete result selects exactly one letter from the mapping for position `0`, one for position `1`, and so on. Mathematically, the answer is the Cartesian product of the per-digit letter sets.

The list

```python
d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
```

stores mappings for digits `2` through `9`. Because list index zero represents digit `2`, a digit character `i` maps to index `int(i) - 2`. The constraints guarantee no `0` or `1`, so every access is valid.

**Start with one empty partial combination**

The algorithm initializes

```python
ans = [""]
```

This is not a completed answer for non-empty input. It is the identity element for concatenation: there is exactly one way to choose letters from zero processed digits, namely the empty prefix.

Starting with `[]` would fail because the nested comprehension would have no existing prefix to extend and would remain empty forever.

**Extend every old prefix with every current letter**

For one digit, let `s` be its mapped letters. The update is

```python
ans = [a + b for a in ans for b in s]
```

The outer comprehension loop chooses every partial prefix `a`; the inner loop attaches each possible current letter `b`. If `ans = ["a", "b", "c"]` and `s = "def"`, the new list is

```text
ad, ae, af, bd, be, bf, cd, ce, cf
```

No prefix is lost, and no current choice is omitted.

Notice that this update does not modify strings already inside the old `ans`. Strings are immutable, so every `a + b` expression creates a separate extended prefix. Rebinding the name `ans` happens only after the entire new list has been constructed. Consequently, the comprehension can safely read every old prefix while producing the next layer, with no risk that newly created prefixes will themselves be extended during the same digit.

**A useful invariant explains completeness**

After processing the first `r` digits, `ans` contains every string obtainable by choosing one mapped letter from each of those `r` digits, exactly once.

The invariant is true at `r = 0` because `[""]` contains the one empty selection. During the next update, every existing valid prefix is paired with every legal letter for digit `r`. That produces all and only valid length-`r + 1` selections. Distinct choice sequences produce distinct strings because each position records its chosen letter.

After the final digit, every entry has length `len(digits)` and represents a complete selection. The invariant proves that the returned list contains the full answer with no duplicates.

**Trace `digits = "23"`**

1. Begin with `ans = [""]`.
2. Digit `2` maps to `"abc"`; extending the empty prefix gives `["a", "b", "c"]`.
3. Digit `3` maps to `"def"`; extending each prefix gives nine combinations from `"ad"` through `"cf"`.

The exact order comes from comprehension nesting, but the contract permits any order.

**Why empty input returns an empty answer rather than `[""]`**

The mathematical Cartesian product of zero sets contains an empty tuple, but the problem's API expects no phone-number combinations when no digits are supplied. The explicit guard

```python
if not digits:
    return []
```

implements that product-specific output convention before the internal identity state is created. The current Reference requires a non-empty string, but the guard preserves the conventional behavior.

## Complexity detail

Let $n$ be the number of digits and let

$$
P=\prod_{r=0}^{n-1} c_r,
$$

where $c_r$ is `3` or `4`, the number of letters mapped by digit `r`.

- **Time complexity: $O(nP)$, bounded by $O(n\cdot4^n)$.** The algorithm must produce `P` strings of length `n`. Each concatenation creates a new prefix string, and total construction work is bounded by the output-character count across levels.
- **Space complexity of the returned answer: $O(nP)$.** The final list stores `P` strings of length `n`. During an update, the old and new prefix lists coexist temporarily, so the exact iterative implementation also has output-proportional working memory. If required output is excluded, a recursive backtracking implementation can use $O(n)$ path/stack space; that convention explains the manifest's $O(n)$ entry.

With `n <= 4`, the maximum number of combinations is `4^4 = 256`.

## Alternatives and edge cases

- **Recursive backtracking:** Append one choice, recurse to the next digit, then pop. It has the same output time and $O(n)$ auxiliary path space excluding results.
- **Mixed-radix enumeration:** Number combinations from `0` to `P - 1` and decode each position using the corresponding choice count. This avoids recursive state but requires careful index arithmetic.
- **Queue-style breadth-first expansion:** Repeatedly remove partial prefixes and append extensions. It expresses the same Cartesian product with more mutation.
- **One digit:** The empty identity prefix expands directly to that digit's three or four letters.
- **Digits `7` and `9`:** They have four choices and determine the worst-case branching factor.
- **Repeated digits:** Positions are independent; `"22"` correctly includes `"aa"`, `"ab"`, and all nine ordered choices.
- **No `0` or `1`:** The contract excludes unmapped digits, so no missing-mapping policy is needed.
- **Input preservation:** The digit string and mapping are read-only; every result string is newly created.
