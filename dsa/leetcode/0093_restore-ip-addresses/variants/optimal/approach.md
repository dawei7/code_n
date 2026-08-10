## General

A valid result is determined entirely by three cut positions that divide the original digits into exactly four consecutive components. No digit may be moved or discarded. The selected solution explores possible component lengths with depth-first search, but rejects a component immediately if it violates either IPv4 rule:

- its numerical value must lie from `0` through `255`; and
- a multi-digit component may not begin with `0`.

Because a valid component has at most three digits, each recursive state tries only the next one, two, or three characters.

**Meaning of the search state**

In `dfs(i)`, the index `i` is the first digit not yet assigned to a component. The list `t` holds the valid components already chosen, in their original order. The invariant is that joining `t` without dots equals exactly the consumed prefix `s[:i]`.

The loop chooses an inclusive endpoint `j` from `i` through at most `i + 2`. Therefore `s[i:j + 1]` has length one, two, or three. If `check(i, j)` accepts it, the algorithm appends that substring, recursively processes the suffix beginning at `j + 1`, and then pops the substring to restore `t` for the next candidate endpoint.

The pop is what makes one mutable path list reusable. Without it, a component selected in one branch would remain present when exploring a sibling branch, so the path would no longer correspond to the consumed digits.

**Why the component check is exact**

The first condition rejects a substring such as `00`, `01`, or `025`: if `s[i] == "0"` and `i != j`, its length is greater than one and it has a forbidden leading zero. A one-character `0` is accepted because then `i == j`.

After the leading-zero rule, `int(s[i:j + 1])` converts the candidate to its numerical value. The input is guaranteed to contain only digits, and the loop guarantees a nonempty slice, so conversion is safe. Checking the inclusive range through `0 <= value <= 255` accepts exactly the permitted values. The lower-bound comparison is redundant for a digit-only nonnegative substring but documents the complete address rule.

Limiting candidate length to three is also necessary. Every four-digit nonnegative decimal string is either numerically above `255` or begins with a zero; in the latter case it is already invalid as a multi-digit component.

**When a path becomes an answer**

The first base condition requires both all digits to be consumed and exactly four components to have been chosen. Only then does `".".join(t)` form and record an address.

Both halves are needed. Consuming the string with only three components is invalid because an IPv4 address requires four. Choosing four components while digits remain is also invalid because digits cannot be dropped. The second base condition stops either impossible state: no digits remain before four pieces are formed, or four pieces already exist before all digits are consumed.

Although the code says `i >= n`, valid recursion can only reach `i == n`: every endpoint is below `n`, and the recursive index is `j + 1`. The broader comparison is harmless.

**Trace for `101023`**

One branch chooses `1`, then `0`, then `10`, then `23`, reaching the end with four pieces and recording `1.0.10.23`. Another chooses `10`, `10`, `2`, and `3`, recording `10.10.2.3`.

A branch that tries to take `01` after the initial `1` is rejected immediately because it has a leading zero. A branch may also consume too many digits in early components and reach the end with fewer than four pieces; the base condition rejects it. Systematically trying all lengths one through three ensures the other valid results in the Reference are reached as well.

**Why the output is complete and has no duplicates**

Every valid address determines one unique sequence of four component lengths. At each depth, the DFS tries the length used by that address, and `check` accepts it because the address is valid. Following those four choices reaches and records the address, so none is missed.

Conversely, a recorded path contains four individually valid components and consumes every digit exactly once in order, so every recorded string is a valid restoration. Two distinct recursion paths differ at some selected endpoint, hence at some dot position. Their dotted strings differ, so the algorithm cannot record the same address twice.

**An optional prune the source does not use**

If $r$ components remain and $d$ digits remain, continuation is possible only when

$$
r\le d\le3r.
$$

The exact optimal source does not perform this test. That does not affect correctness or the stated asymptotic bound because search depth and branching are fixed by the four-component IPv4 format. It merely explores a few branches whose digit count already proves failure.

## Complexity detail

There are at most three length choices at each of four component positions, so the search explores at most a constant multiple of $3^4$ states. Each check parses at most three digits, and each successful answer contains at most twelve digits plus three dots. Since both “four” and “three” are fixed protocol constants, time is $O(1)$ with respect to the input length, matching the manifest.

The recursion depth is at most four, `t` stores at most four short substrings, and each candidate slice has at most three characters. These are all fixed bounds, so auxiliary space is $O(1)$. Even the number and total length of possible IPv4 outputs are bounded by constants because a valid source has at most twelve digits. Under a generalized problem with $P$ parts of up to $L$ digits, the analogous search would be exponential in $P$; the constant result here depends on IPv4 fixing $P=4$ and $L=3$.

For input length greater than twelve, no branch can consume the entire string within four iterations, so the result is empty. The source may still inspect a bounded prefix search tree, never all twenty characters combinatorially.

## Alternatives and edge cases

- **Three nested cut loops:** Enumerate lengths of the first three components; the fourth consumes the remainder. This avoids recursion and has the same fixed bound, but the repeated index arithmetic is more verbose.
- **Remaining-length pruning:** Before branching, reject states whose unconsumed digit count is outside one to three times the remaining component count. This reduces failed calls without changing asymptotic complexity.
- **Enumerating all dot positions:** For each choice of three gaps, validate four substrings. It is correct but examines more invalid layouts unless length bounds are incorporated.
- **Exactly four zeros:** `0000` permits only four single-character components, producing `0.0.0.0`. Any attempt to group two zeros fails the leading-zero check.
- **Too short or too long:** Fewer than four digits cannot fill four nonempty components; more than twelve cannot fit within four three-digit components. Both return an empty list.
- **Value boundary:** `255` is accepted and `256` is rejected. Three digits alone do not guarantee validity.
- **Leading-zero boundary:** `0` is valid, while `00` and `01` are invalid even though their integer values are within range.
- **Input preservation:** The method reads slices from `s` and never changes or reorders the source digits.
- **Output order:** DFS order follows shorter component choices first. The contract allows any order, so no final sort is required.
