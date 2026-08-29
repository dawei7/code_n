## General

**Accumulate net shifts instead of editing every range**

Applying one shift directly to every character in its interval can touch $O(n)$ positions. With up to $5\cdot10^4$ operations, repeated direct edits can become quadratic.

Character shifts add together. A position shifted forward three times and backward once has the same final result as one net forward shift of two, regardless of operation order. The algorithm therefore computes one net integer shift for every index and transforms the string once.

**Encode an inclusive range by two boundaries**

The difference array `d` has length `n + 1`. For an operation on inclusive interval `[i, j]` with signed amount `v`, it performs:

```python
d[i] += v
d[j + 1] -= v
```

The first update says that beginning at `i`, the running shift changes by `v`. The second says that immediately after `j`, the change ends.

The extra cell at index `n` is a sentinel. When an interval ends at the last string position `n - 1`, `j + 1` equals `n` and remains a valid difference-array index, avoiding a boundary branch.

Input direction `1` already means forward `+1`. Direction `0` means backward, so the code converts it to `-1` before recording the boundaries.

**Recover every position's net shift**

After all operations are encoded, `d` contains changes rather than final per-position values. The prefix loop:

```python
for i in range(1, n + 1):
    d[i] += d[i - 1]
```

turns those changes into running sums. Afterward, `d[i]` for a string position is the sum of every signed operation whose interval covers `i`.

To see why, a range contributes `+v` at its start to all following prefix sums, then contributes `-v` after its end, canceling itself for later positions. It is therefore present exactly over its inclusive interval.

**Rotate each letter with modular arithmetic**

`ord(s[i]) - ord('a')` maps lowercase letters to numbers `0` through `25`. Adding `d[i]` applies the net shift. Taking modulo `26` wraps the alphabet:

```python
(ord(s[i]) - ord('a') + d[i] + 26) % 26
```

Adding `ord('a')` and calling `chr` maps the result back to a letter.

The added `26` is harmless but not sufficient by itself to make every large negative intermediate nonnegative. Python's modulo operator already returns a result in `0` through `25` even for negative operands, so arbitrary accumulated backward shifts work correctly. Modularly, adding one extra `26` does not change the remainder.

The generator transforms every original character, and `''.join(...)` assembles the final immutable string efficiently.

**Trace overlapping operations**

For `s = "abc"` and operations `[0,1,-1]`, `[1,2,+1]`, and `[0,2,+1]`, the net shifts by position are:

```text
index 0: -1 + 1 = 0
index 1: -1 + 1 + 1 = 1
index 2:      1 + 1 = 2
```

Applying those totals to `a, b, c` gives `a, c, e`, so the result is `"ace"`. This matches sequential application because rotations compose by addition.

**Why operation order can be collapsed**

Forward shift is adding one modulo 26, and backward shift is adding negative one. Integer addition is associative and commutative, so the final displacement at an index is simply the sum of covering operations. Intermediate wrapped letters do not matter:

$$
((x+a)\bmod26+b)\bmod26=(x+a+b)\bmod26.
$$

The difference array calculates exactly this sum for each position.

**Why the entire algorithm is correct**

Each operation deposits its signed value at its start and removes it after its end. Prefix accumulation therefore makes `d[p]` equal the sum of precisely the operations covering position `p`. The modular character conversion applies exactly that many net alphabet steps to the original letter, including wraparound.

Since each output position is transformed independently using its correct net shift, joining all characters produces the same final string as applying all input operations one at a time.

## Complexity detail

Let $n$ be the string length and $m$ the number of shift operations. Recording two boundaries for every operation takes $O(m)$ time. Prefix accumulation and character construction each take $O(n)$ time. Total time is $O(n+m)$.

The difference array uses $n+1$ integers, and the joined output has length $n$. Auxiliary/result storage is $O(n)$. The generator avoids a separate list of all converted characters, though `join` still creates the final string.

## Alternatives and edge cases

- **Apply each range directly:** It is straightforward but can take $O(nm)$ time when intervals are long.
- **Fenwick tree:** Range updates with point queries can solve the problem in $O((n+m)\log n)$, but an offline difference array is simpler and faster.
- **All-string interval:** The end cancellation lands safely at sentinel index `n`.
- **Single-character interval:** Updates at `i` and `i+1` affect exactly one prefix position.
- **Overlapping shifts:** Their signed contributions add in the running prefix sum.
- **Forward and backward cancellation:** Equal opposite coverage produces net zero and leaves the original letter.
- **Large shift magnitude:** Modulo 26 reduces any accumulated total to the equivalent alphabet rotation.
- **Wrap from `z` to `a`:** Numeric value 25 plus one becomes zero modulo 26.
- **Wrap from `a` to `z`:** Python's negative modulo maps negative one to 25.
- **Sentinel entry:** `d[n]` is accumulated but never used to transform a character; it only terminates ranges cleanly.
