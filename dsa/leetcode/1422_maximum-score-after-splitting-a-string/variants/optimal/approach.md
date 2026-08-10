## General

**Update the score when one character crosses the split**

For a chosen split, the score is:

$$
\text{zeros in the left part} + \text{ones in the right part}.
$$

Checking every split independently would repeatedly recount almost the same characters. Moving a split one position to the right changes only one character: that character leaves the right substring and enters the left substring.

The solution tracks:

- `l`: the number of zeros currently in the left substring.
- `r`: the number of ones currently in the right substring.

Their sum is the score for the current split.

**Initialize an empty-left conceptual state**

The code starts with:

```python
l, r = 0, s.count("1")
```

Before processing any character, imagine that the left side is empty and the right side is the whole string. There are zero left zeros, while `r` equals every one in `s`.

That imaginary split is not legal because the left substring is empty. The algorithm does not score it. Instead, each loop iteration first moves one character into the left side and then evaluates the resulting legal split.

**Never move the final character**

The loop scans `s[:-1]` rather than all of `s`. This slice contains every character except the last. After processing character at index `i`, the split lies between `i` and `i+1`.

If the last character were processed, the right substring would become empty, which the contract forbids. Because `s` has length at least two, `s[:-1]` contains at least one character and every legal split is visited exactly once.

**Update the left zero count with XOR**

For current binary character `x`:

```python
l += int(x) ^ 1
```

`int(x)` is either zero or one. Bitwise XOR with one flips that bit:

| `x` | `int(x) ^ 1` | Meaning |
|---|---:|---|
| `"0"` | 1 | one new zero entered the left |
| `"1"` | 0 | the left zero count is unchanged |

Thus the compact expression is equivalent to incrementing `l` only when `x == "0"`.

**Update the right one count**

The same moved character was previously part of the right substring:

```python
r -= int(x)
```

If `x` is one, it leaves the right side and `r` decreases by one. If `x` is zero, the number of right-side ones is unchanged.

After both updates, `l` and `r` refer to the same split: the current character is included on the left and excluded from the right. Updating only one counter would mix two different split positions.

**Record the best legal score**

`ans = max(ans, l + r)` compares the current split score with every earlier one. `ans` begins at zero. Scores cannot be negative because they are counts, so this is a safe initial value. The input `"10"` demonstrates that the maximum can actually be zero.

After the loop, every split after positions zero through `len(s)-2` has been evaluated, so `ans` is the maximum.

**Trace `s = "011101"`**

Initially, `l = 0` and `r = 4` because the full string contains four ones.

| Character moved left | Left substring | Right substring | `l` | `r` | Score |
|---|---|---|---:|---:|---:|
| `0` | `0` | `11101` | 1 | 4 | 5 |
| `1` | `01` | `1101` | 1 | 3 | 4 |
| `1` | `011` | `101` | 1 | 2 | 3 |
| `1` | `0111` | `01` | 1 | 1 | 2 |
| `0` | `01110` | `1` | 2 | 1 | 3 |

The last source character remains in the right part at the final legal split. The maximum recorded score is five.

**Why the invariant proves correctness**

Before an iteration, `l` counts zeros among characters already processed, while `r` counts ones among all unprocessed characters. The two updates transfer the current character and preserve those meanings. Therefore, after each transfer, `l + r` equals the score of that exact legal split.

The loop visits every possible nonempty-left, nonempty-right boundary once. Taking the maximum over these exact scores returns the required answer.

## Complexity detail

Let $n$ be the string length. `s.count("1")` scans the string once in $O(n)$ time. The loop scans $n-1$ characters and performs constant work per character, so total time is $O(n)$.

The counters and current character use $O(1)$ algorithmic state. In Python, `s[:-1]` creates a new substring of length $n-1$, so the exact expression incurs $O(n)$ temporary allocation. An index loop or `itertools.islice` would retain the same logic with strict $O(1)$ auxiliary space. The manifest's $O(1)$ bound describes the counting algorithm rather than Python slice materialization.

## Alternatives and edge cases

- **Explicit character branches:** Replace the XOR arithmetic with `if x == "0"` and `else`. It is more immediately readable and has identical complexity.
- **Prefix and suffix arrays:** Precompute zero counts from the left and one counts from the right. This answers each split quickly but uses $O(n)$ extra storage for information two counters can maintain.
- **Recount each split:** Scanning both substrings for every boundary takes $O(n^2)$ time.
- **One-pass algebraic variant:** Maximize left zeros minus left ones, then add total ones. It can avoid the separate initial count but needs careful handling of the final character.
- **All zeros:** `r` remains zero and `l` grows at each legal split, so the best split puts all but the final zero on the left.
- **All ones:** `l` remains zero and `r` decreases; the first split leaves the most ones on the right.
- **Length two:** The loop evaluates exactly the only legal split.
- **Score zero:** For `"10"`, neither the left contains a zero nor the right a one, so zero is correctly returned.
- **Nonempty constraint:** Excluding the final source character from the loop is essential; scoring after it would use an illegal empty right substring.
- **Binary-input guarantee:** The XOR trick relies on `int(x)` being exactly zero or one.
