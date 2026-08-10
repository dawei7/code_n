## General

**Normalize so the first string is not longer**

The competitive solution chooses the opposite normalization from the optimal
variant: after a possible recursive swap, `s` is the shorter string or has the
same length as `t`. Thus $m \le n$.

If $n-m>1$, one insertion, deletion, or replacement cannot reconcile the
lengths, and the method immediately returns false. The remaining cases have a
length shift of either zero or one:

- `shift = 0` means an equal-length replacement is required;
- `shift = 1` means `t` contains one extra character that must be skipped.

The method uses only indices. It never constructs suffix strings.

**Consume the complete common prefix**

The first `while` loop advances `i` while `i < m` and `s[i] == t[i]`. When it
stops, either every character of the shorter string has matched or `i` is the
first mismatch.

Everything before `i` should remain unchanged. Spending the single edit in
that already equal prefix would create a new discrepancy and leave the first
actual mismatch unresolved.

The next alignment depends on the length gap.

**Equal lengths spend one replacement**

When `shift == 0`, the method increments `i` once. If `i` names a mismatch,
this skips one character in both strings, representing the one replacement.
The second loop then requires every later position to match directly.

If the strings were already identical, the first loop ended with `i == m`.
The unconditional increment makes `i == m + 1`. The final check `i == m`
therefore returns false, correctly distinguishing zero edits from one.

For equal empty strings, the same mechanism changes zero to one and returns
false. No indexing occurs during that increment.

**A length gap spends one insertion**

When `shift == 1`, the code does not increment `i` before the second loop.
Instead, it compares `s[i]` with `t[i + shift]`, which is `t[i + 1]`.
Conceptually, `t[i]` is the one inserted character being skipped.

If the first loop reached `i == m`, every character of `s` matched the prefix
of `t`. The extra character is at the end of `t`; the second loop is empty and
the final equality succeeds.

If a mismatch appeared earlier, all characters following the skipped position
must match under the one-index offset. Any further mismatch stops the loop
before `i` reaches `m`, producing false.

**Trace each edit category**

For `s = "ab"` and `t = "acb"`, both begin with `a`, so the prefix loop stops
at `i = 1`. The shift is one. The second loop compares `s[1]`, which is `b`,
with `t[2]`, also `b`, and advances to two. The method returns true: `c` is the
one extra character.

For `"cab"` and `"cad"`, the shift is zero and the first mismatch is at two.
Incrementing `i` skips both final characters as one replacement. Since `i`
equals the length, the result is true.

For `"ab"` and `"cd"`, the first mismatch is at zero. The equal-length branch
skips it, but the second loop immediately finds another mismatch at index one.
The final index is not `m`, so the answer is false.

For `"a"` and `""`, normalization swaps the arguments to `s = ""` and
`t = "a"`. The common-prefix and suffix loops are empty, and `i == m == 0`,
so the answer is true.

**Why the final index is a complete test**

After normalization and the length rejection, precisely one edit form is
possible. The first loop proves the prefix before `i` equal. The alignment
step consumes exactly one candidate edit: one position from both equal-length
strings, or one extra position from the longer string through `shift`.

The second loop advances only across matching aligned characters. It reaches
`m` exactly when the entire shorter string has been accounted for using one
edit. For equal strings, the deliberate increment moves beyond `m` and rejects
the zero-edit case. Therefore `return i == m` is necessary and sufficient.

## Complexity detail

Let $m$ and $n$ be the input lengths. Each loop moves `i` only forward, and
together they inspect no more than the shorter length plus constant work. The
one possible argument swap is followed by the actual scan. Time is
$O(m+n)$, matching the manifest.

Only lengths, `i`, and `shift` are stored. No substring or collection is
allocated, and recursion depth is at most one normalization call. Auxiliary
space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Suffix slicing after the first mismatch:** Concise, but Python creates linear-size temporary strings and loses the $O(1)$ auxiliary-space property.
- **Two independent cursors:** Advance both, skipping the longer cursor once at the first mismatch. This is equivalent to the `shift` formulation.
- **Dynamic programming:** Computes arbitrary edit distance but costs $O(mn)$ and obscures the exactly-one special structure.
- **Equal strings:** The forced equal-length skip makes the final comparison false.
- **Length gap greater than one:** Rejected before indexing.
- **Extra first character:** Shifted suffix comparisons begin at `t[1]`.
- **Extra final character:** The common prefix consumes all of `s`, and the one-length gap makes the result true.
- **One replacement at the end:** Incrementing past the mismatch reaches `m`.
- **Empty inputs:** Both empty is false; exactly one one-character string is true.
- **Symmetric relation:** Swapping arguments changes insertion to deletion but does not change whether the strings are one edit apart.
